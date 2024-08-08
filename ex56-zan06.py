# 1. дефиниция

class Point:
    
    def __init__(self):
        print('--- init Point ---')
        # данни на обекта
        self.x = 10
        self.y = 20

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
    p = Point()

    print(f'type of p is:{type(p)}, point at ({p.x}, {p.y})')

    p.x = 12
    p.y = 10

    p.draw()
    p.move_to(-4, 15)
    p.draw()
    
    print('--- end ---')