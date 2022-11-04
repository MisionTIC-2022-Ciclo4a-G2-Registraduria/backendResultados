from models.vote import Vote


class VoteController:
    def __init__(self):
        """

        """
        print("Vote controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("return all votes")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one vote")

    def create(self, enrollment_,) -> dict:
        """

        :param enrollment_:
        :return:
        """
        print("insert a vote")

    def update(self, id_: str, enrollment_: dict) -> dict:
        """

        :param id_:
        :param enrollment_:
        :return:
        """
        print("update a vote")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete vote")