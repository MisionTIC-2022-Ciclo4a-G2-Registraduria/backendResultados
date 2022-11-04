from flask import Blueprint
from flask import request

from controllers.voteController import VoteController


vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controllers = VoteController()


@vote_blueprints.route("/vote/all", methods=['GET'])
def get_votes():
    response = vote_controllers.index()
    return response, 200


@vote_blueprints.route("/vote/<string:id>", methods=['GET'])
def get_vote_by_id(id_):
    response = vote_controllers.show(id_)
    return response, 200


@vote_blueprints.route("/vote/insert", methods=['POST'])
def insert_vote():
    vote = request.get_json()
    response = vote_controllers.create(vote)
    return response, 201


@vote_blueprints.route("/vote/update/<string:id>", methods=['PATCH'])
def update_vote(id_):
    vote = request.get_json()
    response = vote_controllers.update(id_, vote)
    return response, 201


@vote_blueprints.route("/vote/delete/<string:id>", methods=['DELETE'])
def delete_vote(id_):
    response = vote_controllers.delete(id_)
    return response, 204
