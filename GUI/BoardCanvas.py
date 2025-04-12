from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# The background of the board

class BoardCanvas(Canvas):
    def __init__(self, parent):
        super().__init__(parent, width = 900, height = 600)
        self.pack()

        board_img = Image.open("board.jpg")
        self.board_img_tk = ImageTk.PhotoImage(board_img)
        self.create_image(0, 0, image = self.board_img_tk, anchor = 'nw')
