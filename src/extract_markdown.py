import re
def extract_markdown_images(text: str) -> list[tuple[str,str]]:
    # Captures in the form (alttext, url)
    pattern = r"!\[(.+?)\]\((.+?)\)"
    return re.findall(pattern,str)

def extract_markdown_links(text: str):
    # The same as the image one but here we use the negative look behind to select those that dont start with !
    pattern = r"(?<!!)\[(.+?)\]\((.+?)\)"
    return re.findall(pattern, text)