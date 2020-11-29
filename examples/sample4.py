"""
You can use other nlp package.
"""
import os

from konlpy.tag import Kkma, Komoran, Mecab

from nbclouder import Clouder

# Fill parameters properly
naver_id = ""

clouder = Clouder(naver_id)
post_ids = clouder.get_post_ids(["전체글"])
contents = clouder.get_contents(post_ids)
font_path = "/Library/Fonts/Arial Unicode.ttf"

# Okt - default
okt_white_tags = ("Noun", "Verb", "Adjective")
okt_freq = clouder.get_word_frequency(contents, white_tags=okt_white_tags)
clouder.make_cloud(
    "okt_cloud.png",
    okt_freq,
    font_path=font_path,
)

# Komoran
komoran = Komoran()
komoran_white_tags = ("NNG", "NNP", "NP", "NF") + ("VV", "VA", "NV") + ("XR",)
komoran_freq = clouder.get_word_frequency(contents, komoran.pos, white_tags=komoran_white_tags, preserve_tag=True)
komoran_freq = {
    morph + "다" if pos in ("VV", "VA", "NV") else morph: count for (morph, pos), count in komoran_freq.items()
}
clouder.make_cloud("komoran_cloud.png", komoran_freq, font_path)

# Kkma
kkma = Kkma()
kkma_white_tags = ("NNG", "NNP", "NP", "UN") + ("VV", "VA") + ("XR",)
kkma_freq = clouder.get_word_frequency(contents, kkma.pos, white_tags=kkma_white_tags, preserve_tag=True)
kkma_freq = {morph + "다" if pos in ("VV", "VA") else morph: count for (morph, pos), count in kkma_freq.items()}
clouder.make_cloud("kkma_cloud.png", kkma_freq, font_path)

# Mecab - need additional installation for Mecab
mecab = Mecab()
mecab_white_tags = ("NNG", "NNP", "NP") + ("VV", "VA") + ("XR",)
mecab_freq = clouder.get_word_frequency(contents, mecab.pos, white_tags=mecab_white_tags, preserve_tag=True)
mecab_freq = {morph + "다" if pos in ("VV", "VA") else (morph): count for (morph, pos), count in mecab_freq.items()}
clouder.make_cloud("mecab_cloud.png", mecab_freq, font_path)
