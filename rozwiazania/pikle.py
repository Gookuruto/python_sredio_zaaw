import pickle

dane_testowe = {
    "a": "Alojzy",
    "b": "Baltazar",
    "c": "Celina"
}


def save_to_pickle(data):
    with open("data.pickle", "wb") as f:
        pickle.dump(data, f)


def read_from_pickle(pickle_path):
    with open(pickle_path, "rb") as f:
        data = pickle.load(f)
    return data


def add_object_to_pickle(pickle_path,new_object):
    data = read_from_pickle(pickle_path)
    print(data)
    data.update(new_object)
    save_to_pickle(data)
    print(read_from_pickle(pickle_path))

class PrzykladowaKlasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa

obiekt = PrzykladowaKlasa("Przykład")
save_to_pickle(obiekt)
print(read_from_pickle("data.pickle").nazwa)
#add_object_to_pickle("data.pickle",{"d":"Daniel","e":"Eurydyka"})