# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACf328f709c93ddd15b2f256226dbcdec0']
auth_token = os.environ['1a42b5b4a0b8b91da817b3589303ff6c']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15023059946',
                     to='+19178225018'
                 )

print(message.sid)