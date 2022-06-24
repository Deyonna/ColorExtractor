from asyncio.format_helpers import extract_stack
from PIL import Image
import sys

PATH = r"path to file"
IMAGE = "sample.jpg"

with Image.open(PATH + IMAGE) as img:
    img.load()

# gets colors from image and formats the getcolor outcome to a list with rgb value tuples
def list_colors(img):
    img = img.convert("RGB")
    extracted = Image.Image.getcolors(img)
    extracted = [a[1] for a in extracted]
    return extracted


print(img)
print(list_colors(img))

# exports the rgb values from the tuples from the list
def export_color(c_list):

    for x, color in enumerate(c_list):

        r = color[0]
        g = color[1]
        b = color[2]
        create_color(r, g, b, x)


# creates a file with given rgb values
def create_color(r, g, b, x):
    c1 = Image.new("RGB", (200, 200), (r, g, b))

    c1.save(PATH + "c" + str(x) + ".jpg")


extracted = list_colors(img)
export_color(extracted)


