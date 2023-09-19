from hashlib import new
from multiprocessing.dummy import current_process
from operator import ne
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageGrab
from functions import *

file_path = ""
WIDTH = 600
HEIGHT = 400


#pravi inicijalnu belu sliku za canvas
def get_image():
    img = Image.new("RGB", (400, 400), "white")  
    img_tk = ImageTk.PhotoImage(img)
    return img_tk

#funkcija za otvaranje fajla
def openfile():
    global file_path, current_image
    file_path = fd.askopenfilename()
    if file_path:
        global image
        image = Image.open(file_path)
        ar = float(image.width / image.height)
        new_width = int(ar*HEIGHT)
        image = image.resize((new_width, HEIGHT), Image.LANCZOS)
        #img.thumbnail((600, 400))
        image = ImageTk.PhotoImage(image)
        current_image = image
    
        canvas.create_image(0, 0, anchor=NW, image=current_image)

#funkcija za cuvanje slike
def saveimage():
    global file_path
    if file_path:
        image = ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(), canvas.winfo_rooty() + canvas.winfo_height()))
        file_path = fd.asksaveasfilename(defaultextension=".jpg")
        image.save(file_path)

#funkcija koja otvara ili zatvara polje za unos
def brightFunc():
    if frame_for_input.winfo_ismapped():
        frame_for_input.pack_forget()
    else:
        frame_for_input.pack()
    
#funkcija koja uzima vrednost sa inputa i poziva funkciju za brajtnes
def submit_brightness():
    global file_path, current_image
    value = brightness_input.get()
    value = int(value)
    value /= 100
    current_image = blend(file_path, value)
    ar = float(current_image.width / current_image.height)
    new_width = int(ar * HEIGHT)
    current_image = current_image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)
    frame_for_input.pack_forget()

#funkcija koja otvara ili zatvara polje za unos
def contrastFunc():
    if frame_for_input2.winfo_ismapped():
        frame_for_input2.pack_forget()
    else:
        frame_for_input2.pack()

#funkcija koja uzima vrednost sa inputa, poziva funkciju contrast i ucitava novu sliku na canvas
def submit_contrast():
    global file_path, current_image
    val = contrast_input.get()
    val = int(val)
    current_image = contrast(file_path, val/10)
    ar = float(current_image.width / current_image.height)
    new_width = int(ar * HEIGHT)
    current_image = current_image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

    frame_for_input2.pack_forget()


#funkcija koja poziva funkciju za vertical flip i ucitava novu sliku
def pozovivert():
    global file_path, current_image
    current_image = flip_vertically(file_path)
    ar = float(current_image.width / current_image.height)
    new_width = int(ar * HEIGHT)
    current_image = current_image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)


#funkcija koja poziva funkciju za horizontal flip i ucitava novu sliku
def pozovihor():
    global file_path, current_image
    current_image = flip_horizontally(file_path)
    ar = float(current_image.width / current_image.height)
    new_width = int(ar * HEIGHT)
    current_image = current_image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

def pozovirot(): 
    global file_path, current_image
    current_image = rotation(file_path, 90)
    ar = float(current_image.width / current_image.height)
    new_width = int(ar * HEIGHT)
    current_image = current_image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

    

window = Tk()
window.title("Photoshop")
window.geometry("1000x700")
window.configure(bg="#00004d")
window.resizable(False, False)

frame1 = Frame(
    window,
    padx=10,
    pady=10,
    bg="#00004d"
)

label = Label(
    frame1, 
    text="Photoshop",
    font=Font(size=41),
    borderwidth=0,
    bg="#00004d",
    foreground="white"
)
label.pack(side=LEFT)

ic1 = PhotoImage(file="icons/openfile.png")
openimgBtn = Button(
    frame1,
    image=ic1,
    borderwidth=0,
    command=openfile
)
openimgBtn.pack(side=LEFT)

ic2 = PhotoImage(file="icons/crop.png")
cropPhotoBtn = Button (
    frame1,
    image=ic2,
    borderwidth=0
)
cropPhotoBtn.pack(side=LEFT)

ic8 = PhotoImage(file="icons/rotate.png")
rotate = Button(
    frame1,
    image=ic8,
    borderwidth=0,
    command=pozovirot
).pack(side=LEFT)

ic3 = PhotoImage(file="icons/flip_horizontal.png")
flipHorizontalBtn = Button(
    frame1,
    image=ic3,
    borderwidth=0,
    command=pozovihor
)
flipHorizontalBtn.pack(side=LEFT)

ic4 = PhotoImage(file="icons/flip_vertical.png")
flipVerticalBtn = Button(
    frame1,
    image=ic4,
    borderwidth=0,
    command=pozovivert
)
flipVerticalBtn.pack(side=LEFT)


#Brightness

frame_for_input = Frame(window, padx=10, pady=10, bg="#00004d")

brigth_label = Label(frame_for_input, text="Input value for brightness: ").pack(side=LEFT)

bright_submit = Button(frame_for_input, text="submit", command=submit_brightness).pack(side=LEFT)

brightness_input = Entry(frame_for_input)
brightness_input.pack()


ic5 = PhotoImage(file="icons/brightness.png")
brightness = Button(frame1, image=ic5, borderwidth=0, command=brightFunc)
brightness.pack(side=LEFT)


#Contrast
frame_for_input2 = Frame(window, padx=10, pady=10, bg="#00004d")
contrast_label = Label(frame_for_input2, text="Input value for contrast: ").pack(side=LEFT)
contrast_submit = Button(frame_for_input2, text="submit", command=submit_contrast).pack(side=LEFT)
contrast_input = Entry(frame_for_input2)
contrast_input.pack()

ic6 = PhotoImage(file="icons/contrast.png")
contrast_btn = Button(frame1, image=ic6, borderwidth=0, command=contrastFunc)
contrast_btn.pack(side=LEFT)


#Save
ic7 = PhotoImage(file="icons/save.png")
save = Button(
    frame1,
    image=ic7,
    borderwidth=0,
    command=saveimage
)
save.pack(side=LEFT)

frame1.pack(side=TOP)

photoFrame = Frame(
    window,
    width=600,
    height=400
)
photoFrame.pack(fill=BOTH, expand=TRUE, padx=30, pady=30)  # Moved packing of photoFrame here

canvas = Canvas(photoFrame, width=600, height=400) 
canvas.pack(side=TOP)

current_image = get_image()
canvas.create_image(0, 0, anchor=NW, image=current_image)



window.mainloop()