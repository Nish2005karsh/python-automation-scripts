import smtplib
from email.mime.text import MIMEText
body = input("What's on your mind today?\n")
msg = MIMEText(body)
msg['Subject'] = '📝 Daily Journal'
msg['From'] = 'you@example.com'
msg['To'] = 'you@example.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('you@example.com', 'your_app_password')
server.send_message(msg)
server.quit()
