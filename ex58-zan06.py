# 1. дефиниция

class Point:
    
    def __init__(self, *, x=0, y=0, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        # __x is private
        self.__x = x
        self.__y = y

    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата, представител на типа и т.н.
    print('--- begin ---') 
    p1 = Point()
    p2 = Point(x=10,y=20)

    p1.draw()

    # !! Attribute error!! 
    # print(f'Point x={p1.__x}')
    # p1.__x = 10
    # print(f'Point x={p1.__x}')

    p1.draw()
    p2.draw()
    
    print('--- end ---')