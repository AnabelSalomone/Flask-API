from flask import Flask
from flask_restful import Api, Resource

import json

app = Flask(__name__)
api = Api(app)

filename = "data.json"

with open(filename, 'r') as f:
  data = json.load(f)


class Album(Resource):
  def get(self, name, nb):
    format_nb = nb -1
    format_name = name.replace("+", " ")

    for item in data:
      if item["name"].lower() == format_name.lower():
        return item["tracks"][format_nb]

api.add_resource(Album, "/album/<string:name>/<int:nb>")

if __name__ == "__main__":
  app.run(debug=True)