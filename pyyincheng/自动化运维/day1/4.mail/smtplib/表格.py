#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


SUBJECT = u"官网业务服务质量周报"
HOST = "smtp.163.com"
TO = "yincheng8848@163.com"
TO="3551681057@qq.com"
FROM = "yincheng8848@163.com"

def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png","weekly"))

attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"
#attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

msg['Subject'] = SUBJECT
msg['From']=FROM
msg['To']=TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login("yincheng8848@163.com","tsinghua8888")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print ("邮件发送成功！")
except Exception as e:
    print ("失败："+str(e))
