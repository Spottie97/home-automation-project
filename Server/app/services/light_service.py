from app.models.huelight import HueLightModel
from app.services.error_service import ErrorService

class LightService:
    @staticmethod
    def create_lights(bridge_ip, username, lights_ids):
        try:
            light1 = HueLightModel(bridge_ip, username, lights_ids[0])
            light2 = HueLightModel(bridge_ip, username, lights_ids[1])
            light3 = HueLightModel(bridge_ip, username, lights_ids[2])
            return light1, light2, light3
        except Exception as e:
            ErrorService.raise_error(2003, additional_info=str(e))
