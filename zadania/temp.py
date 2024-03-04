from zadania.context_manager import DBManager

with DBManager() as db:
    print(db.connected)
    db.insert_item("test")
    print(db.db_simulation)
    zaciagniete_dane = db.db_simulation


print(zaciagniete_dane)