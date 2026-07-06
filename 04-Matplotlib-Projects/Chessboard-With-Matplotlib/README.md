# Chess Board Pattern with Python

A Python program that creates a chess board pattern with a mathematical function overlay using Matplotlib.

## How It Works

The program generates two layers:
1. **Chess Board**: A checkerboard pattern created using modulo operations
2. **Function Overlay**: A mathematical function `(1 - x/2 + x⁵ + y⁶) * e^(-(x² + y²))` overlaid on the chess board

Both layers are combined using transparency (alpha) to create the final visualization.

## Requirements

- Python 3.x
- Matplotlib
- NumPy
