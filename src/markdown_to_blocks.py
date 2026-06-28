def markdown_to_blocks(markdown: str) -> list[str]:
    """
    It takes a raw markdown string(a document) and return list of block strings

    Attributes:
        markdown: A string that is to be converted to blocks
    """
    # Later need to change it bad markdown such as \nspace\n etc, will use regular expression
    # In correct markdown each block is seperated by \n\n and also we are stripping of extra, and finally filtering out empty strings
    return list(filter(lambda x : x != "",(map(lambda x : x.strip(), markdown.split("\n\n")))))
    