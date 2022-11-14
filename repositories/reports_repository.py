from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Vote]):

    def get_grades_stats(self, candidate_id):
        query_match = {
            "candidate.$id": ObjectId(candidate_id)
        }
        query_aggregation = {
            "$group": {
                "_id": "$candidate",
                "count": {"$sum": 1}
            }
        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }
        query_limit = {
            "$limit": 15
        }
        pipeline = [query_match, query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)
