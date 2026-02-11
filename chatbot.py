import pandas as pd
import random

# Load the dataset from the CSV file
df = pd.read_csv('dataset.csv')

# Create a dictionary to store the questions and corresponding answers
intents = {}
for index, row in df.iterrows():
    question = row['question'].lower().strip() 
    answer = row['answer']
    if question not in intents:
        intents[question] = answer

# Create a function to respond to the user input
def respond(user_input):
    user_input = user_input.lower().strip() 
    if user_input in intents:
        return intents[user_input]
    else:
        return "I didn't understand that. Can you please rephrase?"

# Create a simple chatbot interface
def chatbot():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye' or user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        response = respond(user_input)
        print("Bot: ", response)

# Run the chatbot
chatbot()