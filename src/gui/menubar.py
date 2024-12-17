"""Menu bar displayed on the main window."""

import tkinter

from gui.dialogs.about_dialog import about
from gui.dialogs.help_dialog import show_help


class Menubar(tkinter.Menu):
    """Menu bar displayed on the main window."""

    def __init__(self, parent, main_window):
        """Initialize the menu bar."""
        super().__init__(tearoff=0)

        self.parent = parent
        self.main_window = main_window

        self.file_menu = tkinter.Menu(self, tearoff=0)
        self.file_menu.add_command(
            label="New configuration",
            image=main_window.icons.file_new_icon,
            compound="left",
            underline=0,
            accelerator="Ctrl+N",
            command=self.main_window.new_configuration,
        )
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Load configuration",
            image=main_window.icons.file_open_icon,
            compound="left",
            underline=0,
            accelerator="Ctrl+L",
            command=self.main_window.load_configuration,
        )
        self.file_menu.add_command(
            label="Save configuration",
            image=main_window.icons.file_save_icon,
            compound="left",
            underline=0,
            accelerator="Ctrl+S",
            command=self.main_window.save_configuration,
        )
        self.file_menu.add_command(
            label="Save configuration as",
            image=main_window.icons.file_save_as_icon,
            compound="left",
            underline=0,
            command=self.main_window.save_as_configuration,
        )
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Quit",
            image=main_window.icons.exit_icon,
            compound="left",
            underline=0,
            accelerator="Ctrl+Q",
            command=main_window.quit,
        )

        self.configuration_menu = tkinter.Menu(self, tearoff=0)
        self.configuration_menu.add_command(
            label="Edit",
            image=main_window.icons.edit_icon,
            compound="left",
            underline=0,
            accelerator="F4",
            command=main_window.edit_configuration,
        )
        self.configuration_menu.add_command(
            label="Check",
            image=main_window.icons.checkbox_icon,
            compound="left",
            underline=0,
            accelerator="F5",
            command=main_window.check_configuration,
        )

        self.help_menu = tkinter.Menu(self, tearoff=0)
        self.help_menu.add_command(
            label="Help",
            image=main_window.icons.help_faq_icon,
            compound="left",
            underline=0,
            accelerator="F1",
            command=show_help,
        )
        self.help_menu.add_separator()
        self.help_menu.add_command(
            label="About",
            image=main_window.icons.help_about_icon,
            accelerator="F11",
            compound="left",
            underline=0,
            command=about,
        )

        self.add_cascade(label="File", menu=self.file_menu, underline=0)
        self.add_cascade(
            label="Configuration", menu=self.configuration_menu, underline=0
        )
        self.add_cascade(label="Help", menu=self.help_menu, underline=0)

        self.parent.bind("<F1>", lambda _: show_help())
        self.parent.bind("<F11>", lambda _: about())
        self.parent.bind(
            "<Control-n>",
            lambda _: self.main_window.new_configuration,
        )
