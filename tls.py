#!/usr/bin/env python3

from tkinter import *

window = Tk()

window.geometry("1000x500")

panel = PanedWindow(window, orient=HORIZONTAL)
panel.pack(side=LEFT, expand=True, fill=BOTH)

panel.add(Frame(panel, borderwidth=2, relief=GROOVE))

panel.add(Button(panel, width=25, text="Fermer", command=window.quit))

panel.add(Label(panel, text='Exchange history', background='grey', anchor=CENTER))

panel.pack()


window.mainloop()