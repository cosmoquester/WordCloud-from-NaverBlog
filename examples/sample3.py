"""
You can save and load frequencies.
"""
from nbclouder import Clouder

# Fill parameters properly
naver_id = ""
categoryNo = 0
par_categoryNo = 0
font_path = "/Library/Fonts/Arial Unicode.ttf"

clouder = Clouder(naver_id, categoryNo, par_categoryNo)
_, word_frequency, *_ = clouder.fire("word_cloud.png", font_path)
# Then 'word_cloud.png' is saved

# Save word frequencies
with open("word_freq.txt", "w", encoding="utf-8") as f:
    f.write(repr(word_frequency))

# Load word frequencies
with open("word_freq.txt", "r", encoding="utf-8") as f:
    word_frequency = eval(f.read())
    word_cloud = clouder.make_cloud("word_cloud2.png", word_frequency, font_path)
