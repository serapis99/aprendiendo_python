from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QGridLayout, QWidget, QTreeView
from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit,QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QDate
from Modelo import Modelo
import re

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.gestor_bd=Modelo()
        self.gestor_bd.crear_tablas()
        self.gestor_bd.cerrar_bd()
        
        
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

        #bloqueando los campos
        self.__bloquear_limpiar_campos()

        # variables de clase
        self.patron_nombres = re.compile(r'^[a-zA-Z\s]+$')
        self.esNuevo=False

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
        self.frame1_entry_fechaNacimiento.setCalendarPopup(True)
        self.frame1_entry_fechaNacimiento.setMinimumDate(QDate(1900, 1, 1)) 
        self.frame1_entry_fechaNacimiento.setMaximumDate(QDate.currentDate())
        self.frame1_entry_fechaNacimiento.setDate(QDate(1800, 1, 1)) 

        self.frame1_label_numBeneficiarios=QLabel("Numero de Beneficiarios")
        self.frame1_entry_numBeneficiarios=QLineEdit()

        self.frame1_label_fechaIngreso=QLabel("Fecha de Ingreso")
        self.frame1_entry_fechaIngreso=QDateEdit()
        self.frame1_entry_fechaIngreso.setDisplayFormat("yyyy-MM-dd")
        self.frame1_entry_fechaIngreso.setCalendarPopup(True)
        self.frame1_entry_fechaIngreso.setDate(QDate.currentDate())
        self.frame1_entry_fechaIngreso.setMinimumDate(QDate(1900, 1, 1)) 
        self.frame1_entry_fechaIngreso.setMaximumDate(QDate.currentDate())
        self.frame1_entry_fechaIngreso.setDate(QDate(1800, 1, 1)) 



        self.frame1_boton_nuevo=QPushButton("Nuevo")
        self.frame1_boton_Guardar=QPushButton("Guardar")
        self.frame1_boton_Cancelar=QPushButton("Cancelar")
        self.frame1_boton_Editar=QPushButton("Editar")
        self.frame1_boton_Eliminar=QPushButton("Eliminar")


        # agregando los eventos

        self.frame1_boton_nuevo.clicked.connect(self.__activar_limpiar_campos)
        self.frame1_boton_Cancelar.clicked.connect(self.__bloquear_limpiar_campos)
        self.frame1_boton_Guardar.clicked.connect(self.__guardar_datos)
        self.frame1_boton_Editar.clicked.connect(self.__editar_campos)
        self.frame1_boton_Eliminar.clicked.connect(self.__eliminar_formulario)

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
        self.__datos_tabla()

        # Añadir frame1 al layout principal
        self.layout.addWidget(self.frame1, 0, 0)

    def __datos_tabla(self):
        # Datos de ejemplo para la tabla
        self.modelo_tabla.clear()
        self.modelo_tabla.setHorizontalHeaderLabels(["Numero Identificacion",
                                                     "Nombres",
                                                     "Apellidos",
                                                     "Tipo Identificacion",
                                                     "Estado Civil",
                                                     "Fecha de nacimiento",
                                                     "Cantidad de beneficiarios",
                                                     "Fecha de Ingreso",
                                                     "Cantidad de Imagenes"])
        
        self.gestor_bd=Modelo()
        data=self.gestor_bd.obtener_formularios()
        self.gestor_bd.cerrar_bd()

        # Llenar el modelo con los datos
        for row in data:
            items = [QStandardItem(str(item)) for item in row]
            self.modelo_tabla.appendRow(items)

        # Crear la vista de la tabla y agregarla al layout de frame1
        self.table_frame1_treeView = QTreeView()
        self.table_frame1_treeView.setModel(self.modelo_tabla)
        self.table_frame1_treeView.setEditTriggers(QTreeView.NoEditTriggers)
        self.layout_frame1.addWidget(self.table_frame1_treeView, 5, 0, 1, 4)

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

    def __editar_campos(self):
        currentIndex = self.table_frame1_treeView.currentIndex().row()

        if currentIndex==-1:
            box = QMessageBox()
            texto="No se selecciono ningun registro a modificar"
            titulo="Error en el registro"
            box.critical(self,titulo,texto, QMessageBox.Ok)
        else:
            # Obtener los datos de la fila seleccionada
            self.esNuevo=False

            datos_fila = [self.modelo_tabla.index(currentIndex, columna).data() 
                      for columna in range(self.modelo_tabla.columnCount())]
            
            self.frame1_entry_numIdentificacion.setEnabled(False)
            self.frame1_entry_nombre.setEnabled(True)
            self.frame1_entry_apellidos.setEnabled(True)
            self.frame1_entry_tipoIdentificacion.setEnabled(True)
            self.frame1_entry_estadoCivil.setEnabled(True)
            self.frame1_entry_fechaNacimiento.setEnabled(True)
            self.frame1_entry_numBeneficiarios.setEnabled(True)
            self.frame1_entry_fechaIngreso.setEnabled(True)

            self.frame1_boton_Guardar.setEnabled(True)
            self.frame1_boton_Cancelar.setEnabled(True)
            self.frame1_boton_nuevo.setEnabled(False)


             # --- validando campos tipo identificacion
              
            if datos_fila[3]=='CC':
                tipoIdentificacion='Cedula Ciudadania'
            elif datos_fila[3]=='TI':
                tipoIdentificacion='Tarjeta de Identidad'
            elif datos_fila[3]=='CE':
                tipoIdentificacion='Cedula Extranjeria'
            elif datos_fila[3]=='RC':
                tipoIdentificacion='Registro Civil'
            else:
                tipoIdentificacion='NA'

            
            # -- validando 

            if datos_fila[4]=="1":
                estadoCivil="Soltero"
            elif datos_fila[4]=="2":
                estadoCivil='Casado'
            elif datos_fila[4]=="3":
                estadoCivil='Union Libre'
            else:
                estadoCivil=0

            fechaNacimiento=datos_fila[5].split("-")
            fechaIngreso=datos_fila[7].split("-")

            self.frame1_entry_numIdentificacion.setText(datos_fila[0])
            self.frame1_entry_nombre.setText(datos_fila[1])
            self.frame1_entry_apellidos.setText(datos_fila[2])
            self.frame1_entry_tipoIdentificacion.setCurrentText(tipoIdentificacion)
            self.frame1_entry_estadoCivil.setCurrentText(estadoCivil)
            self.frame1_entry_fechaNacimiento.setDate(QDate(int(fechaNacimiento[0]),int(fechaNacimiento[1]),int(fechaNacimiento[2])))
            self.frame1_entry_numBeneficiarios.setText(datos_fila[6])
            self.frame1_entry_fechaIngreso.setDate(QDate(int(fechaIngreso[0]),int(fechaIngreso[1]),int(fechaIngreso[2])))

    def __guardar_datos(self):
        if (self.__validar_datos_frame1()):
            box = QMessageBox()
            if(self.esNuevo):
                existe=self.__validar_si_ya_existe()
                if not existe:
              
                    # --- validando campos tipo identificacion
              
                    if self.frame1_entry_tipoIdentificacion.currentText()=='Cedula Ciudadania':
                        tipoIdentificacion='CC'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Tarjeta de Identidad':
                        tipoIdentificacion='TI'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Cedula Extranjeria':
                        tipoIdentificacion='CE'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Registro Civil':
                        tipoIdentificacion='RC'
                    else:
                        tipoIdentificacion='NA'

                    
                    # -- validando 

                    if self.frame1_entry_estadoCivil.currentText()=="Soltero":
                        estadoCivil=1
                    elif self.frame1_entry_estadoCivil.currentText()=='Casado':
                        estadoCivil=2
                    elif self.frame1_entry_estadoCivil.currentText()=='Union Libre':
                        estadoCivil=3
                    else:
                        estadoCivil=0

                    try:
                        self.gestor_bd=Modelo()
                        self.gestor_bd.nuevo_formulario(
                            self.frame1_entry_numIdentificacion.text(),
                            self.frame1_entry_nombre.text(),
                            self.frame1_entry_apellidos.text(),
                            tipoIdentificacion,
                            estadoCivil,
                            self.frame1_entry_fechaNacimiento.date().toString('yyyy-MM-dd'),
                            self.frame1_entry_numBeneficiarios.text(),
                            self.frame1_entry_fechaIngreso.date().toString('yyyy-MM-dd')
                        )
                        self.gestor_bd.cerrar_bd()
                        texto="Se creo el registro correctamente"
                        titulo="registro correcto"
                        box.information(self,titulo,texto, QMessageBox.Ok)
                        self.__datos_tabla()
                        self.__bloquear_limpiar_campos()
                    except:
                        self.gestor_bd.cerrar_bd()
                        texto="Hubo un error y no se creo el registro"
                        titulo="Error en el registro"
                        box.critical(self,titulo,texto, QMessageBox.Ok)
                else:
                    self.gestor_bd.cerrar_bd()
                    texto="El identificador del registro ya existe"
                    titulo="Error en el registro"
                    box.critical(self,titulo,texto, QMessageBox.Ok)
            else:
                    
                # --- validando campos tipo identificacion
              
                    if self.frame1_entry_tipoIdentificacion.currentText()=='Cedula Ciudadania':
                        tipoIdentificacion='CC'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Tarjeta de Identidad':
                        tipoIdentificacion='TI'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Cedula Extranjeria':
                        tipoIdentificacion='CE'
                    elif self.frame1_entry_tipoIdentificacion.currentText()=='Registro Civil':
                        tipoIdentificacion='RC'
                    else:
                        tipoIdentificacion='NA'

                    
                # -- validando 

                    if self.frame1_entry_estadoCivil.currentText()=="Soltero":
                        estadoCivil=1
                    elif self.frame1_entry_estadoCivil.currentText()=='Casado':
                        estadoCivil=2
                    elif self.frame1_entry_estadoCivil.currentText()=='Union Libre':
                        estadoCivil=3
                    else:
                        estadoCivil=0

                    try:
                        self.gestor_bd=Modelo()
                        self.gestor_bd.actualizar_formulario(
                            self.frame1_entry_numIdentificacion.text(),
                            self.frame1_entry_nombre.text(),
                            self.frame1_entry_apellidos.text(),
                            tipoIdentificacion,
                            estadoCivil,
                            self.frame1_entry_fechaNacimiento.date().toString('yyyy-MM-dd'),
                            self.frame1_entry_numBeneficiarios.text(),
                            self.frame1_entry_fechaIngreso.date().toString('yyyy-MM-dd')
                        )
                        self.gestor_bd.cerrar_bd()
                        texto="Se actualizo el registro correctamente"
                        titulo="registro correcto"
                        box.information(self,titulo,texto, QMessageBox.Ok)
                        self.__datos_tabla()
                        self.__bloquear_limpiar_campos()
                    except:
                        self.gestor_bd.cerrar_bd()
                        texto="Hubo un error y no se creo el registro"
                        titulo="Error en el registro"
                        box.critical(self,titulo,texto, QMessageBox.Ok)
        else:
            print("Uno de los campos Fallo la validacion")

    def __eliminar_formulario(self):
        currentIndex = self.table_frame1_treeView.currentIndex().row()
        box = QMessageBox()

        if currentIndex==-1:
            texto="No se selecciono ningun registro a modificar"
            titulo="Error en el registro"
            box.critical(self,titulo,texto, QMessageBox.Ok)
        else:
            # Obtener los datos de la fila seleccionada
            self.esNuevo=False

            datos_fila = [self.modelo_tabla.index(currentIndex, columna).data() 
                      for columna in range(self.modelo_tabla.columnCount())]
            
            self.gestor_bd=Modelo()
            try:
                self.gestor_bd.eliminar_formulario(datos_fila[0])
                texto="El formulario se elimino correctamente"
                titulo="Error en el registro"
                box.information(self,titulo,texto, QMessageBox.Ok)
                self.__datos_tabla()
            except:
                texto="Hubo un error al momento de eliminar el formulario"
                titulo="Error en el registro"
                box.critical(self,titulo,texto, QMessageBox.Ok)
            
            self.gestor_bd.cerrar_bd()
            

    def __validar_si_ya_existe(self):
        self.gestor_bd=Modelo()
        existe_en_base=self.gestor_bd.buscar_formulario(self.frame1_entry_numIdentificacion.text())
        self.gestor_bd.cerrar_bd()
        
        box = QMessageBox()
        if existe_en_base:
            texto="Se Encontro que el Numero de Identificacion ya existe en la base de datos"
            titulo="Error en el registro"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return True
        else:
            return False





    def __validar_datos_frame1(self):

        numIdentificacion=self.frame1_entry_numIdentificacion.text()
        nombre=self.frame1_entry_nombre.text()
        apellido=self.frame1_entry_apellidos.text()
        numBeneficiario=self.frame1_entry_numBeneficiarios.text()

        box = QMessageBox()

        # validando campo numero de Identificacion

        if numIdentificacion.strip()=='':
            texto="El campo numero de Identificacion no puede ser vacio"
            titulo="Campo numero Identificacion"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        else:
            if not numIdentificacion.isnumeric():
                texto="El campo numero de Identificacion debe ser numerico"
                titulo="Campo numero Identificacion"
                box.critical(self,titulo,texto, QMessageBox.Ok)
                return False
            else:
                self.frame1_entry_numIdentificacion.setText(numIdentificacion.strip())

        # validando campo Nombre
                
        if nombre.strip()=='':
            texto="El campo Nombre no puede estar vacio"
            titulo="Campo Nombre"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        
        elif len(nombre)>30:
            texto="El campo Nombre no puede tener mas de 30 caracteres"
            titulo="Campo Nombre"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        
        elif not self.patron_nombres.match(nombre):
            texto="El nombre ingresado no lo consideramos valido"
            titulo="Campo Nombre"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        else:
            self.frame1_entry_nombre.setText(nombre.strip())


        
        # validando campo Apellido
                
        if apellido.strip()=='':
            texto="El campo Apellido no puede estar vacio"
            titulo="Campo Apellido"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        
        elif len(apellido)>30:
            texto="El campo Apellido no puede tener mas de 30 caracteres"
            titulo="Campo Apellido"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        
        elif not self.patron_nombres.match(apellido):
            texto="El Apellido ingresado no lo consideramos valido"
            titulo="Campo Apellido"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        else:
            self.frame1_entry_apellidos.setText(apellido.strip())
        
        # validar tipoIdentificacion
        
        if self.frame1_entry_tipoIdentificacion.currentText()=="Seleccionar":
            texto="Selecciona un Tipo de Identificacion"
            titulo="Campo Tipo de Identificacion"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        
        # validar tipoIdentificacion

        if self.frame1_entry_estadoCivil.currentText()=="Seleccionar":
            texto="Selecciona el estado Civil"
            titulo="Campo Estado Civil"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        

        # validando el numero de beneficiarios

        if numBeneficiario.strip()=='':
            texto="El campo numero de Beneficiarios no puede ser vacio"
            titulo="Campo numero Beneficiarios"
            box.critical(self,titulo,texto, QMessageBox.Ok)
            return False
        else:
            if not numBeneficiario.isnumeric():
                texto="El campo numero de Beneficiarios debe ser numerico"
                titulo="Campo numero Beneficiarios"
                box.critical(self,titulo,texto, QMessageBox.Ok)
                return False
            else:
                self.frame1_entry_numBeneficiarios.setText(numBeneficiario.strip())

        return True
    

    def __activar_limpiar_campos(self):
        self.frame1_entry_numIdentificacion.setText("")
        self.frame1_entry_nombre.setText("")
        self.frame1_entry_apellidos.setText("")
        self.frame1_entry_tipoIdentificacion.setCurrentIndex(0)
        self.frame1_entry_estadoCivil.setCurrentIndex(0)
        self.frame1_entry_fechaNacimiento
        self.frame1_entry_numBeneficiarios.setText("")

        self.frame1_entry_numIdentificacion.setEnabled(True)
        self.frame1_entry_nombre.setEnabled(True)
        self.frame1_entry_apellidos.setEnabled(True)
        self.frame1_entry_tipoIdentificacion.setEnabled(True)
        self.frame1_entry_estadoCivil.setEnabled(True)
        self.frame1_entry_fechaNacimiento.setEnabled(True)
        self.frame1_entry_numBeneficiarios.setEnabled(True)
        self.frame1_entry_fechaIngreso.setEnabled(True)

        self.frame1_boton_Guardar.setEnabled(True)
        self.frame1_boton_Cancelar.setEnabled(True)
        self.frame1_boton_nuevo.setEnabled(False)

        self.esNuevo=True

    def __bloquear_limpiar_campos(self):
        self.frame1_entry_numIdentificacion.setText("")
        self.frame1_entry_nombre.setText("")
        self.frame1_entry_apellidos.setText("")
        self.frame1_entry_tipoIdentificacion.setCurrentIndex(0)
        self.frame1_entry_estadoCivil.setCurrentIndex(0)
        self.frame1_entry_fechaNacimiento
        self.frame1_entry_numBeneficiarios.setText("")

        self.frame1_entry_numIdentificacion.setEnabled(False)
        self.frame1_entry_nombre.setEnabled(False)
        self.frame1_entry_apellidos.setEnabled(False)
        self.frame1_entry_tipoIdentificacion.setEnabled(False)
        self.frame1_entry_estadoCivil.setEnabled(False)
        self.frame1_entry_fechaNacimiento.setEnabled(False)
        self.frame1_entry_numBeneficiarios.setEnabled(False)
        self.frame1_entry_fechaIngreso.setEnabled(False)

        self.frame1_boton_Guardar.setEnabled(False)
        self.frame1_boton_Cancelar.setEnabled(False)
        self.frame1_boton_nuevo.setEnabled(True)

        self.esNuevo=False



    
if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    app.exec()
