import os
def Texter(TEXT, ICON, TITLE):
    f=open('temp.vbs', 'w')
    loophead = 'do\n'
    body =  'x=msgbox(\"'+TEXT+'\", '+ICON+',\"'+TITLE+'\" )\n'
    loopend = 'loop'
    f.write(loophead + body + loopend)
    os.popen('script temp.vbs')
    

if __name__ == '__main__':
    Texter("DUDE","3", "DUde")
