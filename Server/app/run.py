from flask import Flask
from app.controllers.light_controller import light_controller
from app.controllers.chat_controller import chat_controller
import json
import openai

app = Flask(__name__)

# Load the configuration from a JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# Extract the values from the configuration
bridge_ip = config['bridge_ip']
username = config['username']
lights_ids = config['lights']

# Load the API key from a JSON file
with open('api_key.json', 'r') as f:
    api_config = json.load(f)

# Set your API key
openai.api_key = api_config['api_key']

app.register_blueprint(light_controller)
app.register_blueprint(chat_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
