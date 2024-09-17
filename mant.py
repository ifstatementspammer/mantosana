class Geom:
    name="Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def draw(self):
        print('Geom fig zimesana')

class Line(Geom):
    name='Line'
    def draw(self):
        print('Linijas zimesana')

class Rect(Geom):
    pass

#g=Geom()
l=Line()
r=Rect()
l.set_coords(5,6,3,1)
r.set_coords(5,6,3,1)
l.draw()
print(l.name)
r.draw()
print(r.name)
print(l.__dict__)
print(r.__dict__)