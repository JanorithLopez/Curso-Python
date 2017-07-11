import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_texto()
		self.agregar_boton()
		self.agregar_label()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.contenedor.set_row_homogeneous(False)
		self.add(self.contenedor)

	def agregar_texto(self):
		self.texto = Gtk.Entry()
		self.contenedor.attach(self.texto, 0,0,3,1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Cambiar texto')
		self.boton.connect('clicked', self.pasar_texto)
		self.contenedor.attach(self.boton, 1,1,1,1)

	def agregar_label(self):
		self.label = Gtk.Label('Mandar texto')
		self.contenedor.attach(self.label, 0,4,3,1)

	def pasar_texto(self, btn):
		new_txt = self.texto.get_text()
		self.label.set_markup(new_txt).

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
		