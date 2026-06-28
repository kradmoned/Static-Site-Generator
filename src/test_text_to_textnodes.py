import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode,TextType


class TestTextToTextnodes(unittest.TestCase):
    def test_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertListEqual(text_nodes,[
                            TextNode("This is ", TextType.plain_text),
                            TextNode("text", TextType.bold_text),
                            TextNode(" with an ", TextType.plain_text),
                            TextNode("italic", TextType.italic_text),
                            TextNode(" word and a ", TextType.plain_text),
                            TextNode("code block", TextType.code_text),
                            TextNode(" and an ", TextType.plain_text),
                            TextNode("obi wan image", TextType.images, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.plain_text),
                            TextNode("link", TextType.link, "https://boot.dev"),
                            ] )
    # Dont want to write more test cases