def chatbot():
    print("Hello! I am your chatbot. Type bye to exit.")
    print("---------------------------------------")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! What about you?")

        elif user == "what is your name?":
            print("Bot: I am Shazia's chatbot, made in Python.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'.")


chatbot()
