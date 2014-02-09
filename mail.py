import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os


def mail(to, subject, text, attach1, attach2):
   gmail_user = ""
   gmail_pwd = ""

   if not gmail_user or not gmail_pwd:
      import sys
      import getpass
      sys.stdout.write("Usuario correo:")
      gmail_user =  raw_input().lower()
      gmail_pwd = getpass.getpass()

   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part1 = MIMEBase('application', 'pdf')
   part1.set_payload(open(attach1, 'rb').read())
   part2 = MIMEBase('text', 'xml')
   part2.set_payload(open(attach2, 'rb').read())
   Encoders.encode_base64(part1)
   Encoders.encode_base64(part2)
   part1.add_header('Content-Disposition',
                    "attachment; filename=%s" % os.path.basename(attach1))
   msg.attach(part1)

   part2.add_header('Content-Disposition',
                    "attachment; filename=%s" % os.path.basename(attach2))
   msg.attach(part2)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()
   return "Correo enviado a %s" % to

