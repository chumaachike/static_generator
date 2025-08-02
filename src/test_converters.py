import unittest
from textnode import TextNode, TextType
from converters import text_node_to_html_node, split_nodes_delimiter


class TestConverters(unittest.TestCase):
    def test_text(self):
        node = TextNode(TextType.TEXT, "This is a text node")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode(TextType.BOLD, "Bold text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic(self):
        node = TextNode(TextType.ITALIC, "Italic text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode(TextType.CODE, "print('hello')")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")

    def test_link(self):
        node = TextNode(TextType.LINK, "OpenAI", "https://openai.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "OpenAI")
        self.assertEqual(html_node.props.get("href"), "https://openai.com")

    def test_image(self):
        node = TextNode(TextType.IMAGE, "An image", "https://example.com/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props.get("src"), "https://example.com/img.png")
        self.assertEqual(html_node.props.get("alt"), "An image")

    def test_invalid_type_raises(self):
        class FakeType: pass
        node = TextNode(FakeType, "Oops")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def test_basic_code_block(self):
        text = "This is `code block` here"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "`", TextType.CODE)
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.CODE, "code block"),
            TextNode(TextType.TEXT, " here"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        text = "Use `one` and also `two words` here"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "`", TextType.CODE)
        expected = [
            TextNode(TextType.TEXT, "Use "),
            TextNode(TextType.CODE, "one"),
            TextNode(TextType.TEXT, " and also "),
            TextNode(TextType.CODE, "two words"),
            TextNode(TextType.TEXT, " here"),
        ]
        self.assertEqual(result, expected)

    def test_empty_code_block(self):
        text = "This is `` empty block"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "`", TextType.CODE)
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.TEXT, " empty block"),
        ]
        self.assertEqual(result, expected)

    def test_no_backticks(self):
        text = "Plain text only"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "`", TextType.CODE)
        expected = [TextNode(TextType.TEXT, "Plain text only")]
        self.assertEqual(result, expected)

    def test_unmatched_backtick(self):
        text = "This is `unfinished code"
        node = TextNode(TextType.TEXT, text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter(node, "`", TextType.CODE)
        

    def test_with_italics(self):
        text = "This is *italic text* here"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "*", TextType.ITALIC)
        expected = [
            TextNode(TextType.TEXT, "This is "),
            TextNode(TextType.ITALIC, "italic text"),
            TextNode(TextType.TEXT, " here"),
        ]
        self.assertEqual(result, expected)

    def test_nested_like_sequence(self):
        text = "Text with `code and *italic* inside` test"
        node = TextNode(TextType.TEXT, text)
        result = split_nodes_delimiter(node, "`", TextType.CODE)
        expected = [
            TextNode(TextType.TEXT, "Text with "),
            TextNode(TextType.CODE, "code and *italic* inside"),
            TextNode(TextType.TEXT, " test"),
        ]
        self.assertEqual(result, expected)

    