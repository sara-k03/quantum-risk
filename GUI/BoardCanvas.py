from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# The background of the board

class BoardCanvas(Canvas):
    def __init__(self, parent, troop_data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.troop_data = troop_data
        self.territory_coords = {
        "North America": (150, 200),
        "South America": (200, 400),
        "Asia": (700, 200),
        "Europe": (450, 200),
        "Africa": (450, 400),
        "Australia": (800, 500)
        }

        self.red_pawn = ImageTk.PhotoImage(Image.open("RedPawn.png").resize((25, 25)))
        self.blue_pawn = ImageTk.PhotoImage(Image.open("BluePawn.png").resize((25, 25)))

        self.board_img = Image.open("board.jpg")
        self.board_img_tk = ImageTk.PhotoImage(self.board_img)
        self.create_image(0, 0, image = self.board_img_tk, anchor = 'nw')

        self.draw_pawns()

    def draw_pawns(self):
        for territory, info in self.troop_data.items():
            player = info["player"]
            count = info["count"]
            x, y = self.territory_coords.get(territory, (0, 0))

            img = self.red_pawn if player == "A" else self.blue_pawn

            for i in range(count):
                self.create_image(x + (i % 3) * 15, y + (i // 3) * 20, image=img, anchor="nw")
