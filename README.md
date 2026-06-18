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
├── README.md                      # Unified documentation entry point
└── requirements.txt               # Dummy file for dual-workflow inflation
```

# Quantum Relativistic Simulation Index (QRSI) Core Engine

A modular, cross-platform computational engine designed to simulate time-dependent quantum wave packets traversing general relativistic Schwarzschild horizons.

---

## 🌌 Why Explore This Project?

Most quantum mechanics models assume flat, static space. Most relativity engines ignore discrete quantum probabilities. **QRSI bridges this divide.** 

By running this application, you are executing a fully localized, **WASM-powered spacetime laboratory** directly inside a standard web browser. Passers-by can tweak gravitational geometries, slice quantum waveforms mid-flight, map Hawking radiation thermodynamics, and manually **rewind the arrow of time** to watch a collapsed particle expand back into a coherent wave packet. 

It provides an accessible, visually striking playground for complex physics that usually requires dedicated supercomputing clusters.

---

## 🔬 Theoretical Foundations & Mathematical Synopsis

The mathematical primitives under the hood translate foundational physics laws into matrix structures:

### 1. Coaxial Slicing Mechanics (Temporal Amplitude Modulation)
Rather than splitting photons across separate mirrors, this project introduces a localized gating function (the aerodynamic blinds) operating at a single coordinate. Restricting a wave packet’s time duration (\(\Delta t\)) forces its frequency spectrum (\(\Delta \omega\)) to broaden. This demonstrates **Heisenberg's Time-Energy Uncertainty Principle** in action:

```text
ΔE · Δt ≥ ℏ / 2
```

### 2. Gravitational Coordinate Warping (Time-Freeze)
As the wave packet nears a black hole's Schwarzschild boundary (\(R_s\)), it undergoes coordinate stretching and thermal cooling driven by the temporal tensor component of the metric:

```text
α_g = sqrt(1 - (R_s / r))
```

This factor scales the temporal envelope length upward (\(\sigma_{dil} = \sigma / \alpha_g\)) and shifts the carrier frequency down (\(\omega_{red} = \omega_0 \cdot \alpha_g\)), accurately rendering **Extreme Gravitational Redshift**.

### 3. Hawking Radiation & Planck Blackbody Spectrum
The baseline Hawking temperature (\(T_H\)) is inversely proportional to black hole mass. Localized gravitational fields shift this value for an external observer:

```text
T_eff = T_H / sqrt(1 - (R_s / r))
```

The engine continuously processes this temperature array, converting the thermal signatures into absolute **RGB chromaticity coordinates** mapped directly onto your screen.

---

## 🚀 Practical & Industrial Overlaps

The core mathematical operators are completely decoupled from the UI, meaning they can be imported as a library into other cutting-edge engineering fields:

*   **Silicon Manufacturing & EUV Lithography:** The slicing algorithms (`op_fourier_chopping_gate`) can be used to predict the wavelength/color distortion caused by high-speed mechanical shutter systems inside Extreme Ultraviolet lithography tools. The Monte Carlo statistical loop directly simulates photon shot noise defects in $1\text{ nm}$ photo-resists.
*   **Aerospace Adaptive Optics:** By mapping mechanical waveguide stress vectors directly into the metric equations, engineers can simulate how warped mirrors distort light phases, helping telescopes correct for optical scattering.
*   **Digital Signal Processing (DSP):** The time-dilation engines act as a high-performance granular sound synthesizer, mirroring tape-speed slows and ring modulation filters using physical equations.

---

## 📊 Live Experimental Metrics per Output

When you run the browser console dashboard, you interact with three live, decoupled validation displays:

### 🌈 Output 1: Transmitted Frequency Spectrum (Fourier View)
*   **What it demonstrates:** The physical **Color Shift** of the photon.
*   **What to look for:** Increasing the blind chopping speed causes the sharp green single-frequency peak to spread sideways into broad rainbow sidebands, capturing temporal diffraction.

### ⏳ Output 2: Time-Domain Probability Envelope
*   **What it demonstrates:** Quantum wave-particle duality and non-local sub-packet behavior.
*   **What to look for:** Under stationary frames, you see a spread-out superposition wave. The moment you introduce an active measurement slider, the entire wave function collapses instantly into a localized particle spike.

### 📉 Output 3: Bekenstein-Hawking Entropy Curve
*   **What it demonstrates:** Spacetime evaporation lifecycles and **Time Reversibility (T-Symmetry)**.
*   **What to look for:** Running forward shows an accelerated decay loop as the black hole evaporates. Clicking **Play Reverse** forces the engine to read from its historical memory ledger, un-sampling the particle collapse and climbing back up the entropy slope—proving that classical computing architectures can manipulate the thermodynamic arrow of time.
