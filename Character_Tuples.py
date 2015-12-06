__author__ = 'Glenn'

class Character_Tuples:
    STAT_TUPLE = ('Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma')
    CLASS_TUPLE = ('Choose Class', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger',
                   'Rogue', 'Sorcerer', 'Warlock', 'Wizard')
    RACE_TUPLE = ('Choose Race', 'Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc',
                  'Tiefling')
    DWARF_TUPLE = (2, 0, 2, 0, 0, 0)
    ELF_TUPLE = (0, 2, 0, 1, 0, 0)
    HALFLING_TUPLE = (0, 2, 0, 0, 0, 1)
    HUMAN_TUPLE = (1, 1, 1, 1, 1, 1)
    DRAGONBORN_TUPLE = (2, 0, 0, 0, 0, 1)
    GNOME_TUPLE = (0, 0, 1, 2, 0, 0)
    HALFELF_TUPLE = (0, 1, 1, 0, 0, 2)
    HALFORC_TUPLE = (2, 0, 1, 0, 0, 0)
    TIEFLING_TUPLE = (0, 0, 0, 1, 0, 2)
    # Skill tuples per class
    BARBARIAN_TUPLE = (1, 3, 7, 10, 11, 17)
    BARD_TUPLE = range(18)
    CLERIC_TUPLE = (5, 6, 9, 13, 14)
    DRUID_TUPLE = (1, 2, 6, 9, 10, 11, 14, 17)
    FIGHTER_TUPLE = (0, 1, 3, 5, 6, 7, 11, 17)
    MONK_TUPLE = (0, 3, 5, 6, 14, 16)
    PALADIN_TUPLE = (3, 6, 7, 9, 13, 14)
    RANGER_TUPLE = (1, 3, 6, 8, 10, 11, 16, 17)
    ROGUE_TUPLE = (0, 3, 4, 6, 7, 8, 11, 12, 13, 15, 16)
    SORCERER_TUPLE = (2, 4, 6, 7, 13, 14)
    WARLOCK_TUPLE = (2, 4, 5, 7, 8, 10, 14)
    WIZARD_TUPLE = (2, 5, 6, 8, 9, 14)
    # Every entry in SKILLS_TUPLE corresponds to the same entry index as SKILLS_MOD_TUPLE
    SKILLS_TUPLE = ('Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight',
                    'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance',
                    'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival')
    SKILLS_MOD_TUPLE = ('dex', 'wis', 'int', 'str', 'cha', 'int', 'wis', 'cha', 'int', 'wis', 'int', 'wis', 'cha',
                        'cha', 'int', 'dex', 'dex', 'wis')
    PROFICIENCY_TUPLE = (2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6)
    LEVEL_TUPLE = (1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    # Tuples for Barbarian gear
    BARBARIAN_MAIN_HAND = ('Choose a weapon', 'Battleaxe', 'Flail', 'Greataxe', 'Greatsword', 'Longsword',
                              'Warhammer')
    BARBARIAN_OFF_HAND = ('None', 'None', 'Scimitar', 'Shortsword', 'Shield')
    BARBARIAN_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Heavy Crossbow', 'Hand Crossbow', 'Shortbow',
                                'Longbow', 'Javelin')
    BARBARIAN_ARMOR = ('Choose armor', 'None', 'Padded', 'Leather', 'Studded', 'Hide', 'Chain Shirt', 'Scale Mail',
                       'Breastplate', 'Half Plate')
    # Tuples for Bard gear
    BARD_MAIN_HAND = ('Choose a weapon', 'Longsword', 'Rapier')
    BARD_OFF_HAND = ('None', 'None', 'Dagger', 'Shortsword')
    BARD_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Hand Crossbow', 'Shortbow')
    BARD_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded')
    # Tuples for Cleric gear
    CLERIC_MAIN_HAND = ('Choose a weapon', 'Greatclub', 'Mace', 'Spear')
    CLERIC_OFF_HAND = ('None', 'None', 'Shield')
    CLERIC_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Shortbow')
    CLERIC_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate',
                    'Half Plate')
    # Tuples for Druid gear
    DRUID_MAIN_HAND = ('Choose a weapon', 'Club', 'Dagger', 'Mace', 'Quarterstaff', 'Scimitar', 'Sickle', 'Spear')
    DRUID_RANGED_WEAPON = ('Choose a weapon', 'Dart', 'Javelin', 'Sling')
    DRUID_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded', 'Hide')
    # Tuples for Fighter gear
    FIGHTER_MAIN_HAND = ('Choose a weapon', 'Battleaxe', 'Flail', 'Greataxe', 'Greatsword', 'Longsword', 'Warhammer')
    FIGHTER_OFF_HAND = ('None', 'None', 'Scimitar', 'Shortsword', 'Shield')
    FIGHTER_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Heavy Crossbow', 'Hand Crossbow', 'Shortbow',
                             'Longbow', 'Javelin')
    FIGHTER_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate',
                     'Half Plate', 'Ring mail', 'Chain mail', 'Splint', 'Plate')
    # Tuples for Monk gear
    MONK_MAIN_WEAPONS = ('Choose a weapon', 'Unarmed', 'Dagger', 'Shortsword', 'Club', 'Mace', 'Quarterstaff')
    MONK_OFF_HAND = ('None', 'None', 'Dagger', 'Shortsword', 'Club')
    MONK_RANGED_WEAPON = ('Choose a weapon', 'Dart', 'Sling', 'Light Crossbow', 'Shortbow')
    MONK_ARMOR = ('None', 'None')
    # Tuples for Paladin gear
    PALADIN_MAIN_HAND = ('Choose a weapon', 'Battleaxe', 'Flail', 'Greataxe', 'Greatsword', 'Longsword', 'Warhammer')
    PALADIN_OFF_HAND = ('None', 'None', 'Scimitar', 'Shortsword', 'Shield')
    PALADIN_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Heavy Crossbow', 'Hand Crossbow', 'Shortbow',
                              'Longbow', 'Javelin')
    PALADIN_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate',
                     'Half Plate', 'Ring mail', 'Chain mail', 'Splint', 'Plate')
    # Tuples for Ranger gear
    RANGER_MAIN_HAND = ('Choose a weapon', 'Battleaxe', 'Flail', 'Greataxe', 'Greatsword', 'Longsword', 'Warhammer')
    RANGER_OFF_HAND = ('None', 'None', 'Scimitar', 'Shortsword', 'Shield')
    RANGER_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Heavy Crossbow', 'Hand Crossbow', 'Shortbow',
                              'Longbow', 'Javelin')
    RANGER_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded', 'Hide', 'Chain Shirt', 'Scale Mail', 'Breastplate',
                    'Half Plate')
    # Tuples for Rogue gear
    ROGUE_MAIN_HAND = ('Choose a weapon', 'Club', 'Dagger', 'Mace', 'Quarterstaff', 'Scimitar', 'Sickle', 'Spear',
                     'Longsword', 'Rapier', 'Shortsword')
    ROGUE_OFF_HAND = ('None', 'None', 'Dagger', 'Shortsword', 'Scimitar', 'Club')
    ROGUE_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Hand Crossbow', 'Shortbow')
    ROGUE_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded')
    # Tuples for Sorcerer gear
    SORCERER_MAIN_HAND = ('Choose a weapon', 'Dagger', 'Quarterstaff')
    SORCERER_RANGED_WEAPON = ('Choose a weapon', 'Dart', 'Sling', 'Light Crossbow')
    SORCERER_ARMOR = ('None', 'None')
    # Tuples for Warlock gear
    WARLOCK_MAIN_HAND = ('Choose a weapon', 'Club', 'Dagger', 'Greatclub', 'Mace', 'Quarterstaff', 'Spear')
    WARLOCK_RANGED_WEAPON = ('Choose a weapon', 'Light Crossbow', 'Dart', 'Shortbow', 'Sling')
    WARLOCK_ARMOR = ('Choose armor', 'Padded', 'Leather', 'Studded')
    # Tuples for Wizard gear
    WIZARD_MAIN_HAND = ('Choose a weapon', 'Dagger', 'Quarterstaff')
    WIZARD_RANGED_WEAPON = ('Choose a weapon', 'Dart', 'Sling', 'Light Crossbow')
    WIZARD_ARMOR = ('None', 'None')
    # Gear to value dicts
    armorClassDict = {'None' : 0, 'Padded' : 1, 'Leather' : 1, 'Studded' : 2, 'Hide' : 2, 'Chain shirt' : 3,
                      'Scale mail' : 4, 'Breastplate' : 4, 'Half plate' : 5, 'Ring mail' : 4, 'Chain mail' : 6,
                      'Splint' : 7, 'Plate' : 8}
    # Max dexterity bonus allowed based on armor (light armor has no actual dex max but stats can't go above 20 which is
    # a +5 modifier
    dexMaxDict = {'None' : 5, 'Padded' : 5, 'Leather' : 5, 'Studded' : 5, 'Hide' : 2, 'Chain shirt' : 2,
                  'Scale mail' : 2, 'Breastplate' : 2, 'Half plate' : 2, 'Ring mail' : 0, 'Chain mail' : 0,
                  'Splint' : 0, 'Plate' : 0}
    # Simple versatility means 1d6 while single hand and 1d8 while two hand.  Martial versatility is 1d8 and 1d10 instead
    weaponDamageDict = {'Club' : '1d4', 'Dagger' : '1d4', 'Greatclub' : '1d8', 'Handaxe' : '1d6', 'Javelin' : '1d6',
                        'Mace' : '1d6', 'Quarterstaff' : 'simpleVersatile', 'Spear' : 'simpleVersatile', 'Dart' : '1d4',
                        'Light Crossbow' : '1d8', 'Shortbow' : '1d6', 'Sling' : '1d4', 'Battleaxe' : 'martialVersatile',
                        'Flail' : '1d8', 'Glaive' : '1d10', 'Greataxe' : '1d12', 'Greatsword' : '2d6',
                        'Halberd' : '1d10', 'Longsword' : 'martialVersatile', 'Maul' : '2d6', 'Morningstar' : '1d8',
                        'Pike' : '1d10', 'Rapier' : '1d8', 'Scimitar' : '1d6', 'Shortsword' : '1d6',
                        'Trident' : 'simpleVersatile', 'War pick' : '1d8', 'Warhammer' : 'martialVersatile',
                        'Whip' : '1d4', 'Hand Crossbow' : '1d6', 'Heavy Crossbow' : '1d10', 'Longbow' : '1d8'}
    def __init__(self):
        pass
