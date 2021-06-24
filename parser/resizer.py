import os
from PIL import Image

target_size = 1024, 1024
    
for file in os.listdir("../data/hubble/full_size"):
    im = Image.open(f"../data/hubble/full_size/{file}")
    squared = im.resize(target_size, Image.ANTIALIAS)
    squared.save(f"../data/hubble/squared/{file}")
