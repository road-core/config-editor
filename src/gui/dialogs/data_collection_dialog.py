"""Data collection dialog."""

import tkinter

from gui.dialogs.help_dialog import show_help
from gui.icons import Icons


class DataCollectionDialog(tkinter.Toplevel):
    """Data collection dialog."""

    def __init__(self, parent: tkinter.Toplevel, icons: Icons) -> None:
        """Initialize data collection dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Data collection settings")
        self.icons = icons
        self.parent = parent

        # don't display the dialog in list of opened windows
        self.transient(parent)

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

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
