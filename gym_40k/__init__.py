from gym_40k.envs.warhammer40k_v0 import Warhammer40KV0
from gym.envs.registration import register

register(
    id="40kVsRandomBot-v0",
    entry_point="gym_40k.envs:Warhammer40KV0",
    kwargs={"opponent": "random"},
)

register(
    id="40kVsVsSelf-v0",
    entry_point="gym_40k.envs:Warhammer40KV0",
    kwargs={"opponent": "none"},
    # max_episode_steps=100,
    # reward_threshold=.0, # optimum = .0
)