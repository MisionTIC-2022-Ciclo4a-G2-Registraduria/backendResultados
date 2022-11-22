from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/votes_candidate/all", methods=["GET"])
def get_report_highest_cantidad():
    response = reports_controller.report_highest_stats()
    return response, 200
