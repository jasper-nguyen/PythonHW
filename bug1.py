# TODO: there's code missing in one or more lines below
class Base:
    def __init__(self, x, y, size):
        # TODO: will need to fill this in
        #Initialize x, y and size variable from parameters
        self.x = x
        self.y = y
        self.size = size
        
    def draw(self):
        return ""
        
class Circle(Base): #Add parameter to circle class and change init so that circle inhertets from base class
    pass
        
    def draw(self):
        return f"""
        
({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
    , '                 ' ,
  ,                         ,
 ,                           ,
,                             ,
,                             ,
,                             ,
 ,                           ,
   ,                        ,
     ,                  , '
       ' - , _ _ _ ,  '
              """
class Square(Base):
    pass #Change init to pass so that square class inherets from base parent class
        
    def draw(self): #Add self so that draw can return the shape
        return f"""
({self.x}, {self.y})
{self.size}
--------------------
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
--------------------
"""

# All of the code below is correct
def draw_any_shape(myShape):
    print(myShape.draw())
    
def main():
    s = Square(1,2,3)
    draw_any_shape(s)
    
    c = Circle(2,2,1)
    draw_any_shape(c)
main()
