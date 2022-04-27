import os
from PIL import Image
import shutil

TAMING_ROOT = f"{os.path.abspath(os.path.dirname(__file__))}/../.."
# Parameters
SIZE = 256
PREFIX = "flickr10k"

if __name__ == "__main__":
    modes = ["images", "segmentations"]
    for mode in modes:
        dir = f"{PREFIX}_{mode}"
        dirw = f"{PREFIX}{SIZE}_{mode}"
        fr = os.path.join(TAMING_ROOT, "data", dir)
        print(f"Reading {dir}...")
        fw = os.path.join(TAMING_ROOT, "data", dirw)
        os.makedirs(fw, exist_ok=True)
        for dirc in os.listdir(fr):
            if dirc in ['.DS_Store']:
                continue
            fw_dirc = os.path.join(fw, dirc)
            os.makedirs(fw_dirc, exist_ok=True)
            print(fw_dirc)
            fr_dirc = os.path.join(fr, dirc)
            for file in os.listdir(fr_dirc):
                f_img_read = os.path.join(fr_dirc, file)
                f_img_save = os.path.join(fw_dirc, file)
                img = Image.open(f_img_read)
                img = img.resize((256, 256), Image.NEAREST)
                img.save(f_img_save)
    shutil.copyfile(
        os.path.join(TAMING_ROOT, "data", f"{PREFIX}_examples.txt"),
        os.path.join(TAMING_ROOT, "data", f"{PREFIX}{SIZE}_examples.txt")
    )
    print("Done")
