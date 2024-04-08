from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from api import text2SQL

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)  

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/query', methods=['POST'])
def chat():
    # Process user input and interact with your chatbot/GPT-2 model
    user_input = request.json.get('query', "")
    schema = request.json.get('schema', "")
    if user_input is None:
        return 'Please provide a query', 400
    
    response = text2SQL(schema, user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=8000,debug=True)
