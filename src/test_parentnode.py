import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_single_leaf_node(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_leaf_node_without_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_parent_node_with_multiple_children(self):
        child1 = LeafNode("span", "first")
        child2 = LeafNode("i", "second")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><span>first</span><i>second</i></div>"
        )

    def test_parent_node_with_no_children(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_nested_three_levels(self):
        grandchild = LeafNode("b", "deep")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        root = ParentNode("section", [parent])
        self.assertEqual(
            root.to_html(),
            "<section><div><span><b>deep</b></span></div></section>"
        )


    def test_invalid_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, "no tag").to_html()

    def test_child_without_value_and_no_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [LeafNode("p", None)]).to_html()

    def test_multiple_nested_siblings(self):
        child1 = ParentNode("ul", [
            LeafNode("li", "Item 1"),
            LeafNode("li", "Item 2"),
        ])
        child2 = LeafNode("p", "Paragraph")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><ul><li>Item 1</li><li>Item 2</li></ul><p>Paragraph</p></div>"
        )
