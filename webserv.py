#!/home/andrea/Soft/anaconda2/envs/numrel/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import json 
  
# Opening JSON file 
with open('data.json') as json_file: 
    data = json.load(json_file)
#

db_dict = {"entry_00" : data}

app = Flask(__name__)


@app.route('/db/dict',methods=['GET'])

def read_db():
    return jsonify({'db': db_dict})

@app.route('/db/dict/<dict_id>',methods=['GET'])

def get_result(dict_id="entry_00"):
    vals = db_dict[dict_id]["address"]["values"]
    val  = np.sum(np.array(vals))
    resu = 0
    for v in str(val):
    	resu += int(v)
    #

    return jsonify({"result" : resu})


if __name__ == "__main__":
    app.run()
