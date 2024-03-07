from tkinter import *
import settings
import utils
from cell import Cell


root = Tk()

# override the settings of the window
root.configure(bg='black')  # change the backround color
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # change the dimensions of the window (WIDTH x HEIGHT)
root.title("My minesweeper")  # change the title of the window root.resizable(False, False)  # deactivate resizable

# frames
top_frame = Frame(
    root,
    bg='black',    # backround of the frame
    width=settings.WIDTH,
    height=utils.height_prct(25),
)
top_frame.place(x=0, y=0)   # place the frame - receive the pixels value, base of the x&y axis - exemple: 0,0 - top left corner

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prect(25),
    height=utils.height_prct(75), # diff between height and top_frame.height
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=settings.HEIGHT
)
center_frame.place(x=utils.width_prect(25), y=utils.height_prct(25))

"""
EXEMPLE:
c1 = Cell()
c1.create_button(center_frame)  # create button in center frame
# place the button with grid is much easier
c1.cell_button_obj.grid(
    column=0, row=0
)
"""

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button(center_frame)
        c.cell_button_obj.grid(
            column=x, row=y
        )

# call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_lebel_obj.place(x=0, y=0)

Cell.randomize_mines()  # pick some random cells for mines (based on the setting.MINES_COUNT)

# run the window
root.mainloop()  # loop untill we close the window
