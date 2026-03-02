

# Start loop

# Take user input

# If input is DONE -> break loop

# Else -> write input to file

# Close file
from datetime import datetime

with open("conversation.txt", "a",encoding="utf-8") as f:
    print(f"----------NEW SESSION  {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}----------")
    while True:
        user_input = input("You: ")
        if (user_input.strip()).lower() == "done":
            break            
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" USER: "+ user_input + "\n")