from gym_40k.engine.dice import Dice

from enum import Enum
class RandomQuantity(Enum):
    D3      = 1
    D3Plus1 = 2
    TwoD3   = 3
    D6      = 4
    D6Plus1 = 5
    TwoD6   = 6
    Fixed   = 7

def resolveRandomQuantity(randomQuantity, baseNumber):
    if randomQuantity == RandomQuantity.Fixed:
        return baseNumber
    if randomQuantity == RandomQuantity.D3:
        die = Dice(1,3)
        return die.roll()
    if randomQuantity == RandomQuantity.D3Plus1:
        die = Dice(1,3)
        return die.roll() + 1
    if randomQuantity == RandomQuantity.D6:
        die = Dice(1,6)
        return die.roll()
    if randomQuantity == RandomQuantity.D6Plus1:
        die = Dice(1,6)
        return die.roll() + 1
    if randomQuantity == RandomQuantity.TwoD6:
        die1 = Dice(1,6)
        die2 = Dice(1,6)
        return die1.roll() + die2.roll()