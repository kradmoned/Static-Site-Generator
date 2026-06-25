from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str,str] | None = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Parent Node must have tag")
        if self.children is None:
            raise ValueError("Parent Node must have children")
        pretag = f"<{self.tag}{self.props_to_html()}>"
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        post_tag = f"</{self.tag}>"
        return pretag+child_html+post_tag 