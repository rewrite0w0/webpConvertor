from PIL import Image

print(Image)

image_old = "./src/main-img_03_b.png"
image_new = "./src/main-img_03_b.webp"

im = Image.open(image_old)
im.save(image_new, format = "WebP", lossless = True)