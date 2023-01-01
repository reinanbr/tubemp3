<h1 align='center'>TubeMp3</h1>
<p align='center'>

<br/>
<a href="https://github.com/perseu912"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<br/>
<p align='center'>
<!-- github dados -->
<!-- sites de pacotes -->
<a href='https://pypi.org/project/tubemp3/'><img src='https://img.shields.io/pypi/v/tubemp3'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/tubemp3'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/tubemp3"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/tubemp3?color=orange">
<br/>


<img src='https://img.shields.io/badge/system-linux%20%7C%20deb-brightgreen'>

<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/perseu912/tubemp3">

<br/>
<!-- outros premios e analises -->
<!-- <a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/perseu912/noawclg?logo=codefactor">
</a> -->
<!-- redes sociais -->
<a href='https://instagram.com/reysofts/'><img src='https://shields.io/badge/insta-reysofts-darkviolet?logo=instagram&style=flat'></a>
<a href='https://discord.gg/pFZP86gvEm'><img src='https://img.shields.io/discord/856582838467952680.svg?label=discord&logo=discord'></a>

</p>
</p>
<p align='center'> <b>Library for getting music from YouTube</b></p>
<hr/>

## Instalation


```sh
sudo apt update && sudo apt upgrade -y
```

```sh
sudo apt install ffmpeg sox python3 python3-pip -y
```

```sh
pip3 install tubemp3 -U
```

## Examples:

<hr>

<br>

### coding


<br>

with url:

```py
from tubemp3.api import info_url

url='https://music.youtube.com/watch?v=B_HSa1dEL9s'

res = info_url(url)

for key in res.keys():
    print(f'{key}: {res[key]}','\n')
```
results:
```sh
[youtube] B_HSa1dEL9s: Downloading webpage
title: For Whom The Bell Tolls (Remastered) 

track: For Whom The Bell Tolls (Remastered) 

duration: 310 

artist: Metallica 

channel: Metallica 

year: 2022 

album: Ride The Lightning (Remastered) 

id_video: B_HSa1dEL9s 

url_m4a: https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/
videoplayback?expire=1672556531&ei=k9uwY4KZKoaZobIPgrOigA0&
ip=2804%3A2108%3Afcf6%3Abe07%3A8cc2%3A985b%3A2332%3Aa511&
id=o-AFe6AF4hh8V2O0q5_ZfLPR2z-BKhuQn55TFZcQOIIVwW&itag=140&
source=youtube&requiressl=yes&mh=qb&mm=31%2C29&
mn=sn-npqpo5g5cg-2o1e%2Csn-bg0eznzr&ms=au%2Crdu&mv=m&mvi=1&
pl=40&gcr=br&initcwndbps=778750&vprv=1&mime=audio%2Fmp4&
ns=WZK8_LEes6LiCdnpIj4ez3MK&gir=yes&clen=5018216&dur=309.
973&lmt=1661906335401511&mt=1672534612&fvip=2&
keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=2318224&n=_Xrn3u1o2oiygs8fc&
sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&
lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgagpGXuqKY0aDx841yUqVtODeXzqJNcpib8Jx2GtVfQ
ECIAujzKGJucW8TwZ_eoOWqt_xI7IfXSYlIVDSWLlOk8tO&sig=AOq0QJ8wRgIhALtD7-iYCvo4baCxdLsRRhuVP6Jn5ucmj2crKIN_syd4AiEAod5kdZNa3-dGVgZUQeraAVVqiAm0eKKSsXOQauJUFo4= 

thumbnail: https://i.ytimg.com/vi_webp/B_HSa1dEL9s/maxresdefault.webp 

ytdl: {'id': 'B_HSa1dEL9s', 'title': 'For Whom The Bell Tolls (Remastered)', 'formats': [{'asr': 48000, 'filesize': 1817167, 'format_id': '249', 'format_note': ....
```

### on terminal

<br>

with name:

```sh
$ getmusic 'no time for caution' 
```
result:
```sh
[download] Downloading playlist: no time for caution hq music
[youtube:search] query "no time for caution hq music": Downloading page 1
[youtube:search] playlist no time for caution hq music: Downloading 1 videos
[download] Downloading video 1 of 1
[youtube] rpWC9-VBjPM: Downloading webpage
[youtube] Downloading just video rpWC9-VBjPM because of --no-playlist
[youtube] rpWC9-VBjPM: Downloading player e06dea74
[download] Finished downloading playlist: no time for caution hq music
1
music: 
title:Hans Zimmer - No Time For Caution HQ (Interstellar)
duration:247
artist:Hans Zimmer
id:rpWC9-VBjPM
album:No Time for Caution
year:2015
WARNING: The url doesn't specify the protocol, trying with http
[youtube] rpWC9-VBjPM: Downloading webpage
[download] Destination: music/Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.webm
[download] 100% of 3.97MiB in 01:32
[ffmpeg] Destination: music/Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.mp3
Deleting original file music/Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.webm (pass -k to keep)
```
find  the file:
```sh
$ ls music/
```

```sh
Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.mp3 
```
play the file:
```sh
$ play music/Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.mp3
```
```sh
music/Hans_Zimmer_-_No_Time_For_Caution_HQ__Interstellar_.mp3:

 File Size: 7.94M     Bit Rate: 258k
  Encoding: MPEG audio    
  Channels: 2 @ 16-bit   
Samplerate: 48000Hz      Album: No Time for Caution
Replaygain: off         Artist: Hans Zimmer
  Duration: 00:04:06.55  Title: No Time for Caution

In:19.1% 00:00:47.10 [00:03:19.45] Out:2.26M [   ===|==-   ]        Clip:0    
```