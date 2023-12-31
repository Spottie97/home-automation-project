# Home Automation Project
## Description
The aim of this project is to develop a server on my Raspberry Pi that can Automate things in my house. I will update the project as I move along. I will be starting with the lights. Since this project will be an app I would like it to be accessible from anywhere in the world. Thus I will need to build an API for this, I will also develop a mobile app to control the API as I find it be more convient.

## Phases of Development
 - Ability to turn lights on/off. The lights I use are the Philips Hue lights as they connect to the WiFi.
 - Ability to open blinds, I build my own electric blinds, I will post a link to them once I get to this point.
 - Ability to communicate with items with in the house using voice commands via ChatGPT
 - Ability to control my speakers volume, skip, play, pause, voice search, connect to my phone to access my spotify playlist
 - Ability to control my cooking equipment e.g. stove, rice cooker etc.
 - Ability to turn TV on/off.
 - Ability to know my location in the house at all times and then pick the speaker closest to me to respond to my voice command.
 - Ability to Google/Bing something for me
 - Ability to access my calander and modify it.

## Tools and Languages used
 - React Native
 - Java
 - Python
 - HuggingFace LLM API
 - Google API
 - Spotify API
 - Philip Hue API

## How to use
Currently not in working state but this is how it will work.
App
- Create an account or sign into account
- You will now see a blank page with a "+" icon in the top right of the screen.
- Interact withe "+" icon
- This will prompt you to add a new device, currently it limited to specific device but just follow the on screen instructions to add a new device.
- Save changes
- You will now see a new icon appear on the once blank page, this is the device you just added.
- You can now tap on the icon and it will take you to a new page were you can controll this device from.
- Thats it, you all set up.

## Deployment Guide
Since this project is being developed on a different machine then the one its going to run we will create the .ini file once it has been deployed on the Raspberry Pi.
To do this you can follow these steps:
 1. Create a new service file for your script with sudo nano /etc/systemd/system/mylights.service. Replace "mylights" with the name you want to give your service.
 2. In the editor that opens, add the following:
```
[Unit]
Description=My Lights Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /path/to/your/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
 Replace /path/to/your/main.py with the absolute path to your main.py script. The Restart=always directive means the service will restart if it ever crashes or stops for any reason.
 3. Save the file and exit the editor by pressing Ctrl+X, then Y to confirm saving the changes, and finally Enter to confirm the file name.
 4. Enable the service so it starts on boot:
```
sudo systemctl enable mylights.service
```
 5. Start the service now so you don't have to reboot:
```
sudo systemctl start mylights.service
```
 6. Check the status of your service to make sure it's running correctly:
```
sudo systemctl status mylights.service
```
The status command will show you if the service is active and running, and also show the latest log messages from your script. If there are any errors, they will appear here.

Please note that this will run your script as root. If you want to run it as a different user, you can add a User=username line under the [Service] section, replacing username with the name of the user.

Also, be aware that this will run your script in the background, and it will not be able to receive input from the keyboard or output to the screen. If your script depends on user input or you need to see the output, you'll have to modify it to read input from a file or write output to a file.
