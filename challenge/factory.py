from log_source import FileLogSource, CsvLogSource

class LogSourceFactory:
    @staticmethod
    def create_source(source_type):
        if source_type == "txt":
            return FileLogSource()
        elif source_type == "csv":
            return CsvLogSource()
        raise ValueError("Unknown source type")
