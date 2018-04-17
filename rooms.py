class Wind_Door():
    def __init__(self, w, h):
         self.square = w * h

class Room():
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)

    def win_door(self, d,e, f,g, m=1, n=1):
        self.window = Wind_Door(d, e)
        self.door = Wind_Door(f, g)
        self.numb_w = m
        self.numb_n = n

    def wallpapers(self):
        self.wallpapers = (self.square -
                self.window.square * self.numb_w -
                self.door.square * self.numb_n)

    def printer(self):
        print('The area of the wall is equal: {0} m2'.format(self.square))
        print('The area of the wallpapers: {0} m2'.format(str(self.wallpapers)))
