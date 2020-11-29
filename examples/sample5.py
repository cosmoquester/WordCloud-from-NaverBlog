"""
Make WordCloud with shapes you want
"""
from nbclouder import Clouder
from PIL import Image
import numpy as np

# Fill parameters properly
naver_id = ""

# Make ping shaped mask
icon = Image.open("examples/pig.png")
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)

clouder = Clouder(naver_id)
clouder.fire(["전체글"], "word_cloud.png", "/Library/Fonts/Arial Unicode.ttf", mask=mask)
