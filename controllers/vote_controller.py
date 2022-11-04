from models.vote import Vote
from repositories.vote_repository import VoteRepository


class VoteController:

    def __init__(self):
        """

        """
        print("Vote controller ready")
        self.vote_repository = VoteRepository()

    # Equivalent to 'all'
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
        return vote.__dict__

    def create(self, vote_: dict) -> dict:
        """

        :param vote_:
        :return:
        """
        print("insert vote")
        vote = Vote(vote_)
        vote_ = self.vote_repository.save(vote)
        return vote_.__dict__

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        print("update vote")
        vote = Vote(vote_)
        vote_ = self.vote_repository.update(id_, vote)
        return vote_.__dict__

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete vote")
        return self.vote_repository.delete(id_)
