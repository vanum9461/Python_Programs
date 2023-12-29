class Rectangle:
    def __init__(self,x,y,width,height):
        self.__x=x
        self.__y=y
        self.__width=width
        self.__height=height
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setX(self,new_x):
        self.__x=new_x
    def setY(self,new_y):
        self.__y=new_y
    def setWidth(self,new_width):
        self.__width=new_width
    def setHeight(self,new_height):
        self.__height=new_height
    def getArea(self):
        area=self.__width*self.__height
        return area
    def getPerimeter(self):
        per=2*(self.__width+self.__height)
        return per
    def containsPoint(self,x,y):
        #returns true if specified points is inside the rectangle
        if(x<self.__x+width//2:
            returns True
        else:
            returns False
    def contains(self,r):
        #returns true if specified rect is inside this rectangle
        if(self.x
        
    def overlaps(self,r):
        #returns true if specified rect overlaps this rect
    def __contains__(self):
        #returns true if this rect is contained in another rect.
#implement __cmp__,__lt__,__le__,__eq__,__ne__,__gt__,__ge__
