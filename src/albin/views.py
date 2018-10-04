from albin import albin
from flask import jsonify
import pandas
import json


@albin.route("/s/<keyword>")
def list_comics_with_keyword_in_title(keyword):
    xkcd = pandas.read_pickle("xkcd_metadata.pkl")
    relevant = xkcd[xkcd["safe_title"].str.lower().str.contains(keyword.lower())]
    return jsonify(json.loads(relevant.to_json(orient="records")))
