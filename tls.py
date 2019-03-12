#!/usr/bin/env python3

from tkinter import *

def prepare_gui_structure():
  window = Tk()  # Create a window
  window.geometry("1000x500")  # Define window size
  window.title("TLS Learning Software")  # Define window title
  # now, set a panel in the window
  panel = PanedWindow(window, orient=HORIZONTAL)  # Add panel to window
  panel.pack(side=LEFT, expand=True, fill=BOTH)  # Set the panel alignment to left


def add_permanent_elements():
  panel.add(Button(panel, width=75, text="Fermer", command=window.quit))
  panel.add(Label(panel, text='Exchange history', background='grey', anchor=CENTER))
  panel.pack()


if __name__ == "__main__":
  prepare_gui_structure()
  add_permanent_elements()
  window.mainloop()