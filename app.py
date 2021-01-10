import json
from flask import Flask
from flask import Response
from flask import request
from waitress import serve

app = Flask(__name__)

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

with open('./resources/data.json') as raw:
    data = json.load(raw)

@app.route('/starships')
def starships():
    order = request.args.get('order', default = 'asc', type = str)
    if order in ['asc', 'ascending']:
        desc = False
    elif order in ['desc', 'descending']:
        desc = True
    else:
        return Response('Invalid order parameter', status=400)
    return {'starships': sorted(data, key=lambda k: float(k['hyperdrive_rating']) if is_float(k['hyperdrive_rating']) else float('inf'), reverse = desc) }

if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=8080) 
