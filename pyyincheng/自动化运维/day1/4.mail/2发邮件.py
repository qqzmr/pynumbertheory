import smtplib
import string
host="smtp.163.com"
subject="hello baby"
to="yincheng8848@163.com"
to="3551681057@qq.com"
Myfrom="yincheng8848@163.com"
body=string.join(("From:%s" %Myfrom,
                  "To:%s"%to,
                  "Subject:%s"%subject,
                  "",
                  "hello python hello world"),"\r\n")
sever=smtplib.SMTP()
sever.connect(host,25)
sever.starttls()
sever.login("yincheng8848@163.com","tsinghua8888")
sever.sendmail(Myfrom,[to],body)
sever.quit()