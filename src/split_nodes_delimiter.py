from textnode import TextNode,TextType
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

           

        
