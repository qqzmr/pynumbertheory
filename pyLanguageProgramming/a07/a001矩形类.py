# -*-coding:utf-8-*-


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width * self.height)


if __name__ == "__main__":
    rect = Rectangle(3, 2)
    print(rect.getArea())
    print(rect.getPerimeter())
