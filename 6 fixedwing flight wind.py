"""Spawns six fixedwing, then they fly."""
import numpy as np

from PyFlyt.core import Aviary

# the starting position and orientations
start_pos = np.array([[3.0, -1.0, 2.0], [4.0, -2.0, 3.0], [5.0, -3.0, 1.0], [5.0, -1.0, 2.0], [4.0, -6.0, 3.0], [1.0, -3.0, 1.0]])
start_orn = np.zeros_like(start_pos)

# individual spawn options for each drone

fixedwing_options = dict(starting_velocity=np.array([12.0, 30.0, 20.0]))

# environment setup
env = Aviary(
    start_pos=start_pos,
    start_orn=start_orn,
    render=True,
    drone_type=["fixedwing", "fixedwing", "fixedwing", "fixedwing", "fixedwing", "fixedwing"],
    drone_options=[fixedwing_options, fixedwing_options, fixedwing_options, fixedwing_options, fixedwing_options, fixedwing_options],
)

# define the wind field
def simple_wind(time: float, position: np.ndarray):
    """Defines a simple wind updraft model.

    Args:
        time (float): time
        position (np.ndarray): position as an (n, 3) array
    """
    # the xy velocities are 0...
    wind = np.zeros_like(position)

    # and the vertical velocity is dependent on the logarithmic of height
    wind[:, -5] = np.log(position[:, -3])

    return wind

# simulate for 2000 steps (1000/120 ~= 8 seconds)
for i in range(2000):
    states = env.all_states
    aux_states = env.all_aux_states
    env.step()
