from flask import Blueprint, request
from app.services.chat_service import ChatService

chat_controller = Blueprint('chat_controller', __name__)

@chat_controller.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    ai_message = ChatService.generate_message(user_message)
    return {'message': ai_message}
