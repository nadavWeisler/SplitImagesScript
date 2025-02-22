import os
from PIL import Image

def split_images(input_folder, output_folder, split_type="left-right"):
    """
    Splits all images in the input_folder based on the specified split type and saves them in output_folder.

    Args:
        input_folder (str): Path to the folder containing images.
        output_folder (str): Path to the folder where split images will be saved.
        split_type (str): "left-right" for vertical split, "up-down" for horizontal split.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            width, height = img.size

            base_name, ext = os.path.splitext(filename)

            if split_type == "left-right":
                # Left half
                left_half = img.crop((0, 0, width // 2, height))
                left_half_path = os.path.join(output_folder, f"{base_name}_left{ext}")
                left_half.save(left_half_path)

                # Right half
                right_half = img.crop((width // 2, 0, width, height))
                right_half_path = os.path.join(output_folder, f"{base_name}_right{ext}")
                right_half.save(right_half_path)

                print(f"Processed: {filename} -> {left_half_path}, {right_half_path}")

            elif split_type == "up-down":
                # Top half
                top_half = img.crop((0, 0, width, height // 2))
                top_half_path = os.path.join(output_folder, f"{base_name}_top{ext}")
                top_half.save(top_half_path)

                # Bottom half
                bottom_half = img.crop((0, height // 2, width, height))
                bottom_half_path = os.path.join(output_folder, f"{base_name}_bottom{ext}")
                bottom_half.save(bottom_half_path)

                print(f"Processed: {filename} -> {top_half_path}, {bottom_half_path}")

            else:
                print(f"Invalid split type: {split_type}")

if __name__ == "__main__":
    input_folder = "input_images"  # Change this to your folder containing images
    output_folder = "output_images"  # Folder where split images will be saved
    split_type = input("Enter split type ('left-right' or 'up-down'): ").strip().lower()

    split_images(input_folder, output_folder, split_type)
