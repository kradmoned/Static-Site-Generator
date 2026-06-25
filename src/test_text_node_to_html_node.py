import unittest
from textnode import TextNode, TextType,text_node_to_html_node
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.plain_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is a text node", TextType.bold_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'b')
        self.assertEqual(html_node.value, "This is a text node")
    def test_italic(self):
        node = TextNode("This is a text node", TextType.italic_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'i')
        self.assertEqual(html_node.value, "This is a text node")
    def test_code(self):
        node = TextNode("This is a text node", TextType.code_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'code')
        self.assertEqual(html_node.value, "This is a text node")
    def test_image(self):
        node = TextNode("Picture", TextType.images,"img/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"],"img/")
        self.assertEqual(html_node.props["alt"],"Picture")
    def test_link(self):
        node = TextNode("Link", TextType.link,"www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'a')
        self.assertEqual(html_node.value, "Link")
        self.assertEqual(html_node.props["href"],"www.google.com")
    
    def test_ivalid(self):
        node = TextNode("invalid", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        