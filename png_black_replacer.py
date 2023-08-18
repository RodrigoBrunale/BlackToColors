import os
import subprocess
from PIL import Image

# Updated color definitions remain the same...

def replace_black_dynamic_size(directory=None):
    # If no directory is provided, use the current directory where the script is running
    if directory is None:
        directory = os.getcwd()

    transparent_filter = "colorkey=0x000000:0.1:0.0"

    # Create folders if they don't exist
    originals_folder = os.path.join(directory, "originals")
    transparent_folder = os.path.join(directory, "transparent")
    os.makedirs(originals_folder, exist_ok=True)
    os.makedirs(transparent_folder, exist_ok=True)

    # Move all PNGs in the main directory to the originals folder (if not already there)
    for filename in os.listdir(directory):
        if filename.endswith(".png") and not filename.startswith("tmp_"):
            os.rename(
                os.path.join(directory, filename),
                os.path.join(originals_folder, filename)
            )

    # Process each PNG in the originals folder
    for filename in os.listdir(originals_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(originals_folder, filename)

            # Get the resolution of the current image
            with Image.open(input_path) as img:
                width, height = img.size
            
            # Create transparent image
            output_transparent = os.path.join(transparent_folder, filename)
            cmd_transparent = ["ffmpeg", "-i", input_path, "-vf", transparent_filter, output_transparent]
            subprocess.run(cmd_transparent)

            # For each color, overlay the transparent image over the color background
            for color_name, hex_code in COLORS_UPDATED.items():
                color_folder = os.path.join(directory, f"{color_name} - {hex_code}")
                os.makedirs(color_folder, exist_ok=True)

                background_path = os.path.join(directory, f"tmp_{color_name}.png")
                output_path = os.path.join(color_folder, filename)

                # Create solid color background using the image's resolution
                cmd_background = ["ffmpeg", "-f", "lavfi", "-i", f"color=c=0x{hex_code}:s={width}x{height}", "-frames:v", "1", background_path]
                subprocess.run(cmd_background)

                # Overlay the transparent image over the color background
                cmd_color = ["ffmpeg", "-i", background_path, "-i", output_transparent, "-filter_complex", "[0:v][1:v]overlay", output_path]
                subprocess.run(cmd_color)

                # Clean up the temporary background file
                os.remove(background_path)

    print("Images processed and saved in respective folders!")

# Call the function without any arguments to use the current directory
replace_black_dynamic_size()
