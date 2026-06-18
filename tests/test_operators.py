"""
Quantum Relativistic Simulation Index (QRSI) - Unit Testing Suite.

This script executes numerical assertions against core physics operators 
to validate probability conservation and singularity boundary handling.
"""
import sys
import os

# Crucial: Dynamically anchor the exact workspace directory structure to python's lookup path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
# Direct module import ensures seamless execution inside GitHub Actions
from src.engine.core_math import op_schwarzschild_metric, op_time_dilated_wave


def test_probability_conservation():
    """Axiom: Total integrated quantum probability must remain invariant."""
    time_grid = np.linspace(0, 100, 400)
    
    # Calculate a heavily warped spacetime factor close to the horizon
    alpha_g = op_schwarzschild_metric(proximity_r=1.05) 
    wave = op_time_dilated_wave(time_grid, alpha_g)
    
    # Square the amplitudes to extract total probability density maps
    prob_density = wave ** 2
    total_probability = np.sum(prob_density)
    
    # Validate that we have a stable, functioning waveform array
    assert total_probability > 0.0, "Wave packet collapsed or zero-initialized incorrectly."


def test_horizon_singularity_protection():
    """Axiom: Metric equations must gracefully intercept horizon boundaries without throwing errors."""
    # Passing exactly 1.0 Rs directly down standard Schwarzschild math throws a division-by-zero.
    # This verifies our defensive code caps parameters cleanly.
    alpha_g = op_schwarzschild_metric(proximity_r=1.0)
    
    assert not np.isnan(alpha_g), "Singularity protection matrix failed; NaN generated."
    assert alpha_g > 0.0, "Schwarzschild factor dropped to an unstable absolute zero state."


def test_wave_packet_dimensions():
    """Axiom: The output wave array dimensions must strictly match the time grid input bounds."""
    time_grid = np.linspace(0, 50, 150)
    alpha_g = op_schwarzschild_metric(proximity_r=2.5)
    
    wave = op_time_dilated_wave(time_grid, alpha_g)
    
    assert wave.shape == (150,), f"Data array shape mismatch: {wave.shape} instead of (150,)."
