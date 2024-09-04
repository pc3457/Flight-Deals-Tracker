import smtplib

from twilio.rest import Client

my_email = "your_email_id"
password = "your_mail_pass"


class NotificationManager:



    def send_emails(self, customer_email, email_body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password=password)
            connection.send_message(from_addr=my_email,
                                    to_addrs=customer_email,
                                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                                    )

        print(email_body)
