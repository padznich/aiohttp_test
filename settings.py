import os

from libs.yaml_reader import YamlReader


conf_path = os.path.join(os.path.dirname(__file__), "config/polls.yaml")
conf = YamlReader(conf_path)
