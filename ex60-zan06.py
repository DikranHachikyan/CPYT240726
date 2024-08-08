# 1. дефиниция

class Point:
    # Данни на класа
    # !!!статична променлива!!!
    count = 0

    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        # __x is private
        self.x = x
        self.y = y
        self.is_visible = visible
        Point.count += 1

    def draw(self):
        print(f'draw point at ({self.x}, {self.y}) (visible:{self.is_visible})', end=',')
        print(f'n instances: {Point.count}')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy
    
    # методи за достъп до данните (Python подход)
    # get
    @property
    def x(self):
        return self.__x
    
    # set 
    @x.setter
    def x(self,x):
        assert x >= 0, f'negative x {x}'
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        assert y >= 0, f'negative u {y}'
        self.__y = y

    @property
    def is_visible(self):
        return self.__visible
    
    @is_visible.setter
    def is_visible(self, visible):
        self.__visible = visible

    # Специални методи
    # Предефиниране на методи (function overriding)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, right):
        if not isinstance(right, Point):
            raise NotImplemented(f'Mot yet implemented!')
        return self.x == right.x and self.y == right.y
    
    def __del__(self):
        Point.count -= 1
        print(f'destroy object {self}')
# End of Point

def show():
    p = Point(x=1,y=1)
    p.draw()
    print(f'show n instances {Point.count}')

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата, представител на типа и т.н.
    print('--- begin ---') 
    p1 = Point()
    p2 = Point(x=10,y=20)

    print(f'Point: {p2}')
    print(f'P2 coords:' + str(p2))

    if p1 == p2:
        print(f'{p1} equals {p2}')
    else:
        print(f'{p1} does not equals {p2}')

    p3 = p1
    if p3 == p1:
        print(f'{p3} = {p1}')
    
    show()

    p2.draw()

    print('--- end ---')