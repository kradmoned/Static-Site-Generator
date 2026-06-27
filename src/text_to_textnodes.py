from textnode import TextNode,TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_node_images import split_nodes_image
from split_nodes_links import split_nodes_links

def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.plain_text)
    new_nodes = split_nodes_delimiter([node],"**",TextType.bold_text)
    new_nodes = split_nodes_delimiter(new_nodes,"_",TextType.italic_text)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.code_text)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    return new_nodes
