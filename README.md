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
