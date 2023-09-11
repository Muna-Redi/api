#!/usr/bin/python3
""" simple Api script """

from flask import Flask, jsonify, abort
from datetime import date, datetime


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

time = "%Y-%m-%dT%H:%M:%S.%f"
week_days = {
        "0" : "Monday",
        "1" : "Tuesday",
        "2" : "Wednesday",
        "3" : "Thursday",
        "4" : "Friday",
        "5" : "Saturday",
        "6" : "Sunday"
        }


@app.route('/<slack_name>/<track>', methods=["GET"])
def api_endpoint(slack_name, track):
    """ returns a json """
    my_info = {
            "slack_name": "Munachyme",
            "current_day": week_days[str(date.today().weekday())],
            "utc_time": str(datetime.now().strftime(time)),
            "track": "backend",
            "github_file_url":
            "github_repo_url":
            "status_code": 200
            }
    if slack_name != "Munachyme" or track != "backend":
        return abort(404)

    return jsonify(my_info)
if _name_ == "__main__":
    app.run(port=5000)
