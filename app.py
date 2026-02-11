from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)
def load_data():
    try:
        df = pd.read_csv('dataset.csv')
        return df
    except FileNotFoundError:
        print("Error: dataset.csv file not found")
        return None
    except pd.errors.EmptyDataError:
        print("Error: dataset.csv file is empty")
        return None

def process_data(df):
    intents = {}
    for index, row in df.iterrows():
        question = row['question'].lower().strip() 
        answer = row['answer']
        if question not in intents:
            intents[question] = answer
    return intents

def respond(user_input, intents):
    user_input = user_input.lower().strip() 
    if user_input in intents:
        return {"response": intents[user_input]}
    else:
        return {"response": "I didn't understand that. Can you please rephrase?"}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json.get('message')
    if message:
        df = load_data()
        if df is not None:
            intents = process_data(df)
            response = respond(message, intents)
            return jsonify(response)
        else:
            return jsonify({"error": "Error loading data"}), 500
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)