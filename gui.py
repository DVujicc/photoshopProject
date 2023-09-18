from ctypes import alignment
from operator import le
from string import whitespace
from struct import pack
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog as fd
from functools import partial
from PIL import ImageTk, Image

def openfile(lista):
    imageloc = fd.askopenfilename() 
    print(imageloc)
    lista[0] = imageloc


window = Tk()
window.title("Photoshop")
window.geometry("1000x700")
window.configure(bg="#6e6e6e")
window.resizable(False, False)

frame1 = Frame(
    window,
    padx=10,
    pady=10,
    bg="#6e6e6e"
)

label = Label(
    frame1, 
    text="Photoshop",
    font=Font(size=41),
    borderwidth=0,
    bg="#6e6e6e",
    foreground="white"
)
label.pack(side=LEFT)

imageloc = ["icons/save.png"]

nekipartial = partial(openfile, imageloc)

ic1 = PhotoImage(file="icons/openfile.png")
openimgBtn = Button(
    frame1,
    image = ic1,
    borderwidth=0,
    command=nekipartial
).pack(side=LEFT)

ic2 = PhotoImage(file="icons/crop.png")
cropPhotoBtn = Button (
    frame1,
    image=ic2,
    borderwidth=0
).pack(side=LEFT)

ic3 = PhotoImage(file="icons/flip.png")
flipHorizontalBtn = Button(
    frame1,
    image = ic3,
    borderwidth=0
).pack(side=LEFT)

ic4 = PhotoImage(file="icons/flip_vertical.png")
flipVerticalBtn = Button(
    frame1,
    image = ic4,
    borderwidth=0
).pack(side=LEFT)

ic5 = PhotoImage(file="icons/brightness.png")
brightness = Button(
    frame1,
    image = ic5,
    borderwidth=0
).pack(side=LEFT)

ic6 = PhotoImage(file="icons/contrast.png")
contrast = Button(
    frame1,
    image = ic6,
    borderwidth=0
).pack(side=LEFT)

ic7 = PhotoImage(file="icons/save.png")
save = Button(
    frame1,
    image = ic7,
    borderwidth=0
).pack(side=LEFT)

frame1.pack(side=TOP)

photoFrame = Frame(
    window,
    bg="white",
    width=400,
    height=500,
).pack()

image = Image.open(imageloc[0])
photo = ImageTk.PhotoImage(image)

window.mainloop()