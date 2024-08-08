# 1. дефиниция

class Point:
    
    def __init__(self, *, x=0, y=0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        # __x is private
        self.set_x(x)
        self.set_y(y)
        self.set_visible(visible)

    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_y()}) (visible:{self.is_visible()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)
    
    # методи за достъп до данните (класически подход)

    def set_x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x

    def get_x(self):
        return self.__x  

    def set_y(self,y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    def get_y(self):
        return self.__y
    
    def set_visible(self, visible):
        self.__visible = visible

    def is_visible(self):
        return self.__visible    
        

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата, представител на типа и т.н.
    print('--- begin ---') 
    p1 = Point()
    p2 = Point(x=10,y=20)

    if p1.is_visible():
        p1.draw()
    
    p1.set_x(10)
    p1.set_y(14)

    p1.draw()
    
    p1.set_x(-1)
    
    print('--- end ---')