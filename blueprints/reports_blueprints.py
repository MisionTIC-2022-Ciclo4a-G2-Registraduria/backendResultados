from flask import Blueprint, jsonify
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/table/<string:candidate_id>", methods=['GET'])
def get_report_highest_table(candidate_id):
    response = reports_controller.report_table_stats(candidate_id)
    return jsonify(response)


@reports_blueprints.route("/reports/candidate/<string:candidate_id>", methods=['GET'])
def get_report_highest_candidate(candidate_id):
    response = reports_controller.report_candidate_stats(candidate_id)
    return jsonify(response)
