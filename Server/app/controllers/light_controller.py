from flask import Blueprint, request
from app.services.light_service import LightService

light_controller = Blueprint('light_controller', __name__)
light1, light2, light3 = LightService.create_lights()  # add arguments as needed

@light_controller.route('/lights', methods=['POST'])
def control_lights():
    data = request.get_json()
    # TODO: Add logic here
    return 'OK'
