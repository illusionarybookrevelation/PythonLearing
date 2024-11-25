def world(execute):
    class Sky:
        def __init__(self,*args,**kwargs):
            self.z = 0
            self.great = execute(*args,**kwargs)
        def quit(self):
            self.great.quit()
            print("z is ",self.z)
    return Sky
@world
class Lili:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def quit(self):
        print("x is ",self.x)
        print("y is ",self.y)

if __name__ == '__main__':
    Mili = Lili(100,200)
    Mili.quit()
