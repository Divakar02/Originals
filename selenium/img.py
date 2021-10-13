from PIL import Image
a=str(input("Enter name: "))
x=a.capitalize()
if x=='Hinata':
    im = Image.open(r"C:\\myfiles\hinataa.png")
    im.show()

