from abc import ABC, abstractmethod

class ILogSource(ABC):
    @abstractmethod
    def get_logs(self):
        pass

class FileLogSource(ILogSource):
    def get_logs(self):
        return ["Log from TXT file"]

class CsvLogSource(ILogSource):
    def get_logs(self):
        return ["Log from CSV row 1", "Log from CSV row 2"]
