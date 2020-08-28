#!/usr/bin/env python3

import os
import requests

image_dir = "supplier-data/images/"
url = "http://localhost/upload/"

imagelist = [x for x in os.listdir(image_dir) if x.lower().endswith("jpeg")]

for image in imagelist:
    image_path = os.path.join(image_dir, image)
    print("uploading image:", image_path)
    with open(image_path, "rb") as img:
        r = requests.post(url, files={'file': img})
        print(r)

