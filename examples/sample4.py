"""
You can use other nlp package.
"""
import os

from konlpy.tag import Kkma, Komoran, Mecab

from nbclouder import Clouder

# Fill parameters properly
naver_id = ""
categoryNo = 0
par_categoryNo = 0


clouder = Clouder(naver_id, categoryNo, par_categoryNo)
post_ids = clouder.get_post_ids()
contents = clouder.get_contents(post_ids)

# Okt - default
okt_white_tags = ("Noun", "Verb", "Adjective")
okt_freq = clouder.get_word_frequency(contents, white_tags=okt_white_tags)
clouder.make_cloud(
    "okt_cloud.png",
    okt_freq,
    font_path="/Library/Fonts/Arial Unicode.ttf",
)

# Komoran
komoran = Komoran()
komoran_white_tags = ("NNG", "NNP", "NP", "NF") + ("VV", "VA", "NV") + ("XR",)
komoran_freq = clouder.get_word_frequency(contents, komoran.pos, white_tags=komoran_white_tags, preserve_tag=True)
komoran_freq = {
    morph + "다" if pos in ("VV", "VA", "NV") else morph: count for (morph, pos), count in komoran_freq.items()
}
clouder.make_cloud(komoran_freq, font_path="/Library/Fonts/Arial Unicode.ttf", img_path="komoran_cloud.png")

# Kkma
kkma = Kkma()
kkma_white_tags = ("NNG", "NNP", "NP", "UN") + ("VV", "VA") + ("XR",)
kkma_freq = clouder.get_word_frequency(contents, kkma.pos, white_tags=kkma_white_tags, preserve_tag=True)
kkma_freq = {morph + "다" if pos in ("VV", "VA") else morph: count for (morph, pos), count in kkma_freq.items()}
clouder.make_cloud(kkma_freq, font_path="/Library/Fonts/Arial Unicode.ttf", img_path="kkma_cloud.png")

# Mecab - cannot word in Windows
mecab = Mecab()
mecab_white_tags = ("NNG", "NNP", "NP") + ("VV", "VA") + ("XR",)
mecab_freq = clouder.get_word_frequency(contents, mecab.pos, white_tags=mecab_white_tags, preserve_tag=True)
mecab_freq = {morph + "다" if pos in ("VV", "VA") else (morph): count for (morph, pos), count in mecab_freq.items()}
clouder.make_cloud(mecab_freq, font_path="/Library/Fonts/Arial Unicode.ttf", img_path="mecab_cloud.png")
