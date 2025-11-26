# Visualization Example

This repository contains a small Python script that creates a simple bar-chart visualization showing allowed HTTP methods per protocol.
The chart is written directly to an SVG file so it does not require any third-party libraries or frameworks.

## Files
- `visualization.py` — Generates the SVG bar chart using the standard library.
- `visualization.svg` — Output image produced by the script.
- `index.html` — Simple, responsive page that centers and displays the SVG visualization.

## How to run
1. Ensure you have Python 3 available.
2. Execute the script:
   ```bash
   python visualization.py
   ```
3. Open `index.html` in your browser to view the visualization with responsive styling (or open `visualization.svg` directly). The HTML page will display the latest SVG written by the script, so rerun the command above whenever you update the data.
