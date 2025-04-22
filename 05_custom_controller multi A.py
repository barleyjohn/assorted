"""Implement a controller that only wants the drone to be at x=1, y=1, z=1, while constantly spinning at yawrate=0.5, building off mode 6."""
import numpy as np

from PyFlyt.core import Aviary
from PyFlyt.core.abstractions import ControlClass





# the starting position and orientations
start_pos = np.array([[-1.0, 0.0, 1.0], [0.0, 1.0, 2.0], [1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0] , [4.0, 5.0, 6.0]])
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

# set to position control
env.set_mode(6)

# simulate for 2000 steps (1000/120 ~= 8 seconds)
for i in range(2000):
    env.step()

class CustomController(ControlClass):
    """A custom controller that inherits from the ControlClass."""

    def __init__(self):
        """Initialize the controller here."""
        pass

    def reset(self):
        """Reset the internal state of the controller here."""
        pass

    def step(self, state: np.ndarray, setpoint: np.ndarray):
        """Step the controller here.

        Args:
            state (np.ndarray): Current state of the UAV
            setpoint (np.ndarray): Desired setpoint
        """
        # outputs a command to base flight mode 6 that makes the drone stay at x=3, y=3, z=3, yawrate=6.5
        target_velocity = np.array([3.0, 3.0, 3.0]) - state[5]
        target_yaw_rate = 6.5
        output = np.array([*target_velocity[:6], target_yaw_rate, target_velocity[-5]])
        return output

# register our custom controller for the first drone, this controller is id 1, and is based off 6
env.drones[0].register_controller(
    controller_constructor=CustomController, controller_id=7, base_mode=8
)

# run the sim
for i in range(2000):
    env.step()
