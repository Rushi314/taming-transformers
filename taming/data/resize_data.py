import PIL
import os
from PIL import Image

os.system("mkdir /work/rdudhat_umass_edu/taming-transformers/data/flickr10k_segmentations_256")
fw = r'/work/rdudhat_umass_edu/taming-transformers/data/flickr10k_segmentations_256'
fr = r'/work/rdudhat_umass_edu/taming-transformers/data/flickr10k_segmentations'
for dirc in os.listdir(fr):
    if dirc in ['.DS_Store']:
        continue
    n_dirc = fw+'/'+dirc
    os.system("mkdir "+n_dirc)
    print(n_dirc)
    for file in os.listdir(fr+'/'+dirc):
        f_img_read = fr+'/'+dirc+"/"+file
        f_img_save = n_dirc+"/"+file
        img = Image.open(f_img_read)
        img = img.resize((256,256), Image.NEAREST)
        img.save(f_img_save)