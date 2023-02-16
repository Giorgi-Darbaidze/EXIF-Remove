print("""
███████╗██╗  ██╗██╗███████╗    ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
██╔════╝╚██╗██╔╝██║██╔════╝    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
█████╗   ╚███╔╝ ██║█████╗      ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  
██╔══╝   ██╔██╗ ██║██╔══╝      ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  
███████╗██╔╝ ██╗██║██║         ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═╝╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝                                           
""")


import os
from PIL import Image

cwd = os.getcwd()
os.chdir("image")
files = os.listdir()

if len(files) == 0:
    print("You don't have have files in the ./images folder.")
    exit()

for file in files:
    try:
        img = Image.open(file)
        img_data = list(img.getdata())
        img_no_exif = Image.new(img.mode, img.size)
        img_no_exif.putdata(img_data)
        img_no_exif.save(file)
    except IOError:
        print("File format not supported!")