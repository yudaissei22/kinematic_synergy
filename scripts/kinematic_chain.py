import time
import mujoco
from mujoco import viewer
import numpy as np
import os

model = mujoco.MjModel.from_xml_path("../models/scene.xml")
data = mujoco.MjData(model)
view = viewer.launch_passive(model, data)

