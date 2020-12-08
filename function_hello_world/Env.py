from dotenv import load_dotenv

class Env():
    def __init__(self):
        load_dotenv()

    # from os import environ
    # from osbot_utils.utils.Files import path_combine, parent_folder
    # from osbot_utils.utils.Yaml import yaml_load

    #     self.config_folder = parent_folder(__file__)
    #     self.config_file   = "config.yaml"
    #
    # def path_to_config_file(self):
    #     return path_combine(self.config_folder, self.config_file)
    #
    # def load(self):
    #     return yaml_load(self.path_to_config_file())