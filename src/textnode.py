from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text_type, text, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode):
        return (
            textNode.text == self.text 
            and textNode.text_type == self.text_type 
            and textNode.url == self.url
            )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
