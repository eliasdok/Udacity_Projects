# Sending an SMS using the Twilio API
from twilio.rest import Client
# put your own credentials here
account_sid = "AC0f29b00ec845ce4a29c3ae8353ce8df7"
auth_token = "b3321875a8085b99155049226a277b83"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+14156198294",
  from_="+12565769307",
  body="Tomorrow's forecast in Financial District, San Francisco is Clear",
  media_url="https://climacons.herokuapp.com/clear.png")
