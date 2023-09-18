from cgitb import text
from operator import le
from struct import pack_into
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog as fd
from turtle import left
from PIL import Image, ImageTk
from functions import *

def openfile():
    file_path = fd.askopenfilename()
    print(file_path)
    if file_path:
        # Open and display the image using Pillow
        img = Image.open(file_path)
        img.thumbnail((600, 400))
        img = ImageTk.PhotoImage(img)
    
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.img = img

def brightFunc():
    if frame_for_input.winfo_ismapped():
        frame_for_input.pack_forget()
    else:
        frame_for_input.pack()
    

def submit_brightness():
    value = brightness_input.get()
    print(value)
    frame_for_input.pack_forget()


def contrastFunc():
    if frame_for_input2.winfo_ismapped():
        frame_for_input2.pack_forget()
    else:
        frame_for_input2.pack()

def submit_contrast():
    value = contrast_input.get()
    print(value)
    frame_for_input2.pack_forget()

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
    borderwidth=0
).pack(side=LEFT)

ic3 = PhotoImage(file="icons/flip_horizontal.png")
flipHorizontalBtn = Button(
    frame1,
    image=ic3,
    borderwidth=0
)
flipHorizontalBtn.pack(side=LEFT)

ic4 = PhotoImage(file="icons/flip_vertical.png")
flipVerticalBtn = Button(
    frame1,
    image=ic4,
    borderwidth=0
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
contrast = Button(frame1, image=ic6, borderwidth=0, command=contrastFunc)
contrast.pack(side=LEFT)


#Save
ic7 = PhotoImage(file="icons/save.png")
save = Button(
    frame1,
    image=ic7,
    borderwidth=0
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



window.mainloop()