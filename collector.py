# AI Memory Assistant Project
# git status# Open conversation file in append mode

# Start loop

# Take user input

# If input is DONE -> break loop

# Else -> write input to file

# Close file
import json
from datetime import datetime
import os

FILE_NAME = "memory.json"

def load_memory():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_memory(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    memory = load_memory()

    print("Type 'done' to end session.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "done":
            print("Session saved.")
            break

        entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "role": "USER",
            "message": user_input
        }

        memory.append(entry)
        save_memory(memory)

if __name__ == "__main__":
    main()