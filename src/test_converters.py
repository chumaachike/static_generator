import unittest
from textnode import TextNode, TextType
from converters import text_node_to_html_node


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
