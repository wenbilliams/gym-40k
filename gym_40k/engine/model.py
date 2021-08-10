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
    base_size = 1,
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
    weapons = []
    ):
  
    # TODO - Buffs, Debuggs, healing
    self.wounds          = wounds
    self.base_size       = base_size
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

    # These are attacks placed on this model 
    self.attacks         = []


    self.position = Position()

  def add_attack(attack):
    self.attacks.append(attack)

  def resolve_attacks():
    for attack in self.attacks:
      print(self.name + " resolving attack: " + attack)

      if attack.roll_to_hit():
        if attack.roll_to_wound():
          
        else:
          print("Failed to wound")
      else:
        print("Attack Missed")

      
      # Roll to hit
      # 
