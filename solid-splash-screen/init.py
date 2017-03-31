#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

class Splash(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="inkscape-splash")
        maingrid = Gtk.Grid()
        self.add(maingrid)

        image = Gtk.Image()
        # set the path to the image below
        image.set_from_file("/opt/Inksplash/inkscape.png")
        maingrid.attach(image, 1, 0, 1, 1)
	

def splashwindow():
    window = Splash()
    window.set_decorated(False)
    window.set_resizable(False)
    window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,5))
    window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("grey"))
    window.set_opacity(5.0)
    window.set_position(Gtk.WindowPosition.CENTER)
    window.show_all()
    Gtk.main()

splashwindow()
