import serial
import socket
import time
import os.path

BAUD_RATE = 9600

class data_trans:
    def __init_(self,message):
        self.usb = None

    def connect_usb(self):
        # USB Serial Options
        usb_options = ['/dev/ttyACM0', '/dev/ttyACM1']
        usb_options_existing = filter(os.path.exists, usb_options)
        assert(len(usb_options_existing) == 1)
        usb_port = usb_options_existing[0]
        print(usb_port)

        while True:
            try:
                print("Attempting to connect...")
                self.usb = serial.Serial(usb_port, BAUD_RATE)
                self.usb.close()
                time.sleep(2)
                self.usb.open()
                time.sleep(2)
                print("Connected!")
                break
            except serial.SerialException:
                print("[ERROR] Could not connect to requested port.")
                time.sleep(1)

    def write_usb(self,message):

        # Send information over USB.
        self.usb.flush()
        self.usb.write(message)
        self.usb.flush()



if __name__ == '__main__':

    # Establish USB connection
    a = data_trans()
    a.connect_usb()

    while True:
        messag = 'HI'
        a.write_usb(messag)


