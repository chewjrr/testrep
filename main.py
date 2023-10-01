import random
from PIL import Image, ImageDraw

# Задаем размеры изображения
width = 80
height = 40

#Комментарий, судьба которого, быть уничтоженным 

# Создаем новое изображение
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Заполняем каждый пиксель случайным цветом
for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw.point((x, y), (r, g, b))

# Отображаем изображение в консоли
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        print("\x1b[48;2;{};{};{}m \x1b[0m".format(r, g, b), end="")
    print()