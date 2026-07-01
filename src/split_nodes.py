from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


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


def split_nodes_delimiter(old_nodes: list[TextNode], delimeter: str, text_type: TextType )-> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        # These nodes are already processed
        if node.text_type !=  TextType.plain_text:
            new_nodes.append(node)
            continue
        # For text Nodes
        texts = node.text.split(delimeter)
        # In case of incorret markdown meaning no closing delimeter 
        if len(texts) % 2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for i in range(len(texts)):
            # First one keeps the same type as original
            if (i % 2) == 0:
                #In case of empty string, we will not append as it is not required
                if texts[i] == "":
                    continue
                new_nodes.append(TextNode(texts[i], node.text_type))
            # It is the delimited one
            else:
                if texts[i] == "":
                    continue
                new_nodes.append(TextNode(texts[i], text_type))
    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Split a list of text nodes based on links

    Attributes:
        old_nodes: A list of nodes in which , an link text will be checked
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.plain_text:
            new_nodes.append(node)
            continue
        image_texts = extract_markdown_links(node.text)
        current_node = node
        for alt_text,link in image_texts:
            before,after = current_node.text.split(f"[{alt_text}]({link})", maxsplit=1)
            if before != "":
                # The before contains the text portion
                new_nodes.append(TextNode(before,TextType.plain_text))
                # It is the middle link node that we delimited on
            # No need to check for "" here, because even if this is "" in after we need to append the middle node by createing it
            new_nodes.append(TextNode(alt_text,TextType.link,link))
            # It holds the after node
            current_node = TextNode(after, TextType.plain_text)
        if current_node.text != "":
            new_nodes.append(current_node)
    return new_nodes