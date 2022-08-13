from PIL import Image
filename = r'assets/coolcode.png'
img = Image.open(filename)
img.save('logo.ico')
