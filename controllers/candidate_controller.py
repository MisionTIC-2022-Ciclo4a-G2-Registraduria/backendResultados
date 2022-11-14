from models.candidate import Candidate
from models.politicalparty import PoliticalParty
from repositories.candidate_repository import CandidateRepository
from repositories.politicalparty_repository import PoliticalRepository


# TODO check validations and errors codes
class CandidateController:

    def __init__(self):
        """

        """
        print("Candidate controller ready")
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalRepository()

    def assign_political_party(self, candidate_id: str, politicalParty_id: str) -> dict:
        """

        :param candidate_id:
        :param politicalParty_id:
        :return:
        """
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(politicalParty_id)
        political_party = PoliticalParty(political_party_dict)
        # TODO setattr(candidate, "political_party", political_party)
        candidate.political_party = political_party
        return self.candidate_repository.save(candidate)

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
        print("return one table")
        candidate = self.candidate_repository.find_by_id(id_)
        return candidate

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("insert candidate")
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("update candidate")
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
