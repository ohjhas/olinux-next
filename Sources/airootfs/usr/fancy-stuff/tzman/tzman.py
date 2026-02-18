#!/usr/bin/env python3

import gi
import subprocess
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ZONEINFO_DIR = "/usr/share/zoneinfo"


class TimezoneApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Timezone Choose")
        self.set_border_width(10)
        self.set_default_size(400, 500)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)

        self.search_entry = Gtk.SearchEntry()
        self.search_entry.connect("search-changed", self.on_search_changed)
        box.pack_start(self.search_entry, False, False, 0)

        self.liststore = Gtk.ListStore(str)
        self.load_timezones()

        self.treeview = Gtk.TreeView(model=self.liststore)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Timezone", renderer, text=0)
        self.treeview.append_column(column)

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.treeview)
        box.pack_start(scrolled, True, True, 0)

        self.button = Gtk.Button(label="Apply")
        self.button.connect("clicked", self.on_apply_clicked)
        box.pack_start(self.button, False, False, 0)

    def load_timezones(self):
        for root, dirs, files in os.walk(ZONEINFO_DIR):
            for name in files:
                path = os.path.join(root, name)
                rel = os.path.relpath(path, ZONEINFO_DIR)
                if not rel.startswith(("posix", "right")) and "/" in rel:
                    self.liststore.append([rel])

    def on_search_changed(self, entry):
        text = entry.get_text().lower()
        self.liststore.clear()
        for root, dirs, files in os.walk(ZONEINFO_DIR):
            for name in files:
                path = os.path.join(root, name)
                rel = os.path.relpath(path, ZONEINFO_DIR)
                if (
                    "/" in rel
                    and not rel.startswith(("posix", "right"))
                    and text in rel.lower()
                ):
                    self.liststore.append([rel])

    def on_apply_clicked(self, button):
        selection = self.treeview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter:
            timezone = model[treeiter][0]
            subprocess.run(["timedatectl", "set-timezone", timezone])
            dialog = Gtk.MessageDialog(
                self,
                0,
                Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK,
                "Success.",
            )
            dialog.format_secondary_text(timezone)
            dialog.run()
            dialog.destroy()


if __name__ == "__main__":
    if os.geteuid() != 0:
        print("must run as sudo.")
        exit(1)

    win = TimezoneApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
