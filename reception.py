from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

# --------------------------------------------------------------------------------------------
# INITIALISATION

app = Flask(__name__)
ask = Ask(app, "/Tricon_Infotech")


@app.route('/')
def homepage():
	return "Welcome to Tricon Recption"



@ask.launch
def start_skill():
	welcome_message = 'Hello, welcome to Tricon Infotech? I am Alexa. Whom are you here to meet?'
	return question(welcome_message)



@ask.intent 







if __name__ == '__main__':
	app.run(debug=True)
