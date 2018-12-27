import pexpect
from pexpect  import EOF,TIMEOUT

'''
ip="10.36.132.138"
user="root"
password="111111"


child=pexpect.spawn("/usr/bin/ssh",[user+"@"+ip])
child.expect("(?i)password:")
child.sendline(password)
child.expect("#")
child.sendline("ls")
child.expect("#")
child.sendline("cd /home/yincheng")
child.expect("#")
child.sendline("mkdir  zxcvbnm2017")
child.expect("#")
child.close()
'''
ip="10.36.132.138"
user="yincheng"
password="111111"


child=pexpect.spawn("/usr/bin/ssh",[user+"@"+ip])
child.expect("(?i)password:")
child.sendline(password)
child.expect("\$") #正则表达式,转移字符处理
child.sendline("ls")
child.expect("\$")
child.sendline("cd /home/yincheng")
child.expect("\$")
child.sendline("mkdir  zxcvbnm2017")
child.expect("\$")
child.close()