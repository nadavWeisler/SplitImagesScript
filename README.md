# SplitImagesScript

## Image Splitting Script

This script provides functionality to split images into two equal parts, either horizontally or vertically.

## Usage

```python
from split_images import split_images

# Split images horizontally (left/right)
split_images("input_folder", "output_folder", split_type="h")

# Split images vertically (top/bottom)
split_images("input_folder", "output_folder", split_type="v")
```

## Features

- Process all images in the input folder (.png, .jpg, .jpeg, .bmp, .gif)
- Create two new images for each input image
- Save the split images in the output folder with appropriate suffixes
  - `_left/_right` for horizontal splits
  - `_top/_bottom` for vertical splits

## Requirements

- Pillow (PIL) library

## How to Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
