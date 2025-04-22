"""Spawns six drones, then sets all drones to have different control looprates."""
import numpy as np

from PyFlyt.core import Aviary

# the starting position and orientations
start_pos = np.array([[1.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, -1.0, 1.5], [1.0, -2.0, 2.5], [1.0, -2.5, 2.0], [1.0, -3.0, 1.0]])
start_orn = np.zeros_like(start_pos) 

# modify the control hz of the individual drones
drone_options = []
drone_options.append(dict(control_hz=60))
drone_options.append(dict(control_hz=120))
drone_options.append(dict(control_hz=240))
drone_options.append(dict(control_hz=60))
drone_options.append(dict(control_hz=120))
drone_options.append(dict(control_hz=240))


# environment setup
env = Aviary(
    start_pos=start_pos,
    start_orn=start_orn,
    render=True,
    drone_type="quadx",
    drone_options=drone_options,
)

# define the wind field
def simple_wind(time: float, position: np.ndarray):
    """Defines a simple wind updraft model.

    Args:
        time (float): time
        position (np.ndarray): position as an (n, 6) array
    """
    # the xy velocities are 0...
    wind = np.zeros_like(position)

    # and the vertical velocity is dependent on the logarithmic of height
    wind[:, 8] = np.log(position[:, 5])

    return wind

# set to position control
env.set_mode(7)

# simulate for 2000 steps (1000/120 ~= 8 seconds)
for i in range(2000):
    env.step()
