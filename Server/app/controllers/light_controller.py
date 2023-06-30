from flask import Blueprint, request, current_app
from app.services.light_service import LightService
from app.services.error_service import ErrorService, CustomError

light_controller = Blueprint('light_controller', __name__)

# Define lights as a global variable
lights = None

@light_controller.before_app_first_request
def create_lights():
    global lights
    try:
        bridge_ip = current_app.config.get('BRIDGE_IP')
        username = current_app.config.get('USERNAME')
        lights_ids = current_app.config.get('LIGHT_IDS')  

        lights = LightService.create_lights(bridge_ip, username, lights_ids)
    except Exception as e:
        ErrorService.raise_error(2003, additional_info=str(e))

@light_controller.route('/lights', methods=['POST'])
def control_lights():
    global lights
    try:
        data = request.get_json()

        if not data:
            ErrorService.raise_error(2001)

        if 'light_id' not in data:
            ErrorService.raise_error(2002)

        if 'state' not in data:
            ErrorService.raise_error(2006)

        light_id = data['light_id']
        state = data['state']

        if light_id not in [1, 2, 3]:
            ErrorService.raise_error(2007)

        if state == 'on':
            lights[light_id - 1].turn_on()
        elif state == 'off':
            lights[light_id - 1].turn_off()
        else:
            ErrorService.raise_error(2008)

        return 'OK'
    except CustomError as e:
        return {'error': str(e), 'error_code': e.error_code}, 400
