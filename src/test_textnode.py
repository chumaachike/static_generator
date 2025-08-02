import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        #test 2
        node1 = TextNode("Test is a node", TextType.CODE, None)
        node2 = TextNode("Test is a node", TextType.CODE)
        self.assertEqual(node1, node2)

        #test 3
        node1 = TextNode("Test is a node", TextType.CODE, "pornhub.com")
        node2 = TextNode("Test is a node", TextType.CODE)
        self.assertNotEqual(node1, node2)

        #test 4
        node1 = TextNode("Test is a node", TextType.LINK)
        node2 = TextNode("Test is a node", TextType.CODE)
        self.assertNotEqual(node1, node2)




if __name__ == "__main__":
    unittest.main()