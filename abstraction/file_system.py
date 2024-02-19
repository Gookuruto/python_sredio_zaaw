from abc import ABC, abstractmethod


class FileSystem(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read_file(self, filename):
        pass


class LocalFileSystem(FileSystem):
    def connect(self):
        return "Connected to local file system"

    def read_file(self, filename):
        with open(filename, "r") as file:
            return file.read()


local_fs = LocalFileSystem()
print(local_fs.connect())
print(local_fs.read_file("example.txt"))
