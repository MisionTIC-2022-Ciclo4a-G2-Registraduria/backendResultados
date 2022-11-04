from models.candidate import Candidate


class CandidateController:
    def __init__(self):
        """

        """
        print("Candidate controller ready")

    def index(self):
        """

        :return:
        """
        print("return all candidates")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one candidate")

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """
        print("insert a candidate")

    def update(self, id_, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("update a candidate")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete candidate")