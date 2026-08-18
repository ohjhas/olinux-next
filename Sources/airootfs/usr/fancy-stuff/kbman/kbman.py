#!/usr/bin/env python3
import gi
import subprocess
import re

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def load_layouts():
    layouts = []
    try:
        with open("/usr/share/X11/xkb/rules/base.lst", "r") as f:
            content = f.read()
    except FileNotFoundError:
        return [("us", "English (US)")]

    m = re.search(r"^! layout\n(.*?)^!", content, re.S | re.M)
    if not m:
        return [("us", "English (US)")]

    for line in m.group(1).splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 1)
        if len(parts) == 2:
            code, desc = parts
            layouts.append((code, desc))

    layouts.sort(key=lambda x: x[1])
    return layouts


class KeyboardSwitcher(Gtk.Window):
    def __init__(self):
        super().__init__(title="kbman")
        self.set_default_size(360, 480)
        self.set_border_width(8)

        self.layouts = load_layouts()
        self.search_text = ""

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Search layouts...")
        self.search_entry.connect("search-changed", self.on_search_changed)
        vbox.pack_start(self.search_entry, False, False, 0)

        self.store = Gtk.ListStore(str, str)
        for code, desc in self.layouts:
            self.store.append([code, desc])

        self.filter_model = self.store.filter_new()
        self.filter_model.set_visible_func(self.filter_func)

        self.tree = Gtk.TreeView(model=self.filter_model)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Layout", renderer, text=1)
        self.tree.append_column(column)
        self.tree.set_headers_visible(False)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        scroll.add(self.tree)
        vbox.pack_start(scroll, True, True, 0)

        apply_btn = Gtk.Button(label="Apply")
        apply_btn.connect("clicked", self.on_apply)
        vbox.pack_start(apply_btn, False, False, 0)

        self.status_label = Gtk.Label(label="")
        vbox.pack_start(self.status_label, False, False, 0)

        test_label = Gtk.Label(label="Test your keyboard here")
        test_label.set_halign(Gtk.Align.START)
        vbox.pack_start(test_label, False, False, 0)

        self.test_entry = Gtk.Entry()
        vbox.pack_start(self.test_entry, False, False, 0)

    def filter_func(self, model, iter, data):
        if not self.search_text:
            return True
        code = model[iter][0].lower()
        desc = model[iter][1].lower()
        return self.search_text in code or self.search_text in desc

    def on_search_changed(self, entry):
        self.search_text = entry.get_text().lower()
        self.filter_model.refilter()

    def on_apply(self, button):
        selection = self.tree.get_selection()
        model, tree_iter = selection.get_selected()
        if tree_iter is None:
            self.status_label.set_text("Select a layout first")
            return

        code = model[tree_iter][0]
        desc = model[tree_iter][1]

        try:
            subprocess.run(["setxkbmap", code], check=True)
        except Exception as e:
            self.status_label.set_text(f"setxkbmap failed: {e}")
            return

        try:
            subprocess.run(
                ["pkexec", "localectl", "set-x11-keymap", code], check=True
            )
            self.status_label.set_text(f"Layout set to {desc}")
        except subprocess.CalledProcessError:
            self.status_label.set_text(
                f"Session updated to {desc}, permanent change cancelled or failed"
            )
        except FileNotFoundError:
            self.status_label.set_text("pkexec not found, could not set permanently")


def main():
    win = KeyboardSwitcher()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
