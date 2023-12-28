from Modelo.operaciones import suma
from Modelo.operaciones import resta
from Modelo.operaciones import multiplicar
from Modelo.operaciones import dividir
from decimal import Decimal
class Modelo:
    def __init__(self):
        self.valor_actual = "0"
        self.valor_guardado = 0
        self.operacion_pendiente = None
        self.ultimo_digito=None

    def realizar_operacion(self, operacion):
        if self.operacion_pendiente==None:
            self.valor_guardado=self.pasar_numero(self.valor_actual)
        else:
            num1=self.valor_guardado
            num2=self.pasar_numero(self.valor_actual)
            resultado=0
            if self.operacion_pendiente=="+":
                resultado=suma(num1,num2)
            elif self.operacion_pendiente=="-":
                resultado=resta(num1,num2)
            elif self.operacion_pendiente=="*":
                resultado=multiplicar(num1,num2)
            elif self.operacion_pendiente=="/":
                resultado=dividir(num1,num2)

            self.valor_guardado=resultado
            print(f"{num1} {self.operacion_pendiente} {num2} = {resultado}")

        self.operacion_pendiente=operacion
        self.ultimo_digito=operacion

    def pasar_numero(self,cadena):
        numero=0
        if "." in cadena:
            numero=Decimal(cadena)
        else:
            numero=int(cadena)
        return numero

    def actualizar_valor(self, digito):

        if self.ultimo_digito in ['+', '-', '*', '/']:
            self.valor_actual="0"
            self.ultimo_digito=None

        if self.valor_actual=="0" and digito!=".":
            self.valor_actual=digito
        else:
            self.valor_actual+=digito

    def obtener_resultado(self):
        if self.ultimo_digito in ['+', '-', '*', '/']:
            self.valor_actual="0"
            self.ultimo_digito=None
        self.realizar_operacion(None)

    def reiniciar(self):
        self.valor_actual = "0"
        self.valor_guardado = 0
        self.operacion_pendiente = None
        self.ultimo_digito=None