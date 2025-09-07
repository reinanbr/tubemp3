
<br/>
<p align="center">

</p>

<p align="center">
  <!-- PyPI -->
  <a href="https://pypi.org/project/tubemp3/"><img src="https://img.shields.io/pypi/v/tubemp3?style=flat-square"></a>
  <a href="#"><img src="https://img.shields.io/pypi/dm/tubemp3?style=flat-square"></a>
  <img src="https://img.shields.io/pypi/l/tubemp3?style=flat-square&color=orange">
  
  <!-- CI/CD -->
  <a href="https://github.com/reinanbr/tubemp3/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/reinanbr/tubemp3/tests.yml?branch=main&style=flat-square&label=tests"></a>
  <a href="https://codecov.io/gh/reinanbr/tubemp3"><img src="https://img.shields.io/codecov/c/github/reinanbr/tubemp3?style=flat-square"></a>

<!-- Sistema -->
<br/>
  <img src="https://img.shields.io/badge/system-linux%20%7C%20deb-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square">

<!-- Social -->
<br/>
  <a href="https://instagram.com/reysofts/"><img src="https://img.shields.io/badge/insta-reysofts-darkviolet?logo=instagram&style=flat-square"></a>
</p>

<p align="center"><b>Library for downloading and converting YouTube music to MP3 with comprehensive testing and CI/CD.<br>(Optimized for Linux systems).</b></p>

<hr/>

## Installation

### System Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg yt-dlp -y
```

### Install via pip
```bash
pip3 install tubemp3 -U
```

---

## Usage

### CLI Example

```bash
tubemp3 "https://music.youtube.com/watch?v=Wy_6jN1Yrx8&si=pgL_4Ozjafkkms8X" "/sdcard/Alarms/root_kali.mp3"
```

<details>
  <summary><b>Sample Output</b></summary>

```txt
tube search info:
file: /sdcard/Alarms/root_kali.mp3
link: https://music.youtube.com/watch?v=Wy_6jN1Yrx8&si=pgL_4Ozjafkkms8X
search: False
info music link:
'title': '3.1_4-root@kali.0cc'
'artist': 'Mac Quayle'
'album': 'Mr. Robot, Vol. 5'
'duration': '152'
'format': 'webm'
'filesize': '3091263'
...
converting to MP3...
saving metadata...
```

</details>

---

### Python API

#### Download via URL

```python
from tubemp3 import get_info_link as gil
from tubemp3.file import download

music = gil("https://music.youtube.com/watch?v=yspAcpXEzSM")
download(music)
```

#### Search and Download

```python
from tubemp3 import search_music
from tubemp3.file import download

music = search_music("like a player wolverine deadpool chor")[0]
download(music)
```

#### Get Metadata Only

```python
from tubemp3 import search_music

query = "like a player wolverine deadpool chor"
music = search_music(query)[0]

for key, value in music.items():
    print(f"{key}: {value}")
```

#### Info from link

```python
from tubemp3 import search_music
from tubemp3  import get_info_link
from kitano import puts

    query = "like a player wolverine deadpool chor"
    musics = search_music(query)

    assert len(musics) > 0
    puts(f"Total musics found: {len(musics)}")

    music = musics[0]
    info = get_info_link(music.url)
    puts('--- Music Info ---')
    puts(info)
---
