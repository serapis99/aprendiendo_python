from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QGridLayout, QWidget, QTreeView
from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Taller de desarrollo")
        self.setGeometry(100, 100, 1200, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Configuración del layout principal
        self.layout = QGridLayout(central_widget)
        self.layout.setColumnStretch(0, 2)  # Establecer el estiramiento de la columna 0
        self.layout.setColumnStretch(1, 1)  # Establecer el estiramiento de la columna 1
        self.layout.setRowStretch(0, 1)     # Establecer el estiramiento de la fila 0

        # Configuración del frame1
        self.__configurar_frame1()

        # Configuración del frame2
        self.__configurar_frame2()

        self.show()

    def __configurar_frame1(self):
        # Crear el frame1 y establecer un color de fondo
        self.frame1 = QFrame(self)
        self.frame1.setStyleSheet("background-color: lightblue;")

        # Crear un layout específico para frame1
        self.layout_frame1 = QGridLayout(self.frame1)

        # creando los widget para el layout

        self.frame1_label_numIdentificacion=QLabel("Numero de Identificacion")
        self.frame1_entry_numIdentificacion=QLineEdit()

        self.frame1_label_nombres=QLabel("Nombres")
        self.frame1_entry_nombre=QLineEdit()

        self.frame1_label_apellidos=QLabel("Apellidos")
        self.frame1_entry_apellidos=QLineEdit()

        self.frame1_label_tipoIdentificacion=QLabel("Tipo de Identificacion")
        self.frame1_entry_tipoIdentificacion=QComboBox()
        tipoIdentificacion=["Seleccionar","Cedula Ciudadania",'Tarjeta de Identidad','Cedula Extranjeria','Registro Civil']
        self.frame1_entry_tipoIdentificacion.addItems(tipoIdentificacion)

        self.frame1_label_estadoCivil=QLabel("Estado Civil")
        self.frame1_entry_estadoCivil=QComboBox()
        estadoCivil=["Seleccionar","Soltero",'Casado','Union Libre']
        self.frame1_entry_estadoCivil.addItems(estadoCivil)

        self.frame1_label_fechaNacimiento=QLabel("Fecha de nacimiento")
        self.frame1_entry_fechaNacimiento=QDateEdit()
        self.frame1_entry_fechaNacimiento.setDisplayFormat("yyyy-MM-dd")

        self.frame1_label_numBeneficiarios=QLabel("Numero de Beneficiarios")
        self.frame1_entry_numBeneficiarios=QLineEdit()

        self.frame1_label_fechaIngreso=QLabel("Fecha de Ingreso")
        self.frame1_entry_fechaIngreso=QDateEdit()
        self.frame1_entry_fechaIngreso.setDisplayFormat("yyyy-MM-dd")
        self.frame1_entry_fechaIngreso.setCalendarPopup(True)


        self.frame1_boton_nuevo=QPushButton("Nuevo")
        self.frame1_boton_Guardar=QPushButton("Guardar")
        self.frame1_boton_Cancelar=QPushButton("Cancelar")
        self.frame1_boton_Editar=QPushButton("Editar")
        self.frame1_boton_Eliminar=QPushButton("Eliminar")


        # agregando los elementos al layout

        self.layout_frame1.addWidget(self.frame1_label_numIdentificacion,0,0)
        self.layout_frame1.addWidget(self.frame1_entry_numIdentificacion,0,1)

        self.layout_frame1.addWidget(self.frame1_label_nombres,0,2)
        self.layout_frame1.addWidget(self.frame1_entry_nombre,0,3)

        self.layout_frame1.addWidget(self.frame1_label_apellidos,1,0)
        self.layout_frame1.addWidget(self.frame1_entry_apellidos,1,1)

        self.layout_frame1.addWidget(self.frame1_label_tipoIdentificacion,1,2)
        self.layout_frame1.addWidget(self.frame1_entry_tipoIdentificacion,1,3)

        self.layout_frame1.addWidget(self.frame1_label_estadoCivil,2,0)
        self.layout_frame1.addWidget(self.frame1_entry_estadoCivil,2,1)

        self.layout_frame1.addWidget(self.frame1_label_fechaNacimiento,2,2)
        self.layout_frame1.addWidget(self.frame1_entry_fechaNacimiento,2,3)

        self.layout_frame1.addWidget(self.frame1_label_numBeneficiarios,3,0)
        self.layout_frame1.addWidget(self.frame1_entry_numBeneficiarios,3,1)

        self.layout_frame1.addWidget(self.frame1_label_fechaIngreso,3,2)
        self.layout_frame1.addWidget(self.frame1_entry_fechaIngreso,3,3)

        self.layout_frame1.addWidget(self.frame1_boton_nuevo,4,0)
        self.layout_frame1.addWidget(self.frame1_boton_Guardar,4,1)
        self.layout_frame1.addWidget(self.frame1_boton_Cancelar,4,2)
        self.layout_frame1.addWidget(self.frame1_boton_Editar,6,0)
        self.layout_frame1.addWidget(self.frame1_boton_Eliminar,6,1)

        # Crear el modelo y la vista de la tabla
        self.modelo_tabla = QStandardItemModel()
        self.modelo_tabla.setHorizontalHeaderLabels(["Numero Identificacion",
                                                     "Nombres",
                                                     "Apellidos",
                                                     "Tipo Identificacion",
                                                     "Estado Civil",
                                                     "Fecha de nacimiento",
                                                     "Cantidad de beneficiarios",
                                                     "Fecha de Ingreso"])
        self.__datos_tabla()

        # Añadir frame1 al layout principal
        self.layout.addWidget(self.frame1, 0, 0)

    def __datos_tabla(self):
        # Datos de ejemplo para la tabla
        data = [
            ["1023902902", "ruben dario", "gacha castelblanco", "cc", "soltero", "1990-12-05", '0', '2022-08-16']
        ]

        # Llenar el modelo con los datos
        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            self.modelo_tabla.appendRow(items)

        # Crear la vista de la tabla y agregarla al layout de frame1
        treeView = QTreeView()
        treeView.setModel(self.modelo_tabla)
        treeView.setEditTriggers(QTreeView.NoEditTriggers)
        self.layout_frame1.addWidget(treeView, 5, 0, 1, 4)

    def __configurar_frame2(self):
        # Crear el frame2 y establecer un color de fondo
        self.frame2 = QFrame(self)
        self.frame2.setStyleSheet("background-color: lightgreen;")
        self.layout_frame2 = QGridLayout(self.frame2)

         # Crear el modelo y la vista de la tabla
        self.modelo_tabla_imagenes = QStandardItemModel()
        self.modelo_tabla_imagenes.setHorizontalHeaderLabels(["Nombre Imagen",
                                                     "Fecha"])
        self.__tabla_imagenes()

        # creando los widget para el layout

        self.frame2_label_nombreImagen=QLabel("Nombre de la Imagen")
        self.frame2_entry_nombreImagen=QLineEdit()

        self.frame2_label_fechaImagen=QLabel("Fecha Imagen")
        self.frame2_entry_fechaImagen=QDateEdit()
        self.frame2_entry_fechaImagen.setDisplayFormat("yyyy-MM-dd")
        self.frame2_entry_fechaImagen.setCalendarPopup(True)

        self.frame2_boton_guardar=QPushButton("Guardar")
        self.frame2_boton_editar=QPushButton("Editar")
        self.frame2_boton_eliminar=QPushButton("Eliminar")

        # agregando los elementos al layout

        self.layout_frame2.addWidget(self.frame2_label_nombreImagen,0,0)
        self.layout_frame2.addWidget(self.frame2_entry_nombreImagen,0,1,1,2)

        self.layout_frame2.addWidget(self.frame2_label_fechaImagen,1,0)
        self.layout_frame2.addWidget(self.frame2_entry_fechaImagen,1,1,1,2)

        self.layout_frame2.addWidget(self.frame2_boton_guardar,2,0)
        self.layout_frame2.addWidget(self.frame2_boton_editar,2,1)
        self.layout_frame2.addWidget(self.frame2_boton_eliminar,2,2)


        # Añadir frame2 al layout principal
        self.layout.addWidget(self.frame2, 0, 1)

    def __tabla_imagenes(self):
        # Datos de ejemplo para la tabla
        data = [
            ["imagen 1", "1990-12-05"],
            ["imagen 2", "1990-12-12"],
            ["imagen 3", "1990-12-18"],
            ["imagen 4", "1990-12-25"]
        ]

        # Llenar el modelo con los datos
        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            self.modelo_tabla_imagenes.appendRow(items)

        # Crear la vista de la tabla y agregarla al layout de frame1
        treeView = QTreeView()
        treeView.setModel(self.modelo_tabla_imagenes)
        treeView.setEditTriggers(QTreeView.NoEditTriggers)
        self.layout_frame2.addWidget(treeView, 3, 0, 1, 3)

if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    app.exec()
