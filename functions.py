import PIL 
import numpy as np
import cv2
from PIL import Image 

######## kako napraviti da funkcionise za png i jpg ?????????????? #########



###### crop ######

def crop_jpg(image_location, height, width):
    image = Image.open(image_location)
    box = (height, height, width, width)
    cropped_image = image.crop(box)
    cropped_image.save("cropped_img.jpg")
    return cropped_image

##### flip #####
    
def flip_horizontally(image_location):
    im = Image.open(image_location)
    out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    out.save('transpose-output.jpg')
    return out 
    
def flip_vertically(image_location):
    im = Image.open(image_location)
    out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    out.save('transpose-output.jpg')
    return out 

##### rotate #####

def rotate_jpg(image_location, angle):
    expand = True
    im = Image.open(image_location)
    out = im.rotate(angle, expand=True)
    out.save('rotate-output.png')
    return out 






    










