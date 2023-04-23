from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_strava_webhook():
    if request.method == 'POST':
        data = request.json
        # Gérer les données du webhook Strava ici
        # ...
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
