import random

class DiceRoller:
    #constructor for rolls
    def __init__(self, value, type):
        self.value = value
        self.type = type

    #formatting for roll type and value for printing
    def __str__(self):
        return f"{self.type} roll: {self.value}"

    # Logic for rolling a d4
    def roll_d4(self):
        self.type = "d4"
        self.value = random.randint(1,4)

    # Logic for rolling a d6
    def roll_d6(self):
        self.type = "d6"
        self.value = random.randint(1,6)

    # Logic for rolling a d8
    def roll_d8(self):
        self.type = "d8"
        self.value = random.randint(1,8)

    # Logic for rolling a d10
    def roll_d10(self):
        self.type = "d10"
        self.value = random.randint(1,10)

    # Logic for rolling a d12
    def roll_d12(self):
        self.type = "d12"
        self.value = random.randint(1,12) 
    # Logic for rolling a d20
    def roll_d20(self):
        self.type = "d20"
        self.value = random.randint(1,20)
    # Logic for rolling a d100
    def roll_d100(self):
        self.type = "d100"
        self.value = random.randint(1,100)

    # Logic for applying a modifier to the roll
    def apply_modifier(self, value, modifier):
        return value + modifier
    
    # Roll a collection of dice and return a list of the dice
    def roll_dice(self, num_to_roll, roll_function):
        dice_list = []
        for i in range(1, num_to_roll):
            dice_roll = roll_function()
            dice_list.append(dice_roll)
        return dice_list
    
    # Special mechanics:

    # Reroll a number of dice?
    def reroll(self, roll_function, rolls_to_reroll):
        new_rolls = []
        for roll in rolls_to_reroll:
            new_roll = roll_function()
            new_rolls.append(new_roll)
        return new_rolls
    
    # Advantaged roll: take highest from a collection of rolls
    def roll_advantage(self, rolls):
        return max(rolls)
    
    # Disadvantaged roll: take lowest from a collection of rolls
    def roll_disadvantage(self, rolls):
        return min(rolls)
    
    # Apply modifier to each roll in a collection then return the collection
    def modify_each_roll(self, rolls, modifier):
        moded_rolls = []
        for roll in rolls:
            modified_roll = self.apply_modifier(roll, modifier)
            moded_rolls.append(modified_roll)
        return moded_rolls
    
    # Apply modifier to each roll in a collection then total
    def modify_each_roll_and_total(self, rolls, modifier):
        total = 0
        for roll in rolls:
            modified_roll = self.apply_modifier(roll, modifier)
            total += modified_roll
        return total

    # Apply modifier to the total of a collection of rolls
    def modify_total(self, rolls, modifier):
        total = 0
        for roll in rolls:
            total += roll
        modified_total = self.apply_modifier(total, modifier)
        return modified_total
    
    