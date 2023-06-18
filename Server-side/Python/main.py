from mylights import HueLight

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

# Change light color
if light1.set_color(0, 254):
    print('Changed color of light1 to red')
else:
    print('Failed to change color of light1')
