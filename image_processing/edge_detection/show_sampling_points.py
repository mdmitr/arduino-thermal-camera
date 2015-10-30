import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.color import rgb2gray

from skimage import feature
from skimage.morphology import disk
from skimage.morphology import erosion, dilation

import edge_detection as ed

parser = argparse.ArgumentParser(description='Shows additional sampling points for the given picture')
parser.add_argument('filename', help='file with image', default='pic1.jpg', nargs='?')
args = parser.parse_args()

print(args.filename)
im = ndi.imread(args.filename)
img = rgb2gray(im)
img_dark = ed.find_dark_regions(img)
img_edges = ed.find_edges(img)
img = img_dark + img_edges

# display results
fig = plt.figure()
ax0 = fig.add_subplot(111)
ax0.imshow(img, cmap=plt.cm.gray)
ax0.axis('off')
ax0.set_title('Sobel filter', fontsize=12)

plt.tight_layout()
plt.show() 
