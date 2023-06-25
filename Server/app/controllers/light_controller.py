from flask import Blueprint, request
from app.services.light_service import LightService
from app.services.error_service import ErrorService, CustomError

light_controller = Blueprint('light_controller', __name__)

# If lights cannot be created, let the exception propagate and crash the app
light1, light2, light3 = LightService.create_lights()  

@light_controller.route('/lights', methods=['POST'])
def control_lights():
    try:
        data = request.get_json()

        if not data:
            ErrorService.raise_error(2001)

        # Add more specific error checks here based on what data you expect
        # For example, if you expect a 'light_id' field:
        if 'light_id' not in data:
            ErrorService.raise_error(2002)

        # TODO: Add logic here
        return 'OK'
    except CustomError as e:
        return {'error': str(e), 'error_code': e.error_code}, 400
