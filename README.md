# Pheeno Joystick
This is a project for controlling the [Pheeno robot](http://www.math.ucla.edu/~bertozzi/papers/PheenoICRA2016.pdf). 

## Software Dependencies

- Python 2.7
- pygame

## Outline of the project

This project is segmented into two nodes, the transmission node and the receiving node. This uses pygame to get data from the joystick and sockets to establish TCP/IP communication.

## File Structure

1. Both the transmitter and the receiver should be connected to the same wifi network.
2. The transmitter folder contains the program for transmission of the joystick commands.`
3. The receiver folder contains the programs for the receiving of the joystick commands.

## How to run the project

1. Start a new terminal in the transmitter node and run the python file `$ python pheeno_joystick_send.py`
2. This program will demand the IP address of the other nodes to be entered as argument.
3. In the receiver node upload the arduino code to the teensy microcontroller
3. In the receiver node run the python file `$ python pheeno_joystick_receive.py`.
