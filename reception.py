
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

from twilio.rest import Client

# --------------------------- Initialization --------------------------------------------------

app = Flask(__name__)
ask = Ask(app, "/tricon_reception")


@app.route('/')
def homepage():
	return "Welcome to Tricon Reception"



@ask.launch
def start_skill():
	# response = render_template(welcome_message)
	welcome_message = 'Hello, welcome to Tricon Infotech. I am Alexa. Whom are you here to meet?'
	return question(welcome_message)


# -------------------------------- Main Program --------------------------------------------------

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


client = Client(account_sid, auth_token)



# def getNameList(person):
employee_list = ['Vikash','Manish', 'Kanchan', 'Henry', 'Aisha']

employee_dict = {'Manish': '+00000000000',
				'Kanchan': '+00000000000',
				'Aisha': '+00000000000',
				'Henry': '+00000000000',
				'Vikash': '+00000000000' 
}

# 	return employee_list



@ask.intent("GetEmployeeIntent")
def final_response(person):
	if (person is None):
		#response = render_template(no_response)
		no_response = 'I am sorry. I quite didnt get that. Whom do you want to meet'
		return question(no_response)

	else:
		if (person in employee_list):
			# response = render_template(wait_response)
			wait_response = 'Please be seated. Someone will come to you shortly'
			print person
			message = send_message(person)
			return statement(wait_response)


		else:
			# response = render_template(personNotFound)
			personNotFound = 'I am sorry. Noone works by that name in Tricon'
			return statement(personNotFound)


def send_message(person):
	message = client.messages.create(
		to = employee_dict[person],
		from_="+19284874266",
     	body="Someone is here to meet you at Tricon Reception"
     	)




if __name__ == '__main__':
	app.run(debug=True)

