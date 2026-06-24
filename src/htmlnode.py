
class HTMLNode:
    """
    Represents a node in an HTML Document Tree

    Attributes:
        tag: The HTML tag name (e.g. 'p', 'a')
        value: The text of node
        children: The list of children inside the object
        props: The properties of the tag in a dictionary   
    """
    def __init__(self,
                tag: str | None = None,
                value: str | None = None,
                children: list["HTMLNode"] | None = None,
                props: dict[str, str] | None = None):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list["HTMLNode"] | None = children
        self.props: dict[str, str] | None = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        """
        returns a formatted string from the props dictionary representing HTML attribute
        With space preappended
        """
        html_string: str = ""
        if not self.props:
            return html_string
        for key in self.props:
            html_string += f' {key}="{self.props[key]}"' 
        return html_string
    def __repr__(self):
        return f"HTMLNode{self.tag},{self.value},{self.children},{self.props}"

