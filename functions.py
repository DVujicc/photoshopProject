import PIL 
import numpy as np
import cv2
from PIL import Image 

######## kako napraviti da funkcionise za png i jpg ?????????????? #########



###### crop ######

def crop(image_location, height, width):
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

def rotate(image_location, angle):
    expand = True
    im = Image.open(image_location)
    out = im.rotate(angle, expand=True)
    out.save('rotate-output.png')
    return out 

##### brightness #####

def blend(image_location, brightness, value):  #### podeli input sa 100          
    it1 = np.nditer(image_location)
    it2 = np.nditer(brightness)            
    for (x) in it1:
        for (y) in it2:
            newImage = (x + y) * value
    return out

##### contrast #####

def contrast(image_location, value): #### podeli input sa 10
    im = Image.open(image_location)
    image_array = np.array(im)
    contrast_factor = value
    contrast_img = image_array * contrast_factor
    contrast_img = np.clip (contrast_img, 0, 255)
    out = Image.fromarray(contrast_img.astype(np.uint8))
    out.save("output_image.jpg")
    return out





    










