import unittest
from block_to_block_type import BlockType,block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "Hello my name is kradmoned"
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)
    
    def test_heading(self):
        blocks = []
        blocks.append("# Heading 1")
        blocks.append("## Heading 2")
        blocks.append("### Heading 3")
        blocks.append("#### Heading 4")
        blocks.append("##### Heading 5")
        blocks.append("###### Heading 6")
        for block in blocks:
            self.assertEqual(block_to_block_type(block),BlockType.HEADING)
        false_block = "#heading"
        self.assertNotEqual(block_to_block_type(false_block), BlockType.HEADING)
    
    def test_code(self):
        block = """```
printf("Hello,world");
printf("This is me");
```"""     
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    
    def test_quote(self):
        block = """>hello
> Jello
>bello"""
        false_block = """> hello
> jello
 >lelo"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type(false_block), BlockType.QUOTE)
    def test_unordered_list(self):
        block = """- hello
- Today
- is morning"""
        self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)
        false_blocl = """- Helo
-Today
-is morning"""
        self.assertNotEqual(block_to_block_type(false_blocl), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = """1. Hello
2. Jello
3. Fellow"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        false_block = """1. Hello
2. Jello
4. fello"""
        self.assertNotEqual(block_to_block_type(false_block), BlockType.ORDERED_LIST)