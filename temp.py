import os
from PIL import Image
import datetime

# src 폴더 내 png 파일 찾기
# 여기서 배열 안에 튜플
data_files = [(root, dirs, files) for (root, dirs, files) in os.walk("./src/")]


arr = []

def makeList():
    for x in data_files:
        if len(x[2]) > 1 :
            for fileName in x[2] :
                arr.append([x[0], fileName])
                # print(f"root: {x[0]},\n files: {x[2]} \n\n")




def convert_image():
    for x in arr:
        if x[1].__contains__(".png") :
            print(x)
            im = Image.open(f"{x[0]}\\{x[1]}")
            rename = x[1].replace(".png",".webp")
            im.save(f"{x[0]}\\{rename}", format="Webp", lossless=False)


        # im = Image.open(f"./src/{x}")

        # y = x.replace(".png",".webp")
        # # print(y)
        # im.save(f"./src/{folderName}/{y}", format="WebP",lossless=False)





def init():
    makeList()


    # print(len(arr))
    convert_image()

init()