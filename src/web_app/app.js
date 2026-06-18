// Global App Configuration Configurations
let pyodideInstance = null;
let waveChartObj = null;
let entropyChartObj = null;
let simulationLedger = []; // Time buffer caching frames for time-reversal play
let currentLedgerIndex = 0;
let isReversing = false;

// Core Python Mathematical Logic injected into the browser runtime string footprint
const pythonEngineSource = `
import numpy as np

def run_frame_pipeline(mass, prox_r, blind_f, frame, max_frames=150):
    time_grid = np.linspace(0, 100, 300)
    
    # 1. Execute Schwarzschild metric calculation
    bounded_r = max(prox_r, 1.0001)
    schwarz_factor = float(np.sqrt(1.0 - (1.0 / bounded_r)))
    
    # 2. Compute Wave Equation expansion profile
    dilated_length = 6.0 / (schwarz_factor + 1e-6)
    redshifted_freq = 0.4 * schwarz_factor
    center_time = (time_grid[-1] - time_grid) / 2.0
    envelope = np.exp(-0.5 * ((time_grid - center_time) / dilated_length)**2)
    wave_profile = envelope * np.sin(2 * np.pi * redshifted_freq * time_grid)
    
    # 3. Apply chopping gate modulations
    if blind_f > 0.0:
        shutter_state = 0.5 * (1.0 + np.sign(np.sin(2 * np.pi * blind_f * time_grid)))
        wave_profile *= shutter_state
        
    # 4. Process Bekenstein-Hawking Entropy Curve decay values
    t_evap = max_frames * 0.8 * ((mass / 5.0) ** 3)
    if frame < t_evap:
        mass_decay = mass * ((1.0 - (frame / t_evap)) ** (1.0 / 3.0))
        entropy_val = (mass_decay ** 2) * 100.0
    else:
        entropy_val = 0.0
        
    return time_grid.tolist(), (wave_profile**2).tolist(), float(entropy_val), float(schwarz_factor)
`;

// Initialize Charts on DOM Load
function initializeCharts() {
    const ctxWave = document.getElementById('waveChart').getContext('2d');
    waveChartObj = new Chart(ctxWave, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Quantum Wave Probability Density ($|\\psi|^2$)', data: [], borderColor: '#2dd4bf', backgroundColor: 'rgba(45, 212, 191, 0.1)', fill: true, borderWidth: 1.5, pointRadius: 0 }] },
        options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0, max: 1.1 } } }
    });

    const ctxEntropy = document.getElementById('entropyChart').getContext('2d');
    entropyChartObj = new Chart(ctxEntropy, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Bekenstein-Hawking Entropy ($S_{BH}$)', data: [], borderColor: '#f87171', borderWidth: 2, pointRadius: 0 }] },
        options: { responsive: true, maintainAspectRatio: false }
    });
}

// Instantiate Pyodide Environment
async function bootstrapWasmEngine() {
    initializeCharts();
    const logger = document.getElementById('telemetryBox');
    
    try {
        logger.value = "⏳ Initializing WebAssembly Virtual Runtime...\n";
        pyodideInstance = await loadPyodide();
        logger.value += "📦 Compiling Numerical Libraries (NumPy)...\n";
        await pyodideInstance.loadPackage("numpy");
        
        // Execute and mount the pure mathematical string logic onto the Python engine space
        await pyodideInstance.runPythonAsync(pythonEngineSource);
        
        logger.value += "🚀 System Core Active. Ready for processing loops.";
        const runBtn = document.getElementById('runBtn');
        runBtn.innerText = "⚡ Fire Simulation Sequence";
        runBtn.disabled = false;
    } catch (err) {
        logger.value = `❌ Boot Failure: ${err.message}`;
    }
}

// Execute Full Core Lifecycle Loop and Store to Timeline Array Matrix Ledger
async function compileFullLifecycle() {
    if (isReversing) return;
    const logger = document.getElementById('telemetryBox');
    logger.value = "🛰️ Regenerating frame matrix logs...";
    
    const mass = parseFloat(document.getElementById('massSlider').getVal || document.getElementById('massSlider').value);
    const prox = parseFloat(document.getElementById('proxSlider').value);
    const freq = parseFloat(document.getElementById('freqSlider').value);
    
    simulationLedger = []; // Reset time ledger cache
    const totalFrames = 150;
    
    // Map frame metrics sequentially into memory array
    for (let f = 0; f < totalFrames; f++) {
        let result = pyodideInstance.globals.get('run_frame_pipeline')(mass, prox, freq, f);
        let jsArray = result.toJs();
        
        simulationLedger.push({
            frame: f,
            timeGrid: jsArray[0],
            waveProfile: jsArray[1],
            entropy: jsArray[2],
            schwarzFactor: jsArray[3]
        });
    }
    
    currentLedgerIndex = totalFrames - 1; // Park pointer at final point of collapse
    document.getElementById('reverseBtn').disabled = false;
    renderTargetFrame(currentLedgerIndex);
}

// Render a Specifc Logged Frame Coordinate Asset
function renderTargetFrame(index) {
    const data = simulationLedger[index];
    const logger = document.getElementById('telemetryBox');
    
    logger.value = `⏱️ Timeline Frame Pointer: ${index}/149\n` +
                   `📏 Dilation Factor (alpha_g): ${data.schwarzFactor.toFixed(4)}\n` +
                   `📉 Current Entropy: ${data.entropy.toFixed(2)} kB\n` +
                   `📊 Mode: ${index >= 90 ? "⚠️ PARTICLE COLLAPSE PROFILE" : "🌊 COHERENT WAVE FIELD"}`;
                   
    // Update Graph Objects
    waveChartObj.data.labels = data.timeGrid.map(t => t.toFixed(1));
    waveChartObj.data.datasets[0].data = data.waveProfile;
    waveChartObj.update('none'); // Update smoothly without canvas resets

    // Graph the overall cumulative metrics curve profile up to the current needle index
    entropyChartObj.data.labels = simulationLedger.slice(0, index + 1).map(d => d.frame);
    entropyChartObj.data.datasets[0].data = simulationLedger.slice(0, index + 1).map(d => d.entropy);
    entropyChartObj.update('none');
}

// Reverse Playback VCR Loop Architecture
function executeReverseLoop() {
    if (!isReversing || currentLedgerIndex <= 0) {
        isReversing = false;
        document.getElementById('reverseBtn').innerText = "⏪ Play Reverse Log";
        return;
    }
    currentLedgerIndex--;
    renderTargetFrame(currentLedgerIndex);
    setTimeout(executeReverseLoop, 40); // 40ms interval yields a steady 25 FPS update profile
}

// Client-Side CSV Exporter Module
function exportLedgerToCSV() {
    if (simulationLedger.length === 0) return;
    let csvContent = "data:text/csv;charset=utf-8,Frame,Entropy,SchwarzFactor\n";
    simulationLedger.forEach(row => {
        csvContent += `${row.frame},${row.entropy},${row.schwarzFactor}\n`;
    });
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "qrsi_entropy_time_log.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Event Bindings Mapping
document.getElementById('runBtn').addEventListener('click', compileFullLifecycle);
document.getElementById('exportBtn').addEventListener('click', exportLedgerToCSV);
document.getElementById('reverseBtn').addEventListener('click', () => {
    if (isReversing) {
        isReversing = false;
    } else {
        isReversing = true;
        document.getElementById('reverseBtn').innerText = "⏸ Pause Rewind";
        executeReverseLoop();
    }
});

// Bootstrap Initialization
window.onload = bootstrapWasmEngine;
