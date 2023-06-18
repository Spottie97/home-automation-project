from flask import Flask, request
from mylights import HueLight

app = Flask(__name__)

# Replace with your actual bridge IP, username, and light IDs
light1 = HueLight('bridge ip', 'username', 'light id 1')
light2 = HueLight('bridge ip', 'username', 'light id 2')
light3 = HueLight('bridge ip', 'username', 'light id 3')

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
    # You can add similar blocks for light 2 and light 3
    # ...

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
