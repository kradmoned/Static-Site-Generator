from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split a list of text nodes based on images
    
    Attributes:
        old_nodes: A list of nodes in which , an image text will be checked
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.plain_text:
            new_nodes.append(node)
            continue
        image_texts = extract_markdown_images(node.text)
        current_node = node
        for alt_text,link in image_texts:
            before,after = current_node.text.split(f"![{alt_text}]({link})", maxsplit=1)
            if before != "":
                # The before contains the text portion
                new_nodes.append(TextNode(before,TextType.plain_text))
                # It is the middle link node that we delimited on
            # No need to check for "" here, because even if this is "" in after we need to append the middle node by createing it
            new_nodes.append(TextNode(alt_text,TextType.images,link))
            # It holds the after node
            current_node = TextNode(after, TextType.plain_text)
        if current_node.text != "":
            new_nodes.append(current_node)
    return new_nodes
