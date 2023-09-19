import PIL 
import numpy as np
import cv2
from PIL import Image, ImageEnhance

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
    out.save(image_location)
    return out 
    
def flip_vertically(file_path):
    im = Image.open(file_path)
    out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    out.save(file_path)
    return out 

##### rotate #####

def rotation(image_location, angle):
    expand = True
    im = Image.open(image_location)
    out = im.rotate(angle, expand=True)
    out.save(image_location)
    return out 

##### brightness #####

def blend(image_location, value): 
    #### podeli input sa 100
    width, height = image_location.size
    brightness = Image.new("RGB", (width, height), (255, 255, 255))          
    it1 = np.nditer(image_location)
    it2 = np.nditer(brightness)            
    for (x) in it1:
        for (y) in it2:
            newImage = (x + y) * value
    return newImage

##### contrast #####

def contrast(file_path, value): #### podeli input sa 10
    im = Image.open(file_path)
    image_array = np.array(im)
    contrast_factor = value
    contrast_img = image_array * contrast_factor
    contrast_img = np.clip (contrast_img, 0, 255)
    out = Image.fromarray(contrast_img.astype(np.uint8))
    out.save(file_path)
    return out





    










