
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
	welcome = render_template('welcome_message')
	return question(welcome)


# -------------------------------- Main Program --------------------------------------------------

# Your Account SID from twilio.com/console
account_sid = "ACe7aa947f226b5887756ae30fbeeb92d2"

# Your Auth Token from twilio.com/console
auth_token  = "10a7156914eeece38350e56577b31ab8"


client = Client(account_sid, auth_token)



# def getNameList(person):
employee_list = ['Vikash','Manish', 'Kanchan', 'Henry', 'Aisha']

employee_dict = {'Manish': '+16099066201',
				'Kanchan': '+17186660179',
				'Aisha': '+17323576509',
				'Henry': '+13475456457',
				'Vikash': '+13475456457' 
}


@ask.intent("GetEmployeeIntent")
def final_response(person):
	if (person is None):
		NoResponse = render_template('no_response')
		return question(NoResponse)

	else:
		if (person in employee_list):
			WaitResponse = render_template('wait_response')
			# print person
			message = send_message(person)
			return statement(WaitResponse)


		else:
			NoPerson = render_template('personNotFound')
			return statement(NoPerson)


def send_message(person):
	message = client.messages.create(
		to = employee_dict[person],
		from_="+19284874266",
     	body="Someone is here to meet you at Tricon Reception"
     	)



if __name__ == '__main__':
	app.run(debug=True)

