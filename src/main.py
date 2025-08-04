import sys
import os
import shutil
from generate_page import generate_pages_recursive, recursive_copy
def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    recursive_copy()
    generate_pages_recursive("./template.html", basepath)




if __name__ == "__main__":
    main()