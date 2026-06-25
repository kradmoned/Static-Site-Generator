import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_childrens(self):
        child_node = LeafNode(None, "child")
        child_node2 = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node,child_node2])
        self.assertEqual(parent_node.to_html(), "<div>child<p>child</p></div>")

    def test_to_html_with_a(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        childrens = [node1,node2]
        parent = ParentNode("div",childrens,)
        self.assertEqual(parent.to_html(),'<div><p>Hello, world!</p><a href="https://www.google.com">Click me!</a></div>')
    
    def test_to_html_with_parent_property(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        childrens = [node1,node2]
        parent = ParentNode("div",childrens,{"id":"312"})
        parent2 = LeafNode(None,"Grand")
        grand_parent = ParentNode("div",[parent2,parent],{"id":"123"})
        result = '<div id="123">Grand<div id="312"><p>Hello, world!</p><a href="https://www.google.com">Click me!</a></div></div>'
        self.assertEqual(grand_parent.to_html(), result)
    def test_to_html_with_no_children(self):
        parent = ParentNode('p',None)
        with self.assertRaises(ValueError) as e:
            parent.to_html()
        self.assertEqual(str(e.exception),"Parent Node must have children")
    def test_to_html_with_no_tags(self):
        child = LeafNode('p','hello')
        parent = ParentNode(None,[child])
        with self.assertRaises(ValueError) as e:
            parent.to_html()
        self.assertEqual(str(e.exception),"Parent Node must have tag")
    
    

