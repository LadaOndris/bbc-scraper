import csv
from abc import ABC, abstractmethod


class Writer(ABC):

    @abstractmethod
    def write_row(self, key, value):
        pass


class CsvWriter(Writer):

    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        self.headers = ['Header', 'Content']
        self.writer = csv.DictWriter(self.file, delimiter=",", fieldnames=headers)

    def write_row(self, header, content):
        self.writer.writerow({
            self.headers[0]: header,
            self.headers[1]: content
        })

    def __del__(self):
        self.file.close()
