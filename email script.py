"""
script to check if there's pdfs or epubs in a specific folder and if tehre are to email them to your kindle's email separately

Things to add:
1. Make a notefile with their encrypted personal information or just personal information
2. Make script run on startup

Notes:
1. The script deletes the files after emailing them
2. Works only with gmail so far
3. You can only add authorized email addresses. 
"""
import os
from os import listdir, path
from os.path import isfile, join

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mypath = input("Enter Directory: ") #Enter Directory here

if path.exists(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        print(i,"\n")
else:
    os.mkdir(mypath, mode=0o777)
    print("Directory has been made, please move files into it.")
 #Directory's made now try to email it

#user can change these three lines depending on preferences
fromaddr = #Your email
pswrd =  #your password
toaddr = #your kindle's email

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr

for i in onlyfiles:
    filename = i
    attachment = open(mypath+i, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pswrd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    os.remove(mypath + i)
server.quit()
