import tkinter as tk
from tkinter import ttk

class Vista(tk.Tk):
    def __init__(self,controlador):
        super().__init__()
        self.title("Calculadora")
        self.centrar(250,300)
        self.valor_var = tk.StringVar()
        self.valor_var.set("0")
        self.agregar_botones_pantalla()
        self.punto_presionado = False
        self.controlador=controlador


    def centrar(self,ancho,alto):
        ancho_ventana=ancho
        alto_ventana=alto

        # obtener la resolucion de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla= self.winfo_screenheight()

        # Calcular la posición para centrar la ventana
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    def agregar_botones_pantalla(self):

        pantalla = ttk.Entry(self, 
                             textvariable=self.valor_var, 
                             font=('Arial', 20), 
                             justify='right', 
                             state='disabled')
        pantalla.grid(row=0, column=0, columnspan=4, sticky='nsew',padx=5,pady=5)

        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        columna = 0
        for boton_texto in botones:

            ttk.Button(self, 
                       text=boton_texto, 
                       command=lambda t=boton_texto: self.click_boton(t)
                       ).grid(row=fila, column=columna, sticky='nsew',padx=5,pady=5)
            columna += 1

            if columna > 3:
                columna = 0
                fila += 1
        
        # Configuración del layout
        self.grid_rowconfigure(0, weight=2)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i+1, weight=1)

    def habilitar_deshabilitar_punto(self,activar):
            for widget in self.winfo_children():
                if isinstance(widget, ttk.Button) and widget['text'] == '.':
                    if activar:
                        widget['state'] = tk.NORMAL
                    else:
                        widget['state'] = tk.DISABLED


    def click_boton(self, valor):

        if valor.isdigit():
            self.controlador.actualizar_valor(valor)
            
        elif valor == '.' and not self.punto_presionado:
            self.punto_presionado = True  # Desactivar el botón del punto después de presionarlo una vez
            self.controlador.actualizar_valor(valor)
            self.habilitar_deshabilitar_punto(False)
            
        elif valor in ['+', '-', '*', '/']:
            self.punto_presionado = False  # Restablecer el estado del punto cuando se realiza una operación
            self.controlador.realizar_operacion(valor)
            self.habilitar_deshabilitar_punto(True)

        elif valor == '=':
            self.controlador.obtener_resultado()
            self.punto_presionado = False  # Restablecer el estado del punto al presionar '='
            self.habilitar_deshabilitar_punto(True)

        else:  # Restablecer
            self.controlador.reiniciar()
            self.valor_var.set("0")
            self.punto_presionado = False
            self.habilitar_deshabilitar_punto(True)


