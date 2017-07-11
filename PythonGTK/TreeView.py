"""
 Crea un TreeView

 1- Crea el model de datos (Gtk.ListStore(type, type, ..., type))
 2- Crear el widget que contiene o muestra los datos de modelo, TreeView(<model>)
 3- Definir las columnas y su contenido

  3.1- Crear celda para cada una de la fila. Los CellRenderer son widget que 
  sirven para mostrar su contenido dentro de otro
  3.2- Crear columna TreeViewColum del TreeView, mostraran los datos usando args
  (Titulo, CellRenderer, posicion en el modelo de la info a mostrar.)
  3.3- Agregar cada TreeViewColum al TreeView widget

"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0,0,1,1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1
			)

    def agregar_lista(self):
    	self.modelo = Gtk.ListStore(str, float)
    	self.modelo.append(['Valor1', 1.5])

    	self.lista_activos = Gtk.TreeView(self.modelo)

        descripcion = Gtk.CellRendererText()
        columna_descripcion = Gtk.TreeViewColum('Descripcion', descripcion, text=0)

        monto = Gtk.CellRendererText()
        columna_monto = Gtk.TreeViewColum('Monto', monto, text=1)

        self.lista_activos.append_colum(columna_descripcion)
        self.lista_activos.append_colum(columna_monto)

        self.contenedor.attach_next_to(
        	self.lista_activos,
        	self.boton,
        	Gtk.PositionType.BOTTOM,
        	1,
        	1
        	)


if __name__ == '__main__':
    ventana = MiVentana()
    ventana.show_all()
    Gtk.main()