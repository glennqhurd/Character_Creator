from Tkinter import *
from ttk import *
from Character import Character
from Character_Tuples import *

__author__ = 'Glenn'

#  Images used for display
DRAGON_IMAGE = file='C:\\Users\\Glenn\\Pictures\\dragon_PNG981_small.gif'

class Character_Creator:

    def __init__(self):
        self.character = Character()
        self.tuples = Character_Tuples()
        self.skillCount = 0
        self.mainHandTuple = self.tuples.BARBARIAN_MAIN_HAND
        self.offHandTuple = self.tuples.BARBARIAN_OFF_HAND
        self.rangedTuple = self.tuples.BARBARIAN_RANGED_WEAPON
        self.armorTuple = self.tuples.BARBARIAN_ARMOR

    def pointBuyCallback(self, statIndex, additionMode):
        """
        Callback for the increment buttons that checks if the amount of points after the increment would be negative then
        if negative makes the increment button inactive and if not negative increments the label for the respective stat and
        subtracts from the available point total
        :param statPage:
        :param statCharacter:
        :param statIndex:
        :return:
        """
        #  True triggers addition
        if additionMode:
            self.character.Increment(statIndex)
            self.pointsTotalLabel.config(text=self.character.points)
            self.statLabelList[statIndex].config(text=self.character.stats[statIndex])
            self.statModList[statIndex].config(text=self.strFormat(self.character.modifiers[statIndex]))
            self.minusButtonList[statIndex].config(state='active')
            for i in range(len(self.tuples.STAT_TUPLE)):
                if self.character.canIncrement(i) == False:
                    self.plusButtonList[i].config(state='disabled')
            self.calculateResults()
        #  False triggers subtraction
        else:
            self.character.Decrement(statIndex)
            self.pointsTotalLabel.config(text=self.character.points)
            self.statLabelList[statIndex].config(text=self.character.stats[statIndex])
            self.statModList[statIndex].config(text=self.strFormat(self.character.modifiers[statIndex]))
            for i in range(len(self.character.tuples.STAT_TUPLE)):
                self.plusButtonList[i].config(state='active')
            if self.character.canDecrement(statIndex) == False:
                self.minusButtonList[statIndex].config(state='disabled')
            self.calculateResults()

    #def statsCallback(self):
    #    statsDict = self.character.assignRandomStats()

    def calculateResults(self):
        # Updates information when button Calculate Stats is pressed
        # Saving throw modifiers
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.savingThrowValues[i].config(text=self.strFormat(self.character.modifiers[i]))
        self.character.assignAC()
        self.ACValue.config(text=(self.character.armorClass))
        self.initiativeValue.config(text=self.strFormat(self.character.modifiers[1]))

        # Skill checks refresh
        for i in range(len(self.tuples.SKILLS_TUPLE)):
            if self.tuples.SKILLS_MOD_TUPLE[i] == 'str':
                if self.skillVar[i].get() == 1:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[0] +
                                                                   int(self.proficiencyValue.cget('text'))))
                else:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[0]))
            elif self.tuples.SKILLS_MOD_TUPLE[i] == 'dex':
                if self.skillVar[i].get() == 1:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[1] +
                                                                   int(self.proficiencyValue.cget('text'))))
                else:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[1]))
            elif self.tuples.SKILLS_MOD_TUPLE[i] == 'int':
                if self.skillVar[i].get() == 1:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[3] +
                                                                   int(self.proficiencyValue.cget('text'))))
                else:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[3]))
            elif self.tuples.SKILLS_MOD_TUPLE[i] == 'wis':
                if self.skillVar[i].get() == 1:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[4] +
                                                                   int(self.proficiencyValue.cget('text'))))
                else:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[4]))
            elif self.tuples.SKILLS_MOD_TUPLE[i] == 'cha':
                if self.skillVar[i].get() == 1:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[5] +
                                                                   int(self.proficiencyValue.cget('text'))))
                else:
                    self.skillsValue[i].config(text=self.strFormat(self.character.modifiers[5]))
        self.perceptionValue.config(text=self.strFormat(self.character.modifiers[4]))

    def calculateStatsLevel(self, selected):
        # Proficiency modifier changes
        self.proficiencyValue.config(text=self.strFormat(self.tuples.PROFICIENCY_TUPLE[selected-1]))
        self.calculateHP()

    def calculateStatsRace(self, selected):
        self.character.setRace(selected)
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.character.adjustModifiers(i)
        self.calculateResults()
        self.calculateHP()
        if selected == 'Dwarf':
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.DWARF_TUPLE[i])
        elif(selected == 'Elf'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.ELF_TUPLE[i])
        elif(selected == 'Halfling'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.HALFLING_TUPLE[i])
        elif(selected == 'Human'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.HUMAN_TUPLE[i])
        elif(selected == 'Dragonborn'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.DRAGONBORN_TUPLE[i])
        elif(selected == 'Gnome'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.GNOME_TUPLE[i])
        elif(selected == 'Half-Elf'):
            # Half-Elf is tricky because it lets you choose two score to increase.  For now, the program will increase
            # Dex and Con
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.HALFELF_TUPLE[i])
        elif(selected == 'Half-Orc'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.HALFORC_TUPLE[i])
        elif(selected == 'Tiefling'):
            for i in range(len(self.tuples.STAT_TUPLE)):
                self.statRaceList[i].config(text='+%d' % self.tuples.TIEFLING_TUPLE[i])
        # This code will refresh the display on the modifiers when a race is chosen
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.statModList[i].config(text=self.character.modifiers[i])
        if selected == 'Dwarf' or selected == 'Gnome' or selected == 'Halfling':
            self.speedValue.config(text='20ft.')
        else:
            self.speedValue.config(text='30ft.')

    def skillCallback(self, index):
        tempClass = self.classVar.get()
        if tempClass == 'Barbarian':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.BARBARIAN_TUPLE)):
                    self.skillBoxes[self.tuples.BARBARIAN_TUPLE[i]].config(state='normal')
        elif tempClass == 'Bard':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 2:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.BARD_TUPLE)):
                    self.skillBoxes[self.tuples.BARD_TUPLE[i]].config(state='normal')
        elif tempClass == 'Cleric':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.CLERIC_TUPLE)):
                    self.skillBoxes[self.tuples.CLERIC_TUPLE[i]].config(state='normal')
        elif tempClass == 'Druid':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.DRUID_TUPLE)):
                    self.skillBoxes[self.tuples.DRUID_TUPLE[i]].config(state='normal')
        elif tempClass == 'Fighter':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.FIGHTER_TUPLE)):
                    self.skillBoxes[self.tuples.FIGHTER_TUPLE[i]].config(state='normal')
        elif tempClass == 'Monk':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.MONK_TUPLE)):
                    self.skillBoxes[self.tuples.MONK_TUPLE[i]].config(state='normal')
        elif tempClass == 'Paladin':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.PALADIN_TUPLE)):
                    self.skillBoxes[self.tuples.PALADIN_TUPLE[i]].config(state='normal')
        elif tempClass == 'Ranger':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 2:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.RANGER_TUPLE)):
                    self.skillBoxes[self.tuples.RANGER_TUPLE[i]].config(state='normal')
        elif tempClass == 'Rogue':
            if self.skillVar[index].get() == 3:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.ROGUE_TUPLE)):
                    self.skillBoxes[self.tuples.ROGUE_TUPLE[i]].config(state='normal')
        elif tempClass == 'Sorcerer':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.SORCERER_TUPLE)):
                    self.skillBoxes[self.tuples.SORCERER_TUPLE[i]].config(state='normal')
        elif tempClass == 'Warlock':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.WARLOCK_TUPLE)):
                    self.skillBoxes[self.tuples.WARLOCK_TUPLE[i]].config(state='normal')
        elif tempClass == 'Wizard':
            if self.skillVar[index].get() == 1:
                self.skillCount += 1
                if self.skillCount > 1:
                    for i in range(len(self.tuples.SKILLS_TUPLE)):
                        if self.skillVar[i].get() == 0:
                            self.skillBoxes[i].config(state='disabled')
            else:
                self.skillCount = self.skillCount - 1
                for i in range(len(self.tuples.WIZARD_TUPLE)):
                    self.skillBoxes[self.tuples.WIZARD_TUPLE[i]].config(state='normal')
        self.calculateResults()

    def calculateClass(self, value):
        self.skillCount = 0
        self.resetGearLists()
        for i in range(len(self.tuples.SKILLS_TUPLE)):
            self.skillVar[i].set(0)
            self.skillBoxes[i].config(state='disabled')
            self.calculateHP()
        if self.classVar.get() == 'Barbarian':
            for i in range(len(self.tuples.BARBARIAN_TUPLE)):
                self.skillBoxes[self.tuples.BARBARIAN_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d12')
        if self.classVar.get() == 'Bard':
            for i in range(len(self.tuples.BARD_TUPLE)):
                self.skillBoxes[self.tuples.BARD_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Cleric':
            for i in range(len(self.tuples.CLERIC_TUPLE)):
                self.skillBoxes[self.tuples.CLERIC_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Druid':
            for i in range(len(self.tuples.DRUID_TUPLE)):
                self.skillBoxes[self.tuples.DRUID_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Fighter':
            for i in range(len(self.tuples.FIGHTER_TUPLE)):
                self.skillBoxes[self.tuples.FIGHTER_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d10')
        if self.classVar.get() == 'Monk':
            for i in range(len(self.tuples.MONK_TUPLE)):
                self.skillBoxes[self.tuples.MONK_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Paladin':
            for i in range(len(self.tuples.PALADIN_TUPLE)):
                self.skillBoxes[self.tuples.PALADIN_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d10')
        if self.classVar.get() == 'Ranger':
            for i in range(len(self.tuples.RANGER_TUPLE)):
                self.skillBoxes[self.tuples.RANGER_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d10')
        if self.classVar.get() == 'Rogue':
            for i in range(len(self.tuples.ROGUE_TUPLE)):
                self.skillBoxes[self.tuples.ROGUE_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Sorcerer':
            for i in range(len(self.tuples.SORCERER_TUPLE)):
                self.skillBoxes[self.tuples.SORCERER_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d6')
        if self.classVar.get() == 'Warlock':
            for i in range(len(self.tuples.WARLOCK_TUPLE)):
                self.skillBoxes[self.tuples.WARLOCK_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d8')
        if self.classVar.get() == 'Wizard':
            for i in range(len(self.tuples.WIZARD_TUPLE)):
                self.skillBoxes[self.tuples.WIZARD_TUPLE[i]].config(state='normal')
                self.HPDiceValue.config(text='1d6')

    def calculateHP(self):
        temp = self.classVar.get()
        level = int(self.levelVar.get())
        if temp == 'Barbarian':
            self.HPValue.config(text=str(12 + ((7 + self.character.modifiers[2]) * (level - 1)) +
                                         self.character.modifiers[2]))
        elif temp == 'Fighter' or temp == 'Paladin' or temp == 'Ranger':
            self.HPValue.config(text=str(10 + ((6 + self.character.modifiers[2]) * (level - 1)) +
                                         self.character.modifiers[2]))
        elif temp == 'Sorcerer' or temp == 'Wizard':
            self.HPValue.config(text=str(6 + ((4 + self.character.modifiers[2]) * (level - 1)) +
                                         self.character.modifiers[2]))
        else:
            self.HPValue.config(text=str(8 + ((5 + self.character.modifiers[2]) * (level - 1)) +
                                         self.character.modifiers[2]))

    def resetGearLists(self):
        self.mainHandVar.set('Unarmed')
        self.offHandVar.set('Unarmed')
        self.armorVar.set('No armor')

    def strFormat(self, statMod):
        # Formats the modfifier value into a string if positive of the form '+%d' or an intger if it's negative
        if statMod < 0:
            return statMod
        else:
            return '+%d' % statMod

    def statFrameDisplay(self):
        #  Stats frame of the window
        self.statPage = Frame(self.root, padding=12)
        self.statPage.grid(row=0, column=0, sticky=(N, W))
        self.statPage.rowconfigure(0, weight=1)
        self.statPage.columnconfigure(0, weight=1)

        #  List of labels for stats such as Strength and Dexterity
        Label(self.statPage, text='Stats:').grid(row=0, column=0)
        Label(self.statPage, text='Race Bonus:').grid(row=0, column=2)
        Label(self.statPage, text='Modifiers:').grid(row=0, column=3)
        self.statLabelList = [Label(self.statPage, text=8, width=2) for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.statLabelList[i].grid(row=(i + 1), column=1, sticky=W)
        self.statRaceList = [Label(self.statPage, text='+0', width=3) for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.statRaceList[i].grid(row=(i + 1), column=2)
        self.statModList = [Label(self.statPage, text='-1') for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.statModList[i].grid(row=(i + 1), column=3)
        [Label(self.statPage, text=self.tuples.STAT_TUPLE[i]).grid(row=(i + 1), sticky=W)
            for i in range(len(self.tuples.STAT_TUPLE))]
        self.levelLabel = Label(self.statPage, text='Level:')
        self.levelVar = StringVar(self.statPage)
        self.levelVar.set('1')
        self.levelOption = OptionMenu(self.statPage, self.levelVar, *self.tuples.LEVEL_TUPLE,
                                      command=self.calculateStatsLevel)
        self.levelLabel.grid(row=3, column=6)
        self.levelOption.grid(row=3, column=7, sticky='W')
        self.pointsTextLabel = Label(self.statPage, text='Available Points:')
        self.pointsTotalLabel = Label(self.statPage, text=self.character.points)
        #  Displays available points for point buy
        self.pointsTextLabel.grid(row=4, column=6, columnspan=2)
        self.pointsTotalLabel.grid(row=5, column=6, columnspan=2)
        #  Displays the increment and decrement buttons for point buy
        self.minusButtonList = [Button(self.statPage, text='-', command=lambda i=i: self.pointBuyCallback(i, False),
                                       state='disabled', width=2) for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.minusButtonList[i].grid(row=(i+1), column=4)
        self.plusButtonList = [Button(self.statPage, text='+', command=lambda i=i: self.pointBuyCallback(i, True),
                                      width=2) for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.tuples.STAT_TUPLE)):
            self.plusButtonList[i].grid(row=(i+1), column=5)
        #for i in range(len(self.character.STAT_TUPLE)):
            #self.plusButtonList[i].config(command=lambda: self.pointAddCallback(i))
        self.classVar = StringVar(self.statPage)
        self.classVar.set('Pick class')
        self.classOption = OptionMenu(self.statPage, self.classVar, *self.tuples.CLASS_TUPLE,
                                      command=self.calculateClass)
        self.classOption.config(width=len(self.tuples.CLASS_TUPLE[0]))
        self.raceVar = StringVar(self.statPage)
        self.raceVar.set('Pick race')
        self.raceOption = OptionMenu(self.statPage, self.raceVar, *self.tuples.RACE_TUPLE,
                                     command=self.calculateStatsRace)
        self.raceOption.config(width=len(self.tuples.RACE_TUPLE[0]))
        #  Displays the optionboxes for classes and races
        self.classOption.grid(row=1, column=6, columnspan=2)
        self.raceOption.grid(row=2, column=6, columnspan=2)
        #Button(self.statPage, text='Calculate stats', command=lambda: self.calculateCallback()).grid(row=7, sticky=W)
        self.attackLabel = Label(self.statPage, text='Attack Bonus:').grid(row=6, column=6, columnspan=2)
        # Write labels for each weapon's attack bonus
        # Weapon portion of the sheet
        # Main hand weapon
        self.mainHandLabel = Label(self.statPage, text='Main hand:').grid(row=7, column=0, sticky='W')
        self.mainHandVar = StringVar(self.statPage)
        self.mainHandVar.set('Choose a weapon')
        self.mainHandMenu = OptionMenu(self.statPage, self.mainHandVar, *self.mainHandTuple)
        self.mainHandMenu.config(width=18)
        self.mainHandMenu.grid(row=7, column=1, sticky='W', columnspan=3)
        self.mainHandDamage = Label(self.statPage, text='1d12+2', width=7)
        self.mainHandDamage.grid(row=7, column=4, columnspan=2)
        # Off hand weapon (for dual wield)
        self.offHandLabel = Label(self.statPage, text='Off hand:').grid(row=8, column=0, sticky='W')
        self.offHandVar = StringVar(self.statPage)
        self.offHandVar.set('Choose a weapon')
        self.offHandMenu = OptionMenu(self.statPage, self.offHandVar, *self.offHandTuple)
        self.offHandMenu.config(width=18)
        self.offHandMenu.grid(row=8, column=1, sticky='W', columnspan=3)
        # Ranged weapon
        self.rangedLabel = Label(self.statPage, text='Ranged: ').grid(row=9, column=0, sticky='W')
        self.rangedVar = StringVar(self.statPage)
        self.rangedVar.set('Choose a weapon')
        self.rangedMenu = OptionMenu(self.statPage, self.rangedVar, *self.rangedTuple)
        self.rangedMenu.config(width=18)
        self.rangedMenu.grid(row=9, column=1, sticky='W', columnspan=3)
        # Armor
        self.armorLabel = Label(self.statPage, text='Armor:').grid(row=10, column=0, sticky='W')
        self.armorVar = StringVar(self.statPage)
        self.armorVar.set('Choose armor')
        self.armorMenu = OptionMenu(self.statPage, self.armorVar, *self.armorTuple)
        self.armorMenu.config(width=18)
        self.armorMenu.grid(row=10, column=1, columnspan=3)
        for child in self.statPage.winfo_children():
            child.grid_configure(padx=0, pady=2)

    def resultsPageDisplay(self):
        #  Results frame of the window
        self.ResultsPage = Frame(self.root, padding=12)
        self.ResultsPage.grid(row=0, column=1, sticky=(N, S, E, W), rowspan=2)
        #  HP Label and value
        Label(self.ResultsPage, text='Total HP:').grid(row=1, column=0, sticky='W')
        self.HPValue = Label(self.ResultsPage, text='0')
        self.HPValue.grid(row=1, column=1)
        #  HP Dice label and value
        Label(self.ResultsPage, text='Hit Dice:').grid(row=2, column=0, sticky='W')
        self.HPDiceValue = Label(self.ResultsPage, text='1d6')
        self.HPDiceValue.grid(row=2, column=1)
        #  Armor Class label and value
        Label(self.ResultsPage, text='Armor Class:').grid(row=3, column=0, sticky='W')
        self.ACValue = Label(self.ResultsPage, text=self.character.armorClass)
        self.ACValue.grid(row=3, column=1)
        #  Initiative label and value
        Label(self.ResultsPage, text='Initiative:').grid(row=4, column=0, sticky='W')
        self.initiativeValue = Label(self.ResultsPage, text=self.strFormat(self.character.modifiers[1]))
        self.initiativeValue.grid(row=4, column=1)
        #  Proficiency label, stringvar, and Proficiency value
        Label(self.ResultsPage, text='Proficiency Bonus:').grid(row=5, column=0)
        self.proficiencyValue = Label(self.ResultsPage, text='+2')
        self.proficiencyValue.grid(row=5, column=1)
        #  Saving throws labels
        Label(self.ResultsPage, text="Saving Throws:").grid(row=6, column=0, sticky='W')
        [Label(self.ResultsPage, text=self.tuples.STAT_TUPLE[i]).grid(row=(i + 7), sticky=W)
            for i in range(len(self.tuples.STAT_TUPLE))]
        self.savingThrowValues = [Label(self.ResultsPage, text=self.strFormat(self.character.modifiers[i]))
                                  for i in range(len(self.tuples.STAT_TUPLE))]
        for i in range(len(self.savingThrowValues)):
            self.savingThrowValues[i].grid(row=i+7, column=1)
        #  Perception label and value
        Label(self.ResultsPage, text='Perception:').grid(row=13, column=0, sticky='W')
        self.perceptionValue = Label(self.ResultsPage, text='-1')
        self.perceptionValue.grid(row=13, column=1)
        #  Movement speed label and value
        Label(self.ResultsPage, text='Move Speed:').grid(row=14, column=0, sticky='W')
        self.speedValue = Label(self.ResultsPage, text='30ft.')
        self.speedValue.grid(row=14, column=1)
        for child in self.ResultsPage.winfo_children():
            child.grid_configure(padx=0, pady=2)

    def skillsPageDisplay(self):
        #  Skills frame
        self.SkillsPage = Frame(self.root, padding=12)
        self.SkillsPage.grid(row=0, column=2, rowspan=2)
        #  Skills label and values
        Label(self.SkillsPage, text='Skills:').grid(row=1, column = 3, sticky='W')
        self.skillVar = []
        self.skillBoxes = []
        self.skillsValue = [Label(self.SkillsPage, text='-1') for i in range(len(self.tuples.SKILLS_TUPLE))]
        for i in range(len(self.tuples.SKILLS_TUPLE)):
            self.skillVar.append(IntVar())
            self.skillBoxes.append(Checkbutton(self.SkillsPage, text=self.tuples.SKILLS_TUPLE[i],
                                               variable=self.skillVar[i]))
            self.skillBoxes[i].grid(row=i+2, column=3, sticky='W')
        for i in range(len(self.tuples.SKILLS_TUPLE)):
            self.skillBoxes[i].config(command=lambda i=i: self.skillCallback(i), state='disabled')
        for i in range(len(self.tuples.SKILLS_TUPLE)):
            self.skillsValue[i].grid(row=i+2, column=4)
        for child in self.SkillsPage.winfo_children():
            child.grid_configure(padx=0, pady=2)

    def TotalDisplay(self):
        self.root = Tk()
        # self.s = Style()
        # self.s.theme_use()

        self.statFrameDisplay()
        self.resultsPageDisplay()
        self.skillsPageDisplay()


        self.root.mainloop()


if __name__ == '__main__':
    characterCreator = Character_Creator()
    characterCreator.TotalDisplay()