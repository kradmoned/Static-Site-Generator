from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,
                tag: str | None,
                 value: str,
                     props: dict[str,str] | None = None):
        """
        Represent a single HTML Tag with no children

        Attributes:
            value: The plain Text(required)
            tag: The HTML tag can be none
            proc: The properties of tag in a dictionary
        """
        super().__init__(tag= tag, value=value, props=props, children= None)
    
    def to_html(self):
        """
        Convert a single html node to tag
        """
        # If there are no value then we raise an error because value is required
        if self.value is None:
            raise ValueError
        # In case of no tag , return the value as it iss
        if self.tag == None:
            return self.value
        pretag: str = f"<{self.tag}{self.props_to_html()}>"
        value: str = self.value
        post_tag: str = f"</{self.tag}>"
        return f"{pretag}{value}{post_tag}"
    def __repr__(self):
        return f'LeafNode({self.tag},{self.value},{self.props})'
    