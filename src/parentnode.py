from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag,  children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be None or empty")

        html = f"<{self.tag}>"

        for child in getattr(self, "children", []):
            # Ensure the child is a node
            if hasattr(child, "to_html"):
                html += child.to_html()
            elif isinstance(child, str):
                html += child
            else:
                raise ValueError("Invalid child: must be a node or string")

        html += f"</{self.tag}>"
        return html


