from bson import ObjectId

from models.candidate import Candidate
from models.vote import Vote
from models.table import Table
from repositories.candidate_repository import CandidateRepository
from repositories.vote_repository import VoteRepository
from repositories.table_repository import TableRepository


# TODO check validations and errors codes
class VoteController:
    def __init__(self):
        """

        """
        print("Vote controller ready")
        self.vote_repository = VoteRepository()
        self.candidate_repository = CandidateRepository()
        self.table_repository = TableRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("return all votes")
        return self.vote_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one vote")
        vote = self.vote_repository.find_by_id(id_)
        return vote

    def create(self, vote_, table_id: str, candidate_id: str) -> dict:
        """

        :param table_id:
        :param candidate_id:
        :param vote_:
        :return:
        """
        print("insert a vote")
        vote = Vote(vote_)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        vote.table = table_obj
        vote.candidate = candidate_obj
        return self.vote_repository.save(vote)

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        print("update a vote")
        vote = Vote(vote_)
        vote_ = self.vote_repository.update(id_, vote)
        return vote_

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete vote")
        return self.vote_repository.delete(id_)

    def get_tables_by_candidate(self, candidate_id):
        """

        :param candidate_id:
        :return:
        """
        query = {"candidate.$id: ObjectId(candidate_id)"}
        return self.vote_repository.query(query)

    def list_tables_by_candidate(self, candidate_id):
        """

        :param candidate_id:
        :return:
        """
        return self.vote_repository.get_tables_by_candidate(candidate_id)
