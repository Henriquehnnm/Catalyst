import json
from pathlib import Path

def main_reader():
    base_dir = Path(__file__).parent

    file_path = base_dir / "oldapi.json"
    
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return f"File not found in {file_path}"

