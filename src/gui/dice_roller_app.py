from tkinter import Tk, Button, Label, Entry
from mechanics.dice_mechanics import DiceRoller, ModifierHandler

#Placeholder code till I decide how the GUI will be set up
class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("D&D Dice Roller")

        self.dice_roller = DiceRoller()
        self.modifier_handler = ModifierHandler()

        self.setup_gui()

    def setup_gui(self):
        self.label_result = Label(self.root, text="Result:")
        self.label_result.pack()

        self.entry_modifier = Entry(self.root, width=10)
        self.entry_modifier.pack()

        self.button_roll = Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.button_roll.pack()

    def roll_dice(self):
        # Get the modifier from the entry field
        modifier = int(self.entry_modifier.get()) if self.entry_modifier.get() else 0

        # Roll a d20
        roll_result = self.dice_roller.roll_d20()

        # Apply modifier
        modified_result = self.modifier_handler.apply_modifier(roll_result, modifier)

        # Update the result label
        self.label_result.config(text=f"Result: {modified_result}")