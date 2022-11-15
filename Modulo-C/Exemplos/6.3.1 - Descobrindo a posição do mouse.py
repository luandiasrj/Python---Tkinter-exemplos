from tkinter import *


class AutoCADE:
    def __init__(self, raiz):
        raiz.title('AutoCADÊ')
        self.canvas = Canvas(raiz, width=300, height=300, bg='#beff8c',
                             cursor='hand2')
        self.canvas.bind('<1>', self.desenhar)
        self.canvas.pack()

    def desenhar(self, event):
        x_origem = self.canvas.winfo_rootx()
        y_origem = self.canvas.winfo_rooty()
        x_abs = self.canvas.winfo_pointerx()
        y_abs = self.canvas.winfo_pointery()
        try:
            P = (x_abs - x_origem, y_abs - y_origem)
            self.canvas.create_line(self.ultimo_P, P)
            self.ultimo_P = P
        except:
            self.ultimo_P = (x_abs - x_origem, y_abs - y_origem)


inst = Tk()
AutoCADE(inst)
inst.mainloop()