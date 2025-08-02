from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        self.tag = tag
        self.value=value
        self.props=props
    
    def to_html(self):
        if not self.value:
            raise ValueError("value must be provided")
        
        if not self.tag:
            return f"{self.value}"
        
        html = super().props_to_html()
        return f"<{self.tag}{' ' + html if html else ''}>{self.value}</{self.tag}>" 

    