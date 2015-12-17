from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    the_date_time=str(datetime.datetime.now())
    return "<html><h1>Yowza</h1> <h3>This is a python app running in AWS </h3> The current datetime: " + the_date_time +  "</html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
