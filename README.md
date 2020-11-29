# WordCloud from NaverBlog

- 네이버 블로그 글을 읽어와 자동으로 단어 구름을 만들어 줍니다. 네 제가 쓰려고 만들었습니다.

# Install

```bash
pip install git+https://github.com/psj8252/WordCloud-from-NaverBlog.git
```
위 명령어로 설치하시면 됩니다.

# Usage

```python
from nbclouder import Clouder

naver_id = "psj8252"
clouder = Clouder(naver_id)
clouder.fire(['IT and 컴퓨터', '후기'], "my_blog_cloud.png", "/Library/Fonts/Arial Unicode.ttf")
```
우선 Clouder 인스턴스를 초기화해줍니다. 다음으로 'IT and 컴퓨터', '후기' 카테고리에 있는 모든 글로 wordcloud를 만듭니다.

WordCloud를 만드는 가장 간단한 방법은 fire 함수를 사용하는 것입니다. 사용할 글의 카테고리, 이미지를 저장할 경로, font 파일을 넘겨주면 바로 해당 카테고리의 모든 글을 읽어 분석한 뒤 WordCloud를 만들어 저장합니다.


```python
clouder.category_names()
# >>> ['★', '나의 글', 'Essay Series', 'Miscellany', 'Poetry', 'Etc', 'My pictures', 'Calligraphy', '필사', '꽃을 보듯 너를 본다', 'Quotes', '후기', '책 - 소감', '책 - Review', '영화', '공연', '방송', 'IT and 컴퓨터', '프로그래밍', '정보보안', '전체글']
```
category_names 함수를 호출하면 입력한 id의 카테고리 목록을 반환합니다. 위에는 제 id를 입력해서 제 블로그의 카테고리들이 나왔습니다. 이 카테고리들 중에서 사용할 카테고리들을 넘겨주면 됩니다.

```python
from nbclouder import Clouder
from datetime import datetime

naver_id = "psj8252"
clouder = Clouder(naver_id)
datetime_filter_fn = lambda post_datetime: post_datetime.year == 2020
clouder.fire(['IT and 컴퓨터', '후기'], "my_blog_cloud.png", "/Library/Fonts/Arial Unicode.ttf", datetime_filter_fn=datetime_filter_fn)
```
examples/sample2.py 에 있는 것처럼 특정 날짜의 게시물만 가져오고 싶을 수 있습니다. (ex 올해 글만 보고 싶다)

그럴 때는 위와 같이 datatime_filter_fn 을 넘겨줌으로써 필터링이 가능합니다.

examples에 몇 가지 다르게 사용할 수 있는 예시들을 넣어두었으니 참고하시기 바랍니다.
