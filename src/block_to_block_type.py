from enum import Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE  = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    """
    Returns the Block Type of a block
    """
    if block.startswith(("# ","## ","### ","#### ","##### ", "###### " )):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_quote(block: str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_unordered_list(block:str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def is_ordered_list(block:str) -> bool:
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
    return True
