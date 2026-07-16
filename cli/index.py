import argparse
import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parser.parser import ProjectParser
from storage.sqlite import SQLiteStorage

def main():
    parser = argparse.ArgumentParser(description="Index a Python project into PyGraph")
    parser.add_argument("project_dir", help="Path to the Python project directory")
    parser.add_argument("--db", default="pygraph.db", help="Path to SQLite database")

    args = parser.parse_args()

    if not os.path.isdir(args.project_dir):
        print(f"Error: {args.project_dir} is not a valid directory.")
        return

    storage = SQLiteStorage(args.db)
    project_parser = ProjectParser(args.project_dir, storage)
    
    print(f"Parsing project at {args.project_dir}...")
    project_parser.parse_all()
    print(f"Graph stored successfully in {args.db}.")

if __name__ == "__main__":
    main()
