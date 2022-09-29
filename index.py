from PIL import Image

print(Image)

# image_old = "./src/page4/testResult_card-4.png"
# image_new = "./src/page4/testResult_card-4.webp"


page=""
name="class1Laser"


image_o = f"./src/{page}/{name}.png"
image_n = f"./src/{page}/{name}.webp"

im = Image.open(image_o)
im.save(image_n, format = "WebP", lossless = False)