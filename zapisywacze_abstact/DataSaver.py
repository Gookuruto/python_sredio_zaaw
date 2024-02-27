from abc import ABC,abstractmethod

class DataSaver(ABC):
    @abstractmethod
    def save_data(self,data,file_path):
        pass