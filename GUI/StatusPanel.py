from tkinter import Frame, Label, LEFT, RIGHT

class StatusPanel(Frame):
    def __init__(self, parent, player_territories):
        super().__init__(parent, bg = "#452d09", height = 50)
        self.pack_propagate(0)
        player_colors = {
            'A': "#ffc1c1",
            'B': "#b2bef2",
        }

        font_settings = ("Arial", 14, "bold")

        self.a_label = Label(self, text=f"A: {len(player_territories["PLAYER A"])} territories",
                             fg=player_colors["A"], bg="#452d09", font=font_settings, anchor="w")
        self.a_label.pack(side=LEFT, padx=20, fill="both", expand=True)

        self.b_label = Label(self, text=f"B: {len(player_territories["PLAYER B"])} territories",
                             fg=player_colors["B"], bg="#452d09", font=font_settings, anchor="e")
        self.b_label.pack(side=RIGHT, padx=20, fill="both", expand=True)