
<div style="text-align: right;">
  <img src="https://github.com/Vishal01Mehra/NetPing/blob/main/Resources/Main.jpg">
</div>

# NetPing 

This Python script provides a GUI to monitor the connection status of various devices by pinging their IP addresses. The status is displayed using circular indicators that turn green when a device is reachable and red when it is not.

## Features

- Monitor multiple devices by their IP addresses.
- Visual indicators (green/red circles) to show connection status.
- Asynchronous ping checks to keep the GUI responsive.
- Adjustable ping check interval.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Subprocess module

## Installation

- Clone the repository:
   ```sh
   git clone https://github.com/Vishal01Mehra/NetPing.git
   cd NetPing
   
## Adjusting the Ping Check Interval
- The interval between ping checks can be adjusted by changing the interval parameter (in milliseconds) when creating NetPing instances:
   ``` python
   indicator = ConnectionIndicator(root, name, ip, i, interval=500)

## Adding more devices
- To monitor additional devices, add them to the devices dictionary in the NetPing.py file:
   ``` python
   devices = {
       'Router': '192.168.1.1',
       'Camera': '192.168.1.2',
       'Printer': '192.168.1.3',
       'New Device': '192.168.1.4'
   }

## Usage
   ```python
   python3 NetPing.py
