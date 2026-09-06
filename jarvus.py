import webbrowser

def assistant(command):
    command = command.lower().strip()

    websites = {
        "open google": "https://www.google.com",
        "open youtube": "https://www.youtube.com",
        "open tiktok": "https://www.tiktok.com",
        "open github": "https://github.com"
    }

    if command in websites:
        print("Opening...")
        webbrowser.open(websites[command])
    elif command == "hello":
        print("Hello! 👋")
    elif command == "exit":
        return False
    else:
        print("I don't understand that command.")

    return True

while True:
    command = input("You: ")

    if not assistant(command):
        print("Goodbye! 👋")
        break
