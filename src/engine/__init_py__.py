"""
Quantum Relativistic Simulation Index (QRSI) Core Engine Package.

This module initializes the core mathematical primitives, making them accessible
directly from the top-level package namespace while shielding external tools 
from internal file configurations.
"""

# Explicitly import operators from your internal file
from .core_math import (
    op_schwarzschild_metric,
    op_time_dilated_wave,
    op_fourier_chopping_gate,
    op_bekenstein_hawking_entropy,
)

# Define exactly what gets exported when someone runs 'from src.engine import *'
__all__ = [
    "op_schwarzschild_metric",
    "op_time_dilated_wave",
    "op_fourier_chopping_gate",
    "op_bekenstein_hawking_entropy",
]

# Structural package metadata for your GitHub Rolling Release ledger
__version__ = "1.0.0"
__author__ = "Quantum Relativistic Simulation Index Architecture Group"
