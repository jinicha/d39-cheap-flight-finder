import requests
from twilio.rest import Client
import config

ACCOUNT_SID = config.ACCOUNT_SID
AUTH_TOKEN = config.AUTH_TOKEN
SEND_FROM = config.SEND_FROM
SEND_TO = config.SEND_TO


class NotificationManager:
    def send_message(self, message):
      client = Client(ACCOUNT_SID, AUTH_TOKEN)
      message = client.messages.create(
          body=message,
          from_=SEND_FROM,
          to=SEND_TO
      )
