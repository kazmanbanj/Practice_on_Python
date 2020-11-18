from twilio.rest import Client
 
account_sid = 'sid_here' 
auth_token = '[auth_token_here]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+16073005814',
                              body='Hello there one more',
                              to='+2348163282411' 
                          ) 
 
print(message.sid)