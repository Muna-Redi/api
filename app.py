#!/usr/bin/python3
""" simple Api script """

from flask import Flask, jsonify, request, abort
from datetime import date, datetime


app = Flask(__name__)

week_days = {
        "0" : "Monday",
        "1" : "Tuesday",
        "2" : "Wednesday",
        "3" : "Thursday",
        "4" : "Friday",
        "5" : "Saturday",
        "6" : "Sunday"
        }


@app.route('/api', methods=["GET"])
def api_endpoint():
    """ returns a json """
    repo_url = "https://github.com/Muna-Redi/api.git"
    file_url = "https://github.com/Muna-Redi/api/blob/main/app.py"
    slack_name = request.args['slack_name']
    track = request.args['track']

    my_info = {
            "slack_name": "Munachyme",
            "current_day": week_days[str(date.today().weekday())],
            "utc_time": str(datetime.now().isoformat + 'Z'),
            "track": "backend",
            "github_file_url": file_url,
            "github_repo_url": repo_url,
            "status_code": 200
            }
    if slack_name != "Munachyme" or track != "backend":
        return abort(404)
    return jsonify(my_info)
if __name__ == "__main__":
    app.run()
