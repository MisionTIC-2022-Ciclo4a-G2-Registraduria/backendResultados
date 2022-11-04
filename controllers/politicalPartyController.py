from models.politicalParty import PoliticalParty


class PoliticalPartyController:
    def __init__(self):
        """

        """
        print("Political Party controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("return all political parties")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one political party")

    # equivalent to insert
    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """
        print("insert a political party")

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("update a political party")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete political party")
