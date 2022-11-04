from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController


vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/all", methods=['GET'])
def get_votes():
    response = vote_controller.index()
    return response, 200


@vote_blueprints.route("/vote/<string:id_>", methods=['GET'])
def get_vote_by_id(id_):
    response = vote_controller.show(id_)
    return response, 200


@vote_blueprints.route("/vote/insert", methods=['POST'])
def insert_vote():
    vote = request.get_json()
    response = vote_controller.create(vote)
    return response, 201


@vote_blueprints.route("/vote/update/<string:id_>", methods=['PATCH'])
def update_vote(id_):
    vote = request.get_json()
    response = vote_controller.update(id_, vote)
    return response, 201


@vote_blueprints.route("/vote/delete/<string:id_>", methods=['DELETE'])
def delete_vote(id_):
    response = vote_controller.delete(id_)
    return response, 204
