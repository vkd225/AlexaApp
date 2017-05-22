

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)


employee_dict = {'Manish': '+000000000',
				'Kanchan': '+000000000',
				'Aisha': '+000000000',
				'Henry': '+000000000',
				'Vikash': '+000000000' 
}



# message = client.messages.create(
#     to="+13475456457", 
#     from_="+19284874266",
#     body="Test Message for Alexa")

# print(message.sid)


person = 'Vikash'

# def send_message():
# 	message = client.messages.create(
# 		to = employee_dict[person]

# 		)




print employee_dict[person]