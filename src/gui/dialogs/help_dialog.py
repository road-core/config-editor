"""Help dialog implementation."""

import tkinter
from typing import Optional


class HelpDialog(tkinter.Toplevel):
    """Help dialog implementation."""

    def __init__(
        self,
        parent: Optional[tkinter.Toplevel],
        title: str = "Help",
        help_text: list[tuple[str, Optional[str]]] = [],
    ) -> None:
        """Perform initialization of help dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Help")
        self.transient(parent)

        self.grab_set()

        f = tkinter.LabelFrame(self, text=title)

        scrollbar = tkinter.Scrollbar(f)
        text = tkinter.Text(f, height=30, width=80)

        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)

        # define new tags that can be used in help text
        text.tag_configure("<h1>", font=("Arial", 20, "bold"))
        text.tag_configure("<h2>", font=("Arial", 16, "bold"))

        for t in help_text:
            if len(t) == 2:
                if t[1] is not None:  # make type checker happy
                    text.insert(tkinter.END, t[1] + "\n", t[0])
            else:
                text.insert(tkinter.END, t[0] + "\n")

        # text.insert(tkinter.END, "Help\n", "<h1>")
        # text.insert(tkinter.END, "Config editor\n", "<h2>")

        # help_message = "****"
        # text.insert(tkinter.END, help_message)

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
    help_text: list[tuple[str, Optional[str]]] = [
        ("<h1>", "Road core service configuration editor"),
        ("<h2>", "Main help"),
        ("help text", None),
    ]
    HelpDialog(None, help_text=help_text)


def show_help_for_auth_dialog() -> None:
    """Display help for auth dialog."""
    help_text: list[tuple[str, Optional[str]]] = [
        ("<h1>", "Road core service configuration editor"),
        ("<h2>", "Authentication configuration dialog"),
        ("help text", None),
    ]
    HelpDialog(None, help_text=help_text)
