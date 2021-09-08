import smtplib
from email.mime.text import MIMEText


class gmail:

    def sendMail(me, you, msg):

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(me, 'Dh2fpswl!')
        msg = MIMEText(msg, 'html')
        msg['Subject'] = 'Stock Insider Tracking'
        smtp.sendmail(me, you, msg.as_string())
        smtp.quit()
