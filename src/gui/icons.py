"""All icons used on the GUI."""

import tkinter

import icons.added
import icons.application_exit
import icons.checkbox
import icons.configure
import icons.edit
import icons.file_new
import icons.file_open
import icons.file_save
import icons.file_save_as
import icons.help_about
import icons.help_faq
import icons.list
import icons.removed
import icons.server


class Icons:
    """All icons used on the GUI."""

    def __init__(self) -> None:
        """Initialize all icons and convert them to PhotoImage."""
        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
        self.help_faq_icon = tkinter.PhotoImage(data=icons.help_faq.icon)
        self.help_about_icon = tkinter.PhotoImage(data=icons.help_about.icon)
        self.file_new_icon = tkinter.PhotoImage(data=icons.file_new.icon)

        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)
        self.file_save_as_icon = tkinter.PhotoImage(data=icons.file_save_as.icon)

        self.edit_icon = tkinter.PhotoImage(data=icons.edit.icon)
        self.checkbox_icon = tkinter.PhotoImage(data=icons.checkbox.icon)

        self.list_icon = tkinter.PhotoImage(data=icons.list.icon)
        self.configure_icon = tkinter.PhotoImage(data=icons.configure.icon)
        self.server_icon = tkinter.PhotoImage(data=icons.server.icon)

        self.added_icon = tkinter.PhotoImage(data=icons.added.icon)
        self.removed_icon = tkinter.PhotoImage(data=icons.removed.icon)
