from tkinter import Tk, Button, Label, Entry, OptionMenu, StringVar, Checkbutton, Radiobutton
from mechanics.dice_mechanics import DiceRoller

#Placeholder code till I decide how the GUI will be set up
class DiceRollerApp:
    roll_functions = {
    "d4": DiceRoller().roll_d4,
    "d6": DiceRoller().roll_d6,
    "d8": DiceRoller().roll_d8,
    "d10": DiceRoller().roll_d10,
    "d12": DiceRoller().roll_d12,
    "d20": DiceRoller().roll_d20,
    "d100": DiceRoller().roll_d100
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        self.dice_roller = DiceRoller()

        # Initialize widgets
        self.dice_entry_label = None
        self.entry_dice_num = None

        self.modifier_entry_label = None
        self.modifier_entry = None

        self.die_type_label = None
        self.die_type_selection =None
        self.selected_die_type = None

        self.reroll_var
        self.reroll_button = None

        self.advantage_disadvantage_var = None
        self.advantage_button = None
        self.disadvantage_button = None

        self.modify_var
        self.modify_each_roll_button = None
        self.modify_each_roll_and_total_button = None
        self.modify_total_button = None

        self.label_result = None

        self.setup_gui()

    # Sets up GUI by calling helper functions for each part
    def setup_gui(self):
        # Create number of dice input field
        self.input_dice_num()

        # Create die type selection menu
        self.die_type_menu()

        # Create modifier input field
        self.input_modifier()

        # Create options for aditional mechanics
        self.mechanics_selection()

        # Create roll button
        roll_button = Button(self.root, text="Roll Dice", command=self.roll_dice)
        roll_button.pack()
        

    # Text input for num of Dice
    def input_dice_num(self):
        self.dice_entry_label = Label(self.root, text="Number of Dice to Roll: ")
        self.dice_entry_label.pack()
        self.dice_num_entry = Entry(self.root)
        self.dice_num_entry.pack()

    # Text input for modifiers
    def input_modifier(self):
        self.modifier_entry_label = Label(self.root, text="Modifier to add: ")
        self.modifier_entry_label.pack()
        self.modifier_entry = Entry(self.root)
        self.modifier_entry.pack()

    # Option Menu for Die Type
    def die_type_menu(self):
        # Variable to hold the selected die type
        die_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
        self.selected_die_type = StringVar()
        self.selected_die_type.set(die_types[0])
        
        self.die_type_label = Label(self.root, text="Select Die Type: ")
        self.die_type_label.pack()

        self.die_type_selection = OptionMenu(self.root, self.selected_die_type, *die_types)
        self.die_type_selection.pack()

    # Special Mechainics selection
    def mechanics_selection(self):
        # Reroll option
        self.reroll_var = StringVar()
        self.reroll_button = Checkbutton(self.root, text="Reroll", variable=self.reroll_var, onvalue="Reroll", offvalue="")
        self.reroll_button.pack()

        # Advantage and Disadvantage options
        self.advantage_disadvantage_var = StringVar()
        self.advantage_button = Radiobutton(self.root, text="Advantage", variable=self.advantage_disadvantage_var, value="Advantage")
        self.advantage_button.pack()

        self.disadvantage_button = Radiobutton(self.root, text="Disadvantage", variable=self.advantage_disadvantage_var, value="Disadvantage")
        self.disadvantage_button.pack()

        #Modify options
        self.modify_var = StringVar()
        self.modify_each_roll_button = Radiobutton(self.root, text="Modify Each Roll", variable=self.modify_var, value="Modify Each Roll")
        self.modify_each_roll_button.pack()

        self.modify_each_roll_and_total_button = Radiobutton(self.root, text="Modify Each Roll and Total", variable=self.modify_var, value="Modify Each Roll and Total")
        self.modify_each_roll_and_total_button.pack()

        self.modify_total_button = Radiobutton(self.root, text="Modify Total", variable=self.modify_var, value="Modify Total")
        self.modify_total_button.pack()


    def roll_dice(self):
        # Get the Number of dice to roll from the entry field
        num_dice = int(self.dice_num_entry.get())

        # Get die type selection and roll function
        die_type = self.selected_die_type.get()
        roll_function = self.roll_functions[die_type]

        # Get the modifier from the entry field
        modifier = int(self.modifier_entry.get())
        
        # Call Roll Dice to get the collection of rolls
        rolls = DiceRoller.roll_dice(num_dice, roll_function)

        # Apply selection of mechanics to obtain the results of the rolls
        reroll_flag = self.reroll_var.get()

        