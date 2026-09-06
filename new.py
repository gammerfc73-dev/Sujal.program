import webbrowser

print("🤖 Sujal Assistant")
print("Type commands like:")
print("open Google")
print("open TikTok")
print("open YouTube")
print("exit")

while True:
    command = input("\nYou: ").lower().strip()

    if command == "open google":
        print("🤖 Opening Google...")
        webbrowser.open("https://www.google.com")

    elif command == "open tiktok":
        print("🤖 Opening TikTok...")
        webbrowser.open("https://www.tiktok.com")

    elif command == "open youtube":
        print("🤖 Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif command == "exit":
        print("🤖 Goodbye! 👋")
        break

    else:
        print("🤖 I don't know that command yet.")
