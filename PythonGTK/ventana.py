import gi
gi.require_version('Gtk',  '3.0')
from gi.repository import Gtk

#This is to Print "Hello world " in the terminal 

class Mywindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="My firts app in Fedora")
		self.button = Gtk.Button(label = 'PLease, CLick Here')
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)
	def on_button_clicked(self, widget):
		#print("Hello WORLD")
		win = Gtk.Window(title= "THis is a replica")
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

		
win = Mywindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


#This is to show a simple windows
"""
win = Gtk.Window(title= "MI first APP in Python")
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
"""