from tkinter import *
import math

mycolor = '#%02x%02x%02x' % (0, 49, 62)
treecolor = '#%02x%02x%02x' % (174, 150, 56)
root = Tk()

canvas = Canvas(root, width='400', height='400', bg=mycolor)
canvas.pack()

start_x = 200
start_y = 350
end_x = 200
end_y = 310
tribe = canvas.create_line(start_x, start_y, end_x, end_y, fill=treecolor)

def tree(line_length, start_x, start_y, deg_left, deg_center, deg_right):
    if line_length < 8:
        return 0
    else:

        angle_in_degrees = deg_left
        angle_in_radians = angle_in_degrees * math.pi / 180
        end_x = start_x + line_length * math.cos(angle_in_radians)
        end_y = start_y + line_length * math.sin(angle_in_radians)
        canvas.create_line(start_x, start_y, end_x, end_y, fill=treecolor)
        (tree(line_length-4, end_x, end_y, deg_left - 15, deg_center, deg_right - 15))

        angle_in_degrees = deg_right
        angle_in_radians = angle_in_degrees * math.pi / 180
        end_x = start_x + line_length * math.cos(angle_in_radians)
        end_y = start_y + line_length * math.sin(angle_in_radians)
        canvas.create_line(start_x, start_y, end_x, end_y, fill=treecolor)
        (tree(line_length-4, end_x, end_y, deg_left + 15, deg_center, deg_right + 15 ))

        angle_in_degrees = deg_center
        angle_in_radians = angle_in_degrees * math.pi / 180
        end_x = start_x + line_length * math.cos(angle_in_radians)
        end_y = start_y + line_length * math.sin(angle_in_radians)
        canvas.create_line(start_x, start_y, end_x, end_y, fill=treecolor)
        (tree(line_length-4, end_x, end_y, deg_left, deg_center, deg_right))

print(tree(40, 200, 310, -115, -90, -65))

root.mainloop()