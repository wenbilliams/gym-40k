class Unit():
  """Container for a unit of models"""

  def __init__(
    self,
    # string
    name,
    # int
    team):

    self.models = []
    self.name = name
    self.team = team

  def addModel(model):
    print("Unit " + self.name + " adding model: " + model)
    self.models.append(model)