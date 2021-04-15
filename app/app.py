from flask import Flask
import requests, json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    # namesvc request
    try:
        title_lookup = requests.get('http://name-service:5001')
        title_lookup_res = title_lookup.status_code
        title = title_lookup.text
    except requests.exceptions.ConnectionError as e:
        title = ""
        title_lookup_res = e

    # internet time API request
    try:
        date_lookup = requests.get('http://worldtimeapi.org/api/timezone/Europe/London')
        date_lookup_res = date_lookup.status_code
        try:
            date_temp = json.loads(date_lookup.text)['datetime'].split('T')[0].split('-')
            date = date_temp[2]+"/"+date_temp[1]+"/"+date_temp[0]
        except:
            date = "ERROR"
    except requests.exceptions.ConnectionError as e:
        date = ""
        date_lookup_res = e
        

    # timesvc request
    try:
        time_lookup = requests.get('http://time-service:5000')
        time_lookup_res = time_lookup.status_code
        time = time_lookup.text
    except requests.exceptions.ConnectionError as e:
        time = ""
        time_lookup_res = e

    # build basic html response
    txt_response = "{}<br><br>It is currently {} on {}.<br><br>".format(title, time, date)
    service_status = "<u>Service Status:</u><br>name = {}<br>worldtimeapi = {}<br>time = {}".format(title_lookup_res, date_lookup_res, time_lookup_res)
    return txt_response + service_status

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
