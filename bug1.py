class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def shape(self):
        return "This is a"
        
    def draw(self):
        return ""

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """



    def shape(self):
        return super().shape() +" circle"
