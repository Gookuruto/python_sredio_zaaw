import pickle

from zapisywacze_abstact.DataSaver import DataSaver


class PickleSaver(DataSaver):
    def save_data(self, data, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
