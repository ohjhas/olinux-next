import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import os
import subprocess
import shlex

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    gi.require_version('Gst', '1.0')
    from gi.repository import Gst
    Gst.init(None)
    HAVE_GST = True
except Exception:
    HAVE_GST = False

PAGE_ORDER = ['8f682a0e', '43b25f69']

class App(Gtk.Window):
    def __init__(self):
        super().__init__(title='About this PC')
        self.set_default_size(468, 485)
        self.set_resizable(True)
        icon_path = os.path.join(BASE_DIR, 'assets', 'omegastart.png')
        if os.path.isfile(icon_path):
            self.set_icon_from_file(icon_path)
        self.connect('destroy', Gtk.main_quit)
        self.stack = Gtk.Stack()
        self.radio_meta = {}
        self.add(self.stack)
        self.player = None
        self.build_pages()

    def build_pages(self):
        radio_registries = {}
        fixed_8f682a0e = Gtk.Fixed()
        fixed_8f682a0e.set_size_request(468, 485)
        radio_registries['8f682a0e'] = {}
        _img_path = os.path.join(BASE_DIR, 'assets', 'olinuxlogo.png')
        try:
            _pb = GdkPixbuf.Pixbuf.new_from_file(_img_path)
            _pb = _pb.scale_simple(152, 149, GdkPixbuf.InterpType.BILINEAR)
            w_fcaa463f = Gtk.Image.new_from_pixbuf(_pb)
        except Exception:
            w_fcaa463f = Gtk.Image.new_from_icon_name('image-missing', Gtk.IconSize.DIALOG)
        w_fcaa463f.set_size_request(152, 149)
        fixed_8f682a0e.put(w_fcaa463f, 0, 10)
        w_accebbc2 = Gtk.Label(label='OmegaLinux NEXT')
        w_accebbc2.set_size_request(306, 52)
        fixed_8f682a0e.put(w_accebbc2, 124, 66)
        _provider = Gtk.CssProvider()
        _provider.load_from_data('* { font-size: 35px; }'.encode())
        w_accebbc2.get_style_context().add_provider(_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        try:
            _out = subprocess.check_output(shlex.split('cat /etc/hostname'), stderr=subprocess.STDOUT, timeout=5)
            _out = _out.decode('utf-8', 'replace').strip()
        except Exception as exc:
            _out = f'<command error: {exc}>'
        _label_text = 'Hostname: $output'.replace('$output', _out)
        w_ad8cc53e = Gtk.Label(label=_label_text)
        w_ad8cc53e.set_size_request(160, 36)
        fixed_8f682a0e.put(w_ad8cc53e, 154, 141)
        try:
            _out = subprocess.check_output(shlex.split('awk \'/MemTotal/ {printf "%.2f GB", $2/1024/1024}\' /proc/meminfo'), stderr=subprocess.STDOUT, timeout=5)
            _out = _out.decode('utf-8', 'replace').strip()
        except Exception as exc:
            _out = f'<command error: {exc}>'
        _label_text = 'RAM: $output'.replace('$output', _out)
        w_2d1a063e = Gtk.Label(label=_label_text)
        w_2d1a063e.set_size_request(159, 33)
        fixed_8f682a0e.put(w_2d1a063e, 154, 177)
        try:
            _out = subprocess.check_output(shlex.split("awk -F': ' '/model name/{print $2;exit}' /proc/cpuinfo"), stderr=subprocess.STDOUT, timeout=5)
            _out = _out.decode('utf-8', 'replace').strip()
        except Exception as exc:
            _out = f'<command error: {exc}>'
        _label_text = 'CPU: $output'.replace('$output', _out)
        w_90abe7ae = Gtk.Label(label=_label_text)
        w_90abe7ae.set_size_request(468, 31)
        fixed_8f682a0e.put(w_90abe7ae, 0, 210)
        try:
            _out = subprocess.check_output(shlex.split('bash -c "lspci | grep -i vga | head -n1 | sed \'s/^.*: //\'"'), stderr=subprocess.STDOUT, timeout=5)
            _out = _out.decode('utf-8', 'replace').strip()
        except Exception as exc:
            _out = f'<command error: {exc}>'
        _label_text = 'GPU: $output'.replace('$output', _out)
        w_8cc6d08e = Gtk.Label(label=_label_text)
        w_8cc6d08e.set_size_request(468, 36)
        fixed_8f682a0e.put(w_8cc6d08e, 0, 241)
        w_3feb6f39 = Gtk.Label(label='Version: Deep Blue Sea (R2)')
        w_3feb6f39.set_size_request(233, 31)
        fixed_8f682a0e.put(w_3feb6f39, 117, 277)
        w_9948a592 = Gtk.Label(label='Archiso configuration files are publicly available on GitHub')
        w_9948a592.set_size_request(352, 33)
        fixed_8f682a0e.put(w_9948a592, 58, 316)
        w_0899d796 = Gtk.Label(label='at omega-linux/olinux-next.')
        w_0899d796.set_size_request(234, 20)
        fixed_8f682a0e.put(w_0899d796, 117, 349)
        w_0b91a794 = Gtk.Button(label='Credits')
        w_0b91a794.set_size_request(120, 32)
        fixed_8f682a0e.put(w_0b91a794, 16, 433)
        w_0b91a794.connect('clicked', self.make_action_handler('goto_page', '43b25f69'))
        w_a1408c3a = Gtk.Button(label='Ok')
        w_a1408c3a.set_size_request(56, 32)
        fixed_8f682a0e.put(w_a1408c3a, 395, 433)
        w_a1408c3a.connect('clicked', self.make_action_handler('quit', ''))
        self.stack.add_titled(fixed_8f682a0e, '8f682a0e', 'InfoGenPage')
        fixed_43b25f69 = Gtk.Fixed()
        fixed_43b25f69.set_size_request(468, 485)
        radio_registries['43b25f69'] = {}
        w_1c14fd1d = Gtk.Label(label='Credits')
        w_1c14fd1d.set_size_request(134, 45)
        fixed_43b25f69.put(w_1c14fd1d, 8, 10)
        _provider = Gtk.CssProvider()
        _provider.load_from_data('* { font-size: 35px; }'.encode())
        w_1c14fd1d.get_style_context().add_provider(_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        w_af6998c6 = Gtk.Label(label='AnddyCort (GitLab) - "classic-menu" LXPanel plugin')
        w_af6998c6.set_size_request(311, 38)
        fixed_43b25f69.put(w_af6998c6, 19, 71)
        w_7709b7d9 = Gtk.Label(label='Eric Naim, Piotr Gorski (CachyOS) - CachyOS LTS Kernel')
        w_7709b7d9.set_size_request(330, 28)
        fixed_43b25f69.put(w_7709b7d9, 19, 109)
        w_df19da04 = Gtk.Label(label='Arch Linux - base')
        w_df19da04.set_size_request(102, 33)
        fixed_43b25f69.put(w_df19da04, 19, 137)
        w_a411157c = Gtk.Button(label='<- Back')
        w_a411157c.set_size_request(120, 32)
        fixed_43b25f69.put(w_a411157c, 330, 435)
        w_a411157c.connect('clicked', self.make_action_handler('goto_page', '8f682a0e'))
        self.stack.add_titled(fixed_43b25f69, '43b25f69', 'CredsPage')
        self.stack.set_visible_child_name('8f682a0e')

    def run_action(self, action_type, action_value):
        if action_type == 'shell':
            if action_value:
                try:
                    subprocess.Popen(shlex.split(action_value))
                except Exception as exc:
                    print(exc)
        elif action_type == 'next_page':
            self.goto_relative(1)
        elif action_type == 'prev_page':
            self.goto_relative(-1)
        elif action_type == 'goto_page':
            self.stack.set_visible_child_name(action_value)
        elif action_type == 'quit':
            Gtk.main_quit()

    def make_action_handler(self, action_type, action_value):
        def handler(widget, *args):
            self.run_action(action_type, action_value)
        return handler

    def make_radio_trigger_handler(self, page_id, group):
        def handler(widget, *args):
            for radio_widget, action_type, action_value in self.radio_meta.get((page_id, group), []):
                if radio_widget.get_active():
                    self.run_action(action_type, action_value)
                    break
        return handler

    def goto_relative(self, delta):
        current = self.stack.get_visible_child_name()
        if current not in PAGE_ORDER:
            return
        idx = (PAGE_ORDER.index(current) + delta) % len(PAGE_ORDER)
        self.stack.set_visible_child_name(PAGE_ORDER[idx])

    def start_music(self, path, loop):
        if not HAVE_GST or not os.path.isfile(path):
            return
        self.player = Gst.ElementFactory.make('playbin', 'player')
        self.player.set_property('uri', Gst.filename_to_uri(path))
        bus = self.player.get_bus()
        bus.add_signal_watch()
        def on_message(bus, message):
            if message.type == Gst.MessageType.EOS and loop:
                self.player.seek_simple(Gst.Format.TIME, Gst.SeekFlags.FLUSH, 0)
                self.player.set_state(Gst.State.PLAYING)
        bus.connect('message', on_message)
        self.player.set_state(Gst.State.PLAYING)

def main():
    win = App()
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
