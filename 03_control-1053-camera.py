"""Spawn a single drone, then command it to go to two setpoints consecutively, and plots the xyz output."""
import matplotlib.pyplot as plt
import numpy as np

from PyFlyt.core import Aviary

# initialize the log
log = np.zeros((1000, 3), dtype=np.float32)

# the starting position and orientations
start_pos = np.array([[0.0, 0.0, 1.0]])
start_orn = np.array([[0.0, 0.0, 0.0]])

# environment setup
env = Aviary(
    start_pos=start_pos,
    start_orn=start_orn,
    render=True,
    drone_type="quadx",
    drone_options=dict(
        use_camera=True,

        camera_FOV_degrees=110,
        camera_fps=30,
        # by default, camera_fps=control_hz,
        # but this makes the simulation slow,
        # see https://github.com/jjshoots/PyFlyt/pull/43
    ),
)

# set to position control
env.set_mode(7)

# for the first 500 steps, go to x=13, y=3, z=3
setpoint = np.array([-10.0, 5.0, 0.0, 3.0])
env.set_setpoint(0, setpoint)

for i in range(1000):
    env.step()

    # record the linear position state
    log[i] = env.state(0)[-1]

# for the next 500 steps, go to x=0, y=0, z=2, rotate 45 degrees
setpoint = np.array([0.0, 0.0, np.pi / 4, 2.0])
env.set_setpoint(0, setpoint)

for i in range(500, 1000):
    env.step()

    # record the linear position state
    log[i] = env.state(0)[-1]

# plot stuff out
plt.plot(np.arange(1000), log)
plt.show()

# get the camera image and show it
RGBA_img = env.drones[0].rgbaImg
DEPTH_img = env.drones[0].depthImg
SEG_img = env.drones[0].segImg

plt.imshow(RGBA_img)
# plt.show()
plt.imshow(DEPTH_img)
# plt.show()
plt.imshow(SEG_img)
plt.show()