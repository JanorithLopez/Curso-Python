import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VentanaBalance(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(VentanaBalance, self).__init__(*args, **kwargs)
        self.set_default_size(500, 300)
        self.connect('delete-event', Gtk.main_quit)

        self.agregar_cont_activo()
        self.agregar_label_act()
        self.agregar_entr_descripcion_act()
        self.agregar_entr_monto_act()
        self.agregar_boton_activo()
        self.agregar_lista_act()

        self.agregar_label_pas()
        self.agregar_entr_descripcion_pas()
        self.agregar_entr_monto_pas()
        self.agregar_boton_pasivo()
        self.agregar_lista_pas()

        self.agregar_totales()

    def agregar_cont_activo(self):
        self.contenedor_activo = Gtk.Grid()
        self.contenedor_activo.set_column_homogeneous(True)
        self.add(self.contenedor_activo)

    def agregar_label_act(self):
        self.label_activo = Gtk.Label('--- ACTIVOS ---')
        self.contenedor_activo.attach(self.label_activo, 1,-1,1,1)

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
        col_descripcion_act = Gtk.TreeViewColumn('Descripcion activo', descripcion_act, text=0)

        monto_act = Gtk.CellRendererText()
        col_monto_act = Gtk.TreeViewColumn('Monto activo', monto_act, text=1)

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

    # PASIVOS
    def agregar_label_pas(self):
        self.label_pasivo = Gtk.Label('--- PASIVOS ---')
        self.contenedor_activo.attach(self.label_pasivo, 1,6,1,1)

    def agregar_entr_descripcion_pas(self):
        self.entada_descripcion_pas = Gtk.Entry()
        self.contenedor_activo.attach(self.entada_descripcion_pas, 0,7,2,1 )

    def agregar_entr_monto_pas(self):
        self.entrada_monto_pas = Gtk.Entry()
        self.contenedor_activo.attach(self.entrada_monto_pas, 2,7,1,1)

    def agregar_boton_pasivo(self):
        self.boton_pasivo = Gtk.Button('Agregar Pasivo')
        self.contenedor_activo.attach_next_to(
            self.boton_pasivo,
            self.entada_descripcion_pas,
            Gtk.PositionType.BOTTOM,
            3,
            1)
        self.boton_pasivo.connect('clicked', self.agregar_fila_pas)

    def agregar_lista_pas(self):
        self.modelo_pas = Gtk.ListStore(str, float)

        self.lista_datos_pas = Gtk.TreeView(self.modelo_pas)

        descripcion_pas = Gtk.CellRendererText()
        col_descripcion_pas = Gtk.TreeViewColumn('Descripcion pasivo', descripcion_pas, text=0)

        monto_pas = Gtk.CellRendererText()
        col_monto_pas = Gtk.TreeViewColumn('Monto pasivo', monto_pas, text=1)

        self.lista_datos_pas.append_column(col_descripcion_pas)
        self.lista_datos_pas.append_column(col_monto_pas)

        self.contenedor_activo.attach_next_to(
            self.lista_datos_pas,
            self.boton_pasivo,
            Gtk.PositionType.BOTTOM,
            3,
            1)

    def agregar_fila_pas(self, btn):
        texto_pas = self.entada_descripcion_pas.get_text()
        monto_pasivo = self.entrada_monto_pas.get_text()
        cantidad_pas = float(monto_pasivo)
        self.modelo_pas.append([texto_pas, cantidad_pas])

    # SUMAR PASIVOS Y ACTIVOS

    def agregar_totales(self):
        self.total_activos = Gtk.Label('-- Total Activos --')
        self.contenedor_activo.attach(self.total_activos, 0,10,1,1)

        self.total_pasivos = Gtk.Label('-- Total Pasivos --')
        self.contenedor_activo.attach(self.total_pasivos, 0,11,1,1)

        self.total_capital = Gtk.Label('-- Total Capital --')
        self.contenedor_activo.attach(self.total_capital, 0,12,1,1)

        


if __name__ == '__main__':
    ventana = VentanaBalance()
    ventana.show_all()
    Gtk.main()