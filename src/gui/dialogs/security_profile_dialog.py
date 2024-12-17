"""Security profile dialog."""

import tkinter

from gui.icons import Icons


class TLSSecurityProfileDialog(tkinter.Toplevel):
    """Security profile dialog."""

    def __init__(self, parent: tkinter.Toplevel, icons: Icons) -> None:
        """Initialize security profile dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("TLS security profile")
        self.icons = icons
        self.parent = parent

        # don't display the dialog in list of opened windows
        self.transient(parent)

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # app, lib, uvicorn

        ok_button = tkinter.Button(
            self,
            text="OK",
            command=self.ok,
            compound="left",
            image=self.icons.checkbox_icon,
            width=200,
        )
        ok_button.grid(row=2, column=1, sticky="W", padx=10, pady=10)
        # get the focus
        ok_button.focus_set()

    def ok(self) -> None:
        """Handle Ok button press."""
        self.destroy()
