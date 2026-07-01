import unittest
from markdown_to_html_node import markdown_to_html_node
class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
           html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_quote(self):
        md = """
> This is **line one**
>This is line two
>This is line 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>line one</b> This is line two This is line 3</blockquote></div>"
        )
    def test_ul(self):
        md = """
- This is **line one**
- This is line two
- This is line 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>line one</b></li><li>This is line two</li><li>This is line 3</li></ul></div>"
        )


    def test_ol(self):
        md = """
1. This is **line one**
2.    This is line two
3. This is line 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>line one</b></li><li>This is line two</li><li>This is line 3</li></ol></div>"
        )

    def test_heading(self):
        md = """
# Heading

## Heading

### Heading

#### Heading

##### Heading

###### Heading

####### Paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><h1>Heading</h1><h2>Heading</h2><h3>Heading</h3><h4>Heading</h4><h5>Heading</h5><h6>Heading</h6><p>####### Paragraph</p></div>"
        )
    def test_combined(self):
        md = """
# Heading

## Heading

### Heading

#### Heading

##### Heading

###### Heading

####### Paragraph

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```

> This is **line one**
>This is line two
>This is line 3

- This is **line one**
- This is line two
- This is line 3

1. This is **line one**
2.    This is line two
3. This is line 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.maxDiff = None
        self.assertEqual(
            html, 
            "<div><h1>Heading</h1><h2>Heading</h2><h3>Heading</h3><h4>Heading</h4><h5>Heading</h5><h6>Heading</h6><p>####### Paragraph</p><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><blockquote>This is <b>line one</b> This is line two This is line 3</blockquote><ul><li>This is <b>line one</b></li><li>This is line two</li><li>This is line 3</li></ul><ol><li>This is <b>line one</b></li><li>This is line two</li><li>This is line 3</li></ol></div>"
        )
if __name__ == "__main__":
    unittest.main()