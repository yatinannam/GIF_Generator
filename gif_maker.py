import os
from PIL import Image

def create_gif(input_folder, output_file, duration=200, loop=0):
    """
    Create a looping GIF from images in a folder.
    """
    frames = []
    for file in sorted(os.listdir(input_folder)):
        if file.endswith((".png", ".jpg", ".jpeg")):
            filepath = os.path.join(input_folder, file)
            img = Image.open(filepath).convert("RGB")
            frames.append(img)

    if not frames:
        print("No images found in the folder.")
        return

    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop
    )
    print(f"GIF saved as {output_file}")


if __name__ == "__main__":
    create_gif("frames", "output.gif", duration=150, loop=0)
