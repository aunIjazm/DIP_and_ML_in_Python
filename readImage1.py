import numpy as np
#from scipy.ndimage import imread, imsave
from PIL import Image

img_url = Image.open('images/microscop1.jpg')

img = np.array(img_url)

print(img)
print(img.dtype, img.shape)

#tinted_Img = img * [0., 0., 1.]
#tinted_Img = img * [0., 1., 0.]
tinted_Img = img * [0., 0., 1.]
tinted_Img = np.clip(tinted_Img, 0, 255).astype(np.uint8)
Image.fromarray(tinted_Img).save('images/outputImgs/tinted5.jpg')