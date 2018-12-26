# coding:utf-8

import dns.resolver
import os
import httplib  # python2可用

appdomian = "facebook.com"  # 域名不能加入前缀www
appdomian = "taobao.com"  # 域名不能加入前缀www


def get_iplist(domain=""):  # 抓取网站的所有的ip列表，
    iplist = []
    try:
        A = dns.resolver.query(domain, "A")  # 查询A记录
    except Exception as e:
        print(e)
        return None
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return iplist

print(get_iplist(domain=appdomian))

def  checkip(ip):  # python2可用
    checkurl=ip+":80" #IP<PORT
    getcontent=""
    httplib.socket.setdefaulttimeout(5)#超时
    conn=httplib.HTTPConnection(checkurl) #连接 ip
    try:
        conn.request("GET","/",headers={"host":appdomian})
        result=conn.getresponse()
        getcontent=result.read()
    finally:
        if  getcontent.find("!DOCTYPE") != -1:  # 需要根据具体条件判断
            print("ipOK",checkurl)
        else:
            print("ipNO",checkurl)

iplist=get_iplist(domain=appdomian)
if iplist!=None and len(iplist)!=0  :#判断为空，是否长度为0
    for ip  in iplist:
        checkip(ip)