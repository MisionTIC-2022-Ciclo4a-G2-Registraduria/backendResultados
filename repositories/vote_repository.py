from models.vote import Vote
from repositories.interface_repository import InterfaceRepository
from bson import ObjectId


class VoteRepository(InterfaceRepository[Vote]):
    def get_tables_by_candidate(self, candidate_id):
        query = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query)
