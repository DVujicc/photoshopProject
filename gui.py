from hashlib import new
from multiprocessing.dummy import current_process
from operator import ne
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageGrab
from functions import *

file_path = ""
WIDTH = 700
HEIGHT = 400
image = None
current_image = None
COLOR = "#000033"

def warning_func():
    frame_for_warnings.pack()

def warning_forget():
    frame_for_warnings.pack_forget()

def check(val):
    if val:
        try:
            int(val)
            warning_forget()
        except ValueError:
            warning_func()
    else:
        warning_forget()

def check_crop(left, top, right, bottom):
    if left and top and right and bottom:
        try:
            int(left)
            int(top)
            int(right)
            int(bottom)
            warning_forget()
        except ValueError:
            warning_func()
    else:
        warning_forget()

def calculateCenter(new_width):
    canvas_center_x = WIDTH / 2
    canvas_center_y = HEIGHT / 2
    image_x = canvas_center_x - new_width / 2
    image_y = canvas_center_y - HEIGHT / 2
    return image_x, image_y

def calculateCenterH(new_height):
    canvas_center_x = WIDTH / 2
    canvas_center_y = HEIGHT / 2
    image_x = canvas_center_x - WIDTH / 2
    image_y = canvas_center_y - new_height / 2
    return image_x, image_y

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

        image_x, image_y = calculateCenter(new_width)
        canvas.create_image(image_x, image_y, anchor=NW, image=current_image)

#funkcija za cuvanje slike OVO POPRAVI
def saveimage():
    global file_path, canvas, image
    if file_path:
        image = image.convert("RGB")
        file_path = fd.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
            if not file_path.lower().endswith(valid_extensions):
                file_path += ".jpg"

        image.save(file_path, format="JPEG")

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
    check(value)
    value = int(value)
    value /= 100
    image = blend(image, value)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width > WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        current_image = image.resize((new_width, HEIGHT))
        image_x, image_y = calculateCenter(new_width)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)
    
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
    check(val)
    val = int(val)
    image = contrast(image, val/10)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width > WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        current_image = image.resize((new_width, HEIGHT))
        image_x, image_y = calculateCenter(new_width)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)

    frame_for_input2.pack_forget()


#funkcija koja poziva funkciju za vertical flip i ucitava novu sliku
def pozovivert():
    global file_path, current_image, image
    image = flip_vertically(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width > WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        current_image = image.resize((new_width, HEIGHT))
        image_x, image_y = calculateCenter(new_width)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)


#funkcija koja poziva funkciju za horizontal flip i ucitava novu sliku
def pozovihor():
    global file_path, current_image, image
    image = flip_horizontally(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width > WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        current_image = image.resize((new_width, HEIGHT))
        image_x, image_y = calculateCenter(new_width)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)

def pozovirot(): 
    global file_path, image, current_image
    image = rotation(image, 90)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width > WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        image_x, image_y = calculateCenter(new_width)
        current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)

def cropfunc():
    if frame_for_input3.winfo_ismapped():
        frame_for_input3.pack_forget()
    else:
        frame_for_input3.pack()
    
def submit_crop():
    global file_path, current_image, image
    val_left = crop_input_left.get()
    val_top = crop_input_top.get()
    val_right = crop_input_right.get()
    val_bottom = crop_input_bottom.get()

    check_crop(val_left, val_top, val_right, val_bottom)
    val_left = int(val_left)
    val_top = int(val_top)
    val_right = int(val_right)
    val_bottom = int(val_bottom)
    image = crop(image, val_left, val_top, val_right, val_bottom)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width >= WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        image_x, image_y = calculateCenter(new_width)
        current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)
    
    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)

    frame_for_input3.pack_forget()


def pozovi_bw():
    global current_image, image
    image = black_and_white(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width >= WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        image_x, image_y = calculateCenter(new_width)
        current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)

    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)


def blur_func():
    global current_image, image
    image = blur(image)
    ar = float(image.width / image.height)
    new_width = int(ar * HEIGHT)
    if new_width >= WIDTH:
        new_height = int(WIDTH / ar)
        current_image = image.resize((WIDTH, new_height))
        image_x, image_y = calculateCenterH(new_height)
    else:
        image_x, image_y = calculateCenter(new_width)
        current_image = image.resize((new_width, HEIGHT), Image.LANCZOS)
    current_image = ImageTk.PhotoImage(current_image)

    canvas.delete("all")
    canvas.create_image(image_x, image_y, anchor=NW, image=current_image)


window = Tk()
window.title("Photoshop")
window.geometry("1000x700")
window.configure(bg=COLOR)
window.resizable(True, True)

frame1 = Frame(
    window,
    padx=10,
    pady=10,
    bg=COLOR
)

label = Label(
    frame1, 
    text="Photoshop",
    font=Font(size=41),
    borderwidth=0,
    bg=COLOR,
    foreground="white"
)
label.pack(side=LEFT, padx=20)

ic1 = PhotoImage(file="icons/openfile.png")
openimgBtn = Button(
    frame1,
    image=ic1,
    borderwidth=0,
    highlightbackground=COLOR,
    command=openfile
)
openimgBtn.pack(side=LEFT)


###   crop   ###

frame_for_input3 = Frame(window, padx=10, pady=10, bg=COLOR)

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
    highlightbackground=COLOR,
    command=cropfunc
)
cropPhotoBtn.pack(side=LEFT)




ic8 = PhotoImage(file="icons/rotate.png")
rotate = Button(
    frame1,
    image=ic8,
    borderwidth=0,
    highlightbackground=COLOR,
    command=pozovirot
).pack(side=LEFT)

ic3 = PhotoImage(file="icons/flip_horizontal.png")
flipHorizontalBtn = Button(
    frame1,
    image=ic3,
    borderwidth=0,
    highlightbackground=COLOR,
    command=pozovihor
)
flipHorizontalBtn.pack(side=LEFT)

ic4 = PhotoImage(file="icons/flip_vertical.png")
flipVerticalBtn = Button(
    frame1,
    image=ic4,
    borderwidth=0,
    highlightbackground=COLOR,
    command=pozovivert
)
flipVerticalBtn.pack(side=LEFT)

#Contrast
frame_for_input2 = Frame(window, padx=10, pady=10, bg=COLOR)
contrast_label = Label(frame_for_input2, text="Input value for contrast: ").pack(side=LEFT)
contrast_input = Entry(frame_for_input2)
contrast_input.pack(side=LEFT)
contrast_submit = Button(frame_for_input2, text="submit", command=submit_contrast).pack(side=LEFT)

ic6 = PhotoImage(file="icons/contrast.png")
contrast_btn = Button(frame1, image=ic6, borderwidth=0, highlightbackground=COLOR, command=contrastFunc)
contrast_btn.pack(side=LEFT)

#Brightness

frame_for_input = Frame(window, padx=10, pady=10, bg=COLOR)

brigth_label = Label(frame_for_input, text="Input value for brightness: ").pack(side=LEFT)

brightness_input = Entry(frame_for_input)
brightness_input.pack(side=LEFT)

bright_submit = Button(frame_for_input, text="submit", command=submit_brightness).pack(side=LEFT)

ic5 = PhotoImage(file="icons/brightness.png")
brightness = Button(frame1, image=ic5, borderwidth=0, highlightbackground=COLOR, command=brightFunc)
brightness.pack(side=LEFT)


#black and white

ic9 = PhotoImage(file="icons/bw.png")
bw_button = Button(frame1, image=ic9, borderwidth=0, highlightbackground=COLOR, command=pozovi_bw)
bw_button.pack(side=LEFT)

#blur
ic10 = PhotoImage(file="icons/blur.png")
blur_button = Button(frame1, image=ic10, borderwidth=0, highlightbackground=COLOR, command=blur_func)
blur_button.pack(side=LEFT)

#Save
ic7 = PhotoImage(file="icons/save.png")
save = Button(
    frame1,
    image=ic7,
    borderwidth=0,
    highlightbackground=COLOR,
    command=saveimage
)
save.pack(side=LEFT)


frame1.pack(side=TOP)

photoFrame = Frame(
    window,
    width=600,
    height=400,
    bg=COLOR
)
photoFrame.pack(fill=BOTH, expand=TRUE, padx=30, pady=40) 

frame_for_warnings = Frame(
    window,
    bg=COLOR
)
warning_label = Label(
    frame_for_warnings,
    text="Wrong input"
).pack()

canvas = Canvas(photoFrame, width=WIDTH, height=HEIGHT, bg=COLOR, borderwidth=0, highlightbackground=COLOR) 
canvas.pack(side=TOP)

canvas.create_image(0, 0, anchor=NW, image=current_image)

window.mainloop()