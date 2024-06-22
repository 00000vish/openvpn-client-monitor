# OpenVPN Client Monitor 

OpenVPN Client Monitor will check the network connection periodically and can shutodnw/restart the OpenVPN client service if the connection is down, it can also check if the ip is leaking and restart it or shutdown the computer.


## ⚠️ Warnings
- #### _For Linux running `openvpn@client.service` only! (currently)_
   - _but can be easily changed your requirements._
- #### _Does not garantee this will prevent ip leaking!_
## Features
- Defualt: Checks every 5 mins and restarts openvpn@client.service if connection is down.
- Very customizable via command line args.
- Configurable checking interval.
- Configurable restart/shutdown/more to come.


# Installation

## Using `installer.sh`
Run installer.sh as sudo to install and setup auto start
```sh
sudo chmod +x ./installer.sh
sudo ./installer.sh
```

## Manual Installation

Install requirements to run/build the OpenVPN Client Monitor with
```sh
python3 -m pip install -r requirements.txt
```


### Building Binary
Make sure you installed requrement.txt first and then run

```sh
pyinstaller -F main.py
```
The single file binary will be in `./dist/main`.

You can run it by _(sudo required)_
```sh
sudo ./dist/main
```

### Setup Autostart
Copy the binary over `./user/bin/` 
```sh
sudo cp ./dist/main /usr/bin/openvpn-client-mon
```

Copy systemd file over to `./etc/systemd/system/`
```sh
cp ./etc/systemd/system/openvpnclientmon.service /etc/systemd/system/openvpnclientmon.service
```
Enable and Start OpenVPN Client Monitor 
```sh
sudo systemctl enable openvpnclientmon.service
sudo systemctl start openvpnclientmon.service
```

### Running it as a script _(not recommended)_

Install requrements as sudo first
```sh
sudo python3 -m pip install -r requirements.txt
```
You can run it by _(sudo required)_
```sh
sudo python3 main.py
```

# Command Line Args

To print command line args options
```sh
./main -h

```

To check the network connection every 100 seconds

```sh
./main -t 100 
```

To check the network connection every 100 seconds and shutdown computer

```sh
./main -t 100 -a 2
```

To check the network connection every 100 seconds and restart 

```sh
./main -t 100 -a 1
```

## Development

Want to contribute? Great!, pull requests are welcomed! Thank you!

### TODO
- [ ] implement logging/log file
- [ ] implement more actions
- [ ] load settings from a config yaml file

## License

MIT
