import random
import datetime

print("Chatbot: Hello! I am your Python chatbot.")
print("Type 'bye' to exit.\n")

greetings = ["Hello!", "Hi there!", "Nice to meet you!", "Hey!"]
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the computer go to the doctor? It caught a virus!",
    "Why do Python programmers wear glasses? Because they can't C."
]

while True:

    user = input("You: ").lower()

    if user in ["hello","hi","hey"]:
        print("Chatbot:", random.choice(greetings))

    elif user == "how are you":
        print("Chatbot: I am doing great! Thanks for asking.")

    elif user == "your name":
        print("Chatbot: I am a simple CLI chatbot built using Python.")

    elif user == "please tell me the time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Chatbot: Current time is", now)

    elif user == "Can u tell me the todays's date":
        today = datetime.date.today()
        print("Chatbot: Today's date is", today)

    elif user == "Tell me a joke":
        print("Chatbot:", random.choice(jokes))

    elif user == "I need a help":
        print("Chatbot: You can ask me about time, date, joke, greetings, or say bye.")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I didn't understand that. Try asking something else.")