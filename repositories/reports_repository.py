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
            "$limit": 3
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
            "$limit": 3
        }
        pipeline = [query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)

    def get_political_stats_winner(self, candidate_id):
        query_aggregation = {
            '$group': {
                '_id': '$candidate',
                'votos': {
                    '$sum': 1
                }
            }

        }
        query_sort = {
            '$sort': {
                'votos': -1
            }
        }
        query_addfields = {
            '$addFields': {
                'politicalparty': "$_id"
            }
        }
        query_lookup = {
            '$lookup': {
                "from": "politicalparty",
                "localField": "politicalparty.$id",
                "foreignField": "_id",
                "as": "politicalparty_info",
            }
        }
        query_limit = {
            "$limit": 3
        }
        pipeline = [query_aggregation, query_sort, query_addfields, query_lookup, query_limit]
        return self.query_aggregation(pipeline)

    def get_political_stats(self, candidate_id):
        query_aggregation = {
            '$group': {
                '_id': '$candidate',
                'votos': {
                    '$sum': 1
                }
            }

        }
        query_sort = {
            '$sort': {
                'votos': -1
            }
        }
        query_addfields = {
            '$addFields': {
                'politicalparty': "$_id"
            }
        }
        query_lookup = {
            '$lookup': {
                "from": "politicalparty",
                "localField": "politicalparty.$id",
                "foreignField": "_id",
                "as": "politicalparty_info",
            }
        }
        pipeline = [query_aggregation, query_sort, query_addfields, query_lookup]
        return self.query_aggregation(pipeline)
