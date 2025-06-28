from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("TestBot", read_only=False, 
              logic_adapters=[
                  
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "I am sorry, but I do not understand.",
                      "maximum_similarity_threshold": 0.90
                  }
                  ])

List_trainer= ListTrainer(bot).train([
    "Hello!",
    "Hi there!",
    "What can you do?",
    "I can chat with you and answer your questions!",
    "What is your name?",
    "My name is TestBot.",
    "What is the weather like today?",
    "I am not sure, but you can check a weather website for the latest updates.",
    "exit || quit || stop || bye",
    "Goodbye! Have a great day!",
])

while True:
    user_response = input("You: ")
    bot_response = bot.get_response(user_response)
    print("Bot:", bot_response)