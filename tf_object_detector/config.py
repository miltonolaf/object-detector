import json
import click
import shutil
import os


class Config(object):
    """docstring for ."""

    def __init__(self):
        super(Config, self).__init__()
        self.project_path = os.getcwd()

    def init_config(self):
        shutil.copy(os.path.dirname(os.path.abspath(__file__)) + '/template.config.json',
                    self.project_path + '/tod.config.json')
        click.echo('Initialized!')

    def get_config(self):
        try:
            with open(self.project_path + '/tod.config.json') as json_file:
                json_file = json_file.read()
                self.config_data = json.loads(json_file)
        except Exception as e:
            click.echo('We did not find your configuration file')

    def config_definition(self):
        self.get_config()
        self.DOWNLOADED_MODELS_DIR = self.config_data['models_dir']
        self.DEMO_MODELS = self.config_data['demo_models']
        self.IMAGES_DIR = self.config_data['images_dir']
