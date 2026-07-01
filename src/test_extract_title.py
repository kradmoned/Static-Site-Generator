import unittest
from extract_title import extract_title
class ExtractTitle(unittest.TestCase):
    def test_header(self):
        md= "# Hello"
        self.assertEqual(extract_title(md), "Hello")
    def test_header_after(self):
        md = "my name is kradmoned \n\n # Chocolate Pizza"
        self.assertEqual(extract_title(md), "Chocolate Pizza")
    def test_no_header(self):
        md = "Death is like a wind always by my side"
        with self.assertRaises(ValueError):
            extract_title(md)