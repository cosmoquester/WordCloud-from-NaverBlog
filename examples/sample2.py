"""
You can filter posts in making word cloud.
"""
from nbclouder import Clouder
from datetime import datetime, timedelta

# Fill parameters properly
naver_id = ""

clouder = Clouder(naver_id)
post_ids = clouder.get_post_ids(["전체글"])
contents = clouder.get_contents(
    post_ids, datetime_filter_fn=lambda post_datetime: post_datetime < datetime.now() - timedelta(days=30)
)

# Filtered by post datetime
word_frequency = clouder.get_word_frequency(contents, white_tags=["Noun"])

word_cloud = clouder.make_cloud("word_cloud.png", word_frequency, "/Library/Fonts/Arial Unicode.ttf")
# Then 'word_cloud.png' is saved
