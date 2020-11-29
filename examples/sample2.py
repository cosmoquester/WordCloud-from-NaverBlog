"""
You can filter posts in making word cloud.
"""
from nbclouder import Clouder

# Fill parameters properly
naver_id = ""

clouder = Clouder(naver_id)
post_ids = clouder.get_post_ids(["전체글"])
contents = clouder.get_contents(post_ids, without_datetime=False)

# Filtered by post datetime
word_frequency = clouder.get_word_frequency(
    [sent for date_time, sent in contents if date_time.year not in (2018, 2017)], white_tags=["Noun"]
)

word_cloud = clouder.make_cloud("word_cloud.png", word_frequency, "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.png' is saved
