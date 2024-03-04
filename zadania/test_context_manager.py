import pytest
from zadania.context_manager import DBManager

@pytest.fixture
def db_manager():
    with DBManager() as db:
        yield db

def test_insert_and_remove_item(db_manager):
    db_manager.insert_item("item1")
    db_manager.insert_item("item2")
    db_manager.insert_item("item3")
    assert db_manager.db_simulation == ["item1", "item2", "item3"]

    db_manager.remove_item("item2")
    assert db_manager.db_simulation == ["item1", "item3"]

    db_manager.remove_item("item1")
    assert db_manager.db_simulation == ["item3"]

def test_disconnect():
    with DBManager() as db:
        pass  # Do nothing inside the context manager
    assert not db.connected
