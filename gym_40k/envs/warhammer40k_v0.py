import gym
from gym import spaces
import numpy as np

class Warhammer40KV0(gym.Env):
  """Base Warhammer 40K Environment, written purely in Python"""
  metadata = {'render.modes': ['human']}

  def __init__(self, arg1, arg2):
    super(Warhammer40KV0, self).__init__()

    self.reward_range = (0, MAX_ACCOUNT_BALANCE)

    # Create Game State

    # Spaces are the represenation of fields that OpenAI Gym uses to marshall data in and out
    # https://github.com/openai/gym/blob/master/gym/spaces/space.py
    # There are multiple default child classes of spaces: https://github.com/openai/gym/tree/master/gym/spaces
    # The types I'll try to use here are:
    # 1: Box - a possibly unbounded Box in R^n
    # 2: Discrete - A Discrete space in math - {0, 1, ..., n-1}
    # Discrete is for selecting from a set of distinct choices
    # 3: Dict - A dictionary of simpler spaces
    # 4: Multi-Binary: An n-shaped binary space. Could be useful to mask the state of units
    # 5: Multi-Discrete: A series of discrete action spaces with different number of actions in each
    # 6: Tuple: A tuple, i.e product of simpler spaces

    # Actions of the format Buy x%, Sell x%, Hold, etc.
    self.action_space = spaces.Box(
      low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)

    # Observation space includes full game state
    self.observation_space = spaces.Box(
      low=0, high=1, shape=(6, 6), dtype=np.float16)

  # step returns four values. These are:
  # observation (object): an environment-specific object representing your observation of the environment. For example, pixel data from a camera, joint angles and joint velocities of a robot, or the board state in a board game.
  # reward (float): amount of reward achieved by the previous action. The scale varies between environments, but the goal is always to increase your total reward.
  # done (boolean): whether it’s time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and done being True indicates the episode has terminated. (For example, perhaps the pole tipped too far, or you lost your last life.)
  # info (dict): diagnostic information useful for debugging. It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment’s last state change). However, official evaluations of your agent are not allowed to use this for learning.
  def step(self, action):
    # Execute one time step within the environment

  def reset(self):
    # Reset the state of the environment to an initial state

  def render(self, mode='human', close=False):
    # Render the environment to the screen
