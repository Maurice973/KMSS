from PIL import Image

image = 'public/images/students.jpg'  # 1600, 900
out_file = 'students.png'

img = Image.open(image)

size = (337.59, 190)
img.thumbnail(size)
img.save(out_file)