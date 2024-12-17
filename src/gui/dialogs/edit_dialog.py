"""Implementation of configuration editor."""

import tkinter
from tkinter import ttk
from typing import Optional

from gui.dialogs.auth_dialog import AuthDialog
from gui.dialogs.cache_dialog import ConversationCacheDialog
from gui.dialogs.data_collection_dialog import DataCollectionDialog
from gui.dialogs.default_model_dialog import DefaultModelSelection
from gui.dialogs.default_provider_dialog import DefaultProviderSelection
from gui.dialogs.llm_dialog import LLMDialog
from gui.dialogs.logging_dialog import LoggingDialog
from gui.dialogs.security_profile_dialog import TLSSecurityProfileDialog
from gui.dialogs.tls_dialog import TLSConfigurationDialog
from gui.icons import Icons

BUTTON_WIDTH = 100


class EditDialog(tkinter.Toplevel):
    """Implementation of configuration editor."""

    def __init__(self, parent: tkinter.Toplevel, icons: Icons) -> None:
        """Initialize the dialog."""
        tkinter.Toplevel.__init__(self, parent)
        self.title("Configuration editor")
        self.icons = icons
        self.parent = parent
        self.group1: Optional[tkinter.LabelFrame] = None
        self.group2: Optional[tkinter.LabelFrame] = None
        self.group3: Optional[tkinter.LabelFrame] = None

        # don't display the dialog in list of opened windows
        self.transient(parent)
        self.add_widgets()
        self.set_dialog_properties()

    def add_widgets(self) -> None:
        """Add all widgets on the dialog."""
        self.add_llm_group()
        self.add_service_settings_group()
        self.add_devel_settings_group()

        # UI groups placement
        if self.group1 is None or self.group2 is None or self.group3 is None:
            return
        self.group1.grid(row=1, column=1, sticky="NSWE", padx=5, pady=5)
        self.group2.grid(row=1, column=2, sticky="NSWE", padx=5, pady=5)
        self.group3.grid(row=1, column=3, sticky="NSWE", padx=5, pady=5)

        # rest
        ok_button = tkinter.Button(
            self,
            text="OK",
            command=self.ok,
            compound="left",
            image=self.icons.checkbox_icon,
            width=200,
        )
        ok_button.grid(row=2, column=1, sticky="W", padx=10, pady=10)

        cancel_button = tkinter.Button(
            self,
            text="Cancel",
            command=self.cancel,
            compound="left",
            image=self.icons.exit_icon,
            width=200,
        )
        cancel_button.grid(row=2, column=2, sticky="W", padx=10, pady=10)
        # set the focus
        ok_button.focus_set()

    def set_dialog_properties(self) -> None:
        """Set edit dialog properties."""
        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # how the buttons should behave
        self.bind("<Return>", lambda _: self.ok())
        self.bind("<Escape>", lambda _: self.destroy())

    def add_llm_group(self) -> None:
        """Add LLM group widgets onto the dialog."""
        # UI groups
        self.group1 = tkinter.LabelFrame(self, text="LLM section", padx=5, pady=8)

        # LLM settings
        button_new_llm = tkinter.Button(
            self.group1,
            text="Add LLM",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.added_icon,
            command=self.new_llm,
        )
        button_new_llm.grid(row=1, column=1, sticky="WE", padx=5, pady=5)

    def add_service_settings_group(self) -> None:
        """Add service settings widgets onto the dialog."""
        self.group2 = tkinter.LabelFrame(self, text="Service settings", padx=5, pady=8)
        # service settings
        label1 = tkinter.Label(self.group2, text="Authentication")
        label1.grid(row=1, column=1, sticky="W", padx=5, pady=5)
        btn_auth = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.auth_config,
        )
        btn_auth.grid(row=1, column=2, sticky="W", padx=5, pady=5)

        label2 = tkinter.Label(self.group2, text="Conversation cache")
        label2.grid(row=2, column=1, sticky="W", padx=5, pady=5)
        btn_cache = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.cache_config,
        )
        btn_cache.grid(row=2, column=2, sticky="W", padx=5, pady=5)

        label3 = tkinter.Label(self.group2, text="Logging")
        label3.grid(row=3, column=1, sticky="W", padx=5, pady=5)
        btn_logging = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.logging_config,
        )
        btn_logging.grid(row=3, column=2, sticky="W", padx=5, pady=5)

        label4 = tkinter.Label(self.group2, text="Default provider")
        label4.grid(row=4, column=1, sticky="W", padx=5, pady=5)
        btn_provider = tkinter.Button(
            self.group2,
            text="Select",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.list_icon,
            command=self.default_provider_selection,
        )
        btn_provider.grid(row=4, column=2, sticky="W", padx=5, pady=5)

        label5 = tkinter.Label(self.group2, text="Default model")
        label5.grid(row=5, column=1, sticky="W", padx=5, pady=5)
        btn_model = tkinter.Button(
            self.group2,
            text="Select",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.list_icon,
            command=self.default_model_selection,
        )
        btn_model.grid(row=5, column=2, sticky="W", padx=5, pady=5)

        label6 = tkinter.Label(self.group2, text="TLS security profile")
        label6.grid(row=6, column=1, sticky="W", padx=5, pady=5)
        btn_sec_profile = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.tls_security_profile,
        )
        btn_sec_profile.grid(row=6, column=2, sticky="W", padx=5, pady=5)

        label7 = tkinter.Label(self.group2, text="TLS configuration")
        label7.grid(row=7, column=1, sticky="W", padx=5, pady=5)
        btn_tls = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.tls_config,
        )
        btn_tls.grid(row=7, column=2, sticky="W", padx=5, pady=5)

        label8 = tkinter.Label(self.group2, text="User data collection")
        label8.grid(row=8, column=1, sticky="W", padx=5, pady=5)
        btn_data_collection = tkinter.Button(
            self.group2,
            text="Configure",
            width=BUTTON_WIDTH,
            compound="left",
            image=self.icons.configure_icon,
            command=self.data_collection_config,
        )
        btn_data_collection.grid(row=8, column=2, sticky="W", padx=5, pady=5)

        label9 = tkinter.Label(self.group2, text="Query validation method")
        label9.grid(row=9, column=1, sticky="W", padx=5, pady=5)
        query_validation_methods = ("LLM", "Keyword")
        query_validation_method = tkinter.StringVar(
            self.group2, query_validation_methods[0], "query_validation_method"
        )

        cb = ttk.Combobox(
            self.group2,
            values=query_validation_methods,
            textvariable=query_validation_method,
            state="readonly",
        )
        cb.current(0)
        cb.grid(row=9, column=2, sticky="W", padx=5, pady=5)

    def add_devel_settings_group(self) -> None:
        """Add devel settings widgets onto the dialog."""
        self.group3 = tkinter.LabelFrame(self, text="Devel settings", padx=5, pady=8)
        # devel settings
        cb1 = tkinter.Checkbutton(
            self.group3, text="Authentication"
        )  # , variable=var1, onvalue=1, offvalue=0)
        cb1.grid(row=1, column=1, sticky="W", padx=5, pady=5)
        cb2 = tkinter.Checkbutton(
            self.group3, text="TLS enabled"
        )  # , variable=var1, onvalue=1, offvalue=0)
        cb2.grid(row=2, column=1, sticky="W", padx=5, pady=5)
        cb3 = tkinter.Checkbutton(
            self.group3, text="Dev UI enabled"
        )  # , variable=var1, onvalue=1, offvalue=0)
        cb3.grid(row=3, column=1, sticky="W", padx=5, pady=5)

    def ok(self) -> None:
        """Handle Ok button press."""
        self.destroy()

    def cancel(self) -> None:
        """Handle Cancel button press."""
        self.destroy()

    def new_llm(self) -> None:
        """Show sialog to add new LLM into configuration."""
        LLMDialog(self, self.icons)

    def auth_config(self) -> None:
        """Show authentication dialog."""
        AuthDialog(self, self.icons)

    def tls_config(self) -> None:
        """Show TLS configuration dialog."""
        TLSConfigurationDialog(self, self.icons)

    def tls_security_profile(self) -> None:
        """Show TLS security profile dialog."""
        TLSSecurityProfileDialog(self, self.icons)

    def cache_config(self) -> None:
        """Show cache configuration dialog."""
        ConversationCacheDialog(self, self.icons)

    def logging_config(self) -> None:
        """Show logging configuration dialog."""
        LoggingDialog(self, self.icons)

    def data_collection_config(self) -> None:
        """Show data collection configuration dialog."""
        DataCollectionDialog(self, self.icons)

    def default_model_selection(self) -> None:
        """Show default model selection dialog."""
        DefaultModelSelection(self, self.icons)

    def default_provider_selection(self) -> None:
        """Show default provider selection dialog."""
        DefaultProviderSelection(self, self.icons)
