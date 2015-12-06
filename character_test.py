import unittest

from Character import *

class TestCharacterMethods(unittest.TestCase):

    def testDefaults(self):
        character = Character()
        for i in range(len(Character.STAT_TUPLE)):
            self.assertEqual(8, character.getStat(i))
            self.assertEqual(Character.DEFAULT_POINTS, character.points)

    def testSetStat(self):
        character = Character()
        character.setStat(1, 10)
        self.assertEqual(10, character.getStat(1))

    def testCanIncrement(self):
        character = Character()
        # default of 8 can be incremented
        self.assertTrue(character.canIncrement(1))
        # cannot increment a stat higher than 15
        character.setStat(1, 15)
        self.assertFalse(character.canIncrement(1))
        # incrementing costs 1 point for values below 13
        character.points = 1
        for i in range(8, 12):
            character.setStat(1, i)
            self.assertTrue(character.canIncrement(1))
        for i in range(13, 14):
            character.setStat(1, i)
            self.assertFalse(character.canIncrement(1))
        # incrementing costs 2 points for values between 13 and 14
        character.points = 2
        for i in range(13, 14):
            character.setStat(1, i)
            self.assertTrue(character.canIncrement(1))

    def testCanDecrement(self):
        character = Character()
        # default of 8 cannot be decremented
        self.assertFalse(character.canDecrement(1))
        # decrementing gains 2 points for values between 14 and 16 up to a max of 27 points
        character.points = 25
        for i in range(14, 16):
            character.setStat(1, i)
            self.assertTrue(character.canDecrement(1))
        # decrementing gains 1 point for values between 9 and 13 up to a max of 27 points
        character.points = 26
        for i in range(9, 13):
            character.setStat(1, i)
            self.assertTrue(character.canDecrement(1))

    def testIncrement(self):
        character = Character()
        for i in range(0, 5):
            for j in range(13, 14):
                character.stats[i] = j
                character.points = 27
                character.Increment(i)
                self.assertEqual(25, character.points)
                self.assertEqual((j + 1), character.stats[i])
                self.assertEqual(((j + 1) - 10)/2, character.modifiers[i])
            for j in range(8, 12):
                character.stats[i] = j
                character.points = 27
                character.Increment(i)
                self.assertEqual(26, character.points)
                self.assertEqual((j + 1), character.stats[i])
                self.assertEqual(((j + 1) - 10)/2, character.modifiers[i])

    def testDecrement(self):
        character = Character()
        for i in range(0, 5):
            for j in range(14, 15):
                character.stats[i] = j
                character.points = 0
                character.Decrement(i)
                self.assertEqual(2, character.points)
                self.assertEqual((j - 1), character.stats[i])
            for j in range(9, 13):
                character.stats[i] = j
                character.points = 0
                character.Decrement(i)
                self.assertEqual(1, character.points)
                self.assertEqual((j - 1), character.stats[i])

if __name__ == '__main__':
    unittest.main()
