import smtplib
import ssl

sender_email = input("Enter your email account: \n")
email_password = str(input("Enter your password (NOT YOUR EMAIL PASSWORD): \n"))
to_emails = input("Enter emails that you want to send (separated by space): \n")
list_email = to_emails.split(" ")
message1 = input("Send your message: \n")
message = f'''
Subject: HI FRIEND!!!
To: {','.join(list_email)}
{message1}
'''
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as smtp:
    try:
        smtp.login(sender_email,email_password)
        smtp.set_debuglevel(1)
        print("login success")
        smtp.sendmail(sender_email, list_email,message,message1)
        print("Has successfully sent the email message to", list_email)
    except ValueError:
        print("Error")
    print("GOOD JOB")
    smtp.quit()
