import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "circl_g_logo.gif", save_all=True, append_images=[images[1]], duration=600, loop=0
)

#Test comment
#Another test comment