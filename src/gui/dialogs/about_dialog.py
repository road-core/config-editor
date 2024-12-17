"""Implementation of simple 'About' dialog."""

from tkinter import messagebox


def about():
    """Show 'about' dialog."""
    messagebox.showinfo(
        "Config editor", "Configuration editor for the Road Core service"
    )
