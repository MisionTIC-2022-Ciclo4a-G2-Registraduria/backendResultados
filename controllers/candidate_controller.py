from models.candidate import Candidate
from repositories.candidate_repository import CandidateRepository


# TODO check validations and errors codes
class CandidateController:

    def __init__(self):
        """

        """
        print("Candidate controller ready")
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("return all candidates")
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one candidate")
        candidate = self.candidate_repository. find_by_id(id_)
        return candidate.__dict__

    def create(self, candidate_: dict) -> Candidate:
        """

        :param candidate_:
        :return:
        """
        print("insert candidate")
        candidate = Candidate(candidate_)
        candidate_ = self.candidate_repository.save(candidate)
        return candidate_.__dict__

    def update(self, id_, candidate_: Candidate) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("update candidate")
        candidate = Candidate(candidate_)
        candidate_ = self.candidate_repository.update(id_, candidate)
        return candidate.__dict__

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete candidate")
        return self.candidate_repository.delete(id_)
