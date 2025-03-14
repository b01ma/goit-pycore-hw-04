import sys
import os
from pathlib import Path
from colorama import Fore, Back, Style

def get_dir_tree(dir_path: Path, indent: int = 0):
    """Recursively prints the directory structure"""
    try:
        if not dir_path.is_dir():
            return

        items = list(dir_path.iterdir())  # Could raise PermissionError

        for item in items:
            if item.is_file():
                print(Style.RESET_ALL, "\t" * indent + Fore.GREEN + f"file: {item.name}")

        for item in items:
            if item.is_dir():
                if item.is_symlink():
                    print(Fore.YELLOW + f"Skip symbolic link: {item.name}", Style.RESET_ALL)
                    continue 
                print(Style.RESET_ALL, "\t" * indent + Fore.BLUE + f"[dir]: {item.name}/", Style.RESET_ALL)
                get_dir_tree(item, indent + 1)

    except PermissionError:
        print(Fore.RED + f"Permission denied: {dir_path}", Style.RESET_ALL)
            

def main():
    """
        Main function to handle command-line execution
        Takes only 1 argument: directory path
    """
    if len(sys.argv) != 2:
        print(Fore.RED + f"Usage: {Back.YELLOW + '[directory_path]'}{Style.RESET_ALL} {Fore.RED + 'is missing or incorrect'}")
        Style.RESET_ALL
        sys.exit(1)

    directory_path = sys.argv[1]

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print(Back.GREEN + f"Directory found: {directory_path}", Style.RESET_ALL)
        dir_path = Path(directory_path) 
        
        get_dir_tree(dir_path)
    else:
        print(Fore.RED + f"Error: {directory_path} is not a valid directory or does not exist.")
        sys.exit(1)

