from PIL import Image

#Image.open("images.png")
import pywhatkit as pyw
pyw.image_to_ascii_art(r'D:\PROGRAMMING\python\thumbs up.png','MyArt')
read_file=open("MyArt.txt","r")
print(read_file.read())