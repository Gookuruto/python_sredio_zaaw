from contextlib import contextmanager


class Database:
    def __init__(self, connected, simulation):
        self.connected = connected
        self._db_simulation = simulation

    @property
    def db_simulation(self):
        if self.connected:
            return self._db_simulation
        else:
            return []

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def insert_item(self, item):
        self._db_simulation.append(item)

    def remove_item(self, item):
        self._db_simulation.remove(item)


class DBManager:
    def __enter__(self):
        """tworzymy obiekt bazy danych i tworzymy połączenia za pomocą funkcji connect(). zwaracamy obiety bazy danych"""
        self.db = Database(True, ["test1", "test2"])
        self.db.connect()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Zamykamy połączenie bazy danych utworzonej podczas wywolania metody __enter__()"""
        self.db.disconnect()


@contextmanager
def db_manager():
    db = Database()
    db.connect()
    yield db
    db.disconnect()


db = Database(True, [])
db_2 = Database(True, [1, 2, 3])

print(db.db_simulation)
print(db_2.db_simulation)
