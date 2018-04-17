import rooms
import os


print('Enter the size of the room (in meters)...')
i = int(input('Long: '))
w = int(input('Width: '))
h = int(input('Height: '))

print('Enter the information about the window openings (in meters)...')
h_w = int(input('Height: '))
w_w = int(input('Width: '))
m = int(input('How match: '))

print('Enter the information about the door opening (in meters)...')
h_d = int(input('Height: '))
w_d = int(input('Width: '))
n = int(input('How match: '))

uroom = rooms.Room(1, w, h)


