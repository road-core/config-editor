"""Help dialog implementation."""

import tkinter
from typing import Optional


class HelpDialog(tkinter.Toplevel):
    """Help dialog implementation."""

    def __init__(self, parent: Optional[tkinter.Toplevel]) -> None:
        """Perform initialization of help dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Nápověda")
        self.transient(parent)

        self.grab_set()

        f = tkinter.LabelFrame(self, text="x")

        scrollbar = tkinter.Scrollbar(f)
        text = tkinter.Text(f, height=5, width=60)

        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)

        text.tag_configure("h1", font=("Arial", 20, "bold"))
        text.tag_configure("h2", font=("Arial", 16, "bold"))

        text.insert(tkinter.END, "Help\n", "h1")
        text.insert(tkinter.END, "Config editor\n", "h2")

        help_message = """"""
        text.insert(tkinter.END, help_message)

        text.config(state=tkinter.DISABLED)
        f.grid(row=0, column=0, sticky="NWSE")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # rest
        ok_button = tkinter.Button(self, text="OK", command=self.ok)
        ok_button.grid(row=1, column=0, sticky="NWSE")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def ok(self) -> None:
        """Ok button handler."""
        self.destroy()


def show_help() -> None:
    """Display help dialog."""
    HelpDialog(None)
