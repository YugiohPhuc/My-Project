import thread
import os, sys

a = "mkfifo chating1"       # tao 2 duong ong
b = "mkfifo chating2"       # chating1: A(in)--> B(out)
                            # chating2: B(in)--> A(out)

create1 = os.system("mkfifo chating1")   
create2 = os.system("mkfifo chating2")

def send():
    while 1:
        msg_out = raw_input()   # doi de nhap vao, neu dung input() thi ko the nhap chu vao
        strOut = "echo " + msg_out + " > chating2"
	os.system(strOut)   # os.system(<lenh>): de viet lenh tren man hinh terminal va ko can co gia tri tra ve
		
def receive():
    while 1:
        strIn = "cat chating1"
        read = os.popen(strIn).read()  # os.popen(<lenh>): de viet lenh tren man hinh terminal, co gia tri tra ve va duoc luu vao bien read. Ta dung read.read() la de doc du lieu tra ve trong bien read
        print (read)

try:        # try la chay 1 lan
        thread.start_new_thread(send, ( ))      # 2 cai Thread nay chay hoan toan doc lap voi nhau va voi chuong trinh (voi while 1 ben duoi)
        thread.start_new_thread(receive, ( ))
except:     # neu ko chay vao try
	print "error"
while 1:
	pass    # tao vong lap vo tan de chuong trinh ko dung lai
