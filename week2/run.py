#!/usr/bin/env python3

import os
import requests

feedback_dir = "/data/feedback"
txtfiles = os.listdir(feedback_dir)
print(txtfiles, "\n")

url = "http://34.69.101.55/feedback/"

for fname in txtfiles:
    with open(os.path.join(feedback_dir, fname), "r") as f:
        content_dict = {
                "title" : f.readline().strip(),
                "name" : f.readline().strip(),
                "date" : f.readline().strip(),
                "feedback" : ' '.join([line.strip() for line in f.readlines()])
                }
        print(content_dict, "\n")
        response = requests.post(url, json=content_dict)
        print(response)

