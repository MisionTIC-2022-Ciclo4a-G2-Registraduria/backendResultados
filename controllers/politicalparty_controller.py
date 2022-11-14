from models.politicalparty import PoliticalParty
from repositories.politicalparty_repository import PoliticalRepository


class PoliticalPartyController:
    def __init__(self):
        """

        """
        print("Political Party controller ready")
        self.politicalParty_repository = PoliticalRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("return all political parties")
        return self.politicalParty_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one table")
        political_party = self.politicalParty_repository.find_by_id(id_)
        return political_party

    # equivalent to insert
    def create(self, political_: dict) -> dict:
        """

        :param political_:
        :return:
        """
        print("insert a political_party")
        political_party = PoliticalParty(political_)
        political_party_ = self.politicalParty_repository.save(political_party)
        return political_party_

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("update a political_party")
        political_party = PoliticalParty(political_party_)
        political_party_ = self.politicalParty_repository.update(id_, political_party)
        return political_party_

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete political party")
        return self.politicalParty_repository.delete(id_)
