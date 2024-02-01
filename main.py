import tkinter as tk
from pygame import mixer

class BotoneraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Botonera con Sonidos")

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

        self.crear_botones()

    def reproducir_sonido(self, sonido):
        mixer.music.load(self.sonidos[sonido])
        mixer.music.play()

    def crear_botones(self):
        # Crear botones dinámicamente
        for sonido in self.sonidos.keys():
            btn = tk.Button(self.root, text=sonido, command=lambda s=sonido: self.reproducir_sonido(s))
            btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BotoneraApp(root)
    root.mainloop()
