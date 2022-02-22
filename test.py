# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)
    



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, width, height):
    #draw rectangle
    draw_rectangle(canvas, 0, 0, width, height, fill="skyBlue1")
    draw_cloud(canvas)
    
def draw_cloud(canvas):
    draw_oval(canvas, 25, 370, 100, 430, fill="white", outline="white")
    draw_oval(canvas, 125, 370, 185, 415, fill="white", outline="white")
    draw_oval(canvas, 160, 340, 350, 435, fill="white", outline="white")
    draw_oval(canvas, 25, 370, 100, 430, fill="white", outline="white")
    draw_oval(canvas, 25, 370, 100, 430, fill="white", outline="white")
def draw_grid(canvas, width, height, interval):
    #draw vertical lines.
    label_x = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_x, f"{x}")
    #draw horizontal line.
    label_y = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_y, y, f"{y}")



# Call the main function so that
# this program will start executing.
main()