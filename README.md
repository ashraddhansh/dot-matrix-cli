# Dot Matrix CLI

`dot-matrix-cli` is a terminal-based ASCII art generator built to explore how images are represented, processed, and transformed into text. The project started as a way to understand the lower-level mechanics behind image processing rather than relying on high-level libraries.

The implementation intentionally stays lightweight and minimal while building core functionality from scratch where possible.

Built with:

- NumPy
- Pillow (PIL)

## Features

- Colorized ASCII output using ANSI truecolor terminal sequences
- Minimal and detailed character ramps
- Sobel-based edge detection
- Edge-only rendering mode
- Edge-enhanced rendering (blend edge information with brightness mapping)
- Adaptive quantile-based brightness distribution
- Character brightness inversion
- Automatic terminal-aware output sizing
- Lightweight implementation with minimal dependencies

# Working

The edge detection implementation uses the Sobel operator and supports both:
- pure edge rendering
- blending edge strength into normal brightness mapping

Character mapping can use either:
- fixed linear bins
- adaptive quantile-based bins based on image brightness distribution

This helps improve detail for images with uneven brightness distributions.

## Features Yet to Be Implemented

- [ ] Custom character ramps
- [ ] Automatic sorting of custom ramps based on character ink coverage
- [ ] Improved edge enhancement pipeline
- [ ] thresholding
- [ ] blur before Sobel
- [ ] edge weighting controls
- [ ] Configurable brightness/edge blending ratios
- [ ] Better terminal dimension handling
- [ ] Output width/height flags
- [ ] Save ASCII output to file
- [ ] More rendering presets
- [ ] Additional edge detection methods
- [ ] Performance improvements for Sobel processing
- [ ] Custom themes
