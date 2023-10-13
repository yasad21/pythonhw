class Base:
    def _init_(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def shape(self):
        return "This is a circle"
class Circle():
def   init  (x, size):
super().  init  (x, y, size)
def draw(self):
return f"""
({self.x}, {self.y})\n{self.size}
, - ~ ~ ~ - ,
, '	' ,
,	,
,	,
,	,
,	,
,	,
,	,
,	,
,	, '
' - , _ _ _ ,	'
"""
def main():
c = Circle(1,2,3) print(c.shape())
print(c.draw())
main()
