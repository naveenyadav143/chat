print("Hello! I am ChatBot 🤖. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()   # take input in lowercase for easy matching

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello there! How can I help you today?")
    
    elif "name" in user_input:
        print("ChatBot: My name is SimpleBot. What's yours?")
    
    elif "weather" in user_input:
        print("ChatBot: I can’t check the weather right now, but it looks like a great day! ☀️")
    
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {now}")
    
    elif "bye" in user_input or "exit" in user_input:
        print("ChatBot: Goodbye! Have a nice day 😊")
        break
    
    else:
        print("ChatBot: Sorry, I don’t understand that. Can you rephrase?")
