import json
import re
import sys
from datetime import datetime
from typing import Callable, Dict, Iterable, List, Optional, Tuple, Union

from bs4 import BeautifulSoup
from konlpy.tag import Okt
from requests import Session
from wordcloud import WordCloud


class Clouder:
    """
    Get posts and make word cloud.

    :param categoryNo: the category number of the board to get posts.
    :param par_categoryNo: the parent category number of the board to get posts.
    :param naver_id: naver id of owner of posts. you should understand this is not your naver id.
    :param NID_AUT: one of naver login cookie, you can find by browser cookies tab. this is necessary if you want to get private posts.
    :param NID_SES: one of naver login cookie. this is similar to NID_AUT.
    """

    def __init__(
        self,
        naver_id: str,
        categoryNo: int,
        par_categoryNo: int,
        NID_AUT: Optional[str] = None,
        NID_SES: Optional[str] = None,
    ):
        self.session = Session()

        self.naver_id = naver_id
        self.categoryNo = categoryNo
        self.par_categoryNo = par_categoryNo

        if NID_AUT and NID_SES:
            self.session.cookies.set("NID_AUT", NID_AUT)
            self.session.cookies.set("NID_SES", NID_SES)
            print("Finished setting cookies")

    def get_post_ids(self) -> List[str]:
        """
        Get list of post ids.

        :return: a list of pid (post id) of Naver blog.
        """
        url = f"http://blog.naver.com/PostTitleListAsync.nhn"
        post_ids = []
        params = {
            "blogId": self.naver_id,
            "currentPage": 1,
            "categoryNo": self.categoryNo,
            "parentCategoryNo": self.par_categoryNo,
            "countPerPage": 30,
            "viewdate": "",
        }
        while True:
            response = self.session.get(url, params=params)
            data = json.loads(response.text.replace("\\", "\\\\"))

            lists = data["postList"]
            ids = [d["logNo"] for d in lists]

            if ids[0] not in post_ids:
                post_ids += ids
                params["currentPage"] += 1
            else:
                print(f"Get post ids: {len(post_ids)} posts found.")
                return post_ids

    def get_contents(
        self, post_ids: List[str], without_datetime: bool = True
    ) -> Union[List[Tuple[datetime, str]], List[str]]:
        """
        Get content of posts.

        post_ids: a list of post id in Naver blog.
        return:  a collection of contents of posts. if without_datetime is true, just return post context.
        """
        contents = []
        url = f"http://blog.naver.com/PostView.nhn"
        params = {"blogId": self.naver_id}
        for post_id in post_ids:
            params["logNo"] = post_id

            # Get contents of a post
            response = self.session.get(url, params=params)

            soup = BeautifulSoup(response.text, "html.parser")

            # Smart editor 3
            text = soup.select_one(f"#post-view{post_id} > div > div > div.se-main-container")
            # Smart editor 2
            if not text:
                text = soup.select_one(
                    f"#post-view{post_id} > div > div > div.se_component_wrap.sect_dsc.__se_component_area"
                )

            if not text:
                text = soup.select_one(f"#post-view{post_id}")
            if text:
                text = text.get_text("\n").replace("\xa0", " ")  # Space unicode replace
            else:
                print(f"[Error] cannot select content in {post_id}.", file=sys.stderr)
                continue

            text = re.sub("\s+", " ", text).strip()
            if without_datetime:
                contents.append(text)
                continue

            date_time = soup.select(
                f"#post-view{post_id} > div > div > div > div > div > div.blog2_container > span.se_publishDate.pcol2"
            )
            date_time += soup.select("#printPost1 > tr > td.bcc > table > tr > td > p.date.fil5")

            if date_time:
                date_time = date_time[0].get_text()
            else:
                print(f"[Error] cannot select datetime in {post_id}.")
                date_time = "1900. 01. 01. 00:00"

            contents.append((datetime.strptime(date_time, "%Y. %m. %d. %H:%M"), text.strip()))

        print(f"Get contexts: {len(contents)} found.")
        return contents

    def get_word_frequency(
        self,
        contents: Union[List[Tuple[datetime, str]], List[str]],
        pos_tagging_fn: Optional[Callable[[str], List[Tuple[str, str]]]] = None,
        white_tags: Iterable[str] = ("Noun", "Verb", "Adjective"),
        preserve_tag: bool = False,
        **kwargs,
    ) -> Union[Dict[str, int], Dict[Tuple[str, str], int]]:
        """
        Calculate Words frequency.

        :param contents: a output of `get_contents` method.
        :param pos_tagging_fn: function to pos_tagging_fn tagging text.
        :param white_tags: a collection of types of tags that should be counted.
        :param preserve_tag: whether preserve and return  tag information. if false, just return {word:count}
        :param `**kwargs`: pos_tagging_fn tagger options.
        :return: morphs counts { morph: count}
        """

        morph_counts = {}

        # Default pos tagger
        if pos_tagging_fn is None:
            okt = Okt()
            pos_tagging_fn = okt.pos
            kwargs = {"stem": True}

        for text in contents:
            pos_tags = pos_tagging_fn(text, **kwargs)
            morphs = [
                ((token, pos_tag) if preserve_tag else token) for token, pos_tag in pos_tags if pos_tag in white_tags
            ]

            for morph in morphs:
                morph_counts[morph] = morph_counts.get(morph, 0) + 1

        print("Word counting complete!")
        return morph_counts

    def make_cloud(
        self,
        image_path: str,
        word_frequency: Dict[str, int],
        font_path: str,
        background_color: str = "white",
        width: int = 800,
        height: int = 600,
        **kwargs,
    ) -> WordCloud:
        """
        Save wordcloud image file on 'image_path'.
        :param image_path: path to save image.
        :param word_frequency: key is word(morphs) and value is count.
        :param font_path: font file path to draw word to image.
        :param `background_color`, `width`, `height`: parameter of 'WordCloud'. refer to 'wordcloud' docs.
        :return: wordcloud object made using 'word_frequency'
        """
        word_cloud = WordCloud(
            font_path=font_path, background_color=background_color, width=width, height=height, **kwargs
        )
        word_cloud.generate_from_frequencies(word_frequency)
        word_cloud.to_file(image_path)
        print(f"Saved image to {image_path}")

        return word_cloud

    def fire(
        self,
        image_path: str,
        font_path: str,
        pos_tagging_fn: Optional[Callable[[str], List[Tuple[str, str]]]] = None,
        white_tags: Iterable[str] = ("Noun", "Verb", "Adjective"),
        background_color: str = "white",
        width: int = 800,
        height: int = 600,
        **kwargs,
    ) -> Tuple[WordCloud, Dict[str, int], List[str], List[str]]:
        """
        Carry out all processes. parameters is same as other functions.
        """
        post_ids = self.get_post_ids()
        contents = self.get_contents(post_ids)
        word_frequency = self.get_word_frequency(contents, pos_tagging_fn, white_tags)
        word_cloud = self.make_cloud(image_path, word_frequency, font_path, background_color, width, height, **kwargs)

        return word_cloud, word_frequency, contents, post_ids
