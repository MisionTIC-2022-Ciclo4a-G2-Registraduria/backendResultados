from flask import Blueprint
from flask import request

from controllers.politicalPartyController import PoliticalPartyController


political_party_blueprints = Blueprint('political_party_blueprints', __name__)
political_party_controller = PoliticalPartyController


@political_party_blueprints.route("/political_party/all", methods=['GET'])
def get_political_parties():
    response = political_party_controller.index()
    return response, 200


@political_party_blueprints.route("/political_party/<string:id>", methods=['GET'])
def get_political_party_by_id(id_):
    response = political_party_controller.show(id_)
    return response, 200


@political_party_blueprints.route("/political_party/insert", methods=['POST'])
def insert_political_party():
    political = request.get_json()
    response = political_party_controller.create(political)
    return response, 201


@political_party_blueprints.route("/political_party/update/<string:id>", methods=['PATCH'])
def update_political_party(id_):
    political = request.get_json()
    response = political_party_controller.update(id_, political)
    return response, 201


@political_party_blueprints.route("/political_party/delete/<string:id>", methods=['DELETE'])
def delete_political_party(id_):
    response = political_party_controller.delete(id_)
    return response,  204

