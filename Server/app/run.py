from flask import Flask
from app.controllers.light_controller import light_controller
from app.controllers.chat_controller import chat_controller
from app.services.error_service import ErrorService, CustomError
import openai
import os
import ast

app = Flask(__name__)

# Extract the values from the environment variables
try:
    bridge_ip = os.environ['BRIDGE_IP']
    username = os.environ['USERNAME']
    lights_ids = ast.literal_eval(os.environ['LIGHT_IDS'])  # Parses the string back into a list

    # Set your API key
    openai.api_key = os.environ['API_KEY']
except KeyError as e:
    ErrorService.raise_error(3006, additional_info=f"Environment variable not found: {str(e)}")
except Exception as e:
    ErrorService.raise_error(3007, additional_info=str(e))

app.register_blueprint(light_controller)
app.register_blueprint(chat_controller)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        ErrorService.raise_error(3005, additional_info=str(e))
