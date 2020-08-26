#!/usr/bin/env python3

import os
from PIL import Image

dirname = "supplier-data/images"
filelist = [f for f in os.listdir(dirname) if f.endswith("tiff")]
#os.mkdir("converted")

for fname in filelist:
    print("Converting file:", fname)
    im = Image.open(os.path.join(dirname, fname))
    print(im)
    im.convert("RGB").resize((600, 400)).save(os.path.join(dirname, os.path.splitext(fname)[0]+".jpeg"), format="jpeg")

