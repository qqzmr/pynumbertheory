#coding:utf-8
import telnetlib
host="10.36.132.138"
user="yincheng"
password="111111"
finish="~]$"

host="192.168.159.1"
user="zdf"
password="1q2w3e4r"
finish="~]$"

tn=telnetlib.Telnet(host)#连接主机

tn.read_until("login:") #一直读到login:,没有就一直等待
tn.write(user+"\n") #写入,\n回车

tn.read_until("Password:")
tn.write(password+"\n")


tn.read_until("~]$")
tn.write("mkdir  1234567abc\n")

tn.read_until("~]$")

tn.close()