from PIL import Image
from scipy import ndimage
import numpy as np

def rotated(inputimg, angle):
    rotated_img = ndimage.rotate(inputimg, angle)
    rotated_img = np.clip(rotated_img, 0, 255).astype(np.uint8)
    Image.fromarray(rotated_img).save('images/outputImgs/rotatedImg2.jpg')
    
def blurred(inputimg):
    blurred_img = ndimage.gaussian_filter(inputimg, sigma=5)
    blurred_img = np.clip(blurred_img, 0, 255).astype(np.uint8)
    Image.fromarray(blurred_img).save('images/outputImgs/blurredImg1.jpg')
    
def denoised(inputimg):
    denoised_img = ndimage.gaussian_filter(inputimg, 1.5)
    denoised_img = np.clip(denoised_img, 0, 255).astype(np.uint8)
    Image.fromarray(denoised_img).save('images/outputImgs/denoisedImg4.jpg')

img = Image.open('images/microscop3.jpg')
img_array = np.array(img)

rotationAngle = 45

rotated(img_array, rotationAngle)
blurred(img_array)
denoised(img_array)