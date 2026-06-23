import unittest
from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is a text node", TextType.bold_text)
        node2: TextNode = TextNode("This is a text node",TextType.bold_text)
        self.assertEqual(node,node2)
        self.assertEqual(TextNode("Geez",TextType.italic_text), TextNode("Geez",TextType.italic_text))
    def test_not_eq_text(self):
        self.assertNotEqual(TextNode("Geez",TextType.italic_text), TextNode("Gez",TextType.italic_text))
    def test_eq_with_url(self):
        self.assertEqual(TextNode("Geez",TextType.italic_text,"Chocolate"), TextNode("Geez",TextType.italic_text,"Chocolate"))
if __name__ == "__main__":
    unittest.main()