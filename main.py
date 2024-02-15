import tkinter as tk
from tkinter import PhotoImage
from pygame import mixer
from PIL import Image, ImageTk

class BotoneraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Botonera con Sonidos")
        self.root.geometry("600x600")  # Ancho x Alto 

        # Inicializar Pygame
        mixer.init()

        # Definir sonidos y botones
        self.sonidos = {

            'Bocina': r'recursos\bocina.mp3',
            'Está gaga claro que si': r'recursos\gaga.mp3',
            'Abracense': r'recursos\abracense.mp3',
            'Dejame que lo piense': r'recursos\dejame_que_lo_piense.mp3',
            #'Gordo Bocon': r'recursos\gordo_bocon.mp3',
            'Yo no se nada': r'recursos\no_se_nada.mp3',
            'Pa que aprenda': r'recursos\pa_que_aprenda.mp3',
            'Prueben Laburando': r'recursos\paren_la_mano.mp3',
            'Ta bien pero': r'recursos\ta_bien.mp3',
            'Tamo Arruinado Hermano': r'recursos\tamo_arruinado_hermano.mp3',
            'Te estan cagando': r'recursos\tene_que_darte.mp3',
            'TRA BA JAR': r'recursos\trabajar_problema.mp3',
            'Uy uy uy': r'recursos\uy_uy.mp3',
            'Vayan a estudiar': r'recursos\vayan_a_estudiar.mp3'
            
        }
        self.imagenes = {
            'fondo' : r'recursos\mr_r0bot.png'
        }        

        # Crear una imagen de fondo
        self.imagen_fondo = PhotoImage(file=self.imagenes['fondo'])
        
        # Configurar un label para mostrar la imagen de fondo
        self.label_fondo = tk.Label(root, image=self.imagen_fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Posicionar el label en toda la ventana
    	
        self.botones_creados = []
        self.crear_botones()

    def reproducir_sonido(self, sonido):
        mixer.music.load(self.sonidos[sonido])
        mixer.music.play()

    def crear_botones(self):
        # Crear botones dinámicamente
        for sonido in self.sonidos.keys():
            if sonido not in self.botones_creados:  # Verificar si el botón ya ha sido creado
                btn = tk.Button(self.root, text=sonido, command=lambda s=sonido: self.reproducir_sonido(s))
                btn.pack(pady=10)  # Utilizar fill='x' para que los botones se expandan horizontalmente
                self.botones_creados.append(sonido)  # Agregar el sonido a la lista de botones creados



if __name__ == "__main__":
    root = tk.Tk()
    app = BotoneraApp(root)
    root.mainloop()
