from setuptools import setup
from setuptools import find_packages, setup

with open("README.md",encoding="utf-8") as fh:
    readme = fh.read()

setup(name='tubemp3',
    version='0.3.6',
    url='https://github.com/reinanbr/tubemp3',
    license='MIT License',
    author='Reinan Br',
    entry_points={
        "console_scripts": ["tubemp3 = tubemp3.in_line:main"],
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='video mp3 m4a mp4 youtube music download',
    description=u'Library for getting music and video in high quality from YouTube',
    packages=find_packages(),
    install_requires=['tqdm','mutagen','requests','yt-dlp'],)
