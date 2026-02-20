import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

import os
import sys
import subprocess

class TourApp(Gtk.Window):
    def __init__(self, force_lang=None):
        Gtk.Window.__init__(self, title="Tutorial")
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)

        if os.path.exists("/usr/fancy-stuff/olinux-tutorial/main.png"):
            self.set_icon_from_file("/usr/fancy-stuff/olinux-tutorial/main.png")

        if force_lang:
            lang = force_lang
        else:
            lang = os.environ.get("LANG", "") + os.environ.get("LANGUAGE", "")
        is_spanish = "es" in lang

        if is_spanish:
            self.page_data = [
                {"image": "/usr/fancy-stuff/olinux-tutorial/olinuxlogo.png", "text": "Bienvenido a OmegaLinux\nAquí verás lo básico para comenzar con tu sistema."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/2.png", "text": "Añadir aplicaciones al panel:\nHaz clic derecho sobre las apps y elige 'Ajustes de Lanzador de Aplicaciones y barra de tareas', luego selecciona la app que quieras y haz clic en Añadir."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/3.png", "text": "Cambiar temas de apariencia:\nAbre LXAppearance desde el menú y elige tus temas, iconos, cursores, etc. Los temas van en /home/usuario/.themes, y los iconos o cursores en .icons."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/4.png", "text": "Instalar apps desde la terminal:\nUsa 'sudo pacman -S nombre-del-paquete', por ejemplo:\nsudo pacman -S vlc\nsudo pacman -S firefox\nsudo pacman -S  celluloid"},
                {"image": "/usr/fancy-stuff/olinux-tutorial/5.png", "text": "Comandos básicos:\nls para listar archivos y carpetas\ncd para cambiar entre carpetas\nrm para eliminar archivos\ntouch para crear archivos vacios\nsudo para correr comandos como administrador\nnano para crear y editar archivos, etc"}
            ]
            self.label_next = "Siguiente"
            self.label_exit = "Listo"
        else:
            self.page_data = [
                {"image": "/usr/fancy-stuff/olinux-tutorial/olinuxlogo.png", "text": "Welcome to OmegaLinux\nHere you’ll learn the basics to get started."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/2.png", "text": "Add applications to the panel:\nRight-click the apps and select 'Application Launch and Task Bar Settings', then choose the app and click Add."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/3.png", "text": "Change appearance themes:\nOpen LXAppearance from the menu and select your themes, icons, cursors, etc. Themes go in ~/.themes and icons/cursors in ~/.icons."},
                {"image": "/usr/fancy-stuff/olinux-tutorial/4.png", "text": "Install apps in the terminal:\nUse 'sudo pacman -S package-name', for example:\nsudo pacman -S vlc\nsudo pacman -S firefox\nsudo pacman -S celluloid"},
                {"image": "/usr/fancy-stuff/olinux-tutorial/5.png", "text": "Basic commands:\nls to list files and folders\ncd to change folders\nrm to delete files\ntouch to create empty files\nsudo to run commands as superuser\nnano to create and edit files, etc"}
            ]
            self.label_next = "Next"
            self.label_exit = "Exit"

        self.current_page = 0

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.set_margin_top(10)
        self.vbox.set_margin_bottom(10)
        self.vbox.set_margin_start(20)
        self.vbox.set_margin_end(20)
        self.add(self.vbox)

        self.image = Gtk.Image()
        self.vbox.pack_start(self.image, True, True, 0)

        self.label = Gtk.Label()
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.set_line_wrap(True)
        self.label.set_max_width_chars(80)
        self.label.set_margin_top(10)
        self.vbox.pack_start(self.label, False, False, 5)

        self.button = Gtk.Button(label=self.label_next)
        self.button.connect("clicked", self.next_page)
        self.vbox.pack_start(self.button, False, False, 10)

        self.update_page()
        self.music_proc = self.play_music_loop()

    def update_page(self):
        page = self.page_data[self.current_page]

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            page["image"], width=600, height=350, preserve_aspect_ratio=True)
        self.image.set_from_pixbuf(pixbuf)

        self.label.set_text(page["text"])
        self.button.set_label(
            self.label_exit if self.current_page == len(self.page_data) - 1 else self.label_next
        )

    def next_page(self, button):
        if self.current_page < len(self.page_data) - 1:
            self.current_page += 1
            self.update_page()
        else:
            self.quit_app()

    def play_music_loop(self):
        try:
            return subprocess.Popen(["play", "/usr/fancy-stuff/olinux-tutorial/OLINUX_HOME_BGM.ogg", "repeat", "1000"])
        except FileNotFoundError:
            print("error")
            return None

    def quit_app(self, *args):
        if self.music_proc:
            try:
                self.music_proc.terminate()
            except Exception as e:
                print(f"Error: {e}")
        Gtk.main_quit()

if __name__ == "__main__":
    lang_arg = None
    for arg in sys.argv[1:]:
        if arg.startswith("--lang="):
            lang_arg = arg.split("=")[-1].lower()

    app = TourApp(force_lang=lang_arg)
    app.connect("destroy", app.quit_app)
    app.show_all()
    Gtk.main()
