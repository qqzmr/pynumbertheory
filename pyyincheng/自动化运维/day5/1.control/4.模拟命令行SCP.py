import pexpect
from pexpect  import EOF,TIMEOUT
from pexpect import pxssh
ip="10.36.132.138"
user="zenmebuxing"
password="fuck"

child=pexpect.spawn("/usr/bin/scp",[user+"@"+ip+":/home/yincheng/scp.py", "/home/python"])
sever=pxssh.pxssh()
sever.login(ip,user,password)
sever.sendline("shutdown -h now")#嘿嘿不玩了
sever.prompt()
child.expect("(?i)password")
child.sendline(password)
child.expect(pexpect.EOF) #自动结束

child.close()
