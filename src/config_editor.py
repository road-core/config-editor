"""Configuration editor for Road Core service."""

from typing import Optional

import yaml

from gui.main_window import MainWindow

DEFAULT_CONFIGURATION_FILE = "olsconfig.yaml"


class ConfigEditor:
    """Class representing instances of configuration editor."""

    def __init__(self) -> None:
        """Initialize configuration editor."""
        self.configuration = None
        self.filename: Optional[str] = None

    def new_configuration(self) -> None:
        """Create new configuration to be edited."""
        self.configuration = None

    def load_configuration(self, filename: str) -> None:
        """Load configuration from YAML file."""
        with open(filename, encoding="utf-8") as fin:
            self.configuration = yaml.safe_load(fin)
            self.filename = filename

    def save_configuration_as(self, filename: str) -> None:
        """Store configuration into YAML file."""
        with open(filename, "w", encoding="utf-8") as fout:
            yaml.dump(self.configuration, fout)

    def save_configuration(self) -> None:
        """Store configuration into YAML file."""
        if self.filename is None:
            return
        with open(self.filename, "w", encoding="utf-8") as fout:
            yaml.dump(self.configuration, fout)

    def check_configuration(self) -> None:
        """Check if configuration is correct one."""


config_editor = ConfigEditor()
config_editor.load_configuration(DEFAULT_CONFIGURATION_FILE)

main_window = MainWindow(config_editor)
main_window.show()
