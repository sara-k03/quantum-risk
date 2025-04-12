from tkinter import Frame, Label, Tk

class StatusPanel(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.players = {
            'A': ['North America', 'Europe', 'South America'],
            'B': ['Asia', 'Australia', 'Africa']
        }
        self.player_colors = {
            'A': 'red',
            'B': 'blue',
        }
        self.create_widgets()

    def create_widgets(self):
        row = 0
        for player, territories in self.players.items():
            color = self.player_colors.get(player, 'black')
            label = Label(self, text=f"{player}: {len(territories)} territories", fg=color)
            label.grid(row=row, column=0, padx=10, pady=5, sticky='w')
            row += 1

if __name__ == "__main__":
    root = Tk()
    root.title("Status Panel Test")
    panel = StatusPanel(root)
    panel.pack(side='bottom', fill='x')
    root.mainloop()