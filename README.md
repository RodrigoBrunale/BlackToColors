
# Colorful Image Transformations 🎨🖼️

Welcome to the wonderful world of image color transformations! This script magically turns those pesky black pixels in your images into an array of delightful colors (or even transparent if you're feeling fancy).

## Table of Contents
- [About the Project](#about-the-project)
- [Design Choices](#design-choices)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Fun Fact](#fun-fact)

## About the Project

Have you ever looked at an image and thought, "I wish the black in this picture was a pastel blue... or red... or transparent!"? Look no further! This Python script uses the power of FFmpeg to replace black pixels in PNG images with a chosen set of colors or even make them transparent. The script is flexible, user-friendly, and ready for you to experiment with.

## Design Choices

1. **Why FFmpeg?** We chose FFmpeg because it's a powerful tool for handling multimedia data. It provides a vast array of capabilities, which made it perfect for our image transformation needs.
2. **Directory Management**: To keep things tidy, the script creates directories for each color transformation. Originals are tucked safely in their own folder, ensuring they remain pristine.
3. **Flexibility**: We've set up a COLORS dictionary, allowing you to easily add or remove colors as you see fit. This makes customizing the output a breeze.
4. **Dark Pastel Colors**: After some deliberation (and some handy feedback), we realized that since we're replacing black, the new colors should be closer to black for the details in the images to pop. So, we went with darker shades which, while being closer to black, still retain a hint of color.

## Getting Started

### Prerequisites

- Ensure you have FFmpeg installed. If you haven't, you can get it [here](https://ffmpeg.org/download.html).
- This script is written in Python. Make sure you have Python installed.

### Usage

1. Place your PNG images in the same directory as the script.
2. Run the script:
   ```bash
   png_black_replacer.py
   ```
3. Watch as directories spring into existence, each containing your images transformed with delightful new colors!
4. If you want to add or modify colors, simply adjust the `COLORS` dictionary in the script. You can even comment out any color if you wish to skip it.

## Fun Fact

Did you know? The human eye can detect approximately 10 million different colors. With this script, you're one step closer to seeing them all! 🌈
