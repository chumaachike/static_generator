from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag,  children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be none")
        
        html = f"<{self.tag}>"
        for child in self.children:
            if not child.value and not child.children:
                raise ValueError("Child tag must have a value")
            html += child.to_html()

        html += f"</{self.tag}>"
        return html

