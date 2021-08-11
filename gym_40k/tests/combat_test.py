from gym_40k.engine.model import Model
from gym_40k.engine.unit import Unit
from gym_40k.engine.weapon import Weapon
from gym_40k.engine.position import Position

teamOneId = 1
teamTwoId = 2

lasgun = Weapon(
    name = "Lasgun",
    range_inches = 24,
    weapon_type = WeaponType.RapidFire,
    attacks = 1,
    weapon_abilities = [],
    random_attacks = RandomQuantity.Fixed,
    random_damage  = RandomQuantity.Fixed,
    strength       = 3,
    damage         = 1,
    ap             = 0)

bolter = Weapon(
    name = "Bolter",
    range_inches = 24,
    weapon_type = WeaponType.RapidFire,
    attacks = 1,
    weapon_abilities = [],
    random_attacks = RandomQuantity.Fixed,
    random_damage  = RandomQuantity.Fixed,
    strength       = 4,
    damage         = 1,
    ap             = 0)

# Single Guardsman
guardsmanModel = Model(
    "Guardsman",
    teamOneId,
    ModelType.Infantry,
    False,
    1,
    28,
    6,
    4,
    4,
    3,
    3,
    1,
    6,
    5,
    0,
    0,
    weapons = [lasgun],
    position = Position()
)

# Single Primaris Intercessor
primarisModel = Model(
    "Primaris Intercessor",
    teamTwoId,
    ModelType.Infantry,
    False,
    2,
    32,
    6,
    3,
    3,
    4,
    4,
    1,
    7,
    3,
    0,
    0,
    weapons = [bolter],
    position = Position()
)

unit1 = Unit("Guardsman Squad", [guardsmanModel], teamOneId)

unit2 = Unit("Primaris Squad", [primarisModel], teamTwoId)

