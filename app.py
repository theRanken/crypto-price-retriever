from flask import Flask
from flask import render_template as render
import json, os

BASE_PATH = os.path.dirname(__file__)
TEMPLATES = os.path.join(BASE_PATH, 'templates')

app = Flask(__name__, template_folder=TEMPLATES)

@app.route("/")
def index():
    '''Returns the Entry Point and index page of the application'''
    
    return render('index.html')


@app.route("/getPrices/<string:bsym>/<string:csym>/")
def price():
    '''
    This view returns prices data from an external api
    accepts two parameters  'bsym' and 'csym' in the URL
    '''

    data = {
        'message':'No Suggestions'
    }

    response = json.dumps(data, indent=4)
    return response


@app.route("/getSuggestions/<string:input>/")
def suggest():
    '''
    This view returns suggestions from an external api
    accepts one parameter 'input'
    '''

    data = {
        'message':'No Suggestions'
    }

    response = json.dumps(data, indent=4)
    return response


if __name__ == "__main__":
    #instantiate the app
    app.run(debug=True)