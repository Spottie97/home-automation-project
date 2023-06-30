class CustomError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class ErrorService:
    error_codes = {
        #ChatBot
        1001: "The request payload does not contain a 'message' key.",
        1002: "The message should not be empty.",
        1003: "An error occurred in the AI service.",
        1004: "An error occurred while generating the message using the OpenAI API.",
        #Lights
        2001: "No JSON data provided.",
        2002: "No 'light_id' field provided in the data.",
        2003: "Error creating lights.",
        2004: "Error setting light state.",
        2005: "Error setting light color.",
        2006: "No 'state' field provided in the data.",
        2007: "Invalid 'light_id' provided.",
        2008: "Invalid 'state' provided.",
        #Blinds

        #Main
        3001: "Configuration file (config.json) not found.",
        3002: "An error occurred while loading config.json.",
        3003: "API configuration file (api_key.json) not found.",
        3004: "An error occurred while loading api_key.json.",
        3005: "An error occurred while starting the Flask application.",
        3006: "Required environment variable not found.",
        3007: "An error occurred while processing environment variables.",
    }

    @classmethod
    def raise_error(cls, error_code):
        if error_code in cls.error_codes:
            raise CustomError(cls.error_codes[error_code], error_code)
        else:
            raise CustomError("Unknown error occurred.", 9999)
