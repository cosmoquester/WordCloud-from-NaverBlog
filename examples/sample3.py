"""
You can save and load frequencies.
"""
from nbclouder import Clouder

# Fill parameters properly
naver_id = ""
categoryNo = 0
par_categoryNo = 0

clouder = Clouder(naver_id, categoryNo, parameters)
_, word_frequency, *_ = clouder.fire("word_cloud.jpg", "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.jpg' is saved

# Save word frequencies
with open("word_freq.txt", "w", encoding="utf-8") as f:
    f.write(repr(word_frequency))

# Load word frequencies
with open("word_freq.txt", "r", encoding="utf-8") as f:
    word_frequency = eval(f.read())
