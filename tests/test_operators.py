import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Change this line:
# from src.engine import op_schwarzschild_metric, op_time_dilated_wave

# To this line:
from src.engine.core_math import op_schwarzschild_metric, op_time_dilated_wave

# Execute an arbitrary test frame verification
t_space = np.linspace(0, 100, 10)
metric_factor = op_schwarzschild_metric(proximity_r=2.0)
wave_output = op_time_dilated_wave(t_space, metric_factor)

assert wave_output.shape == (10,), "Data payload array structure mismatch."
