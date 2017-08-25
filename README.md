# Wakeserver
This is a simple script that runs on a raspberry pi to allow for remote wake on lan functionallity.
There is a init.d script included that is to be used to run the script on boot.
A simple Flask app is ran with a restfull server which when called wakes the desired server.
All logging is sent to the syslog.

### setup
```
sudo pip install -r requirements.txt # install the requirements
# don't forget to modify the remotePower.service file to the correct user and directory
sudo ln remotePower.service /lib/systemd/system # Add systemd service file
sudo systemctl daemon-reload
sudo systemctl enable remotePower.service
sudo service remotePower start # start the application
```
