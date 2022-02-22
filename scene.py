# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from random import randint
from textwrap import fill
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    sun = input("Do you want a sunny scene? (yes/no) ")
    scene_width = 800
    scene_height = 500
    
    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("My Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
       
    if sun.lower() == "yes":
        draw_sky_sunny(canvas, scene_width, scene_height)
    
    elif sun.lower() == "no":
        draw_sky(canvas, scene_width, scene_height)

    draw_ground(canvas, scene_width, scene_height)
    
    #draw_grid(canvas, scene_width, scene_height, 50)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky_sunny(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill="SkyBlue1")  
    draw_cloud(canvas, 20, 350, 410, 100, 0, 1)
    draw_cloud(canvas, 135, 300, 390, 100, 0, 1)
    draw_cloud(canvas, 190, 300, 420, 300, 0, 1)
    draw_cloud(canvas, 430, 340, 390, 100, 0, 1)
    draw_cloud(canvas, 470, 340, 390, 200, 0, 1)
    draw_cloud(canvas, 550, 320, 370, 150, 0, 1)
    draw_cloud(canvas, 530, 300, 340, 125, 0, 1)
    draw_cloud(canvas, 500, 270, 310, 125, 0, 1)
    draw_cloud(canvas, 125, 290, 360, 100, 0, 1)
    draw_cloud(canvas, 80, 250, 340, 380, 0, 1)
    draw_cloud(canvas, 175, 240, 350, 150, 0, 1)
    draw_sun(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill="SkyBlue1")  
    draw_cloud(canvas, 20, 350, 410, 100, 0, 1)
    draw_cloud(canvas, 135, 300, 390, 100, 0, 1)
    draw_cloud(canvas, 190, 300, 420, 300, 0, 1)
    draw_cloud(canvas, 430, 340, 390, 100, 0, 1)
    draw_cloud(canvas, 470, 340, 390, 200, 0, 1)
    draw_cloud(canvas, 550, 320, 370, 150, 0, 1)
    draw_cloud(canvas, 530, 300, 340, 125, 0, 1)
    draw_cloud(canvas, 500, 270, 310, 125, 0, 1)
    draw_cloud(canvas, 125, 290, 360, 100, 0, 1)
    draw_cloud(canvas, 80, 250, 340, 380, 0, 1)
    draw_cloud(canvas, 175, 240, 350, 150, 0, 1)


def draw_ground(canvas, scene_width, scene_height):
    
    draw_pine_tree(canvas, 700, 0, 380)
    draw_pine_tree(canvas, 550, 0, 380) 
    #call the draw_fence function with loop
    for x in range(25, scene_width, 50):
        draw_fence(canvas, x)
    #call the draw_grass function with loop
    for x in range(5, scene_width, 12):
        draw_grass(canvas, x)



def draw_cloud(canvas, cloud_left, cloud_bottom, cloud_top, diameter, space_between_oval, num_oval):
    """draw specific number of ovals
    parameters:
        canvas: drawing window
        cloud_left: starting point of oval on x-axis
        cloud_bottom: bottom/starting point of cloud on y-axis
        cloud_top: top/end of cloud on y-axis
        diameter: width of cloud
        space_between_oval: How far apart a series of cloud are from each other
        num_oval: number of successive clouds in the loop
    return: nothing"""
    interval = diameter + space_between_oval
    
    for column in range (num_oval):
        draw_oval(canvas, cloud_left, cloud_bottom, cloud_left + diameter, cloud_top, fill="white", outline= "white")
        cloud_left += interval

def draw_sun(canvas):
    """This function draws the sun"""
    draw_oval(canvas, 700, 425, 825, 525, fill="yellow1", outline="yellow1")


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_height = height / 8
    trunk_width = height / 10
    left_trunk = center_x - trunk_width / 2
    right_trunk = center_x + trunk_width / 2
    trunk_top = trunk_height + bottom

    draw_rectangle(canvas, left_trunk, bottom, right_trunk, trunk_top, fill="tan4")

    skirt_height = height - trunk_height
    skirt_width = height / 2.5
    left_skirt = center_x - skirt_width / 2
    right_skirt = center_x + skirt_width / 2
    skirt_peak = skirt_height + trunk_top

    draw_polygon(canvas, left_skirt, trunk_top, right_skirt, trunk_top, center_x, trunk_top + skirt_peak, fill="forestGreen")


def draw_fence(canvas, center_x):
    width = 40
    height = 140
    left_bar = center_x - width / 2
    bottom = 0
    right_bar = center_x + width / 2
    top_bar = bottom + height
    
    draw_rectangle(canvas, left_bar, bottom, right_bar, top_bar, fill="white", outline="white")
    draw_polygon(canvas, left_bar, height, right_bar, height, center_x, height + 10, fill="white", outline="white")


def draw_grass(canvas, center_x):
    width = 10
    height = randint(10, 35)
    left_bar = center_x - width / 2
    bottom = 0
    right_bar = center_x + width / 2
    top_bar = bottom + height
    draw_rectangle(canvas, left_bar, bottom, right_bar, top_bar, fill="lawnGreen", outline="lawnGreen")


def draw_grid(canvas, scene_width, scene_height, interval):
    """This function will draw a grid on the canvas"""
    #draw a vertical line.
    label_x = 15
    for x in range(interval, scene_width, interval):
        draw_line(canvas, x, 0, x, scene_height)
        draw_text(canvas, x, label_x, f"{x}")
    label_y = 15
    for y in range(interval, scene_height, interval):
        draw_line(canvas, 0, y, scene_width, y)
        draw_text(canvas, label_y, y, f"{y}")


# Call the main function so that
# this program will start executing.
main()
