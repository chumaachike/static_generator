import os
import shutil
from block_markdown import markdown_to_html_node

def recursive_copy(source=None, destination=None):
    if not source and not destination:
        source, destination = "./static/", "./public"
        for filename in os.listdir(destination):
            file_path = os.path.join(destination, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                shutil.copy(file_path, destination)
            elif os.path.isdir(file_path):
                os.makedirs(os.path.join(destination, filename), exist_ok=True)
                recursive_copy(file_path, os.path.join(destination, filename))
        except Exception as e:
            print(f"Failed to move {file_path} to {destination}. Reason: {e}")


def extract_title(markdown):
    blocks = markdown.splitlines()
    for line in blocks:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    html_string = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_html = html_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

import os

def generate_pages_recursive(template_path, dir_path_content=None, dest_dir_path=None):
    if not dir_path_content and not dest_dir_path:
        dir_path_content, dest_dir_path = "./content", "./public"
        
    for filename in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, filename)
        try:
            if os.path.isfile(file_path):
                dest_file_path = os.path.join(
                    dest_dir_path,
                    os.path.splitext(filename)[0] + ".html"
                )
                generate_page(file_path, template_path, dest_file_path)

            elif os.path.isdir(file_path):
                new_dest_dir = os.path.join(dest_dir_path, filename)
                os.makedirs(new_dest_dir, exist_ok=True)
                generate_pages_recursive(template_path, file_path, new_dest_dir)
                
        except Exception as e:
            print(f"Failed to generate and move {file_path} to {dest_dir_path}. Reason: {e}")
