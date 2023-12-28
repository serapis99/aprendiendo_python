from Modelo.modelo import Modelo
from Vista.Vista import Vista
from Controlador.controlador import Controlador

modelo = Modelo()
vista = Vista(None)
controlador = Controlador(modelo, vista)
vista.controlador = controlador  # Establece la referencia del controlador en la vista
vista.mainloop()