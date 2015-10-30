import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.color import rgb2gray

import edge_detection as ed

parser = argparse.ArgumentParser(description='Shows dark regions from the given picture')
parser.add_argument('filename', help='file with image', default='pic1.jpg', nargs='?')
parser.add_argument('threshold', help='threshold', default='0.3', nargs='?')
args = parser.parse_args()

im = ndi.imread(args.filename)
img = rgb2gray(im)
img = ed.find_dark_regions(img, threshold=float(args.threshold))

#
# plotting the result
#
fig = plt.figure()
ax0 = fig.add_subplot(111)
ax0.imshow(img, cmap=plt.cm.gray)
ax0.axis('off')
ax0.set_title('Dark regions', fontsize=12)
plt.tight_layout()
plt.show()