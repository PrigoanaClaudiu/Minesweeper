from tkinter import Button, Label
import random

import settings


class Cell:
    # class level
    all = []  # a list with all the instances (mines, not mines)
    cell_count_lebel_obj = None
    cell_count = settings.CELL_COUNT # the value of cells


    def __init__(self, x, y, is_mine=False):
        """
        Constructor
        :param is_mine: False -> it's not a mine, True -> it's a mine
        """
        # instance level
        self.is_mine = is_mine
        self.is_open = None
        self.is_mine_candidate = False
        self.cell_button_obj = None  # the button obj, that will receive none when created
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
        # create the button
        button = Button(
            location,
            width=12,  #
            height=4,  # dimensions of the buttons
        )
        # assign event  - Button-1 = left click  - Button-3 = right click
        button.bind('<Button-1>', self.left_click_actions)  # not calling the method, only give it reference
        button.bind('<Button-3>', self.right_click_actions)  # same

        self.cell_button_obj = button

    @staticmethod  # -> a method that it is used by the class and not for the use of instance
    def create_cell_count_label(location):
        """
        1 time calling
        Label -> will display only the text without changing anything
        Function that shows how many cell remains to discover
        :return: lebel to the cell_count_lebel_obj
        """
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left: {Cell.cell_count}",
            width=12,   #
            height=4,   # dimensions of the lbl button
            font=("", 30)   # font("the font we are using", the size)
        )
        Cell.cell_count_lebel_obj = lbl

    # passing 2 args for this functions bcs Kindle
    def left_click_actions(self, event):
        # event will take some infos about what event it happend
        if self.is_mine:
            self.show_mine()
        else:
            # if for displaying all the surrounded cells if there's no mines
            if self.surrounded_cells_mines_length == 0:
                for cell_obs in self.surrounded_cells:
                    cell_obs.show_cell()

            self.show_cell()  # display how many bombs on the cell

    def get_cell_by_axis(self, x, y):
        # return a cell obj based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property  # read only attribute -> now we can use it like an attribute like the ones in __init
    def surrounded_cells_mines_length(self):
        """
        Function that iterate trough the surrounded cells and counter the mines
        :return: the number of mines in surrounded cells
        """
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(
                text=self.surrounded_cells_mines_length
            )

            # replace the text of the cell count label with the newer count
            if Cell.cell_count_lebel_obj:
                Cell.cell_count_lebel_obj.configure(
                    text=f"Cells left: {Cell.cell_count}",

                )
        # mark the cell as opened (for not counting a cell more times than 1)
        self.is_open = True

    @property  # read only attribute -> now we can use it like an attribute like the ones in __init
    def surrounded_cells(self):
        # the 8th cells
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
        ]

        # list comprehension to delete the None cells
        cells = [cell for cell in cells if cell is not None]
        return cells

    def show_mine(self):
        # a logic to interrupt the game and display a message that play lost
        self.cell_button_obj.configure(bg='red')

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_button_obj.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_button_obj.configure(
                bg='SystemButtonFace'   # the default color
            )
            self.is_mine_candidate = False

    # use globally
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
