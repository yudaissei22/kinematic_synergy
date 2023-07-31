import time
import mujoco
from mujoco import viewer
import numpy as np
import os
import matplotlib.pyplot as plt


model = mujoco.MjModel.from_xml_path("../models/scene.xml")
data = mujoco.MjData(model)
view = viewer.launch_passive(model, data)

# def move():

    
      data.actuator(0).ctrl[:] = shoulder_angle
      data.actuator(2).ctrl[:] = elbow_angle
      data.actuator(4).ctrl[:] = wrist_angle
      mujoco.mj_step(model, data)
      view.sync()
      time.sleep(0.002)
    
# def primitive():
#     ratio(1,1)

# def firing_ratio():

#       def ratio(shoulder_angle, a, b):
#     elbow_angle = a * shoulder_angle
#     wrist_angle = b* shoulder_angle

def move(a, b, c, first_angle, last_angle, time):

    # initialize joint angle
    shouder_angle = first_angle
    elbow_angle = shouder_angle * b / a
    wrist_angle = shouder_angle * c / a

    velo_angle = (last_angle - first_angle) / time
    t = velo_angle / 0.002

    for i in range(t):
        data.actuator(0).crtl[:] = shoulder_angle
        data.actuator(0).crtl[:] = elbow_angle
        data.actuator(0).crtl[:] = wrist_angle
        
        # renew joint angle
        shoulder_angle = first_angle + velo_angle * 0.002
        elbow_angle = shoulder_angle * b / a
        wrist_angle = shoulder_angle * c / a 

        mujoco.mj_step(model, data)
        view.sync()
        time.sleep(0.002)

def ratio(shoulder_angle, a,b,c):
    
def angle_list(time, initial_angle, final_angle, a, b, c):
    # radian
  radian_initial_angle = np.pi / 180 * initial_angle
  radian_final_angle = np.pi / 180 * final_angle
  t = time / 0.002
  velo_angle = (radian_final_angle - radian_initial_angle) / t  
  list = np.zeros((t, 4))
  for i in range(t):
    j = i * 0.002
    shoulder_angle = radian_initial_angle * velo_angle * j
    elbow_angle = shoulder_angle * b / a
    wrist_angle = shoulder_angle * b / a
    list[i-1][0] = i
    list[i-1][1] = shoulder_angle 
    list[i-1][2] = elbow_angle
    list[i-1][3] = wrist_angle

def new():
    angle_list(3, 15, -15, 1,1,1)
    print(list)
        
def test():
  for t in range(3000):
      # [rad]
    data.actuator(0).ctrl[:] = -1 + np.sin(t/1000*2*np.pi)
    data.actuator(1).ctrl[:] = -1 + np.sin(t/1000*2*np.pi)
    data.actuator(2).ctrl[:] = -1 + np.sin(t/1000*2*np.pi)
    q = data.qpos
    vel = data.qvel
    print("joint position is",q)
    print("joint velocity is", vel)
    mujoco.mj_step(model, data)
    view.sync()
    time.sleep(0.002)
    
def each(a,b,c):

  for t in range(3000):
    data.actuator(0).ctrl[:] = a
    data.actuator(2).ctrl[:] = b
    data.actuator(4).ctrl[:] = c
    mujoco.mj_step(model, data)
    view.sync()
    time.sleep(0.002)

    
def syn():
    #implement joint angle based on kinematic synergy
    shoulder_angle = 0
    elbow_angle = 0
    wrist_angle = 0

    shoulder = []
    elbow = []
    wrist = []
    x = []
    q = data.qpos
    v = data.qvel
    
    for t in range(3000):        
      shoulder_angle = np.pi / 180 * 60 * t /1500
      if t < 1500:
        a = 1
        b = 1
      else:
        a = -0.5
        b = -0.5
        
      elbow_angle = a * shoulder_angle
      wrist_angle = b * shoulder_angle     
   
      data.actuator(0).ctrl[:] = shoulder_angle
      data.actuator(2).ctrl[:] = elbow_angle
      data.actuator(4).ctrl[:] = wrist_angle
      mujoco.mj_step(model, data)
      view.sync()
      time.sleep(0.002)

    # x = np.linspace(-4, 4, 3000)
    # plt.plot(x, shoulder, color='blue', label='shoulder')
    # plt.plot(x, elbow, color="red", label='elbow')
    # plt.plot(x, wrist, color="green", label='wrist')
    # # plt.plot(x, q, color='blue', label='shoulder')
    # # plt.plot(x, elbow, color="red", label='elbow')
    # # plt.plot(x, wrist, color="green", label='wrist')
    
    # plt.show()

    # print(x)
    # print(shoulder_angle)
    # print(elbow_angle)
    # print(wrist_angle)
