from flask import Blueprint, request
from app.services.chat_service import ChatService
from app.services.error_service import ErrorService, CustomError

chat_controller = Blueprint('chat_controller', __name__)

@chat_controller.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        # Check if 'message' exists in the request data
        if 'message' not in data:
            ErrorService.raise_error(1001)

        user_message = data['message']

        # Check if the message is empty
        if not user_message.strip():
            ErrorService.raise_error(1002)

        ai_message = ChatService.generate_message(user_message)

        # Check if the response from the AI service is an error
        if 'error' in ai_message:
            ErrorService.raise_error(1003)

        return {'message': ai_message}

    except CustomError as e:
        return {'error': str(e), 'error_code': e.error_code}, 400
