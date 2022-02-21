import socket
import xml.etree.ElementTree as xml


soc = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
host = socket.gethostname()
port = 5000
soc.bind(('127.0.0.1',5000))
soc.listen(5)
print ('socket прослушивает')

while True:
    conn, addr = soc.accept()


sock.close()
