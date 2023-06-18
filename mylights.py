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

# Replace with your actual bridge IP and username
bridge_ip_address = 'your bridge ip address'
username = 'your username'

# Create HueLight objects for each of your lights
# Replace with your actual light IDs
light1 = HueLight(bridge_ip_address, username, 'light id 1')
light2 = HueLight(bridge_ip_address, username, 'light id 2')
light3 = HueLight(bridge_ip_address, username, 'light id 3')

# Control the lights
light1.turn_on()
light2.turn_off()
light3.turn_on()


