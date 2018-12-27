#coding:utf-8
import  telnetlib


host="www.qq.com"  #telnet 一个服务器多个端口,大面积扫描服务器,nmap
for port   in range(79,65536):
    telnetlibtest=telnetlib.Telnet() #创建一个对象
    try:
        telnetlibtest.open(host,port,timeout=1)#打开端口,1秒不行就放弃
        print(host,port,"isOK")
    except:
        print(host,port,"isNO")
    finally:
        telnetlibtest.close()
