import unittest
from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_bold(self):
        node = LeafNode("bold", "Hello, world!")
        self.assertEqual(node.to_html(), "<bold>Hello, world!</bold>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_value(self):
        node1 = LeafNode("a",None,{"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node1.to_html()
    
    def test_leaf_to_html_empty_value(self):
        node = LeafNode("p","",None)
        self.assertEqual(node.to_html(),"<p></p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")