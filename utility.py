import os
from PIL import Image

def rename_type(path:str, new_type:str) -> str:
    path_parts = path.split('.')
    path_notype = ""
    for i in range(0, len(path_parts)-2):
        path_notype += path_parts[i]

    return path_notype + '.' + new_type

def png2jpg(path:str, keepOriginal:bool=True) -> None:
    try:
        new_path:str =  rename_type(path, "jpg")
        png_image:Image = Image.open(path)
        jpg_image:Image = png_image.convert("RGC")

        jpg_image.save(new_path)
        png_image.close()
        if not keepOriginal:
            os.remove(path)

    except Exception as e:
        print(f"Error in png2jpg: {e}")

def jpg2png(path:str, keepOriginal:bool=True) -> None:
    try:
        new_path:str = rename_type(path, "png")
        jpg_image:Image = Image.open(path)
        jpg_image.save(new_path)
        jpg_image.close()
        if not keepOriginal:
            os.remove(path)
    
    except Exception as e:
        print(f"Error in jpg2png: {e}")