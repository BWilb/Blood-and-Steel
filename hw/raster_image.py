"""import random

import cherrypy
import os
from PIL import Image
from PIL import ImageDraw
from io import BytesIO

WIDTH = 800
HEIGHT = 600

class HTML:
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'image/png'

        image = Image.new('RGB', (WIDTH, HEIGHT), color='white')

        draw = ImageDraw.Draw(image)

        rectangle_count = 20

        for i in range(rectangle_count):
            x1 = random.randrange(WIDTH)
            y1 = random.randrange(HEIGHT)
            x2 = x1 + random.randrange(20, 80)
            y2 = y1 + random.randrange(20, 80)

            color = [random.randrange(255),
                    random.randrange(255),
                    random.randrange(255)]
            draw.rectangle([x1, y1, x2, y2], fill=color)

            byte_io = BytesIO()
            image.save(byte_io, 'PNG')
            return byte_io.getvalue()
cherrypy.quickstart(HTML())"""

"""def findMinimum(list, num):
    if num == 1:
        return list[0]

    return min(list[num - 1], findMinimum(list, num - 1))

print(findMinimum([56, 76, abs(-9), 4, 78, 1], 6))"""

def calculate(num):
    if num == 0:
        return 0
    return num + 2 * calculate(num - 1)

print(calculate(int(input("enter number: "))))


print("cat\n\tcat")
