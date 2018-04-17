import rooms
import os

def choice():
    print('Select one of the room options. 1, 2, 3, 4, 5') 
    print('First option. 1\n\
            Size room - Long: 6 Width: 3 Height: 2\n\
            Size window - Height: 1, Width: 2\n\
            Size Door - Height: 3, Width: 2')

    print('Second option. 2\n\
            Size room - Long: 3 Width: 7 Height: 2\n\
            Size window - Height: 3, Width: 1\n\
            Size Door - Height: 4, Width: 2')

    print('Third option. 3\n\
            Size room - Long: 4 Width: 2 Height: 3\n\
            Size window - Height: 3, Width: 5\n\
            Size Door - Height: 3, Width: 2')
    try:
        option = float(input('Enter: '))
        return option
    except ValueError:
        print('\n\nSelect from list 1, 2, 3\n\n')
        choice()


def realization():
    option = choice()

    if option == 1:
        uroom = rooms.Room(6, 3, 2)
        uroom.win_door(2, 1, 3, 2)
        uroom.wallpapers()
        uroom.printer()
    elif option == 2:
        uroom = rooms.Room(3, 7, 2)
        uroom.win_door(3, 1, 3, 2)
        uroom.wallpapers()
        uroom.printer()
    elif option == 3:
        uroom = rooms.Room(4, 2, 3)
        uroom.win_door(3, 5, 3, 2)
        uroom.wallpapers()
        uroom.printer()


realization()
