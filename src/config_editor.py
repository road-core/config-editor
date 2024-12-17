"""Configuration editor for Road Core service."""

import yaml

from gui.main_window import MainWindow

DEFAULT_CONFIGURATION_FILE = "olsconfig.yaml"


class ConfigEditor:
    """Class representing instances of configuration editor."""

    def __init__(self):
        """Initialize configuration editor."""
        self.configuration = None

    def new_configuration(self):
        """Create new configuration to be edited."""
        self.configuration = None

    def load_configuration(self, filename):
        """Load configuration from YAML file."""
        with open(filename) as fin:
            self.configuration = yaml.safe_load(fin)
            self.filename = filename

    def save_configuration_as(self, filename):
        """Store configuration into YAML file."""
        with open(filename, "w") as fout:
            yaml.dump(self.configuration, fout)

    def save_configuration(self):
        """Store configuration into YAML file."""
        with open(self.filename, "w") as fout:
            yaml.dump(self.configuration, fout)

    def check_configuration(self):
        """Check if configuration is correct one."""
        pass


config_editor = ConfigEditor()
config_editor.load_configuration(DEFAULT_CONFIGURATION_FILE)

main_window = MainWindow(config_editor)
main_window.show()
