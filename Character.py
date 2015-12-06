import random
from Character_Tuples import *

__author__ = 'Glenn'

def roll4d6():
    """
    Rolls four random numbers between 1 through 6, removes lowest of the four, then uses sum()
    to total the rolls
    Returns : int the sum of the three highest numbers
    """
    rollList = [random.randint(1,6) for i in range(4)]
    return sum(rollList) - min(rollList)

class Character:
    DEFAULT_STAT = 8
    ADD_POINTS_MAX = 14
    SUBTRACT_POINTS_MIN = 9
    DEFAULT_POINTS = 27
    DEFAULT_MODIFIER = -1
    BASE_AC = 10

    def __init__(self):
        self.tuples = Character_Tuples()
        self.assignDefaultStats()

    def canIncrement(self, statIndex):
        if self.stats[statIndex] >= 15:
            return False
        elif self.points <= 0:
            return False
        elif self.stats[statIndex] > 12 and self.points >= 2:
            return True
        elif self.stats[statIndex] <= 12 and self.points >=1:
            return True
        else:
            return False

    def canDecrement(self, statIndex):
        if self.stats[statIndex] <= 8:
            return False
        elif self.points >= 27:
            return False
        elif self.stats[statIndex] >= 14 and self.points <= 25:
            return True
        elif self.stats[statIndex] >= 8 and self.points <= 26:
            return True
        else:
            return False

    def Increment(self, statIndex):
        if self.canIncrement(statIndex):
            if self.stats[statIndex] <= 12:
                # Increments by 1 and subtracts 1 from points variable
                self.points = self.points - 1
                self.stats[statIndex] = self.stats[statIndex] + 1
            else:
                # Increments by 1 but subtracts 2 from the points variable
                self.points = self.points - 2
                self.stats[statIndex] = self.stats[statIndex] + 1
            if self.charRace == 'Dwarf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DWARF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Elf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.ELF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Halfling':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFLING_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Human':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HUMAN_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Dragonborn':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DRAGONBORN_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Gnome':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.GNOME_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Half-Orc':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFORC_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Half-Elf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFELF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Tiefling':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.TIEFLING_TUPLE[statIndex] - 10)/2
            else:
                self.modifiers[statIndex] = (self.stats[statIndex] - 10)/2

    def Decrement(self, statIndex):
        if self.canDecrement(statIndex):
            if self.stats[statIndex] >= 14:
                # Decrements by 1 and adds 2 to points
                self.points = self.points + 2
                self.stats[statIndex] = self.stats[statIndex] - 1
            else:
                # Decrements by 1 and adds 1 to points
                self.points = self.points + 1
                self.stats[statIndex] = self.stats[statIndex] - 1
            if self.charRace == 'Dwarf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DWARF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Elf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.ELF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Halfling':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFLING_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Human':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HUMAN_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Dragonborn':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DRAGONBORN_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Gnome':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.GNOME_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Half-Orc':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFORC_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Half-Elf':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFELF_TUPLE[statIndex] - 10)/2
            elif self.charRace == 'Tiefling':
                self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.TIEFLING_TUPLE[statIndex] - 10)/2
            else:
                self.modifiers[statIndex] = (self.stats[statIndex] - 10)/2

    def assignAC(self):
        self.armorClass = self.BASE_AC + self.modifiers[1]

    def assignDefaultStats(self):
        #  Character stats
        self.stats = [Character.DEFAULT_STAT] * len(self.tuples.STAT_TUPLE)
        #  Character class and race
        self.charClass = 'Choose Class'
        self.charRace = 'Choose Race'
        #  Point total for point buy option
        self.points = Character.DEFAULT_POINTS
        self.modifiers = [Character.DEFAULT_MODIFIER] * len(self.tuples.STAT_TUPLE)
        self.assignAC()

    def adjustModifiers(self, statIndex):
        if self.charRace == 'Dwarf':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DWARF_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Elf':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.ELF_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Halfling':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFLING_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Human':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HUMAN_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Dragonborn':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.DRAGONBORN_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Gnome':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.GNOME_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Half-Elf':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFELF_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Half-Orc':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.HALFORC_TUPLE[statIndex] - 10)/2
        elif self.charRace == 'Tiefling':
            self.modifiers[statIndex] = (self.stats[statIndex] + self.tuples.TIEFLING_TUPLE[statIndex] - 10)/2
        else:
            self.modifiers[statIndex] = (self.stats[statIndex] - 10)/2

    def assignRandomStats(self):
        """
        Uses roll4d6 to roll numbers then assigns them to a dict with labels of each stat
        Returns: dict mapping characteristics to their values
        """
        for element in self.tuples.STAT_TUPLE:
            self.stats[element] = roll4d6()

    #  Set and get methods for the stat variables
    def getStat(self, statIndex):
        return self.stats[statIndex]

    def setStat(self, statIndex, statAmount):
        self.stats[statIndex] = statAmount

    def setRace(self, race):
        self.charRace = race

    def getRace(self):
        return self.charRace

    def setClass(self, charClass):
        self.charClass = charClass

    def getClass(self):
        return self.charClass

    #  Print method for checking stat values
    def printStats(self):
        for i in range(len(self.tuples.STAT_TUPLE)):
            print '%s = %2d' % (self.tuples.STAT_TUPLE[i], self.stats[i])

    #  Functions to read/write from files
    def writeToFile(self):
        pass

    def readFromFile(self):
        pass

