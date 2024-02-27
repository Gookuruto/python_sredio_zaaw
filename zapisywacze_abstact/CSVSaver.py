import csv

from zapisywacze_abstact.DataSaver import DataSaver


class CSVSaver(DataSaver):
    def save_data(self, data, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
