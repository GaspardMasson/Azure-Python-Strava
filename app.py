import requests
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Worldddddddd!"
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Récupérer le payload JSON envoyé par Strava
        payload = request.json

        # Traiter le payload
        # ...

        # Répondre à Strava avec un code d'état HTTP 200 OK
        return 'Success', 200
    else:
        # Si la demande n'est pas une demande POST, renvoyer une erreur 400 Bad Request
        return 'Bad Request', 400

if __name__ == '__main__':
    app.run()
