import unittest
from inline_markdown import (
    text_to_textnodes,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    split_nodes_delimiter,
    
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            TextType.TEXT,
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"            
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(TextType.TEXT, "This is text with an "),
                TextNode(TextType.IMAGE, "image", "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            TextType.TEXT,
            "![image](https://www.example.COM/IMAGE.PNG)",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(TextType.IMAGE, "image",  "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            TextType.TEXT,
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(TextType.TEXT, "This is text with an "),
                TextNode(TextType.IMAGE, "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(TextType.TEXT, " and another "),
                TextNode(
                    TextType.IMAGE, "second image", "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            TextType.TEXT,
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(TextType.TEXT, "This is text with a "),
                TextNode(TextType.LINK,"link", "https://boot.dev"),
                TextNode(TextType.TEXT, " and "),
                TextNode(TextType.LINK,"another link",  "https://blog.boot.dev"),
                TextNode(TextType.TEXT," with text that follows",),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):
        node = TextNode(TextType.TEXT, "**bold** and _italic_")
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode(TextType.BOLD, "bold"),
                TextNode(TextType.TEXT, " and "),
                TextNode(TextType.ITALIC, "italic"),
            ],
            new_nodes,
        )
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode(TextType.TEXT, "This is ",),
                TextNode(TextType.BOLD, "text"),
                TextNode(TextType.TEXT, " with an "),
                TextNode(TextType.ITALIC, "italic"),
                TextNode(TextType.TEXT, " word and a "),
                TextNode(TextType.CODE, "code block"),
                TextNode(TextType.TEXT, " and an "),
                TextNode(TextType.IMAGE, "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(TextType.TEXT, " and a "),
                TextNode(TextType.LINK, "link", "https://boot.dev"),
            ],
            nodes,
        )
    


if __name__ == "__main__":
    unittest.main()
