import PIL 
import numpy as np
import cv2
from PIL import Image, ImageEnhance

######## kako napraviti da funkcionise za png i jpg ?????????????? #########



###### crop ######

def crop(image, left, top, right, bottom):
    box = (left, top, right, bottom)
    cropped_image = image.crop(box)
    return cropped_image

##### flip #####
    
def flip_horizontally(image):
    out = image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    return out 
    
def flip_vertically(image):
    out = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    return out 

##### rotate #####

def rotation(image, angle):
    expand = True
    #im = Image.open(image_location)
    out = image.rotate(angle, expand=True)
    return out 

##### brightness #####

# def blend(image_location, value): 
#     #### podeli input sa 100
#     image = Image.open(image_location)
#     width, height = image.size
#     brightness = Image.new("RGB", (width, height), (255, 255, 255))          
#     it1 = np.nditer(image_location)
#     it2 = np.nditer(brightness)            
#     for (x) in it1:
#         for (y) in it2:
#             newImage = (x + y) * value
#     return newImage
def blend(image, value):
    enhancer = ImageEnhance.Brightness(image)

    # Adjust the brightness using the provided value
    adjusted_image = enhancer.enhance(value)

    return adjusted_image

##### contrast #####

def contrast(image, value): #### podeli input sa 10
    image_array = np.array(image)
    contrast_factor = value
    contrast_img = image_array * contrast_factor
    contrast_img = np.clip (contrast_img, 0, 255)
    out = Image.fromarray(contrast_img.astype(np.uint8))
    return out





    









