import thread
import os, sys

a = 1
b = 0
c = 0

# tao cac duong ong

os.system("mkfifo con_api1")    # con_api1: A(in) --> api(out)
os.system("mkfifo con_api2")    # con_api2: api(in) --> A(out)


def send():
    while c == 1:
            msg_out = raw_input()   # doi de nhap vao, neu dung input() thi ko the nhap chu vao
            if len(msg_out) <= 256:
                if msg_out == "logout":
                    strOut = "echo " + "*104# > con_api1"
                    os.system(strOut)
                    break
                else:
                    strOut = "echo " + "*100#" + msg_out + "*#" + " > con_api1"
                    os.system(strOut)   # os.system(<lenh>): de viet lenh tren man hinh terminal va ko can co gia tri tra ve
            else:
                print ("tin nhan khong duoc dai qua 256 ky tu")
def receive():
    while c == 1:
        strIn = "cat con_api2"
        read = os.popen(strIn).read()  # os.popen(<lenh>): de viet lenh tren man hinh terminal, co gia tri tra ve. Ta dung os.popen(strIn).read() la de doc du lieu tra ve va luu vao bien read
        data = read.split("#")
        if data[0] = "*100":
            data = data[1].slpit("*")
            print (data[0])
        elif data[0] == "*103":
            data = data[1].split("*")
            print (data[0])
            print ("login success")
            a = 0
            b = 1
            break
        elif data[0] == "*104":
            data = data[1].split("*")
            print (data[0])
            print ("logout success")
            a = 1
            c = 0
            print ("nhap vao ky tu bat ky")
            break
        elif data[0] == "*403*":
            print ("room da day")
            a = 1
            b = 0
            break
        elif data[0] == "*404*":
            print ("room khong ton tai")
            a = 1
            b = 0   
            break
        elif data[0] == "*401*":  
            print ("Sai cu phap")
        else data[0] == "*400*":   
            print ("Out of maxlength")

def login():
        username = raw_input("username: ")
        room = raw_input("room: ")
        strOut = "echo " + "*103#" + username + "*#" + room + "*#" + " > con_api1"
        os.system(strOut)
        a = 0
        c = 1
        receive()

while 1:        
    if a == 1:
        login()
    if b = 1:
        thread.start_new_thread(send, ())      # khoi tao 2 chuong trinh Thread
        thread.start_new_thread(receive, ())    # 2 cai Thread nay chay hoan toan doc lap voi nhau va voi chuong trinh chinh (voi while 1)
        b = 0
 
