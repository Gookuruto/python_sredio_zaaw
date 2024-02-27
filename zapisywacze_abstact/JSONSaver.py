import json

from zapisywacze_abstact.DataSaver import DataSaver


class JSONSaver(DataSaver):
    def save_data(self, data, file_path):
        with open(file_path,'w') as f:
            json.dump(data,f)