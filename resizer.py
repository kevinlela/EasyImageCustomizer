import sys
sys.path.append("/Users/xiaqingpan/Library/Python/2.7/bin")


from skimage import data
from skimage.transform import resize
from skimage import io

def resizer(img, width, height):
    resize(img, (width, height))
    return img;

image = data.camera()

io.imsave("origin.png", image)


image = resizer(image, 100, 100)

io.imsave("result.png", image)