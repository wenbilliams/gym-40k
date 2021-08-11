from gym_40k.engine.position import Position
from gym_40k.engine.model_type import ModelType
from gym_40k.engine.attack import Attack

class Model():
  """Base Warhammer 40K Model"""

  def __init__(self,
    name    = "Base human",
    team    = 0,
    type    = ModelType.Infantry,
    flying  = False,
    wounds = 1,
    base_size_mm = 28,
    move = 6,
    weapon_skill = 4,
    ballistic_skill = 4,
    strength = 3,
    toughness = 3,
    attacks = 1,
    leadership = 6,
    armor_save = 5,
    invul_save = 0,
    feel_no_pain = 6,
    weapons = [],
    position = Position()
    ):
  
    # TODO - Buffs, Debuggs, healing
    self.wounds          = wounds
    self.max_wounds          = wounds

    self.base_size_mm    = base_size_mm
    self.move            = move
    self.weapon_skill    = weapon_skill
    self.ballistic_skill = ballistic_skill
    self.strength        = strength
    self.toughness       = toughness
    self.attacks         = attacks
    self.leadership      = leadership
    self.armor_save      = armor_save
    self.invul_save      = invul_save
    self.feel_no_pain    = feel_no_pain
    self.weapons         = weapons
    self.name            = name
    self.team            = team
    self.type            = type
    self.flying          = flying
    self.in_close_combat = False
    self.alive           = True

    # These are attack objects placed on this model 
    self.unresolved_attacks = []

    # These are ints, each one being a quantity of damage
    self.unresolved_wounds  = []
    self.position = position

  def roll_armor_save(ap):
    die = Die(1,6)
    to_save = self.armor_save
    to_save += ap
    if self.invul_save:
      if self.invul_save < to_save:
        so_save = invul_save

    return die.roll() >= to_save

  def roll_feel_no_pain():
    die = Die(1,6)
    if self.feel_no_pain > 0:
      to_save = self.feel_no_pain
    return die.roll() >= to_save

  def add_attack(attack):
    self.unresolved_attacks.append(attack)

  def resolve_attacks():
    for attack in self.unresolved_attacks:
      print(self.name + " resolving attack: " + attack)

      if attack.roll_to_hit():
        if attack.roll_to_wound():
          # TODO - Select which save to allocate:
          if not roll_armor_save(attack.ap):
            self.unresolved_wounds.append(attack.damage)
          else:
            print("Passed armor save")
        else:
          print("Failed to wound")
      else:
        print("Attack Missed")

  def resolve_death():
    # Resolve OnDeath abilities - Explodes, revival, etc.
    self.alive = False
    self.in_close_combat = False
    self.wounds = 0

    # Move off table - Identity position
    self.position = Position()

  def resolve_wounds():
    # TODO - How do we determine the order in which wounds are resolved
    for damage in self.unresolved_wounds:
      if roll_feel_no_pain():
        print("Felt no pain")
      else:
        # TODO - Wound reduction abilities
        self.wounds -= damage

        if self.wounds <= 0:
          resolve_death()
          break

    self.unresolved_wounds.clear()
