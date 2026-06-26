import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode,TextType

class TestSplitNodes_Delimeter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.plain_text)
        node = split_nodes_delimiter([node], "**", TextType.bold_text)
        self.assertEqual(node,[
                            TextNode("This is text with a ", TextType.plain_text),
                            TextNode("bolded phrase", TextType.bold_text),
                            TextNode(" in the middle", TextType.plain_text),
                        ])
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.plain_text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertEqual(new_nodes,[
                    TextNode("This is text with a ", TextType.plain_text),
                    TextNode("code block", TextType.code_text),
                    TextNode(" word", TextType.plain_text),
                ])
    def test_combined(self):
        node = TextNode("This is **b** with `code` and _italic_",TextType.plain_text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        #print(f"\nOld nodes = {new_nodes}")
        result1 = [TextNode("This is ",TextType.plain_text), TextNode("b",TextType.bold_text), TextNode(" with `code` and _italic_",TextType.plain_text)]
        self.assertEqual(new_nodes, result1)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.italic_text)
        result2 = [TextNode("This is ",TextType.plain_text), TextNode("b",TextType.bold_text), TextNode(" with `code` and ",TextType.plain_text),TextNode("italic",TextType.italic_text)]
        #print("\n")
        #print(f"New Nodes = {new_nodes}")
        #print(f"Required = {result2}")
        self.assertEqual(new_nodes, result2)

        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.code_text)        
        result3 = [TextNode("This is ",TextType.plain_text), TextNode("b",TextType.bold_text), TextNode(" with ",TextType.plain_text),TextNode("code",TextType.code_text),TextNode(" and ",TextType.plain_text),TextNode("italic",TextType.italic_text)]
        self.assertEqual(new_nodes, result3)


    def test_incorrect(self):
        node = TextNode("This is **incorect node",TextType.plain_text)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
             

if __name__ == "__main__":
    unittest.main()                