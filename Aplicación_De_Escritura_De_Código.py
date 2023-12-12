from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("abrir.jpeg"))
save_img = ImageTk.PhotoImage(Image.open("guardar.jpeg"))
play_img = ImageTk.PhotoImage(Image.open("reproducir.jpeg"))

label_file_name = Label(root, text="Nombre del archivo: ")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

open_button = Button(root, image = open_img,text="Abrir archivo")
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button = Button(root, image = save_img,text="Guardar archivo")
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

play_button = Button(root, image = play_img,text="Reproducir archivo")
play_button.place(relx=0.17,rely=0.03,anchor=CENTER)


root.mainloop()