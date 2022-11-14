from bson import ObjectId
from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class VoteRepository(InterfaceRepository[Vote]):
    def get_students_by_course(self, vote_id):
        query = {"vote.$id": ObjectId(vote_id)}
        return self.query(query)
