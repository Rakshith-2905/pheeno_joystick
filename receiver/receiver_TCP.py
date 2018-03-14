import socket

class create_sockets:
    def __init__(self, IP,port):
        self.IP = IP
        self.port = port

    def bind(self):

        # Create a socket for TCP communication
        self.sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_STREAM) # TCP
        #managing error exception
        try:
            self.sock.bind((self.IP, self.port))
            print 'bind sucess'
            print ('IP {} socket awaiting messages on port'.format(self.IP,self.port))
        except socket.error:
            print 'Bind failed '

    def receive_message(self):
        self.sock.listen(5)
        (conn, addr) = self.sock.accept()
        data, addr = conn.recvfrom(4096) # buffer size is 1024 bytes
        return data

if __name__ == '__main__':

    # IP address of the host, the device that is receiving the message
    # Create a port that is not been used in the network you can check
    agent1 = create_sockets("192.168.0.10",6062)
    agent1.bind()
    while True:
        data = agent1.receive_message()
        print data
