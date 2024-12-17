"""Main window shown on screen."""

import tkinter
from tkinter import filedialog, messagebox
from typing import Any

from gui.dialogs.edit_dialog import EditDialog
from gui.icons import Icons
from gui.menubar import Menubar
from gui.status_bar import StatusBar
from gui.toolbar import Toolbar


class MainWindow:
    """Main window shown on screen."""

    def __init__(self, config_editor: Any) -> None:
        """Initialize main window."""
        self.config_editor = config_editor
        self.root = tkinter.Tk()
        self.root.title("Road Core config editor")

        self.icons = Icons()

        self.toolbar = Toolbar(self.root, self)
        self.statusbar = StatusBar(self.root)

        self.configure_grid()

        self.toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
        self.statusbar.grid(column=1, row=3, columnspan=2, sticky="WE")

        self.menubar = Menubar(self.root, self)
        self.root.config(menu=self.menubar)
        self.root.geometry("480x320")
        # EditDialog(self.root, self.icons)

    def show(self) -> None:
        """Display the main window on screen."""
        self.root.mainloop()

    def quit(self) -> None:
        """Display message box whether to quit the application."""
        answer = messagebox.askyesno(
            "Do you want to quit the program?", "Do you want to quit the program?"
        )
        if answer:
            self.root.quit()

    def configure_grid(self) -> None:
        """Configure grid on canvas."""
        tkinter.Grid.rowconfigure(self.root, 2, weight=1)
        tkinter.Grid.columnconfigure(self.root, 2, weight=1)

    def new_configuration(self) -> None:
        """Initialize new configuration."""
        answer = messagebox.askyesno(
            "Clear current configuration?", "Clear current configuration?"
        )
        if answer:
            self.config_editor.new_configuration()

    def load_configuration(self) -> None:
        """Load configuration from YAML file."""
        filetypes = [("YAML files", "*.yaml"), ("YAML files", "*.yaml")]
        dialog = filedialog.Open(self.root, filetypes=filetypes)
        filename = dialog.show()  # type: ignore [no-untyped-call]
        if filename is not None and filename != "":
            try:
                self.config_editor.load_configuration(filename)
                messagebox.showinfo("Configuration loaded", "Configuration loaded")
            except Exception as e:
                messagebox.showerror("Configuration loading failed", f"Failure {e}")
                print(e)

    def save_configuration(self) -> None:
        """Save configuration into YAML file."""
        try:
            self.config_editor.save_configuration()
            messagebox.showinfo("Configuration saved", "Configuration saved")
        except Exception as e:
            messagebox.showerror("Configuration saving failed", f"Failure {e}")
            print(e)

    def save_as_configuration(self) -> None:
        """Save configuration into specified YAML file."""
        filetypes = [("YAML files", "*.yaml"), ("YAML files", "*.yaml")]
        dialog = filedialog.SaveAs(self.root, filetypes=filetypes)
        filename = dialog.show()  # type: ignore [no-untyped-call]
        if filename is not None and filename != "":
            try:
                self.config_editor.save_configuration_as(filename)
                messagebox.showinfo("Configuration saved", "Configuration saved")
            except Exception as e:
                messagebox.showerror("Configuration saving failed", f"Failure {e}")
                print(e)

    def edit_configuration(self) -> None:
        """Edit configuration using the specialized dialog."""
        EditDialog(self.root, self.icons)

    def check_configuration(self) -> None:
        """Check configuration."""
        result = self.config_editor.check_configuration()
        print(result)
