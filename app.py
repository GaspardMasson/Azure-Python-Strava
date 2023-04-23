import requests
from flask import Flask, request, abort

app = Flask(__name__)

client_id = '106136'
client_secret = '2510564984d9050ccf1b5bd58b129192c880037c'
callback_url = 'https://stravaappwebhook.azurewebsites.net/webhook'
verify_token = 'STRAVA'

@app.route("/")
def hello():
    return "Hello, Worldddddddd!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

@app.route('/create_webhook', methods=['POST'])
def create_webhook():
    url = 'https://www.strava.com/api/v3/push_subscriptions'
    headers = {'Content-Type': 'application/json'}
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'callback_url': callback_url,
        'verify_token': verify_token
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        subscription_id = response.json()['id']
        return f'Nouvelle souscription créée avec succès. ID de souscription : {subscription_id}', 200
    else:
        return f'La création de la souscription a échoué. Code d\'erreur : {response.status_code}', response.status_code

if __name__ == '__main__':
    app.run()
