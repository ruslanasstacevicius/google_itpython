#!/usr/bin/env python3

import os
from PIL import Image

filelist = [f for f in os.listdir("images") if f.endswith("48dp")]
#os.mkdir("converted")

for fname in filelist:
    print("Converting file:", fname)
    im = Image.open(os.path.join("images", fname))
    im.rotate(90).resize((128, 128)).convert("RGB").save(os.path.join("converted", fname), format="jpeg")

