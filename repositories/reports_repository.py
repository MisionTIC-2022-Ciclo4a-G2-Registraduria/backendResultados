from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Vote]):

    def get_cantidad_stats(self, candidate_id):
        query_match = {
            {"candidate.$id": ObjectId('63705e0a5711ba37559e9522')}
        }
        query_aggregation = {
                "$group": {
                      "_id": "$vote",
                      "cantidad": {"$sum": 1}
                }
        }

        query_sort = {
            "$sort": {
                "cantidad": -1
            }
        }

        query_limit = {
            "$limit": 15
        }
        pipeline = [query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)
