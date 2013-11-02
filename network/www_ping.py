# Find the WWW service of an arbitrary host using socket.getaddrinfo

import socket, sys
from pprint import pprint
if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: www_ping.py <hostname_or_ip>'
    sys.exit(2)

hostname_or_ip = sys.argv[1]

try:
    infolist = socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,)
except socket.gaierror, e:
    print 'Name service failure:', e.args[1]
    sys.exit(1)

pprint(infolist)
info = infolist[0]
socket_args = info[:3]
address = info[4]
s = socket.socket(*socket_args)
print 'Attempting to connect using addres', info[4]
try:
    s.connect(address)
except socket.error, e:
    print 'Network failure,', e.args[1]
else:
    print 'Success: host', info[3], 'is listening on port 80'

