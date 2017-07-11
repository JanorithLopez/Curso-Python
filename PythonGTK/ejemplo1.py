import gi

gi.require_version('Gtk','3.0')

from gi.repository import Gtk


def imprimir_algo(btn):
	print btn
	print 'Hola Mundo'
	


if __name__ == '__main__':

	ventana = Gtk.Window(title= 'Ejemplo1')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Boton 1')
	boton.connect('clicked', imprimir_algo)

	botn2 = Gtk.Button('Boton 2')

	contenedor = Gtk.VBox()

	contenedor.pack_start(boton, False, True,0)
	#contenedor.pack_start(botn2, True, False,0)
	contenedor.pack_end(botn2, False, True,0)

	ventana.add(contenedor)
	ventana.show_all()

	Gtk.main()
