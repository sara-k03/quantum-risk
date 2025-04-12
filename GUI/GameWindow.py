from StatusPanel import StatusPanel
from BoardCanvas import BoardCanvas
from tkinter import Tk

class GameWindow:
    def __init__(self, root):
        root.title("Quantum Risk")

        self.board = BoardCanvas(root)
        self.board.pack(side = 'top')

        self.status = StatusPanel(root)
        self.status.pack(side = 'bottom', fill = 'x')

if __name__ == "__main__":
    root = Tk()
    app = GameWindow(root)
    root.mainloop()