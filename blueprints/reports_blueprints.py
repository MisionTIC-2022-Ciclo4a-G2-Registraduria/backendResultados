from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/highest_stats", methods=['GET'])
def get_report_highest_grades():
    response = reports_controller.report_highest_stats()
    return response, 200
