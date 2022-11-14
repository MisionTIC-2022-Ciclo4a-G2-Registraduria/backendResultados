from models.table import Table
from repositories.table_repository import TableRepository


class TableController:
    def __init__(self):
        """
        This is the constructor of the TableController class
        """
        print("Table controller ready")
        self.table_repository = TableRepository()

    def index(self) -> list:
        """
        This method returns all tables persisted in the db
        :return: table's list
        """
        print("return all tables")
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one table")
        table = self.table_repository.find_by_id(id_)
        return table

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("insert a table")
        table = Table(table_)
        table_ = self.table_repository.save(table)
        return table_

    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("update a table")
        table = Table(table_)
        table_ = self.table_repository.update(id_, table)
        return table_

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete table " + id_)
        return self.table_repository.delete(id_)
