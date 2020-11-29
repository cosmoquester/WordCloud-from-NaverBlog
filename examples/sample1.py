"""
Simply call fire!!!
categoryNo and par_categoryNo is argument to specify board containing posts.
"""
from nbclouder import Clouder

# Fill parameters properly
naver_id = ""
categoryNo = 0
par_categoryNo = 0

clouder = Clouder(naver_id, categoryNo, par_categoryNo)
clouder.fire("word_cloud.png", "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.png' is saved
