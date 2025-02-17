"""Create a tooltip for a given widget."""

# taken from:
# https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter#36221216

import tkinter
from typing import Optional


class Tooltip:
    """Create a tooltip for a given widget."""

    def __init__(self, widget: tkinter.Button, text: str = "widget info") -> None:
        """Initialize the widget."""
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id: Optional[str] = None
        self.tw: Optional[tkinter.Toplevel] = None

    def enter(self, event: tkinter.Event | None = None) -> None:
        """Handle the event: cursor pointer moves to the tooltip area."""
        self.schedule()

    def leave(self, event: tkinter.Event | None = None) -> None:
        """Handle the event: cursor pointer leaves the tooltip area."""
        self.unschedule()
        self.hidetip()

    def schedule(self) -> None:
        """Schedule time for displaying tooltip."""
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self) -> None:
        """Unschedule time for displaying tooltip."""
        current_id = self.id
        self.id = None
        if current_id:
            self.widget.after_cancel(current_id)

    def showtip(self, event: Optional[tkinter.Event] = None) -> None:
        """Show the tooltip on screen."""
        x = y = 0
        x, y, _, _ = self.widget.bbox()  # type: ignore [misc]
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tkinter.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{x}+{y}")
        label = tkinter.Label(
            self.tw,
            text=self.text,
            justify="left",
            background="#ffffff",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
        )
        label.pack(ipadx=1)

    def hidetip(self) -> None:
        """Hide the tooltip."""
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
