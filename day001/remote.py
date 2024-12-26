import os
from socket import *;

 

s = socket()
s.bind(('0.0.0.0',8910))
s.listen()
s, addr = s.accept()
print("{} 来了".format(addr))
print('1.关机')
print('2.重启')
choice = input('请选择:')
s.send(choice.encode())