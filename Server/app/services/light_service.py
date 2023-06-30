from models.huelight import HueLightModel
from services.error_service import ErrorService

class LightService:
    @staticmethod
    def create_lights(bridge_ip, username, lights_ids):
        try:
            lights = [HueLightModel(bridge_ip, username, light_id) for light_id in lights_ids]
            return lights
        except Exception as e:
            ErrorService.raise_error(2003, additional_info=str(e))

