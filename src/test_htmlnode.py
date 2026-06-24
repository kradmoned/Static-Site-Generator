import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_none(self):
        tests = []
        tests.append((HTMLNode(),""))
        for test in tests:
            self.assertEqual(test[0].props_to_html(),test[1])
    def test_props_to_html_empty(self):
        tests = []
        tests.append((HTMLNode(props={}),""))
        for test in tests:
            self.assertEqual(test[0].props_to_html(),test[1])
    def test_props_to_html_with_values(self):
        tests = []
        tests.append((HTMLNode(props= {
            "href": "https://www.google.com",
            "target": "_blank",
        }),' href="https://www.google.com" target="_blank"'))
        for test in tests:
            self.assertEqual(test[0].props_to_html(),test[1])


        