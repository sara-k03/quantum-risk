from .StatusPanel import StatusPanel
from .BoardCanvas import BoardCanvas
from tkinter import Tk

def launch_gui(player_territories, territories):
    root = Tk()
    root.title("Quantum Risk")

    players = {player[-1]: len(terr_list) for player, terr_list in player_territories.items()}
    troop_data = {
        terr: {"player": data["owner"][-1], "count": data["troops"]}
        for terr, data in territories.items() if data["owner"]
    }

    board = BoardCanvas(root, troop_data, width=900, height=600)
    board.pack(side = 'top')

    status = StatusPanel(root, player_territories)
    status.pack(side = 'bottom', fill = 'x')

    root.mainloop()