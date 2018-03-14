"""
Receive Joystick Logitech F310 values over TCP
Enter the ip address of the pheenos on line 14.
the ip address can be found by using the command ifconfig on linux terminal
"""


from receiver_TCP import *
#from usb_routine import *

if __name__ == '__main__':

    # IP address of the host, the device that is receiving the message
    # Create a port that is not been used in the network you can check
    agent1 = create_sockets("10.152.138.247", # Enter the IP address of the pheeno
                            6062) # Port the pheeno wants to use
    agent1.bind()

    # # Establish USB connection
    # a = data_trans()
    # a.connect_usb()

    while True:
        data = agent1.receive_message()
        print(data)
