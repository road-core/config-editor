"""Toolbar displayed on the main window."""

import tkinter

from gui.tooltip import Tooltip


class Toolbar(tkinter.LabelFrame):
    """Toolbar displayed on the main window."""

    def __init__(self, parent: tkinter.Tk, main_window) -> None:  # type: ignore [no-untyped-def]
        """Initialize the toolbar."""
        super().__init__(parent, text="Tools", padx=5, pady=5)

        self.parent = parent
        self.main_window = main_window

        self.button_new_config = tkinter.Button(
            self,
            text="New configuration",
            image=main_window.icons.file_new_icon,
            command=main_window.new_configuration,
        )

        Tooltip(self.button_new_config, "New configuration")

        self.button_file_open = tkinter.Button(
            self,
            text="Load configuration",
            image=main_window.icons.file_open_icon,
            command=main_window.load_configuration,
        )

        Tooltip(self.button_file_open, "Load configuration from file")

        self.button_file_save = tkinter.Button(
            self,
            text="Save configuration",
            image=main_window.icons.file_save_icon,
            command=self.main_window.save_configuration,
        )

        Tooltip(self.button_file_save, "Save configuration")

        self.button_file_save_as = tkinter.Button(
            self,
            text="Save configuration into different file",
            image=main_window.icons.file_save_as_icon,
            command=self.main_window.save_as_configuration,
        )

        Tooltip(self.button_file_save_as, "Save configuration into different file")

        self.button_edit_configuration = tkinter.Button(
            self,
            text="Edit configuration",
            image=main_window.icons.edit_icon,
            command=main_window.edit_configuration,
        )

        Tooltip(self.button_edit_configuration, "Edit configuration")

        self.button_check_configuration = tkinter.Button(
            self,
            text="Check configuration",
            image=main_window.icons.checkbox_icon,
            command=main_window.check_configuration,
        )

        Tooltip(self.button_check_configuration, "Check configuration")

        self.button_quit = tkinter.Button(
            self,
            text="Quit",
            image=main_window.icons.exit_icon,
            command=main_window.quit,
        )

        Tooltip(self.button_quit, "Quit")

        spacer1 = tkinter.Label(self, text="   ")
        spacer2 = tkinter.Label(self, text="   ")
        spacer3 = tkinter.Label(self, text="   ")

        self.button_new_config.grid(column=1, row=1)

        spacer1.grid(column=2, row=1)

        self.button_file_open.grid(column=3, row=1)
        self.button_file_save.grid(column=4, row=1)
        self.button_file_save_as.grid(column=5, row=1)

        spacer2.grid(column=6, row=1)

        self.button_edit_configuration.grid(column=7, row=1)
        self.button_check_configuration.grid(column=8, row=1)

        spacer3.grid(column=9, row=1)
        self.button_quit.grid(column=10, row=1)

    @staticmethod
    def disable_button(button: tkinter.Button) -> None:
        """Disable specified button on toolbar."""
        button["state"] = "disabled"

    @staticmethod
    def enable_button(button: tkinter.Button) -> None:
        """Enable specified button on toolbar."""
        button["state"] = "normal"
