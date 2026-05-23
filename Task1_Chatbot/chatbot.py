print("=================================")
print("      SIMPLE PYTHON CHATBOT      ")
print("=================================")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great. Thanks for asking!")

    elif "your name" in user_input:
        print("Bot: I am a rule-based chatbot.")

    elif "who created you" in user_input:
        print("Bot: I was created by Maruthi Rao.")

    elif "help" in user_input:
        print("Bot: You can ask me simple questions.")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print("Bot: Today's date is", today)

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")