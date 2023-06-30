import openai
from services.error_service import ErrorService

class ChatService:
    @staticmethod
    def generate_message(user_message):
        try:
            # Generate a response using the OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_message,
                max_tokens=60
            )

            # Extract the generated message
            ai_message = response.choices[0].text.strip()
            return ai_message
        except Exception:
            ErrorService.raise_error(1004)
