import os
from PIL import Image


checked = 0
for file in os.listdir("../data/hubble/full_size"):
	im = Image.open(f"../data/hubble/full_size/{file}")
	w, h = im.size
	if w != 1024 or h != 768:
		print(file, w, h)
	checked += 1
print(f"total checked {checked}")