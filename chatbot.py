print("Hello! I am a chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you?")
    
    elif "how are you" in user_input:
        print("Bot: I am fine What about you?")
    
    elif "your name" in user_input:
        print("Bot: I am a simple Python chatbot.")
    
    elif "who made you" in user_input:
     print("Bot: I was created by Anushka Jha using Python ")

    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day")
        break
    
    else:
        print("Bot: Sorry, I didn't understand that.")
