from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    plain_text: str = "text"
    bold_text: str = "bold_text"
    italic_text: str = "italic_text"
    code_text: str = "code_text"
    link: str = "link"
    images: str = "image"

class TextNode:
    def __init__(self,text: str, text_type: "TextType", url: str | None = None):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url
    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"   


def text_node_to_html_node(text_node: "TextNode") -> LeafNode:
    match text_node.text_type:
        case TextType.plain_text:
            return LeafNode(None, text_node.text,None)
        case TextType.bold_text:
            return LeafNode('b',text_node.text)
        case TextType.italic_text:
            return LeafNode('i',text_node.text)
        case TextType.code_text:
            return LeafNode('code',text_node.text)
        case TextType.link:
            return LeafNode('a',text_node.text, {"href": f"{text_node.url}"})
        case TextType.images:
            return LeafNode("img",
                            "",
                            {
                                "src":f"{text_node.url}",
                                "alt":f"{text_node.text}"
                            })
        case _:
            raise Exception