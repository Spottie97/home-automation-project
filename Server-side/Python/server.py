import json
from flask import Flask, request
from mylights import HueLight

app = Flask(__name__)

# Load the configuration from a JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# Extract the values from the configuration
bridge_ip = config['bridge_ip']
username = config['username']
lights_ids = config['lights']

# Create the HueLight objects
light1 = HueLight(bridge_ip, username, lights_ids[0])
light2 = HueLight(bridge_ip, username, lights_ids[1])
light3 = HueLight(bridge_ip, username, lights_ids[2])

@app.route('/lights', methods=['POST'])
def control_lights():
    data = request.get_json()
    
    # Control light 1
    if 'light1' in data:
        if 'on' in data['light1']:
            if data['light1']['on']:
                light1.turn_on()
            else:
                light1.turn_off()
        if 'color' in data['light1']:
            light1.set_color(data['light1']['color']['hue'], data['light1']['color']['sat'])

    # Control light 2
    if 'light2' in data:
        if 'on' in data['light2']:
            if data['light2']['on']:
                light2.turn_on()
            else:
                light2.turn_off()
        if 'color' in data['light2']:
            light2.set_color(data['light2']['color']['hue'], data['light2']['color']['sat'])
            
    # Control light 3
    if 'light3' in data:
        if 'on' in data['light3']:
            if data['light3']['on']:
                light3.turn_on()
            else:
                light3.turn_off()
        if 'color' in data['light3']:
            light3.set_color(data['light3']['color']['hue'], data['light3']['color']['sat'])
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
