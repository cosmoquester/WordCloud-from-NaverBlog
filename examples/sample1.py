from nbclouder import Clouder

# Fill parameters properly
naver_id = ""
categoryNo = 0
par_categoryNo = 0

clouder = Clouder(naver_id, categoryNo, parameters)
clouder.fire("word_cloud.jpg", "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.jpg' is saved
