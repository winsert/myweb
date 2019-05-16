#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 用于发送邮件

__author__ = 'winsert@163.com'

import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# SMTP 服务
#mail_host="smtp.qq.com"  #设置服务器
#mail_post=25
#mail_passwd="usizkavruxkljhci"   #这个是发送QQ账号的授权码，而不是QQ账号的密码，否则发送会失败    
#sender = '1569701115@qq.com'
#receivers = ['13395317077@189.cn']  # 接收邮件的邮箱
mail_host="smtp.189.cn"  #设置服务器
mail_post=25
mail_passwd="442270341"   #这个是发送QQ账号的授权码，而不是QQ账号的密码，否则发送会失败    
sender = '13395317077@189.cn'
receivers = ['13395317077@189.cn']  # 接收邮件的邮箱

def sendMail(sder, subject, msg):

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(sder, 'utf-8')
    message['To'] =  Header("Andy", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
        
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(sender, mail_passwd)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功：",
        print time.asctime(time.localtime(time.time())) #显示查询时间
        print
    except smtplib.SMTPException as e:
        print "无法发送邮件！Error: "
        print e

if __name__ == '__main__':
    
    sder = "MyTest" #邮件发送人
    print 'Sender = ', sder

    subject = "This is a test." #邮件主题
    print 'Subject = ', subject

    mailtime = time.asctime(time.localtime(time.time()))
    msg = u"邮件发送成功：" + str(mailtime) #邮件内容
    print 'Message = ', msg
    print

    sendMail(sder, subject, msg)