import os
from PIL import Image
import shutil
import math

TAMING_ROOT_READ = "/work/dagarwal_umass_edu/taming-transformers/"
TAMING_ROOT_WRITE = f"{os.path.abspath(os.path.dirname(__file__))}/../.."
print(TAMING_ROOT_WRITE)
# Parameters
SIZE = 256
PREFIX = "flickr10k" # "flickr10k"

if __name__ == "__main__":
    modes = ["images", "segmentations"]
    for mode in modes:
        dir = f"{PREFIX}_{mode}"
        dirw = f"{PREFIX}_crop_{mode}_{SIZE}"
        fr = os.path.join(TAMING_ROOT_READ, "data", dir)
        print(fr)
        print(f"Reading {dir}...")
        fw = os.path.join(TAMING_ROOT_WRITE, "data", dirw)
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
                img = Image.open(f_img_read)
                
                # Resize the image in the multiple of 256 dimentions
                width, height = img.size
                width = (math.ceil(width/256))*256
                height = (math.ceil(height/256))*256
                img = img.resize((width, height), Image.NEAREST)
                for i in range(width//256):
                    for j in range(height//256):
                        crop_filepath = os.path.join(fw_dirc, file+f"_{i}_{j}")
                        box = (i*256, j*256, (i+1)*256, (j+1)*256)
                        img2 = img.crop(box)
                        img2.save(crop_filepath+'.png')
                
    #shutil.copyfile(
    #    os.path.join(TAMING_ROOT, "data", f"{PREFIX}_examples.txt"),
    #    os.path.join(TAMING_ROOT, "data", f"{PREFIX}{SIZE}_cexamples.txt")
    #)
    print("Done")
