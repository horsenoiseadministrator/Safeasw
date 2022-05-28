import flask
from flask import request
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Free UK postcode geocoder API</h1>
<p>Uses a 2021 dataset from <a src='https://www.freemaptools.com/download-uk-postcode-lat-lng.htm'>Freemaptools</a></p>'''



@app.route('/api/v1/geocode', methods=['GET'])
def api_id():
    
    if 'postcode' in request.args:
        pcode = request.args['postcode'].upper()
    else:
        return "Error: Please provide a postcode."

    filename = 'data_part_1.csv'

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[1] == pcode:
                rehults = row[2] + ',' + row[3]
                
    csvfile.close


    filename = 'data_part_2.csv'

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[1] == pcode:
                rehults = row[2] + ',' + row[3]
                
    csvfile.close


    filename = 'data_part_3.csv'

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[1] == pcode:
                rehults = row[2] + ',' + row[3]
                
    csvfile.close

    return rehults

app.run()
