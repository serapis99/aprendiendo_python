from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
from PySide6.QtCore import Qt
import sys

app = QApplication()
main_window = QMainWindow()

# Crear un widget de acoplamiento con un QTextEdit
dock_widget = QDockWidget("Explorador", main_window)
text_edit = QTextEdit()
dock_widget.setWidget(text_edit)

# Agregar el widget de acoplamiento a la ventana principal
main_window.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

main_window.show()
sys.exit(app.exec())