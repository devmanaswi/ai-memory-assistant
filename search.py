import json
import os

FILE_NAME = "memory.json"

def load_memory():
    if not os.path.exists(FILE_NAME):
        print("No memory file found.")
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def search_memory(keyword):
    memory = load_memory()
    results = []

    for entry in memory:
        if keyword.lower() in entry["message"].lower():
            results.append(entry)

    return results

def main():
    keyword = input("Enter keyword to search: ")

    results = search_memory(keyword)

    if not results:
        print("No matching memories found.")
    else:
        print(f"\nFound {len(results)} result(s):\n")
        for entry in results:
            print(f"{entry['timestamp']} {entry['role']}: {entry['message']}")

if __name__ == "__main__":
    main()