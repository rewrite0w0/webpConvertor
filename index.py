from PIL import Image

print(Image)

page=""
name=""

image_o = f"./src/{page}/{name}.png"
image_n = f"./src/{page}/{name}.webp"

im = Image.open(image_o)
im.save(image_n, format = "WebP", lossless = False)