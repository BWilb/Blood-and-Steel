"""m, n = 7, 7
o, p = 7, 7
for i in range(m):
    for j in range(n):
        print("*" if j in [0, n - 1] or i in [int(m/2), int(m/2)] else " ", end=' ')
    for l in range(o):
        print("*" if l in [0] or i in ([0, int(o/2)]) or i in [0, o - 1] else " ", end=' ')
    for l in range(o):
        print("*" if l in [0, 0] or i in [o - 1, o - 1] else " ", end=' ')
    for l in range(o):
        print("*" if l in [0, 0] or i in [o - 1, o - 1] else " ", end=' ')
    for j in range(m):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end=' ')
"""

"""or i == j """
"""def print_art(size):
    m, n = size, size
    for i in range(m):
        for j in range(n):
            print("*" if j in [0, n -1] or i in [int(m/2), int(m/2)] else ' ', end=' ')
        for j in range(n):
            print('*' if j in [0] or i in ([0, int(n/2)]) or i in [0, n - 1] else ' ', end=' ')
        for j in range(n):
            print('*' if j in [0,0] or i in [n - 1, n - 1] else ' ', end=' ')
        for j in range(n):
            print('*' if j in [0,0] or i in [n - 1, n - 1] else ' ', end=' ')
        for j in range(n):
            print("*" if i in [0, n - 1] or j in [0, m - 1] else ' ', end=' ')
        print()

print_art(int(input("what size would you like the sign to be(use numbers)?: ")))"""


import cherrypy
import random

from PIL import Image
from PIL import ImageDraw
from io import BytesIO
WIDTH = 800
HEIGHT = 600
class AdLib:
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'image/png'
        image = Image.new('RGB', (WIDTH, HEIGHT), color = 'white')
        draw = ImageDraw.Draw(image)
        rectangle_count = 20
        for i in range(rectangle_count):
            x1 = random.randrange(WIDTH)
            y1 = random.randrange(HEIGHT)
            x2 = x1 + random.randrange(20, 80)
            y2 = y1 + random.randrange(20, 80)
            color = (random.randrange(255),
                    random.randrange(255),
                    random.randrange(255))
        draw.rectangle([x1, y1, x2, y2], fill=color)
        byte_io: BytesIO = BytesIO()
        image.save(byte_io, 'PNG')
        return byte_io.getvalue()

cherrypy.quickstart(AdLib())