import time
import mujoco
from mujoco import viewer
import numpy as np
import os
import matplotlib.pyplot as plt

model = mujoco.MjModel.from_xml_path("models/scene_simple_chain.xml")
# scene.xmlは、エージェントシステムのともやつと別にする。
data = mujoco.MjData(model)
view = viewer.launch_passive(model, data)


def create_trajectory:
    a_pos = np.zeros(500)
    b_pos = np.zeros(500)

    t_max = 2
    tr = 1 # リリースする時間

    init_pos = 0
    fin_pos =  pi / 4 # 45度
    # 角度の単位はrad

    vel = (fin_pos - init_pos) / tr
    

    # 角度列に代入していく

for i in range(1000): 
    if t < ta:
        data.actuator(0).ctrl[:] = a_pos
        data.actuator(1).ctrl[:] = b_pos
        
    elif t >= tr:
        data.actuator(0).ctrl[:] = 0

    mujoco.mj_step(model, data)
    view.sync()
    time.sleep(0.002)
