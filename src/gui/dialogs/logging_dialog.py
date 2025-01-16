"""Logging dialog."""

import tkinter
from tkinter import ttk

from gui.dialogs.help_dialog import show_help
from gui.icons import Icons


class LoggingDialog(tkinter.Toplevel):
    """Logging dialog."""

    def __init__(self, parent: tkinter.Toplevel, icons: Icons) -> None:
        """Initialize logging dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Logging settings")
        self.icons = icons
        self.parent = parent

        # don't display the dialog in list of opened windows
        self.transient(parent)

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # UI groups
        self.uigroup = tkinter.LabelFrame(self, text="Logging levels", padx=5, pady=8)

        label1 = tkinter.Label(self.uigroup, text="Application")
        label2 = tkinter.Label(self.uigroup, text="Libraries")
        label3 = tkinter.Label(self.uigroup, text="Uvicorn")

        label1.grid(row=1, column=1, sticky="W", padx=5, pady=5)
        label2.grid(row=2, column=1, sticky="W", padx=5, pady=5)
        label3.grid(row=3, column=1, sticky="W", padx=5, pady=5)

        debug_levels = ("Not set", "Debug", "Info", "Warning", "Error", "Critical")

        app_log_levels = tkinter.StringVar(
            self.uigroup, debug_levels[0], "app_log_levels"
        )
        print(app_log_levels)
        cb1 = ttk.Combobox(
            self.uigroup,
            values=debug_levels,
            # textvariable=app_log_levels,
            state="readonly",
        )
        cb1.current(0)
        cb1.grid(row=1, column=2, sticky="W", padx=5, pady=5)

        lib_log_levels = tkinter.StringVar(
            self.uigroup, debug_levels[0], "lib_log_levels"
        )
        print(lib_log_levels)
        cb2 = ttk.Combobox(
            self.uigroup,
            values=debug_levels,
            # textvariable=lib_log_levels,
            state="readonly",
        )
        cb2.current(0)
        cb2.grid(row=2, column=2, sticky="W", padx=5, pady=5)

        uvicorn_log_levels = tkinter.StringVar(
            self.uigroup, debug_levels[0], "uvicorn_log_levels"
        )
        print(uvicorn_log_levels)
        cb3 = ttk.Combobox(
            self.uigroup,
            values=debug_levels,
            # textvariable=uvicorn_log_levels,
            state="readonly",
        )
        cb3.current(0)
        cb3.grid(row=3, column=2, sticky="W", padx=5, pady=5)

        # UI groups placement
        self.uigroup.grid(row=1, column=1, sticky="NSWE", padx=5, pady=5)

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

        # get the focus
        ok_button.focus_set()

    def ok(self) -> None:
        """Handle Ok button press."""
        self.destroy()

    def help(self) -> None:
        """Handle Help button press."""
        show_help()
