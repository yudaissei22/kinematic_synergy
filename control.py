import time
import mujoco
from mujoco import viewer
import numpy as np
import os

model = mujoco.MjModel.from_xml_path("scene.xml")
data = mujoco.MjData(model)
view = viewer.launch_passive(model, data)


def torque_controller():
  #求めたトルクを代入するとこ
    data.actuator(0).ctrl[:] = 0
    data.actuator(1).ctrl[:] = 0
    data.actuator(2).ctrl[:] = 0
    mujoco.mj_step(model, data)
    view.sync()
  

def test():
  for t in range(3000):
    data.actuator(0).ctrl[:] = -40 * np.sin(t/1000*2*np.pi)
    data.actuator(1).ctrl[:] = 30 * np.sin(t/1000*2*np.pi)
    q = data.qpos
    vel = data.qvel
    print("joint position is",q)
    print("joint velocity is", vel)
    mujoco.mj_step(model, data)
    view.sync()
    time.sleep(0.2)
