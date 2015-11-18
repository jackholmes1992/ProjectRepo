Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import socket
>>> sock = socket.socket(socket.AH_INET,socket.SOCK_STREAM)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sock = socket.socket(socket.AH_INET,socket.SOCK_STREAM)
AttributeError: module 'socket' has no attribute 'AH_INET'
>>> sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
>>> sock.bind(("127.0.0.1",8000))
>>> sock.listen(2)
>>> (client,(ip,port)) = sock.accept()
>>> client
<socket.socket fd=9, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 55117)>
>>> port
55117
>>> client.send("WATSUP!")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    client.send("WATSUP!")
TypeError: a bytes-like object is required, not 'str'
>>> message = "WATSUP!"
>>> message.encode('utf-8')
b'WATSUP!'
>>> client.send(message)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    client.send(message)
TypeError: a bytes-like object is required, not 'str'
>>> client.send(message.encode('utf-8'))
7
>>> message = message.encode('utf-8')
>>> client.send(message)
7
>>> client.recv(2012)
b'Hey Server, WATSUP MAAAAN!\n'
>>> data = client.recv(2012)
>>> print(data)
b'chachinggg\n'
>>> sock.bind(("127.0.0.1",8000))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sock.bind(("127.0.0.1",8000))
OSError: [Errno 22] Invalid argument
>>> import ftplib
>>> ftp = ftplib.FTP('ftp.cdrom.com','username','email@address.com')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ftp = ftplib.FTP('ftp.cdrom.com','username','email@address.com')
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 118, in __init__
    self.connect(host)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 153, in connect
    source_address=self.source_address)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 689, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 728, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
>>> ftp = ftplib.FTP()
>>> ftp.connect('127.0.0.1')
'220 ProFTPD 1.3.4c Server (ProFTPD) [::ffff:127.0.0.1]'
>>> ftp.login('book','bookpw')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ftp.login('book','bookpw')
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 419, in login
    resp = self.sendcmd('PASS ' + passwd)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 272, in sendcmd
    return self.getresp()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 245, in getresp
    raise error_perm(resp)
ftplib.error_perm: 530 Login incorrect.
>>> ftp.login()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ftp.login()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 417, in login
    resp = self.sendcmd('USER ' + user)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 272, in sendcmd
    return self.getresp()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 243, in getresp
    raise error_temp(resp)
ftplib.error_temp: 421 Login timeout (300 seconds): closing control connection
>>> ftp.login(JackHolmes)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ftp.login(JackHolmes)
NameError: name 'JackHolmes' is not defined
>>> ftp.login('JackHolmes')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    ftp.login('JackHolmes')
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 417, in login
    resp = self.sendcmd('USER ' + user)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 271, in sendcmd
    self.putcmd(cmd)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 198, in putcmd
    self.putline(line)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 193, in putline
    self.sock.sendall(line.encode(self.encoding))
BrokenPipeError: [Errno 32] Broken pipe
>>> ftp.login(JackHolmes,Beats1992)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ftp.login(JackHolmes,Beats1992)
NameError: name 'JackHolmes' is not defined
>>> ftp.login(jack_holmes,Beats1992)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ftp.login(jack_holmes,Beats1992)
NameError: name 'jack_holmes' is not defined
>>> ftp.login(daemon,xampp)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    ftp.login(daemon,xampp)
NameError: name 'daemon' is not defined
>>> ftp.login('daemon','xampp')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ftp.login('daemon','xampp')
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 417, in login
    resp = self.sendcmd('USER ' + user)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 271, in sendcmd
    self.putcmd(cmd)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 198, in putcmd
    self.putline(line)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 193, in putline
    self.sock.sendall(line.encode(self.encoding))
BrokenPipeError: [Errno 32] Broken pipe
>>> ftp.connect('127.0.0.1')
'220 ProFTPD 1.3.4c Server (ProFTPD) [::ffff:127.0.0.1]'
>>> ftp.login('daemon','xampp')
'230 User daemon logged in'
>>> ftp.dir()
drwxrwxrwx  13 jackholmes admin         442 Oct 29 22:49 JSON
-rw-rw-r--   1 root     admin        3553 Jul 21 21:08 applications.html
-rw-rw-r--   1 root     admin         177 Jul 21 21:08 bitnami.css
drwxrwxr-x  29 root     admin         986 Nov  3 11:13 dashboard
-rw-rw-r--   1 root     admin       30894 May 11  2007 favicon.ico
drwxr-xr-x   4 jackholmes admin         136 Nov  3 10:22 helloworld
drwxrwxr-x   4 root     admin         136 Oct 20 13:08 img
-rw-rw-r--   1 daemon   daemon        260 Jul  9 12:00 index.php
drwxr-xr-x  12 jackholmes admin         408 Nov  9 19:42 python
drwxrwxr-x   2 daemon   daemon         68 Oct 20 13:08 webalizer
>>> ftp.pwd()
'/'
>>> ftp
