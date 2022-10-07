import os
from PIL import Image
import datetime

# src 폴더 내 png 파일 찾기

data_files = [x[2] for x in os.walk("./src/")]

prefiltering = data_files[0]

filtered = filter(lambda el: el.__contains__(".png") | el.__contains__("jpg"), prefiltering)

filteredList = (list(filtered))

# print(filteredList)

# 현재시간(폴더 제작용)



# 폴더 생성
# os.mkdir(f"./src/{folderName}")

def mkdir():
    folderName = f"{datetime.datetime.now()}".replace(":","-")
    os.mkdir(f"./src/{folderName}")

# print(filteredList)

def convert_image():
    folderName = f"{datetime.datetime.now()}".replace(":","-")
    os.mkdir(f"./src/{folderName}")
    for x in filteredList:
        # print(x)
        im = Image.open(f"./src/{x}")
        y = x.replace(".png",".webp")
        # print(y)
        im.save(f"./src/{folderName}/{y}", format="WebP",lossless=False)

convert_image()


# page=""
# name="me"

# image_o = f"./src/{page}/{name}.png"
# image_n = f"./src/{page}/{name}.webp"

# im = Image.open(image_o)
# im.save(image_n, format = "WebP", lossless = False)

