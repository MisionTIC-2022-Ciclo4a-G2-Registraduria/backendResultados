from models.candidate import Candidate
from models.political_party import PoliticalParty
from repositories.candidate_repository import CandidateRepository
from repositories.political_party_repository import PoliticalPartyRepository


# TODO check validations and errors codes
class CandidateController:
    def __init__(self):
        """

        """
        print("Candidate controller ready")
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalPartyRepository()

    def assign_political_party(self, candidate_id: str, political_party_id: str) -> dict:
        """

        :param candidate_id:
        :param political_party_id:
        :return:
        """
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)
        political_party = PoliticalParty(political_party_dict)
        candidate.political_party = political_party
        return self.candidate_repository.save(candidate)

    def index(self):
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
        candidate = self.candidate_repository.find_by_id(id_)
        return candidate

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("insert a candidate")
        candidate = Candidate(candidate_)
        candidate_ = self.candidate_repository.save(candidate)
        return candidate_

    def update(self, id_, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("update a candidate")
        candidate = Candidate(candidate_)
        candidate_ = self.candidate_repository.update(id_, candidate)
        return candidate_

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete candidate")
        return self.candidate_repository.delete(id_)
