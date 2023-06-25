from flask import Flask
from app.controllers.light_controller import light_controller
from app.controllers.chat_controller import chat_controller
from app.services.error_service import ErrorService, CustomError
import json
import openai
import sys

app = Flask(__name__)

try:
    # Load the configuration from a JSON file
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    ErrorService.raise_error(3001, additional_info="config.json not found")
except Exception as e:
    ErrorService.raise_error(3002, additional_info=str(e)) 

# Extract the values from the configuration
bridge_ip = config['bridge_ip']
username = config['username']
lights_ids = config['lights']

try:
    # Load the API key from a JSON file
    with open('api_key.json', 'r') as f:
        api_config = json.load(f)
except FileNotFoundError:
    ErrorService.raise_error(3003, additional_info="api_key.json not found")
except Exception as e:
    ErrorService.raise_error(3004, additional_info=str(e))

# Set your API key
openai.api_key = api_config['api_key']

app.register_blueprint(light_controller)
app.register_blueprint(chat_controller)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        ErrorService.raise_error(3005, additional_info=str(e))

