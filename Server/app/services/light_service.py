from app.models.huelight import HueLightModel

class LightService:
    @staticmethod
    def create_lights(bridge_ip, username, lights_ids):
        light1 = HueLightModel(bridge_ip, username, lights_ids[0])
        light2 = HueLightModel(bridge_ip, username, lights_ids[1])
        light3 = HueLightModel(bridge_ip, username, lights_ids[2])
        return light1, light2, light3
