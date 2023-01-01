from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='tubemp3',
    version='0.2.9.1',
    url='https://github.com/perseu912/tubemp3',
    license='MIT License',
    author='Reinan Br',
    entry_points = {
        'console_scripts': ['getmusic=tubemp3.get_music_line:main'],
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='video mp3 m4a mp4 youtube music download',
    description=u'Library for getting music and video in high quality from YouTube',
    packages=find_packages(),
    install_requires=['requests',
    'youtube-dl','mp3-tagger','pydub','stagger','eyed3'],)