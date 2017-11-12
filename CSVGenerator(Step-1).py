import string, random
import csv

from io import BytesIO
from captcha.image import ImageCaptcha

text1 = "abcdefghijklmnopqrstuvwxyz"
text2 = "0123456789"

image = ImageCaptcha(fonts=['font2.otf', 'font1.ttf'])

out = open('test1.csv', 'w')

j = 1

for i in range(16667):
    a = []
    b = []
    c = []

    # Move 1
    a.append(random.choice(text2))
    a.append(random.choice(text1))
    a.append(random.choice(text2))
    a.append(random.choice(text2))
    a.append(random.choice(text1))

    for i in a:
        i = ord(i)
        b.append(str(i))
    c = a

    out.write(''.join(c))
    out.write(",")
    out.write('out%d.png'%j)

    out.write(",")
    out.write(','.join(b))

    data = image.generate(c)
    assert isinstance(data, BytesIO)
    image.write(c , 'out%d.png'% j)

    j += 1
    out.write("\n")

    # Move 2
    a =[]
    b = []
    c = []

    a.append(random.choice(text1))
    a.append(random.choice(text1))
    a.append(random.choice(text2))
    a.append(random.choice(text1))
    a.append(random.choice(text1))

    for i in a:
        i = ord(i)
        b.append(str(i))

    c = a

    out.write(''.join(c))
    out.write(",")
    out.write('out%d.png'%j)

    out.write(",")
    out.write(','.join(b))

    data = image.generate(c)
    assert isinstance(data, BytesIO)
    image.write(c , 'out%d.png'% j)

    j += 1
    out.write("\n")

    # Move 3
    a = []
    b = []
    c = []

    a.append(random.choice(text1))
    a.append(random.choice(text2))
    a.append(random.choice(text2))
    a.append(random.choice(text1))
    a.append(random.choice(text2))

    for i in a:
        i = ord(i)
        b.append(str(i))

    c = a

    out.write(''.join(c))
    out.write(",")
    out.write('out%d.png'%j)

    out.write(",")
    out.write(','.join(b))

    data = image.generate(c)
    assert isinstance(data, BytesIO)
    image.write(c , 'out%d.png'% j)
    j += 1
    out.write("\n")
