from twilio.rest import Client

account_sid = 'AC86197ecce2e07b66d37bc39bb075bba3'
auth_token = '2a1dd14c19652498aa783622348b5b84'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Dear Noordeen, Missed seeing you! Explore more! Try sending money to airtel money or mpamba instantly today with ease using F1RST APP or by dialling *1111#',
  to='whatsapp:+265884114376'
)

print(message.sid)