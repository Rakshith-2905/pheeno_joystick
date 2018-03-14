import socket

agent = []

class create_sockets:
    def __init__(self, IP,port):
        self.IP = IP
        self.port = port

    ## Create a Socket in the given port address.
    def send_message(self,Message):
        # print "target IP:", self.IP
        # print "target port:", self.port

        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_STREAM) # UDP
        sock.connect((self.IP, self.port))
        sock.send(Message)
        # sock.close

def create_agents():
    global agents
    pheeno_no = raw_input("Give the pheeno no: ")
    numbers = map(int, pheeno_no.split())
    # IP address of the host, the device that is receiving the message
    # the port that was created by the host or receiver
    for i,ip in enumerate(numbers):

        IP = "192.168.119." + str(ip)
        port = 6062
        print ("Agent{} is having IP {} and connected to port {}".format(i,IP,port))
        agent.append(create_sockets(IP,int(port)))

    return len(numbers)


if __name__ == '__main__':

    create_agents()

    while True:

        message = raw_input("Give the message: ")
        x = raw_input("Enter agent number: ")
        agent[int(x)].send_message(message)
