import time
import mujoco
from mujoco import viewer
import numpy as np
import os

model = mujoco.MjModel.from_xml_path("scene.xml")
data = mujoco.MjData(model)
view = viewer.launch_passive(model, data)


def pos_syn():

    #implement joint angle based on kinematic synergy
    shoulder_angle = 0
    elbow_angle = 0
    wrist_angle = 0

    for i in range(3000):
      shoulder_angle = i / 3000


    #define ratio
      a = 1
      b = 1
      elbow_anlge = a*shoulder_angle
      wrist_angle = elbow_angle

      print(elbow_angle)
      print(wrist_angle)
      data.actuator(0).ctrl[:] = shoulder_angle
      data.actuator(1).ctrl[:] = elbow_angle
      data.actuator(2).ctrl[:] = wrist_angle
      mujoco.mj_step(model, data)
      view.sync()
      time.sleep(0.002)

def ratio(a, b):
    elbow_angle = a * shoulder_angle
    wrist_angle = b* shoulder_angle
    

    
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
