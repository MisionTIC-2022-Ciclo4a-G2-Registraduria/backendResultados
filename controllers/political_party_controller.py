from models.political_party import PoliticalParty
from repositories.political_party_repository import PoliticalPartyRepository


# TODO check validations and errors codes
class PoliticalPartyController:
    def __init__(self):
        """

        """
        print("Political Party controller ready")
        self.political_party_repository = PoliticalPartyRepository()

    def index(self) -> list:
        """

        :return:
        """
        print("return all political parties")
        return self.political_party_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one political party")
        response = self.political_party_repository.find_by_id(id_)
        return response

    # equivalent to insert
    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """
        print("insert a political party")
        political = PoliticalParty(political_party_)
        political_ = self.political_party_repository.save(political)
        return political_

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("update a political party")
        political = PoliticalParty(political_party_)
        political_ = self.political_party_repository.update(id_, political)
        return political_

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete political party")
        return self.political_party_repository.delete(id_)
