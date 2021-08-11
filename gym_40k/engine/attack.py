from gym_40k.engine.die import Die
from gym_40k.engine.model import Model

class Attack():
  """Class handling an attack action"""

  def __init__(
      self,
      strength,
      damage,
      random_quantity_damage,
      source_model,
      target_model,
      attack_abilities,
      ap
      ):

      self.strength = strength
      self.damage = damage
      self.random_quantity_damage = random_quantity_damage
      self.source_model = source_model
      self.target_model = target_model
      self.attack_abilities = attack_abilities
      self.ap = ap

      # Add attack to target model
      target_model.add_attack(self)

  def roll_to_hit():
      # TODO - Extra modifiers here
      die = Die(1,6)
      return self.source_model.ballistic_skill <= die.roll()

  def roll_to_wound():
      # TODO - Extra modifiers here
      die = Die(1,6)

      if self.target_model.toughness >= self.strength * 2:
          to_wound = 6
      elif self.target_model.toughness > self.strength:
          to_wound = 5
      elif self.target_model.toughness == self.strength:
          to_wound = 4
      elif self.target_model.toughness <= self.strength / 2:
          to_wound = 2
      else:
          to_wound = 3

      return die.roll() >= to_wound

  def resolve_damage():
      return resolveRandomQuantity(self.random_quantity_damage, self.damage)