import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        expected = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="img", props={"src": "image.png"})
        expected = 'src="image.png"'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
