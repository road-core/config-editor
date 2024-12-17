"""Status bar displayed in the main window."""

import tkinter


class StatusBar(tkinter.Frame):
    """Status bar displayed in the main window."""

    def __init__(self, master: tkinter.Tk) -> None:
        """Initialize the class."""
        tkinter.Frame.__init__(self, master)
        self.label = tkinter.Label(self, bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
        self.label.pack(fill=tkinter.X)

    def set(self, string_format, *args):
        """Set status bar messages."""
        self.label.config(text=string_format % args)
        self.label.update_idletasks()

    def clear(self) -> None:
        """Clear status bar content."""
        self.label.config(text="")
        self.label.update_idletasks()
