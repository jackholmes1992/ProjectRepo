Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import ftplib
>>> ftp = ftplib.FTP()
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
drwxr-xr-x  13 jackholmes admin         442 Nov 18 15:11 python
-rw-r--rw-   1 jackholmes admin         388 Nov 18 15:09 transferme.rtf
drwxrwxr-x   2 daemon   daemon         68 Oct 20 13:08 webalizer
>>> f = open("transferred.rtf", "wb")
>>> ftp.rtrbinary("RETR transferme.rtf", f.write)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ftp.rtrbinary("RETR transferme.rtf", f.write)
AttributeError: 'FTP' object has no attribute 'rtrbinary'
>>> f = ftplib.FTP('127.0.0.1','daemon','xampp')
>>> f.connect()
'220 ProFTPD 1.3.4c Server (ProFTPD) [::ffff:127.0.0.1]'
>>> ftp = ftplib.FTP('127.0.0.1','daemon','xampp')
>>> ftp.connect()
'220 ProFTPD 1.3.4c Server (ProFTPD) [::ffff:127.0.0.1]'
>>> f = open("transferred.rtf", "wb")
>>> ftp.retrbinary("RETR transferme.rtf", f.write)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ftp.retrbinary("RETR transferme.rtf", f.write)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 441, in retrbinary
    with self.transfercmd(cmd, rest) as conn:
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 398, in transfercmd
    return self.ntransfercmd(cmd, rest)[0]
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 358, in ntransfercmd
    host, port = self.makepasv()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 336, in makepasv
    host, port = parse227(self.sendcmd('PASV'))
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 272, in sendcmd
    return self.getresp()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/ftplib.py", line 245, in getresp
    raise error_perm(resp)
ftplib.error_perm: 530 Please login with USER and PASS
>>> ftp.login('daemon','xampp')
'230 User daemon logged in'
>>> f = open("transferred.rtf", "wb")
>>> ftp.retrbinary("RETR transferme.rtf", f.write)
'226 Transfer complete'
>>> ftp.dir()
drwxrwxrwx  13 jackholmes admin         442 Oct 29 22:49 JSON
-rw-rw-r--   1 root     admin        3553 Jul 21 21:08 applications.html
-rw-rw-r--   1 root     admin         177 Jul 21 21:08 bitnami.css
drwxrwxr-x  29 root     admin         986 Nov  3 11:13 dashboard
-rw-rw-r--   1 root     admin       30894 May 11  2007 favicon.ico
drwxr-xr-x   4 jackholmes admin         136 Nov  3 10:22 helloworld
drwxrwxr-x   4 root     admin         136 Oct 20 13:08 img
-rw-rw-r--   1 daemon   daemon        260 Jul  9 12:00 index.php
drwxr-xr-x  13 jackholmes admin         442 Nov 18 15:11 python
-rw-r--rw-   1 jackholmes admin         388 Nov 18 15:09 transferme.rtf
drwxrwxr-x   2 daemon   daemon         68 Oct 20 13:08 webalizer
>>> 
