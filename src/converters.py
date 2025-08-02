from textnode import TextNode, TextType
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            # Just raw text
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Unsupported text type: {text_node.text_type}")

def split_nodes_delimiter(old_node: TextNode, delimiter: str, text_type: str):
    parts = old_node.text.split(delimiter)
    if len(parts) % 2 == 0:
        raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {old_node.text}")

    new_nodes = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            if part:  # skip empty plain text
                new_nodes.append(TextNode(old_node.text_type, part))
        else:
            if part:  # skip empty code
                new_nodes.append(TextNode(text_type, part))
    return new_nodes

