from flask import Flask, request, render_template
import requests
import json
from time import sleep
def pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    TOKEN = ''#pushbullet api key
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent') 


app = Flask(__name__)

templateData = ""
@app.route('/', methods=['POST', 'GET'])
def index():
	global templateData
	templateData = {'title' : ''}
	if request.method == 'POST':
		if request.form['submit_button'] == 'Free':
			pushbullet_message("I'm Free","You can come now. ✅")
			templateData = {'title' : 'I\'m free you can come now ✅.'}

		elif request.form['submit_button'] == 'You Can Come, But Don\'t Stay For Too Long':
			pushbullet_message("You can come, but don't stay for too long","I still have work to do 🟨")
			templateData = {'title' : 'You Can Come, But Don\'t Stay  For Too Long. I Still Have Work To Do 🟨'}

		elif request.form['submit_button'] == 'DON\'T COME':
			pushbullet_message("DON'T COME","I'M WORKING 😡")
			templateData = {'title' : 'DON\'T COME I\'M WORKING 😡'}
		else:
			pass # unknown
	else:
		pass
	return render_template('index.html', **templateData)

@app.route('/status')
def status_page():
	global templateData	
	if request.method == 'GET':
		templateData = templateData
	else:
		pass
	return render_template('status.html', **templateData)

if __name__ == "__main__":
	app.run(host= '0.0.0.0')


	