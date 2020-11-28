from setuptools import find_packages, setup

setup(
    name="wordcloud-from-naverblog",
    version="0.0.1",
    description="This is tool for generating word cloud from naver blog posts",
    python_requires='>=3.7',
    install_requires=[],
    url="https://github.com/psj8252/WordCloud-from-NaverBlog.git",
    author="Park Sangjun",
    packages=find_packages(exclude=["tests"]),
)
