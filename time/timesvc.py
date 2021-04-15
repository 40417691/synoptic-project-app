from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
