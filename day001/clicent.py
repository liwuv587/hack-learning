import os
from socket import *;

s = socket()
s.connect(("127.0.0.1",8910))


choice = s.recv(1024).decode()
if choice == '1':
    # os.system('shutdown -s -t 1')
    print("关机啦")
elif choice == '2':
    # os.system('shutdown -r -t 1')
    print("重启啦")

