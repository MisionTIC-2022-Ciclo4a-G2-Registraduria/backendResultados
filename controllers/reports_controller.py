from repositories.reports_repository import ReportsRepository


class ReportsController:
    def __init__(self):
        self.report_repository = ReportsRepository()

    def report_highest_stats(self):
        return self.report_repository.get_cantidad_stats()
