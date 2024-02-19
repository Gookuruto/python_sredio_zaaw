from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass


class MySQL(Database):
    def connect(self):
        return "Connected to MySQL database"

    def query(self, sql):
        return "Executing MySQL query: " + sql


mysql_db = MySQL()
print(mysql_db.connect())
print(mysql_db.query("SELECT * FROM users"))
