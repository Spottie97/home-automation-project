import requests
import json

class HueLight:
    def __init__(self, bridge_ip_address, username, light_id):
        self.bridge_ip_address = bridge_ip_address
        self.username = username
        self.light_id = light_id

    def set_state(self, on):
        data = {'on': on}
        response = requests.put(f'http://{self.bridge_ip_address}/api/{self.username}/lights/{self.light_id}/state', data=json.dumps(data))
        return response.status_code == 200

    def turn_on(self):
        return self.set_state(True)

    def turn_off(self):
        return self.set_state(False)