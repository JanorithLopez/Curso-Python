import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaBalance(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(VentanaBalance, self).__init__(*args, **kwargs)
        self.set_default_size(500, 300)
        self.connect('delete-event', Gtk.main_quit)

        self.agregar_cont_activo()
        self.agregar_entr_descripcion_act()
        self.agregar_entr_monto_act()
        self.agregar_boton_activo()
        self.agregar_lista_act()

    def agregar_cont_activo(self):
        self.contenedor_activo = Gtk.Grid()
        self.contenedor_activo.set_column_homogeneous(True)
        self.add(self.contenedor_activo)

    def agregar_entr_descripcion_act(self):
        self.entada_descripcion_act = Gtk.Entry()
        self.contenedor_activo.attach(self.entada_descripcion_act, 0,0,2,1)

    def agregar_entr_monto_act(self):
        self.entrada_monto_act = Gtk.Entry()
        self.contenedor_activo.attach(self.entrada_monto_act, 2,0,1,1)

    def agregar_boton_activo(self):
        self.boton_activo = Gtk.Button('Agregar Activo')
        self.contenedor_activo.attach_next_to(
            self.boton_activo,
            self.entada_descripcion_act,
            Gtk.PositionType.BOTTOM,
            3,
            1)
        self.boton_activo.connect('clicked', self.agregar_fila_act)

    def agregar_lista_act(self):
        self.modelo_act = Gtk.ListStore(str, float)
        self.lista_datos_ac = Gtk.TreeView(self.modelo_act)

        descripcion_act = Gtk.CellRendererText()
        col_descripcion_act = Gtk.TreeViewColumn('Descripcion', descripcion_act, text=0)

        monto_act = Gtk.CellRendererText()
        col_monto_act = Gtk.TreeViewColumn('Monto', monto_act, text=1)

        self.lista_datos_ac.append_column(col_descripcion_act)
        self.lista_datos_ac.append_column(col_monto_act)

        self.contenedor_activo.attach_next_to(
            self.lista_datos_ac,
            self.boton_activo,
            Gtk.PositionType.BOTTOM,
            3,
            1)

    def agregar_fila_act(self, btn):
        texto_act = self.entada_descripcion_act.get_text()
        monto_activo = self.entrada_monto_act.get_text()
        cantidad_act = float(monto_activo)
        self.modelo_act.append([texto_act, cantidad_act])

if __name__ == '__main__':
    ventana = VentanaBalance()
    ventana.show_all()
    Gtk.main()