from models.table import Table


class TableController:
    def __init__(self):
        """
        This is the constructor of the TableController class
        """
        print("Table controller ready")

    def index(self) -> list:
        """
        This method returns all tables persisted in the DB
        :return: table's list
        """
        print("return all tables")
        data = {
            "_id": "abc123",
            "_cedula": "123456"
        }
        table = Table(data)
        return [table.__dict__]

    def show(self, id_: str) -> dict:
        """
        This method returns
        :param id_:
        :return:
        """
        print("return one table")
        data = {
            "_id": id_,
            "_cedula": "123456"
        }
        table = Table(data)
        return table.__dict__

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("insert a table")
        table = Table(table_)
        return table.__dict__

    def update(self, id_, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("update a table")
        data = table_
        data['_id'] = id_
        table = Table(data)
        return table.__dict__

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete table" + id_)
        return {"Delete count": 1}
