class Circle:

    def __init__(self, x, y, r, visible = True):
      self.center_x = x
      self.center_y = y
      self.r = r
      self.visible = visible

    def display(self):
        if issubclass(type(self), Rectangle):
            print('drew the rectangle')
        elif isinstance(self, Circle):
            print('drew the circle.')
        else:
            print('no work')

    def set_visible(self,is_visible):
        self.visible = is_visible

    def get_center(self):
        return self.center_x, self.center_y

class Rectangle(Circle):

    def __init__(self, x, y, width, height, visible = True):
        super().__init__(x,y,visible)
        # left-bottom corner.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible

    def hide(self):
        self.visible = False

    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.set_visible(True)
    rect.display()
    print('center point',rect.get_center())