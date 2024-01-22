from pathlib import Path

class IOHandler:
    def data_folder_path(self):
        return Path(__file__).parent.parent.parent.joinpath("data")

    def input_folder_path(self):
        return f"{self.data_folder_path()}/input/"

    def input_file_path(self, input_filename):
        return f"{self.data_folder_path()}/input/{input_filename}"

    def output_file_path(self):
        return f"{self.data_folder_path()}/output/"
