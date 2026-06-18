"""
Quantum Relativistic Simulation Index (QRSI) - Core Mathematical Operators.

This module houses the pure, deterministic physics operators used to simulate
time-dependent quantum wave packets interacting with Schwarzschild spacetime fields.
All functions operate natively on NumPy array structures.
"""

import numpy as np


def op_schwarzschild_metric(proximity_r: float) -> float:
    """Calculate the Schwarzschild metric time-dilation scaling factor.

    Math: alpha_g = sqrt(1 - (Rs / r))
    
    Args:
        proximity_r: Radial distance in units of the Schwarzschild radius (Rs).

    Returns:
        The scalar time-dilation factor (alpha_g). Values approach 0 at the horizon.
    """
    # Defensive programming: Gracefully intercept event horizon boundaries 
    # to avoid division by zero or imaginary roots during calculations.
    bounded_r = max(proximity_r, 1.0001)
    return float(np.sqrt(1.0 - (1.0 / bounded_r)))


def op_time_dilated_wave(
    time_grid: np.ndarray, 
    schwarz_factor: float, 
    base_length: float = 6.0, 
    base_freq: float = 0.4
) -> np.ndarray:
    """Generate a gravitationally warped quantum wave packet envelope.

    Math: psi(t) = exp(-0.5 * ((t - t_0) / (sigma / alpha_g))^2) * sin(2*pi * (f_0 * alpha_g) * t)

    Args:
        time_grid: Vector array representing the coordinated time domain slices.
        schwarz_factor: The alpha_g scaling factor from op_schwarzschild_metric.
        base_length: The initial spatial width (sigma) of the unwarped photon packet.
        base_freq: The initial carrier frequency (color) of the unwarped photon.

    Returns:
        A NumPy array containing the real probability amplitudes of the wave packet.
    """
    # General Relativity: Gravity stretches the wave in time (Dilation)
    # and compresses its oscillations (Redshift).
    dilated_length = base_length / (schwarz_factor + 1e-6)
    redshifted_frequency = base_freq * schwarz_factor
    
    # Dynamically locate the temporal center index of the grid array
    center_time = (time_grid[-1] - time_grid[0]) / 2.0
    
    # Compute the physical Gaussian envelope structure
    envelope = np.exp(-0.5 * ((time_grid - center_time) / dilated_length)**2)
    wave_profile = envelope * np.sin(2 * np.pi * redshifted_frequency * time_grid)
    
    return wave_profile


def op_fourier_chopping_gate(
    time_grid: np.ndarray, 
    wave_profile: np.ndarray, 
    blind_frequency: float
) -> np.ndarray:
    """Apply coaxial amplitude modulation via an aerodynamic shutter gate.

    Math: T(t) = 0.5 * (1.0 + sign(sin(2*pi * f_b * t)))
    
    Args:
        time_grid: Vector array representing the coordinated time domain slices.
        wave_profile: The input wave packet array to be operated on.
        blind_frequency: The mechanical chopping frequency of the louver blinds.

    Returns:
        The temporally sliced wave function array.
    """
    if blind_frequency <= 0.0:
        return wave_profile  # 0.0 frequency implies blinds remain locked flat/open
        
    # Generate a discrete square-wave matrix acting as an open/close filter array
    shutter_gating = 0.5 * (1.0 + np.sign(np.sin(2 * np.pi * blind_frequency * time_grid)))
    return wave_profile * shutter_gating


def op_bekenstein_hawking_entropy(
    current_frame: float, 
    max_frames: float, 
    initial_mass: float
) -> float:
    """Evaluate the thermodynamic entropy curve of an evaporating black hole.

    Math: S(t) = ( M(t) )^2 * 100 where M(t) follows a Stefan-Boltzmann decay profile.

    Args:
        current_frame: The active chronological index in the simulation ledger.
        max_frames: The maximum available timeframe allocations for the runtime block.
        initial_mass: The seed solar mass parameter of the black hole.

    Returns:
        The computed Bekenstein-Hawking entropy value in units of k_B.
    """
    # The total evaporation lifespan of a black hole scales with mass cubed (M^3)
    t_evap = max_frames * 0.8 * ((initial_mass / 5.0) ** 3)
    
    if current_frame < t_evap:
        # Mass decay calculation: M(t) = M_0 * (1 - t / t_evap)^(1/3)
        decay_progression = current_frame / t_evap
        mass_decay = initial_mass * ((1.0 - decay_progression) ** (1.0 / 3.0))
        # Bekenstein-Hawking entropy scales precisely with surface area (mass squared)
        entropy_val = (mass_decay ** 2) * 100.0
    else:
        entropy_val = 0.0  # Singularity has fully evaporated out of the coordinate grid
        
    return float(entropy_val)
