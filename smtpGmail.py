import smtplib
from email.mime.text import MIMEText


class gmail:

    def sendMail(me, title, msg):

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # https://myaccount.google.com/security
        # Create APP password
        smtp.login(me, 'ebrejhrfywhkmyjc')
        msg = MIMEText(msg, 'html')
        msg['Subject'] = title
        msg["To"] = 'chunghwan14@gmail.com'
        smtp.sendmail(me, msg["To"].split(","), msg.as_string())
        smtp.quit()
