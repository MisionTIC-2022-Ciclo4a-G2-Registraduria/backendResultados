from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController


vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controllers = VoteController()


@vote_blueprints.route("/vote/all", methods=['GET'])
def get_votes():
    response = vote_controllers.index()
    return response, 200


@vote_blueprints.route("/vote/<string:id_>", methods=['GET'])
def get_vote_by_id(id_):
    response = vote_controllers.show(id_)
    return response, 200


@vote_blueprints.route("/vote/by-candidate/<string:candidate_id>")
def get_votes_by_candidate(candidate_id):
    response = vote_controllers.list_tables_by_candidate(candidate_id)
    return response, 200


@vote_blueprints.route("/vote/insert/table/<string:table_id>/candidate/<string:candidate_id>", methods=['POST'])
def insert_vote(table_id, candidate_id):
    vote = request.get_json()
    response = vote_controllers.create(vote, table_id, candidate_id)
    return response, 201


@vote_blueprints.route("/vote/update/<string:id_>", methods=['PATCH'])
def update_vote(id_):
    vote = request.get_json()
    response = vote_controllers.update(id_, vote)
    return response, 201


@vote_blueprints.route("/vote/delete/<string:id_>", methods=['DELETE'])
def delete_vote(id_):
    response = vote_controllers.delete(id_)
    return response, 204
