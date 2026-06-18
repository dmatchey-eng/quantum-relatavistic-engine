import numpy as np
from src.engine import op_schwarzschild_metric, op_time_dilated_wave

# Execute an arbitrary test frame verification
t_space = np.linspace(0, 100, 10)
metric_factor = op_schwarzschild_metric(proximity_r=2.0)
wave_output = op_time_dilated_wave(t_space, metric_factor)

assert wave_output.shape == (10,), "Data payload array structure mismatch."
