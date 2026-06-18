# quantum-relatavistic-engine
```text
quantum-relativistic-engine/
├── .github/
│   └── workflows/
│       ├── test-and-lint.yml      # Verifies math against matrix tolerances on pull requests
│       └── rolling-release.yml    # Triggers on tags/main merges, builds WASM, deploys GitHub Release
├── src/
│   ├── engine/
│   │   ├── __init__.py
│   │   └── core_math.py           # Pure QRSI mathematical operators (no UI dependencies)
│   └── web_app/
│       ├── index.html             # Unified cross-platform dashboard container
│       └── app.js                 # Pyodide/WASM initialization layer
├── tests/
│   └── test_operators.py          # Asserts Born's Rule and Lorentz normalization invariances
├── LICENSE                        # Standard open-source boilerplate (e.g., MIT or Apache 2.0)
└── README.md                      # Unified documentation entry point
```
# Quantum Relativistic Simulation Index (QRSI) Core Engine

A modular, cross-platform computational engine designed to simulate time-dependent quantum wave packets traversing general relativistic Schwarzschild horizons.

## 🔬 Theoretical Foundations & Mathematical Synopsis

### 1. Coaxial Slicing Mechanics (Temporal Amplitude Modulation)
Rather than dividing wave functions across spatial coordinates, this model forces an interaction within a single spatial point over a discrete timeline grid. The introduction of high-frequency aerodynamic blinds creates an open/closed square gate profile $T(t)$, clipping the wave's duration ($\Delta t$) and forcing spectral broadening via the **Fourier Time-Energy Uncertainty Principle**:
$$\Delta E \cdot \Delta t \ge \frac{\hbar}{2}$$

### 2. Gravitational Warping & Thermal Redshift
As the photon approaches a black hole's Schwarzschild boundary ($R_s$), it undergoes coordinate stretching and cooling driven by the temporal tensor component of the metric:
$$\alpha_g = \sqrt{1 - \frac{R_s}{r}}$$
This forces an exponential freeze of the wave's envelope velocity paired with severe **Gravitational Redshift**, shifting the escaping photon wavelengths along a thermodynamic Planck blackbody curve.

---

## 💻 Code Architecture & Component Breakdown

The engine architecture is split into three decoupled operational primitives located within `src/engine/core_math.py`:

*   **`op_schwarzschild_metric(proximity_r)`**: Resolves local space-time dilation scalars relative to the target event horizon coordinate footprint.
*   **`op_time_dilated_wave(time_grid, schwarz_factor)`**: Evaluates the general relativistic stretching and frequency shifts of the wave envelope.
*   **`op_fourier_chopping_gate(time_grid, wave_profile, blind_frequency)`**: Simulates temporal slicing, generating the multi-color interference profiles.

---

## 📊 Demonstrated Aspects per Graphical Output

When executed via the unified cross-platform dashboard, the system exposes three real-time diagnostic outputs:

### 🌈 Output 1: Transmitted Frequency Spectrum (Fourier View)
*   **Demonstrated Aspect**: Displays the physical **Color Shift** of the photon.
*   **Analytical Metric**: As the chopping frequency increases, the central single-frequency spike broadens into distinct sidebands, mapping how energy breaks apart during temporal diffraction.

### ⏳ Output 2: Time-Domain Probability Envelope
*   **Demonstrated Aspect**: Tracks the wave-particle superposition shape before and after interacting with observers.
*   **Analytical Metric**: Captures the temporal stretching caused by gravity. If an active camera forces a localized capture, this entire envelope collapses instantly into a single coordinate point.

### 📉 Output 3: Bekenstein-Hawking Entropy Curve
*   **Demonstrated Aspect**: Tracks the thermodynamic life cycle and mass decay of the gravitational source over time.
*   **Analytical Metric**: Illustrates **Time Reversibility**. When you execute a reverse playback command, the system retrieves past historical coordinates from the time-ledger log buffer, allowing users to watch a collapsed particle expand back into a coherent wave function while entropy climbs back up the slope.
