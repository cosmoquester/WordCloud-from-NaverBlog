"""
Simply call fire!!!
categoryNo and par_categoryNo is argument to specify board containing posts.
"""
from nbclouder import Clouder

# Fill parameters properly
naver_id = ""

clouder = Clouder(naver_id)
clouder.fire(["전체글"], "word_cloud.png", "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.png' is saved
