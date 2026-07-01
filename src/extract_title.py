
# Will later refactor it 
def extract_title(markdown: str) -> str:
    """
    Extract h1 header from markdown and return it
    """
    for line in markdown.split("\n"):
        
        if line.strip().startswith("# "):
            return line.strip()[2:]
    # If no h1 header in file
    raise ValueError("no h1 header found")