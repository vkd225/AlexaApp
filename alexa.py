from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from datetime import datetime
import requests
import urllib
import re
import random


# --------------------------------------------------------------------------------------------
# INITIALISATION

app = Flask(__name__)
ask = Ask(app, "/Tricon_Infotech")


@app.route('/')
def homepage():
	return "Hello Triconites"


@ask.launch
def new_ask():
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome) \
.reprompt(reprompt)


# # -------------------- Read News ----------------------------------
# def get_headlines():
# 	user_pass_dict = {'user': 'YOUR_USERNAME',
# 						'passwd': 'YOUR_PASSWORD',
# 						'api_type': 'json'}

# 	sess = requests.Session()
# 	sess.headers.update({'User-Agent': 'I am testing Alexa: Vikash'})
# 	sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
# 	time.sleep(1)

# 	url = 'https://reddit.com/r/worldnews/.json?limit=10'
# 	html = sess.get(url)
# 	data = json.loads(html.content.decode('utf-8'))
# 	titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
# 	titles = '... '.join([i for i in titles])
# 	return titles


# @ask.intent("ReadNewsIntent")
# def share_headlines():
# 	headlines = get_headlines()
# 	headlines_msg = 'The Current world news headlines are .... {}'. format(headlines)
# 	return statement(headlines_msg)






# --------------------------------------------------------------------------------------------
# 1) IGN REVIEW APPLICATION


@ask.intent('ReviewLatestIntent')
def launchReview(show):
    if (show is None):
        reprompt_show = render_template("reprompt_show")
        return question(reprompt_show)
    else:
        filShow = processShowName(show)
        latest = getLatestReview(filShow)
        review_title = latest["searchitem_link_2/_text"]
        episode_title = review_title.split(':')[1].replace('"','')
        if (" Review" in episode_title):
            episode_title = episode_title.replace(" Review", "")
        image_url = latest["searchitem_image"].replace("_160w", "_480w").replace("http", "https")
        score = str(latest["reviewscore_number"])
        description = latest["ignreview_description"]
        latestReview_msg = render_template('latest_review', show=show, episode=episode_title, score=score)
        return statement(latestReview_msg) \
            .standard_card(title=review_title + " - " + score,
                            text=description,
                            small_image_url=image_url,
                            large_image_url=image_url)

def processShowName(show):
    showSynonymDict = {}
    showSynonymDict['Marvels Agents of Shield'] = "Marvel's Agents of S.H.I.E.L.D."
    showSynonymDict['Legends of Tomorrow'] = "DC's Legends of Tomorrow"
    if show in showSynonymDict:
        return showSynonymDict[show]
    else:
        return show

def getReviews(show):
    url = ("http://www.ign.com/search?page=0&count=10&filter=articles&type=article&q=review " + show).replace(" ", "%20")
    url = urllib.quote(url, safe='')
    urlRest = "https://api.import.io/store/connector/87e7f75c-3d4c-45cb-93e9-305a52237e63/_query?input=webpage/url:" + url + "&&_apikey=e581e9228fc34f139c3031d520f27af635f6dc576c932b84a8fd6cce4cc4b6a0a8499e8fcc53a7e308bf321c7a6e22998ec481eb1ab47742b062d01d62e174fc95343090d71c6dc63a4255886bf546e1"
    data = requests.get(urlRest).json()
    return data

def processDates(data):
    dateDict = {}
    for i in range(0, len(data["results"])):
        regex = re.compile('(?<=http:\/\/www.ign.com\/articles\/)(.*)(?=\/.*)', re.IGNORECASE)
        date_str = regex.findall(data["results"][i]["searchitem_link_2"])[0].split("/")
        dateDict[i] = datetime(int(date_str[0]), int(date_str[1]), int(date_str[2]))
    return dateDict

def getLatestReview(show):
    data = getReviews(show)
    dateDict = processDates(data)
    i_latest = 0
    for i in dateDict:
        if dateDict[i] > dateDict[i_latest]:
            i_latest = i
    latest = data["results"][i_latest]
    return latest



@app.route('/reddit')
def reddit():
	titles = get_headlines(show)
	return titles


@app.route("/review")
def review():
	# show = 'Flash'
	review = launchReview(show)
	return review




if __name__ == '__main__':
	app.run(debug=True)

