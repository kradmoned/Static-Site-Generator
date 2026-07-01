import os
import shutil


def copy_tree(source : str, dest: str, curr: str) -> None:
    # Build current source and destination
    curr_source = os.path.normpath(os.path.join(source, curr))
    curr_dest = os.path.normpath(os.path.join(dest, curr))
    print(f"Current Destinatio = {curr_dest}")
    # In case the directory does not exist
    if not os.path.exists(curr_dest):
        print(f"{curr_dest} does not exist")
        os.mkdir(curr_dest)
        print(f"Created {curr_dest}")
    # Copy everything in the current
    for item in os.listdir(curr_source):
        # Since item is relative to curr_source, it only list names
        item_path = os.path.join(curr_source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, curr_dest)
            print(f"Copied {item_path} to {curr_dest}")
        else:
            copy_tree(curr_source, curr_dest, item)
            


def prepare_dest(source: str, dest: str) -> None:
    """
    Prepare the destination directory by deleting previous and copying the source directory to it
    """
    if not os.path.exists(source):
        raise FileNotFoundError("source directory does not exist")
    
    # If dest folder exists delete it
    if os.path.exists(dest):
        print(f"A {dest} folder Already Exist")
        shutil.rmtree(dest)
        print(f"Previous {dest} deleted")
    print(f"Copy Started {source} {dest}")
    copy_tree(source, dest, ".")

