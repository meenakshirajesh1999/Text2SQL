from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from api import text2SQL

app = Flask(__name__)
CORS(app)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def chat():
    # Process user input and interact with your chatbot/GPT-2 model
    user_input = request.json.get('query')
    
    response = text2SQL(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=8000,debug=True)
