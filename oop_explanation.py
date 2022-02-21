def calc_area(height, width):
    return height * width

def calc_parimeter(height, width):
    return 2 * (height + width)


class Rectangle:

    def __init__(self, height, width):
        print(f"initializing rectangle with width {width} and height {height}")
        self.__height = height
        self.__width = width
        # self.height = height
        # self.width = width

    def update_height(self, new_height):
        if type(new_height) == float and new_height > 0:
            self.__height = new_height
        else:
            print("error, no update occured")

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"Rectange: w: {self.__width} | h: {self.__height}"

    def __add__(self, other):
        new_rectangle = Rectangle(self.__height + other.__height, self.__width + other.__width)
        return new_rectangle






rect1 = Rectangle(1.5, 2.3)
rect2 = Rectangle(3.5, 5.3)
# rect.update_height('dfgdfg')
# print(rect.area())
# big_rect = rect1 + rect2
big_rect = rect1 + "aaaa"
print(f"big rect: {big_rect}")
