from bs4 import BeautifulSoup
import requests
import pyjson5
import time

page_list_url_template = 'https://esahubble.org/images/archive/category/galaxies/page/{}/'
page_single_image_template = "https://cdn.spacetelescope.org/archives/images/wallpaper1/{}.jpg"


thumbs = []
full_size = []

counter = 1
# get all links - thumbs and 1024x1024
for i in range(1,34):

    page = requests.get(page_list_url_template.format(i))
    soup = BeautifulSoup(page.text, "html.parser")

    page_images = soup.findAll('script')
    for image_obj in pyjson5.loads(page_images[0].string[13:-2]):
        idx = image_obj.get("id")
        thumb = image_obj.get("src")

        # download thumbs
        img_data = requests.get(thumb).content
        with open(f'thumbs/{idx}.jpg', 'wb') as handler:
            handler.write(img_data)
        time.sleep(0.2)
        # download 1024x1024
        fs_image_url = page_single_image_template.format(idx)
        img_data = requests.get(fs_image_url).content
        with open(f'full_size/{idx}.jpg', 'wb') as handler:
            handler.write(img_data)

        time.sleep(0.2)
        thumbs.append(thumb)
        full_size.append(fs_image_url)
        print(f"Pair of thumb-fullsize {counter}/1603 saved")
        counter += 1


# save (just in case)
with open("thumbs.txt", 'w') as f:
    for thumb in thumbs:
        f.write(thumb)
        f.write("\n")

with open("full_size.txt", 'w') as f:
    for fs in full_size:
        f.write(fs)
        f.write("\n")

