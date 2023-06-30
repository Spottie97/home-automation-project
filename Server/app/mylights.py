from services.error_service import ErrorService
import requests
import json
import logging

class HueLight:
    def __init__(self, bridge_ip_address, username, light_id):
        self.bridge_ip_address = bridge_ip_address
        self.username = username
        self.light_id = light_id

    def set_state(self, on):
        data = {'on': on}
        try:
            response = requests.put(f'http://{self.bridge_ip_address}/api/{self.username}/lights/{self.light_id}/state', data=json.dumps(data))
            response.raise_for_status()
            response_data = response.json()
            if 'error' in response_data[0]:
                ErrorService.raise_error(2004, additional_info=response_data[0]['error'])
        except requests.exceptions.RequestException as e:
            ErrorService.raise_error(2004, additional_info=str(e))

    def turn_on(self):
        return self.set_state(True)

    def turn_off(self):
        return self.set_state(False)
    
    def set_color(self, hue, sat):
        data = {'on': True, 'sat': sat, 'hue': hue}
        try:
            response = requests.put(f'http://{self.bridge_ip_address}/api/{self.username}/lights/{self.light_id}/state', data=json.dumps(data))
            response.raise_for_status()
            response_data = response.json()
            if 'error' in response_data[0]:
                ErrorService.raise_error(2005, additional_info=response_data[0]['error'])
        except requests.exceptions.RequestException as e:
            ErrorService.raise_error(2005, additional_info=str(e))
