from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, static_url_path='/static')

token = "INSERT KEY HERE"
patch = "8.17.1"

@app.route("/", methods=['GET'])
def index():
    return render_template("base.html")


@app.route("/getUser/<user>/<region>", methods=['GET'])
def getUser(user, region):
    url = "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(region, user, token)
    return jsonify(callAPI(url, "GET"))


@app.route("/getMatches/<accountId>/<region>/<queue>", methods=['GET'])
def getMatches(accountId, region, queue):
    url = "https://{}.api.riotgames.com/lol/match/v3/matchlists/by-account/{}?endIndex=100&queue={}&api_key={}".format(region, accountId, queue, token)
    matches = callAPI(url, "GET")
    return jsonify(matches)


@app.route("/getEnemy/<gameId>/<region>", methods=['GET'])
def getEnemy(gameId, region):
    url = "https://{}.api.riotgames.com/lol/match/v3/matches/{}?api_key={}".format(region, gameId, token)
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
