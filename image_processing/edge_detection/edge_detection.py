
from skimage.color import rgb2gray
from skimage import feature

from skimage.morphology import disk
from skimage.morphology import erosion, dilation

def find_dark_regions(img, threshold=0.3):
    img = img < threshold
    return img

def find_edges(img, sigma = 4):
    img = feature.canny(img, sigma)

    selem = disk(10)
    img = dilation(img, selem)

    return img
