import os
import readData
from twilio.rest import Client


account_sid = ''
auth_token = ''
#account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message =client.messages.create(from_='+17076402663',
                      to='+254714869114',
                      body='Hi Man, whats up')

