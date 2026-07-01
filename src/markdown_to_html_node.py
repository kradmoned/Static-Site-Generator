from leafnode import LeafNode
from parentnode import ParentNode
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type,BlockType








def markdown_to_html_node(markdown: str) -> ParentNode:
    # convert to blocks
    blocks = markdown_to_blocks(markdown)
    childrens = []
    for block in blocks:
        childrens.append(block_to_html_node(block))
    return ParentNode("div",childrens)
        





def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.PARAGRAPH:
            # the block each contains multiple lines, we want them all to be one single continous sentence
            sentence= " ".join(block.split("\n"))
            node = ParentNode("p",text_to_children(sentence))
            return node
        case BlockType.UNORDERED_LIST:
            li_nodes = block_to_list_items(block)
            ul_node = ParentNode("ul",li_nodes)
            return ul_node
        case BlockType.ORDERED_LIST:
            li_nodes = block_to_list_items(block)
            ol_node = ParentNode("ol",li_nodes)
            return ol_node
        case BlockType.HEADING:
            number_of_hashes = 0
            # There are six ranges of heading from h1 to h6 , by counting number of hashes we can determine the correct tag
            for char in block:
                if char == "#":
                    number_of_hashes += 1
                else:
                    break
            # SInce in the block the text starts after the hashes and a single space or h+1
            starting_index = number_of_hashes + 1
            return ParentNode(f"h{number_of_hashes}",text_to_children(block[starting_index:]))
        case BlockType.QUOTE:
            lines = block.split("\n")
            text = " ".join(list(map(lambda line: line.lstrip(">").strip(),lines)))
            return ParentNode("blockquote",text_to_children(text))
        case BlockType.CODE:
            code_starting_index = 4
            code_ending_index = -3
            # Nested inside pre to preserve formating
            # Code block does not require inline parsing
            return ParentNode("pre",[LeafNode("code", block[code_starting_index:code_ending_index])])


            
            
            


def text_to_children(text: str) -> list[LeafNode]:
    """
    It takes a string and return a list of html nodes representing the children
    """
    # It will convert the text to textnodes which will be then converted to leaf nodes
    return list(map(text_node_to_html_node,text_to_textnodes(text)))
    

def block_to_list_items(block: str) -> list[ParentNode]:
# Each block will be in this form
    #- first
    #- second
    #- third
    lines = block.split("\n")
    # An unordered list consists of many paren
    li_nodes: list[ParentNode] = []

    for line in lines:
    # Now need to remove "- " from the lines
        # Since a line has "- " extra remove and create node representing list item
        li = ParentNode("li",text_to_children(line.split(" ",maxsplit= 1)[1].lstrip()))
        li_nodes.append(li)
    return li_nodes
