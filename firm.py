import socket
#udp listener coroutine
def listen():
    UDP_IP = ""
    UDP_PORT = 5005
    yield(True)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while(True):
        data, addr = sock.recvfrom(1024)
        yield(data, addr) # buffer size is 1024 bytes

#send message (obviously)
def send(msg,add):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg, (add, 5005))
    return()

#interpret UDP commands
def logic(passinval, source):
    parseflags = []
    if(passinval == "00:00:00:00:00"):
        return(None)
    passinval = passinval.split(":")
    for x in range(0, len(passinval)):
        if(passinval[x] == '01'):
            send("01:00:00:00:00")

#function to run
def runner():
    networking = listen()
    currentnetpack = next(networking)
    while(True):
        print("==== LISTENING ====")
        currentnetpack = next(networking)
        currentnetsource = currentnetpack[1][0]
        currentnetput = currentnetpack[0]
        currentnetput = currentnetput.decode('utf-8')
        print("==== RECV ====")
        print(str(currentnetsource) + " - " + str(currentnetput))


send(str.encode("00:00:00:00:00"),str.encode("127.0.0.1"))
#runner()
