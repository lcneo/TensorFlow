import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure
from skimage.restoration import denoise_tv_chambolle
import numpy as np
from PIL import Image

image = data.astronaut()
image = Image.fromarray(image)
im = np.array(image.convert('L'))

# fd, hog_image = hog(im, orientations=8, pixels_per_cell=(16, 16),
#                     cells_per_block=(1, 1), visualise=True)
fd, hog_image = hog(im,  # input image
                  orientations=8,  # number of bins
                  pixels_per_cell=(16, 16), # pixel per cell
                  cells_per_block=(1, 1), # cells per blcok
                  block_norm = 'L2-Hys', #  block norm : str {‘L1’, ‘L1-sqrt’, ‘L2’, ‘L2-Hys’}, optional
                  transform_sqrt = False, # power law compression (also known as gamma correction)
                  feature_vector=False, # flatten the final vectors
                  visualise=True) # return HOG map
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable('box-forced')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable('box-forced')
plt.show()