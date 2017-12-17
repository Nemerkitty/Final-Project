from tkinter import *


class PaintProgram:

    MouseButton = "up"    # Variable containing the state of the mouse button
    MouseX = None
    MouseY = None
    # None is used instead of 0 to avoid any unwanted issues
    # I assume None is very similar to a null
    PenMode = 1
    # Decided if the user will be drawing or erasing
    PenSize = 1

    def eraser_click(self, event=None):
        self.PenMode = self.PenMode * -1

    def increase_size(self, event=None):
        self.PenSize = self.PenSize + 1

    def decrease_size(self, event=None):
        if self.PenSize - 1 > 0:    # Checks if the size is at the minimum
            self.PenSize = self.PenSize - 1

    def mouse_press(self, event=None):
        # Requires an event even though it is not used, as there is an event included when using .bind
        self.MouseButton = "down"
        # Tells the program that the mouse button is clicked

    def mouse_release(self, event=None):
        self.MouseButton = "up"
        # Tells the program that the mouse button is released

    def mouse_move(self, event=None):
            self.draw(event)
            # When the mouse is moving, run the drawing method

    def draw(self, event=None):
        if self.MouseButton == "down":
            if self.PenMode == 1:
                event.widget.create_line(self.MouseX, self.MouseY, event.x, event.y, fill='black', width=self.PenSize)
                # Draws in black
                # event.x and event.y work because the Motion event in .bind contains the current position
                # If the mouse button is clicked, then begin drawing
            elif self.PenMode == -1:
                event.widget.create_line(self.MouseX, self.MouseY, event.x, event.y, fill='white', width=self.PenSize)
                # Draws in white

        self.MouseX = event.x
        self.MouseY = event.y
        # Update the mouse position to the current position

    def __init__(self, root):    # Initializes
        canvas = Canvas(root, width=700, height=500)
        # Creates a canvas with specified dimensions
        canvas.pack()

        canvas.create_rectangle(0, 0, 700, 500, fill='white')
        # Creates a rectangle for the user to draw on, with a white background

        eraser = Button(root, text="Eraser")
        eraser.pack(side=LEFT)    # Creates an eraser button, to switch between drawing and erasing
        eraser.bind("<Button-1>", self.eraser_click)

        increaseSize = Button(root, text="Increase Size")
        increaseSize.pack(side=LEFT)    # Creates a button to increase pen size
        increaseSize.bind("<Button-1>", self.increase_size)

        decreaseSize = Button(root, text="Decrease Size")
        decreaseSize.pack(side=LEFT)    # Creates a button to decrease pen size
        decreaseSize.bind("<Button-1>", self.decrease_size)

        # .bind appears to be an incredibly simple and useful way of receiving keyboard and mouse inputs
        # and tying them to methods written in the program
        canvas.bind("<Motion>", self.mouse_move)
        # Motion refers to the movement of the mouse
        canvas.bind("<ButtonPress-1>", self.mouse_press)
        # ButtonPress-1 is referring to the left mouse button being clicked
        canvas.bind("<ButtonRelease-1>", self.mouse_release)
        # ButtonPress-1 is referring to the left mouse button being released


root = Tk()
paint_program = PaintProgram(root)
root.mainloop()    # Runs and loops the program forever, until it is closed
