import smtplib
from email.message import EmailMessage
import glob

def send_email():
    msg=EmailMessage()
    msg['Subject']='Flipkart & IMDB web scraping'
    msg['From']='Abhishek Kumar'
    msg['To']='x4abhiop@gmail.com','sahniak75@gmail.com'
    # msg.set_content('This is a test email')
    with open('EmailTemplate.txt') as myfile:
        data=myfile.read()
        msg.set_content(data)

    files=glob.glob('*.pdf')
    for file in files:
        with open(file,'rb') as f:
            file_data=f.read()
            file_name=f.name
            msg.add_attachment(file_data,maintype='application',subtype='pdf',filename=file_name)



    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('sahniak9868@gmail.com','eawbeidlglcmoiju')
        smtp.send_message(msg)

    print("Email sent successfully 💕")

if __name__ == '__main__':
    send_email()