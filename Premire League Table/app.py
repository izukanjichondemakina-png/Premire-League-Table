from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "24823f9bca864cd29ce5c9855b9f8e64"

URL = "https://api.football-data.org/v4/competitions/PL/standings"

headers = {
    "X-Auth-Token": API_KEY
}

def get_table():

    try:

        response = requests.get(URL, headers=headers)

        data = response.json()

        standings = data["standings"][0]["table"]

        teams = []

        for team in standings:

            teams.append({

                "position": team["position"],
                "name": team["team"]["name"],
                "logo": team["team"]["crest"],
                "played": team["playedGames"],
                "won": team["won"],
                "draw": team["draw"],
                "lost": team["lost"],
                "points": team["points"],
                "goalDiff": team["goalDifference"]

            })

        return teams

    except Exception as e:

        print(e)
        return []

@app.route("/")

def home():

    return render_template(
        "index.html",
        teams=get_table()
    )

if __name__ == "__main__":

    app.run(debug=True)