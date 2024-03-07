from tkinter import Button
import random

import settings


class Cell:
    all = []    # a list with all the instances (mines, not mines)
    def __init__(self, x, y, is_mine=False):
        """
        Constructor
        :param is_mine: False -> it's not a mine, True -> it's a mine
        """
        self.is_mine = is_mine
        self.cell_button_obj = None # the button obj, that will receive none when created
        self.x = x  # attribute of the cell
        self.y = y  # attribute of the cell

        # append the obj to the Cell.all list
        Cell.all.append(self)

    def create_button(self, location):
        """
        Create a button for every cell
        :param location: the location of the button
        :return:
        """
        #create the button
        button = Button(
            location,
            width=12,   #
            height=4,   # dimensions of the buttons
            text=f"{self.x},{self.y}"
        )
        # assign event  - Button-1 = left click  - Button-3 = right click
        button.bind('<Button-1>', self.left_click_actions)  #   not calling the method, only give it reference
        button.bind('<Button-3>', self.right_click_actions)  # same

        self.cell_button_obj = button

    # passing 2 args for this functions bcs Kindle
    def left_click_actions(self, event):
        # event will take some infos about what event it happend
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_cell(self):
        pass

    def show_mine(self):
        # a logic to interrupt the game and display a message that play lost
        self.cell_button_obj.configure(bg='red')

    def right_click_actions(self, event):
        print(event)
        print("R click")

    #use globally
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )

        # change the is_mine arg to True if it is in that cells we random picked
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # see the obj much friendlier, not by instance names
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"