import socket
import ssl

bindsocket = socket.socket()
bindsocket.bind(('', 10023))
bindsocket.listen(5)

def what_up(connstream, msg):
    print "what: ", msg
    return False

def connect_with_client(connstream):
    msg = connstream.read()
    while msg:
        if not what_up(connstream, msg):
            break
        msg = connstream.read()

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket,
                                 server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key")
    try:
        connect_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
