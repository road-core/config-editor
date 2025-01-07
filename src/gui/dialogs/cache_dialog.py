"""Conversation cache dialog."""

import tkinter
from tkinter import ttk

from gui.dialogs.help_dialog import show_help
from gui.icons import Icons


class ConversationCacheDialog(tkinter.Toplevel):
    """Dialog for editing conversation settings."""

    def __init__(self, parent: tkinter.Toplevel, icons: Icons) -> None:
        """Initialize dialog for editing conversation settings."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Conversation cache")
        self.icons = icons
        self.parent = parent

        # don't display the dialog in list of opened windows
        self.transient(parent)

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # UI groups
        self.uigroup = tkinter.LabelFrame(
            self, text="Conversation cache", padx=5, pady=8
        )

        label1 = tkinter.Label(self.uigroup, text="Type")

        label1.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        cache_types = ("In-memory", "PostgreSQL", "Redis")

        cache_type = tkinter.StringVar(self.uigroup, cache_types[0], "cache_type")
        print(cache_type)

        cb1 = ttk.Combobox(
            self.uigroup,
            values=cache_types,
            # textvariable=app_log_levels,
            state="readonly",
        )
        cb1.current(0)
        cb1.grid(row=1, column=2, sticky="W", padx=5, pady=5)

        ok_button = tkinter.Button(
            self,
            text="OK",
            command=self.ok,
            compound="left",
            image=self.icons.checkbox_icon,
            width=200,
        )
        ok_button.grid(row=2, column=1, sticky="W", padx=10, pady=10)

        help_button = tkinter.Button(
            self,
            text="Help",
            command=self.help,
            compound="left",
            image=self.icons.help_faq_icon,
            width=200,
        )
        help_button.grid(row=2, column=2, sticky="W", padx=10, pady=10)

        # UI groups placement
        self.uigroup.grid(row=1, column=1, sticky="NSWE", padx=5, pady=5)


        # get the focus
        ok_button.focus_set()

    def ok(self) -> None:
        """Handle Ok button press."""
        self.destroy()

    def help(self) -> None:
        """Handle Help button press."""
        show_help()
