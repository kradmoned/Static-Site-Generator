from enum import Enum

class TextType(Enum):
    plain_text: str = "text"
    bold_text: str = "bold_text"
    italic_text: str = "italic_text"
    code_text: str = "code_text"
    link: str = "link"
    images: str = "image"

class TextNode:
    def __init__(self,text: str, text_type: "TextType", url: str | None ):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = None
    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"   