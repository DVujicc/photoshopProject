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
image = None
current_image = None

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
        current_image = ImageTk.PhotoImage(image)

        canvas.create_image(0, 0, anchor=NW, image=current_image)

#funkcija za cuvanje slike OVO POPRAVI
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
    global file_path, current_image, image
    value = brightness_input.get()
    value = int(value)
    value /= 100
    image = blend(image, value)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
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
    global file_path, current_image, image
    val = contrast_input.get()
    val = int(val)
    image = contrast(image, val/10)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

    frame_for_input2.pack_forget()


#funkcija koja poziva funkciju za vertical flip i ucitava novu sliku
def pozovivert():
    global file_path, current_image, image
    image = flip_vertically(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)


#funkcija koja poziva funkciju za horizontal flip i ucitava novu sliku
def pozovihor():
    global file_path, current_image, image
    image = flip_horizontally(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

def pozovirot(): 
    global file_path, image, current_image
    image = rotation(image, 90)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

def cropfunc():
    if frame_for_input3.winfo_ismapped():
        frame_for_input3.pack_forget()
    else:
        frame_for_input3.pack()
    
def submit_crop():
    global file_path, current_image, image
    val_left = int(crop_input_left.get())
    val_top = int(crop_input_top.get())
    val_right = int(crop_input_right.get())
    val_bottom = int(crop_input_bottom.get())
    image = crop(image, val_left, val_top, val_right, val_bottom)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)

    frame_for_input3.pack_forget()


window = Tk()
window.title("Photoshop")
window.geometry("1000x700")
window.configure(bg="#00004d")
window.resizable(True, True)

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


###   crop   ###

frame_for_input3 = Frame(window, padx=10, pady=10, bg="#00004d")

crop_label = Label(frame_for_input3, text="left ").pack(side=LEFT)
crop_input_left = Entry(frame_for_input3)
crop_input_left.pack(side=LEFT)

crop_label2 = Label(frame_for_input3, text="top").pack(side=LEFT)
crop_input_top= Entry(frame_for_input3)
crop_input_top.pack(side=LEFT)

crop_label3 = Label(frame_for_input3, text="right").pack(side=LEFT)
crop_input_right= Entry(frame_for_input3)
crop_input_right.pack(side=LEFT)

crop_label4 = Label(frame_for_input3, text="bottom").pack(side=LEFT)
crop_input_bottom= Entry(frame_for_input3)
crop_input_bottom.pack(side=LEFT)

crop_submit = Button(frame_for_input3, text="submit", command=submit_crop).pack(side=LEFT)

ic2 = PhotoImage(file="icons/crop.png")
cropPhotoBtn = Button (
    frame1,
    image=ic2,
    borderwidth=0,
    command=cropfunc
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
photoFrame.pack(fill=BOTH, expand=TRUE, padx=30, pady=30) 

canvas = Canvas(photoFrame, width=600, height=400) 
canvas.pack(side=TOP)

canvas.create_image(0, 0, anchor=NW, image=current_image)



window.mainloop()