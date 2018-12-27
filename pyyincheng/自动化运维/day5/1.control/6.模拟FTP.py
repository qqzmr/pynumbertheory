#coding:utf-8
import pexpect
import sys


child=pexpect.spawn("ftp hk801.pc51.com")
child.expect("Name .*")
print(child.before)
child.sendline("qinghuabeidacn517")


child.expect("(?i)Password:")
print(child.before)
child.sendline("qq123456")


child.expect("ftp>")
print(child.before) #看到之前的消息
child.sendline("cd www")


child.expect("ftp>")
print(child.before)
child.sendline("get  888888.htm")


child.expect("ftp>") #等待命令执行完成
print(child.before)