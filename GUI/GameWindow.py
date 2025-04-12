from StatusPanel import StatusPanel
from BoardCanvas import BoardCanvas
from tkinter import Tk

class GameWindow:
    def __init__(self, root):
        root.title("Quantum Risk")

        troop_data = {
        "North America": {"player": "A", "count": 5},
        "South America": {"player": "A", "count": 3},
        "Asia": {"player": "A", "count": 1},
        "Africa": {"player": "B", "count": 4},
        "Europe": {"player": "B", "count": 4},
        "Australia": {"player": "B", "count": 4}
        }

        self.board = BoardCanvas(root, troop_data, width=900, height=600)
        self.board.pack(side = 'top')

        self.status = StatusPanel(root)
        self.status.pack(side = 'bottom', fill = 'x')

if __name__ == "__main__":
    root = Tk()
    app = GameWindow(root)
    root.mainloop()