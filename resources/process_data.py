#!/usr/bin/env python3

# script for processing dataset
# outputs to a single file: data.json

import json
import pandas as pd

with open('./starships.json') as raw:
    starships = json.load(raw)
    
with open('./transport.json') as raw:
    transport = json.load(raw)
    
print(starships)

print(transport)

transport = pd.DataFrame([{**x['fields'], **{'pk': x['pk']}} for x in transport]).set_index('pk')

starships = pd.DataFrame([{**x['fields'], **{'pk': x['pk']}} for x in starships]).set_index('pk')

data = starships.merge(transport, on='pk', how='left')

data.to_json('./data.json', orient='records')

with open('./data.json') as raw:
    data = json.load(raw)
    
with open('./people.json') as raw:
    people = json.load(raw)
    
people = {x['pk']: x['fields'] for x in people}

data = [{k: v for k, v in i.items() if k not in ['created', 'edited']} for i in data]

for x in data:
    x['pilots'] = [people[i]['name'] for i in x['pilots']]
    print(x)
    
with open('./data.json', 'w') as json_file:
    json.dump(data, json_file)