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


#TODO a new class or data type for attack rolls and skill checks 
#and i can move some of the handling for the roll modifiers.

class ModifierHandler:
    
    # Logic for applying a modifier to the roll
    def apply_modifier(self, roll, modifier):
        return roll + modifier

    # Logic for advantage/disadvantage rolls where roll_results a list of length 1 or 2 of "d20" type
    def handle_advantage_disadvantage(self, rolls, advantage=False, disadvantage=False):

        #check to see if there are only 1 or 2 rolls in the list
        if len(rolls) > 0 and len(rolls) < 2:
            for roll in rolls:
                #check to see if each roll is a d20 if not raise an exception
                if roll.type != "d20":
                    raise Exception(f"{roll.type} cannot be rolled with advantage or disadvantage")
            #if only 1 roll return that value
            if len(rolls) == 1:
                return rolls[0]
            #else there are 2 rolls we need to check the flags
            else:
                #handle advantage logic
                if advantage == True and disadvantage == False:
                    #choose higher roll
                    return max(rolls[0], rolls[1])
                #handle disadvantage logic
                elif disadvantage == True and advantage == False:
                    #choose lower roll
                    return min(rolls[0], rolls[1])
                else:
                    raise Exception("disadvantage and advantage flags must be different")
            

    # Logic for critical_hits
    def handle_critical_hits(self, roll):
        if roll.type == "d20":
            pass
        else:
            raise Exception(f"{roll.type} cannot crit")

    # Logic for fumbles
    def handle_fumbles(self, roll):
        pass
    