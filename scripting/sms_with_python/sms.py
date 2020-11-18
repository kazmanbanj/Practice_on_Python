from twilio.rest import Client
 
account_sid = 'AC7e2f8a7012021aa0cb914138cfa262dc' 
auth_token = '[cac3b1deb2a6278b2760565c24ed3d44]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+16073005814',
                              body='Hello there one more',
                              to='+2348163282411' 
                          ) 
 
print(message.sid)