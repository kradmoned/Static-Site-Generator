from textnode import TextNode
from textnode import TextType
def main():
    textnode: TextNode = TextNode("Hello", TextType.code_text,"Https://www.google.com")
    print(textnode)
if __name__ == "__main__":
    main()