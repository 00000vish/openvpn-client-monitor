#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run with sudo."
  exit
fi


printf  "\nOpenVPN-Client-Monitor installer"

printf  "\n\nPython3-pip (Required)\n"
read -p 'Install python3-pip? (yes/skip): ' pythonpip

if [ $pythonpip = "yes" ]
  then 
    printf "\n"
    sudo apt install python3-pip
  else  
    echo "skipping..."
fi


printf  "\nPyinstaller (Required)\n"
read -p 'Install Pyinstaller? (yes/skip): ' pyinstaller

if [ $pyinstaller = "yes" ]
  then 
    printf "\n"
    python3 -m pip install pyinstaller
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
cp ./etc/systemd/system/openvpnclientmon.service /etc/systemd/system/openvpnclientmon.service
sudo systemctl enable openvpnclientmon.service
sudo systemctl start openvpnclientmon.service
echo "Done."

printf  "\n\nOpenVPN-Client-Monitor installer Installation Complete!\n\n"
echo  "exiting now... bye"