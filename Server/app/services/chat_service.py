import openai

class ChatService:
    @staticmethod
    def generate_message(user_message):
        # Generate a response using the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=60
        )

        # Extract the generated message
        ai_message = response.choices[0].text.strip()
        return ai_message
