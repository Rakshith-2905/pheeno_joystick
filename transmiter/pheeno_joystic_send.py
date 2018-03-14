"""
Send gamepad Logitecg F310 to pheenos over TCP protocol
"""


from gamepad import *
from sender_TCP import *


# create_agents()
a = create_agents()
print("{} agents created".format(a))

while True:

    out = get()
    if out[4]:
        x = 0
        message = (str(out[1])+','+str(out[0])+';')
        print("agent 0 is controlled {}".format(message))
        agent[int(x)].send_message(message)
    if out[5]:
        x = 1
        try:
            message = (str(out[1])+','+str(out[0])+';')
            print("agent 1 is controlled {}".format(message))
            agent[int(x)].send_message(message)
        except:
            print("Agent not available")
    if out[6]:
        x = 2
        try:
            message = (str(out[1])+','+str(out[0])+';')
            print("agent 2 is controlled {}".format(message))
            agent[int(x)].send_message(message)
        except:
            print("Agent not available")
    if out[7]:
        x = 3
        try:
            message = (str(out[1])+','+str(out[0])+';')
            print("agent 3 is controlled {}".format(message))
            agent[int(x)].send_message(message)
        except:
            print("Agent not available")
    if out[8]:
        x = 4
        try:
            message = (str(out[1])+','+str(out[0])+';')
            print("agent 4 is controlled {}".format(message))
            agent[int(x)].send_message(message)
        except:
            print("Agent not available")
    if out[9]:
        x = 5

        try:
            message = (str(out[1])+','+str(out[0])+';')
            print("agent 5 is controlled {}".format(message))
            agent[int(x)].send_message(message)
        except:
            print("Agent not available")

    if out[10]:
        for i in range(a):
            message = ('Normalize;')
            print message
            agent[i].send_message(message)
    if out[11]:
        for i in range(a):
            message = (str(out[1])+','+str(out[0])+';')
            print ("all agents are being controlled with {}".format(message))
            agent[i].send_message(message)
