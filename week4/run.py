#!/usr/bin/env python3

import os
import requests
import json

descriptions_dir = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

def get_fruit_data():

    fruits = []

    for descfile in os.listdir(descriptions_dir):
        filepath = os.path.join(descriptions_dir, descfile)
        with open(filepath) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            fruit = {}
            fruit["name"] = content[0]
            fruit["weight"] = content[1].strip(" lbs")
            fruit["description"] = content[2]
            fruit["image_name"] = descfile.strip(".txt") + ".jpeg"
            fruits.append(fruit)

    return fruits

if __name__ == "__main__":

    for fruit in get_fruit_data():
        print(fruit, "\n")
        r = requests.post(url, json=fruit)
        print(r.request.url)
        print(r.status_code)

