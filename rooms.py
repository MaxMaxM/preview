"It is the program for definition of quantity of wall-paper"
class Wind_Door():
    """
    Class Wind_Door calculates the area of a rectangular.
    Method __init__ accepts two parameters: length and width
    """
    def __init__(self, w, h):
         self.square = w * h

class Room():
    """
    Class Room is intended for definition of the pasted over area of a room.
    Method __init__ accepts three argumets (length, width and height).
    """
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)

    """
    The first pair parameters - the sizes of a window,
    the second pair - the sizes of a door,
    the fifth and sixth parameters - quantity of windows and doors accordingly.
    """
    def win_door(self, d,e, f,g, m=1, n=1):
        self.window = Wind_Door(d, e)
        self.door = Wind_Door(f, g)
        self.numb_w = m
        self.numb_n = n

    """
    This method calculates the pasted over area.
    """
    def wallpapers(self):
        self.wallpapers = (self.square -
                self.window.square * self.numb_w -
                self.door.square * self.numb_n)

        """
        Displays the information.
        """
    def printer(self):
        print('The area of the wall is equal: {0} m2'.format(self.square))
        print('The area of the wallpapers: {0} m2'.format(str(self.wallpapers)))
        print('The are of the one window: {0} m2'.format(self.window.square))
        print('The area of the one door: {0} m2'.format(self.door.square))
