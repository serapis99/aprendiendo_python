import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title("catalogo de peliculas")
    root.resizable(False,False)
    barra_menu(root)
    Frame(root)

    root.mainloop()
if __name__=='__main__':
    main()