from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

token = "INSERT KEY HERE"

region = "na1"
patch = "8.14.1"
baseUrl = "https://{}.api.riotgames.com/lol/".format(region)


@app.route("/", methods=['GET'])
def index():
    return render_template("base.html")


@app.route("/getUser/<user>/", methods=['GET'])
def getUser(user):
    url = baseUrl + "summoner/v3/summoners/by-name/{}?api_key={}".format(user, token)
    return jsonify(callAPI(url, "GET"))


@app.route("/getMatches/<accountId>", methods=['GET'])
def getMatches(accountId):
    url = baseUrl + "match/v3/matchlists/by-account/{}?endIndex=100&queue=420&api_key={}".format(accountId, token)
    matches = callAPI(url, "GET")
    return jsonify(matches)


@app.route("/getEnemy/<gameId>/<accountId>/", methods=['GET'])
def getEnemy(gameId, accountId):
    accountId = int(accountId)
    url = baseUrl + "match/v3/matches/{}?api_key={}".format(gameId, token)
    match = callAPI(url, "GET")
    return jsonify(match)


@app.route("/getChampions/", methods=['GET'])
def getChampions():
    url = "http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json".format(patch)
    return jsonify(callAPI(url, "GET"))


def callAPI(url, method):
    response = requests.request(method, url, verify=False)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
