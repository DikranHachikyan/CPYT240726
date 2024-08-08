# 1. дефиниция

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.x = x
        self.y = y

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата, представител на типа и т.н.
    print('--- begin ---') 
    p1 = Point()
    p2 = Point(x=10,y=20)

    p1.draw()
    p2.draw()

    p1.move_to(30, 40)
    p1.draw()
    
    print('--- end ---')