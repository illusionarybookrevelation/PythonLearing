from PIL import Image,ImageTk


img = Image.open("../tkinter的GUI/忍三/花颜学姐.jpg")

print(img.format,img.size,img.mode)

img.show()