from textnode import TextNode
import os
import shutil
from generate_page import generate_pages_recursive, recursive_copy
def main():
    # textnode = TextNode("This is some anchor text", "link", "ttps://www.boot.dev")
    # print(textnode)

    recursive_copy()
    generate_pages_recursive("./template.html")




if __name__ == "__main__":
    main()