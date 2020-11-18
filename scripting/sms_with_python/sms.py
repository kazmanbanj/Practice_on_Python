from twilio.rest import Client
 
account_sid = 'sid_token_here' 
auth_token = '[auth_token_here]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='twilio_phone_here',
                              body='Hello there one more',
                              to='+2348163282411' 
                          ) 
 
print(message.sid)