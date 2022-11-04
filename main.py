import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve

from blueprints.candidateBlueprints import candidate_blueprints
from blueprints.politicalPartyBlueprints import political_party_blueprints
from blueprints.voteBlueprints import vote_blueprints
from blueprints.tableBlueprints import table_blueprints


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(political_party_blueprints)
app.register_blueprint(vote_blueprints)
app.register_blueprint(table_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the Results Services"}

    return jsonify(response)


# Config and Execute App
def load_file_config():
    with open("config.json") as file:
        data = json.load(file)

    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
