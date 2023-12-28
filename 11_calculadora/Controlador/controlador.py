class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def actualizar_valor(self, digito):
        self.modelo.actualizar_valor(digito)
        self.vista.valor_var.set(self.modelo.valor_actual)

    def realizar_operacion(self, operacion):
        self.modelo.realizar_operacion(operacion)
        self.vista.valor_var.set(str(self.modelo.valor_guardado))

    def obtener_resultado(self):
        self.modelo.obtener_resultado()
        self.vista.valor_var.set(str(self.modelo.valor_guardado))
        self.reiniciar()

    def reiniciar(self):
        self.modelo.reiniciar()

