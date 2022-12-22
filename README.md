# OpenVPN Client Monitor 

OpenVPN Client Monitor will check the network connection periodically and can shutodnw/restart the OpenVPN client service if the connection is down, it can also check if the ip is leaking and restart it or shutdown the computer.


## ⚠️ Warnings
- #### _For Linux running `openvpn@client.service` only!_
- #### _Does not garantee this will prevent ip leaking!_
## Features
- Defualt: Checks every 5 mins and restarts openvpn@client.service if connection is down.
- Very customizable via command line args.
- Configurable checking interval.
- Configurable restart/shutdown/more to come.


## Installation

Install requirements to run/build the OpenVPN Client Monitor with
```sh
python3 -m pip install -r requirements.txt
```


## Building Executable
Make sure you installed requrement.txt first and then run

```sh
pyinstaller -F main.py
```
The single file executable will be in `./dist/main`.

You can run it by _(sudo required)_
```sh
sudo ./dist/main
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

## Command Line Args

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
[ ] implement logging/log file
[ ] implement more actions
[ ] load settings from a config yaml file

## License

MIT
