from repositories.reports_repository import ReportsRepository


class ReportsController:
    def __init__(self):
        self.report_repository = ReportsRepository()

    def report_table_stats(self, candidate_id):
        return self.report_repository.get_table_stats(candidate_id)

    def report_candidate_stats(self, candidate_id):
        return self.report_repository.get_candidate_stats(candidate_id)
