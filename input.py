from tkinter import *
import automaton
from PIL import ImageTk, Image

screen = Tk()
screen.title("Cellular automaton")
screen.geometry("640x550")

columns_label = Label(screen, text="Number of columns")
columns_label.grid(row=0, column=0)
columns_entry = Entry(screen)
columns_entry.grid(row=1, column=0)

rows_label = Label(screen, text="Number of rows")
rows_label.grid(row=0, column=1)
rows_entry = Entry(screen)
rows_entry.grid(row=1, column=1)

rule_label = Label(screen, text="rule")
rule_label.grid(row=0, column=2)
rule_entry = Entry(screen)
rule_entry.grid(row=1, column=2)

img = ImageTk.PhotoImage(Image.open("res/blank_image.png"))
panel = Label(screen, image=img)
panel.grid(row=3, column=0, columnspan=3)


def callback():
    automaton.count(int(rows_entry.get()), int(columns_entry.get()), int(rule_entry.get()))
    img = Image.open("res/image.png")
    filename = ImageTk.PhotoImage(img)
    canvas = Canvas(screen, height=640, width=640)
    canvas.image = filename
    canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.grid(row=3, column=0, columnspan=3)


B = Button(screen, text="draw!", command=callback)
B.grid(row=2, column=1)

mainloop()
