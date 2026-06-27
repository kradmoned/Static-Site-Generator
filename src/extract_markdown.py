import re
def extract_markdown_images(text: str) -> list[tuple[str,str]]:
    """
    Returns a list of tuples of (alt_text,link) from the img
    """
    # Captures in the form (alttext, url)
    pattern = r"!\[([^]]*)\]\(([^)]*)\)"
    return re.findall(pattern,text)

def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    """
    Return a list of tuples of description,url
    """
    # The same as the image one but here we use the negative look behind to select those that dont start with !
    pattern = r"(?<!!)\[([^]]*)\]\(([^)]*)\)"
    return re.findall(pattern, text)