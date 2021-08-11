from gym_40k.engine.weapon_type import WeaponType
from gym_40k.engine.weapon_ability import WeaponAbility
from gym_40k.engine.random_quantity import RandomQuantity

class Weapon():
  """Base Warhammer 40K Weapon"""

  def __init__(
    self,
    name = "Bolter",
    range_inches = 24,
    weapon_type = WeaponType.RapidFire,
    attacks = 1,
    weapon_abilities = [],
    random_attacks = RandomQuantity.Fixed,
    random_damage  = RandomQuantity.Fixed,
    strength       = 1,
    damage         = 1,
    ap             = 0):
    self.name = name
    self.range_inches = range_inches
    self.weapon_type = weapon_type
    self.attacks = attacks
    self.weapon_abilities = weapon_abilities
    self.random_attacks = random_attacks
    self.random_damage  = random_damage
    self.strength       = strength
    self.damage         = damage
    self.ap             = ap