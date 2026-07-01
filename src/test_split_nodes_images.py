import unittest

from textnode import TextType,TextNode
from split_nodes import split_nodes_image
class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.plain_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.plain_text),
                TextNode("image", TextType.images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.plain_text),
                TextNode(
                    "second image", TextType.images, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_empty(self):
        node = TextNode("", TextType.plain_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual([],new_nodes)


    def test_split_images_single_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.plain_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ",TextType.plain_text),
                              TextNode("image",TextType.images,"https://i.imgur.com/zjjcJKZ.png"),
                              ]
                              , new_nodes)
        

    def test_split_images_image_at_start(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) The rest of the string", TextType.plain_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image",TextType.images,"https://i.imgur.com/zjjcJKZ.png"),TextNode(" The rest of the string",TextType.plain_text)], new_nodes)
    def test_split_images_image_at_end(self):
        node = TextNode("Start ![second image](https://i.imgur.com/3elNhQu.png)", TextType.plain_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("Start ", TextType.plain_text),
                              TextNode("second image", TextType.images,"https://i.imgur.com/3elNhQu.png")
                              ],
                              new_nodes)
    def test_split_images_no_images(self):
        node = TextNode("This is a plain old simple text", TextType.plain_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is a plain old simple text", TextType.plain_text)],new_nodes)
    def test_split_images_with_link(self):
        node = TextNode("Start ![logo](https://example.com/logo.png) middle [Boot.dev](https://www.boot.dev) end", TextType.plain_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("Start ",TextType.plain_text),
                              TextNode("logo",TextType.images,"https://example.com/logo.png"),
                              TextNode(" middle [Boot.dev](https://www.boot.dev) end",TextType.plain_text)
                              ],
                              new_nodes)
        
if __name__ == "__main__":
    unittest.main()