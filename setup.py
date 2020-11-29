from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="wordcloud-from-naverblog",
    version="1.0.0",
    description="This is tool for generating word cloud from naver blog posts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4",
        "konlpy",
        "requests",
        "wordcloud",
    ],
    url="https://github.com/psj8252/WordCloud-from-NaverBlog.git",
    author="Park Sangjun",
    keywords=["wordcloud-generator", "naver-blog"],
    packages=find_packages(exclude=["tests"]),
)
