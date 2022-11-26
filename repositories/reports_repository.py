from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Vote]):

    def get_table_stats(self, candidate_id):
        query_aggregation = {
            '$group': {
                '_id': '$vote',
                'votos': {
                    '$sum': 1
                }
            }

        }
        query_sort = {
            '$sort':{
                'votos': -1
            }
        }
        query_limit = {
            "$limit": 15
        }
        pipeline = [query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)

    def get_candidate_stats(self, candidate_id):
        query_aggregation = {
            '$group': {
                '_id': '$candidate',
                'votos': {
                    '$sum': 1
                }
            }

        }
        query_sort = {
            '$sort':{
                'votos': -1
            }
        }
        query_limit = {
            "$limit": 15
        }
        pipeline = [query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)

