import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ventana import Ventana

app = QApplication(sys.argv)

app.setOrganizationName('Celsia')
app.setOrganizationDomain('Celsia.com')
app.setApplicationName('Pruebas')
vantana_principal=Ventana()
sys.exit(app.exec())
