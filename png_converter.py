import os
import time
import sys
import subprocess
import ensurepip

def install_pillow():
    try:
        import PIL
    except ImportError:
        print("Installing Pillow library...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

def install_pip():
    try:
        import pip
    except ImportError:
        print("Installing pip...")
        ensurepip.bootstrap()
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

install_pip()
install_pillow()

from tkinter import Tk, filedialog
from PIL import Image, UnidentifiedImageError

def main():
    while True:
        root = Tk()
        root.withdraw()
        print("Please select the image file.")
        file_path = filedialog.askopenfilename()

        if not file_path:
            print("Closing the program.")
            sys.exit()

        try:
            image = Image.open(file_path)
            _, ext = os.path.splitext(file_path)
            if not ext.lower() == ".png":
                new_file_path = os.path.splitext(file_path)[0] + ".png"
                image.save(new_file_path)
                print("Converted to PNG!")
                break
            else:
                print("The image is already in PNG format.")
                break
        except UnidentifiedImageError:
            print("Error: The file is not a valid image format. Please try again.")
        except Exception as e:
            print("Error:", str(e))

    time.sleep(1.5)

if __name__ == "__main__":
    main()
