from twilio.rest import Client
import smtplib
import os
TWILIO_SID = "AC0297b20d0406a5c16cee090742491697"
TWILIO_AUTH_TOKEN = "824c35473f8c1f5c715e0ea5c8314b53"
TWILIO_VIRTUAL_NUMBER = "+17622486351"
TWILIO_VERIFIED_NUMBER = "+821056827198"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
    
    def send_email(self,send_to, content):
        my_email = "abdurakhmantimurmalik@gmail.com"
        my_password = os.environ["G_PW"]
        
        #Context creating part!
        txt = ""

        for i in range(len(content)):
            content_txt = f"{content[i]['city']}[{content[i]['iataCode']}]\
                            for {content[i]['lowestPrice']} WON!\n"
            txt += content_txt 
        
        #Emailing part
        for email_v in range(len(send_to["users"])):
            email_adr = send_to["users"][email_v]['email']
            name = send_to["users"][email_v]['firstName']
            last_name = send_to["users"][email_v]['lastName']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()

                connection.login(user=my_email,password=my_password)
                connection.sendmail(from_addr=my_email,to_addrs=email_adr,
                                    msg=f"Subject:NEW Tickets \
                                    \nHello dear {name} {last_name} \
                                    This is Timur's flight club!\
                                    Here's today's selection:\
                                    \n\n{txt}\nFor more contact us!")

