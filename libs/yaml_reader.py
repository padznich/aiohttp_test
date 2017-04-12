
import yaml


class YamlReader:

    def __init__(self, _path):
        with open(_path, "r") as f:
            yaml_data = yaml.load(f.read())

        self.__dict__.update(yaml_data)
