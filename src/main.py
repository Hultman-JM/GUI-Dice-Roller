# Main.py

from tkinter import Tk
from gui.dice_roller_app import DiceRollerApp

def main():
    root = Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()