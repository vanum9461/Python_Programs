class GeometricObject:
    def __init__(self,color="white",filled=False):
        self.__color=color
        self.__filled=filled
    def getColor(self):
        return self.__color
    def setColor(self,new_color):
        self.__color=new_color
    def isFilled(self):
        return self.__filled
    def setFilled(self,new_filled):
        self.__filled=new_filled
    def __str__(self):
        return "Object Color is " + self.__color + "filled is"+str(self.__filled)
"""
g=GeometricObject()
g1=GeometricObject("Red",True)
print(g1)
"""
class Circle(GeometricObject):
    #def __new__(self):
      #  print("New Called")
    def __init__(self,radius,color):
        super().__init__(color=color)
        print("init called")
        self.__radius=radius
    def getRadius(self):
        return self.__radius
    def setRadius(self,new_radius):
        self.__radius=new_radius
    def getArea(self):
        area=3.141*self.__radius*self.__radius
        return area
c=Circle(10,"green")
#print(c.getArea())
print(c.getColor())
#print(dir(Circle))
"""
print(dir(GeometricObject))

"""

class Rectangle(GeometricObject):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
    def getWidth(self):
        return self.__width
    def setWidth(self,new_width):
        self.__width=new_width
    def getHeight(self):
        return self.__height
    def setHeight(self,new_height):
        self.__height=new_height
    def getArea(self):
        area=self.__height*self.__width
        return area
    def getPerimeter(self):
        per=2*(self.__width+self.__height)
        return per

