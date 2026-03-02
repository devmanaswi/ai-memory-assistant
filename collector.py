# AI Memory Assistant Project
# git status# Open conversation file in append mode

# Start loop

# Take user input

# If input is DONE -> break loop

# Else -> write input to file

# Close file
from datetime import datetime

def start_session():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"\n---------- NEW SESSION {timestamp} ----------\n"

def save_message(file, role, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f"{timestamp} {role}: {message}\n")

def main():
    with open("conversation.txt", "a", encoding="utf-8") as f:
        f.write(start_session())

        while True:
            user_input = input("You: ")

            if user_input.strip().lower() == "done":
                print("Session ended.")
                break

            save_message(f, "USER", user_input)

if __name__ == "__main__":
    main()