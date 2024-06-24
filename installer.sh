#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run with sudo."
  exit
fi


printf  "\nOpenVPN-Client-Monitor installer"

printf  "\n\nPython3-pip (Required)\n"
read -p 'Install python3? (yes/skip): ' installpython

if [ $installpython = "yes" ]
  then 
    printf "\n"
    sudo apt install python3 python3-pip python3-venv -y
  else  
    echo "skipping..."
fi


printf  "\n\n"
printf  "\nCreating Python3 venv"
python3 -m venv ./venv
source ./venv/bin/activate
printf  "\nDone Creating Python3 venv"

printf  "\n\n"
read -p 'Install required python modules from requirements.txt?  (yes/skip): ' pyinstaller

if [ $pyinstaller = "yes" ]
  then 
    printf "\n"
    python3 -m pip install -r requirements.txt
  else  
    echo "skipping..."
fi

printf  "\n\nBuilding Binary\n\n"
pyinstaller -F main.py
echo "Done."

printf  "\n\nInstall Binary\n"
sudo cp ./dist/main /usr/bin/openvpn-client-mon
echo "Done."

printf  "\n\nSetting up Autorstart\n"
sudo cp ./etc/systemd/system/openvpnclientmon.service /etc/systemd/system/openvpnclientmon.service
sudo systemctl enable openvpnclientmon.service
sudo systemctl start openvpnclientmon.service
echo "Done."

printf  "\n\nOpenVPN-Client-Monitor installer Installation Complete! (bye)\n\n"
