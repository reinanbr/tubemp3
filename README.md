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
sudo apt install ffmpeg python3 python3-pip -y
```

```sh
pip3 install tubemp3 -U
```


## Examples:

<hr>

<br>

### coding


<br>

#### with url:

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

#### with search
```py

from tubemp3.api import get_info_url,get_info_search

query = 'waht is love'
vds = get_info_search(query,number_results=5)

for vd in vds:
    del vd['ytdl']
    print(vd,'\n')

```
response:
```sh

[download] Downloading playlist: waht is love
[youtube:search] query "waht is love": Downloading page 1
[youtube:search] playlist waht is love: Downloading 5 videos
[download] Downloading video 1 of 5
[youtube] HEXWRTEbj1I: Downloading webpage
[download] Downloading video 2 of 5
[youtube] i0p1bmr0EmE: Downloading webpage
[download] Downloading video 3 of 5
[youtube] MPn6E4za7Os: Downloading webpage
[download] Downloading video 4 of 5
[youtube] z3mzvJiUZao: Downloading webpage
[download] Downloading video 5 of 5
[youtube] TC7tjGJO5oI: Downloading webpage
[download] Finished downloading playlist: waht is love
{'title': 'Haddaway - What Is Love [Official]', 
'track': 'Unknown', 
'duration': 241, 
'artist': 'CoconutMusicGermany', 
'channel': 'CoconutMusicGermany', 
'year': '2014', 
'album': 'Unknown', 
'id_video': 'HEXWRTEbj1I', 
'url_m4a': 'https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1672873426&ei=crG1Y5TVJIvnwgT6qKGABw&ip=2804%3A2108%3Afcf6%3Abe07%3A5020%3A8d5a%3Aa6b3%3A23ad&id=o-AG_p23V5_lC6WC7TPG_woSn7d9OonLlY05cW8Ehqj_g1&itag=140&source=youtube&requiressl=yes&mh=GR&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-bg0eznzr&ms=au%2Crdu&mv=m&mvi=1&pl=40&initcwndbps=918750&vprv=1&mime=audio%2Fmp4&ns=35Dvf-UTMTck_rt2pPlC4BgK&gir=yes&clen=3896196&dur=240.698&lmt=1583594487153971&mt=1672851444&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5531432&n=zh7tK1-I-AgAOXEnW&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAJkQZ0e1nCh0hYjKsimaBmKc5zI2K5uV9isIndndU3HdAiAoGRQG9Ps7B8JXkf6f3W0vIFmM67YV9xeJeE3dXeZ56Q%3D%3D&sig=AOq0QJ8wRQIhAJckM6F3enXYAEjed0aDsNmBq3-TptLUk0AumEoXvi0wAiBCYKbnulVtt7Iv2bFyMOuPEHem65I5Tt6ZAsBG8fIsQA==', 
'thumbnail': 'https://i.ytimg.com/vi/HEXWRTEbj1I/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBJfRv8MtJiH-z3e2hrGw4UUlLwYw'} 

{'title': 'TWICE "What is Love?" M/V', 
'track': 'Unknown', 
'duration': 223,
'artist': 'JYP Entertainment', 
'channel': 'JYP Entertainment', 
'year': '2018',
'album': 'Unknown', 
'id_video': 'i0p1bmr0EmE', 
'url_m4a': 'https://rr2---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1672873427&ei=c7G1Y_GoKOzW1sQP2pOC0A0&ip=2804%3A2108%3Afcf6%3Abe07%3A5020%3A8d5a%3Aa6b3%3A23ad&id=o-AN9gI3VUPQkbhPXANUxlzc4kQQdtcLsNsHw1_H8apfFE&itag=140&source=youtube&requiressl=yes&mh=uz&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-bg0eznls&ms=au%2Crdu&mv=m&mvi=2&pl=40&initcwndbps=918750&vprv=1&mime=audio%2Fmp4&ns=O4DI6it9CfCEMR_bwQr8haoK&gir=yes&clen=3614325&dur=223.283&lmt=1671003915011438&mt=1672851444&fvip=5&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=jGTpl5_RrdxXqfM4g&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgWGkY4i3SgBELNgOLxVCK1hK-8sYDXbxaFyixG1WM3okCIQCA2f3-bphfWpjuD93XFX9CxaWKzgIdMlVyfDEuhGCZjA%3D%3D&sig=AOq0QJ8wRgIhAMGKvaGfz94Dkkjd6iTpGm9_97wIWL-NZ1RW2D0Akr1_AiEA0q_DaKASSmMz764RwzulGE7Np0Ee2jkzTF23yiyH1No=', 
'thumbnail': 'https://i.ytimg.com/vi/i0p1bmr0EmE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBJ3NXnqmFXY3Bsx0kjcL90pgpStw'} 

{'title': 'What Is Love (12" Mix)', 
'track': 'What Is Love (12" Mix)', 
'duration': 402, 
'artist': 'Haddaway', 
'channel': 'Haddaway Channel', 
'year': '2015', 
'album': 'What Is Love',
'id_video': 'MPn6E4za7Os', 
'url_m4a': 'https://rr2---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1672873428&ei=dLG1Y7nXMq3I1sQPp8e_yA4&ip=2804%3A2108%3Afcf6%3Abe07%3A5020%3A8d5a%3Aa6b3%3A23ad&id=o-APO7C8kNjwa7vG5OfVLeB_0DAw3Q-Zl-f0nG3pl-iQ9r&itag=140&source=youtube&requiressl=yes&mh=zC&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-bg07dnr7&ms=au%2Crdu&mv=m&mvi=2&pl=40&gcr=br&initcwndbps=918750&vprv=1&mime=audio%2Fmp4&ns=5_dRSRokQi9IcH9ccQoq5S4K&gir=yes&clen=6511823&dur=402.239&lmt=1628120612101811&mt=1672851444&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=JGTgxIbTpUdtvwNm8&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPkDMsqprhpqSAnoxD_PO4e7ixq-9bwEBqNh7lT4eA17AiBL-2S_mlpP3lv5Ja3rcZZOMKxpppXEYtLWW8tZiMnrVQ%3D%3D&sig=AOq0QJ8wRQIgCwEl9obg7xrspikAEKqGPyk1_byVmA4_uoBhNZNHNucCIQC659JmmwByr9b7NYiYvxT9QeobGLbN0OyPSuGFKyiDQA==',
'thumbnail': 'https://i.ytimg.com/vi/MPn6E4za7Os/maxresdefault.jpg'} 

{'title': 'Haddaway - What Is Love (Moreno J Remix)', 
'track': 'Unknown', 'duration': 489, 
'artist': 'Moreno J', 
'channel': 'Moreno J', 
'year': '2022', 'album': 'Unknown', 
'id_video': 'z3mzvJiUZao', 
'url_m4a': 'https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1672873429&ei=dbG1Y_H7K4PSxASP4ZXgDQ&ip=2804%3A2108%3Afcf6%3Abe07%3A5020%3A8d5a%3Aa6b3%3A23ad&id=o-AMt16smA2XweIETQBi8Kw71SQHJ7RWvFufgyxV5WSpdv&itag=140&source=youtube&requiressl=yes&mh=bM&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-bg07dn6k&ms=au%2Crdu&mv=m&mvi=1&pl=40&initcwndbps=962500&vprv=1&mime=audio%2Fmp4&ns=kdjN5BTGxc8eZUbUupHHYJMK&gir=yes&clen=7916285&dur=489.105&lmt=1654522808604025&mt=1672851679&fvip=2&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Dcr7lAiKvLztuF6e4&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAL12mKaeIzlaLPs2WQpRvFdNNxpnFZRFb-f9oznLenKdAiEAtoUIKEB1v8_ZwDo2kSJ54f4OiayH8YXVwH-x0Nse-vQ%3D&sig=AOq0QJ8wRgIhAORPYlDsWzmlMs3KQUGqTbON9A6p3viXSUtCWPjn9FGwAiEAkZbYQ7dlDAI5YrRCY6k1cQ8eRpFacOAJGvBFE_Gvcgo=', 
'thumbnail': 'https://i.ytimg.com/vi/z3mzvJiUZao/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgUihIMA8=&rs=AOn4CLCGdIZe_pHFB4JQSLBt5jhLsvxH_w'} 

{'title': 'Haddaway - What Is Love (Shuffle Dance)',
 'track': 'Unknown', 'duration': 296, 
 'artist': 'Km Music 1', 
 'channel': 'Km Music 1', 
 'year': '2022', 
 'album': 'Unknown', 
 'id_video': 'TC7tjGJO5oI',
 'url_m4a': 'https://rr2---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1672873431&ei=d7G1Y9moFYPAwwSKkLrQDQ&ip=2804%3A2108%3Afcf6%3Abe07%3A5020%3A8d5a%3Aa6b3%3A23ad&id=o-AG3n9CPXFnOT7deFlFrAMsifjmlnjJp_vR9RsrYTtE1F&itag=140&source=youtube&requiressl=yes&mh=tV&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-bg07dnr7&ms=au%2Crdu&mv=m&mvi=2&pl=40&initcwndbps=918750&vprv=1&mime=audio%2Fmp4&ns=iFArK1FgIFDlTR70xu9IzAcK&gir=yes&clen=4789386&dur=295.891&lmt=1671575648475580&mt=1672851444&fvip=2&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=JEb1lCqvD_TP3sX6A&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhALlIUf8X5ru4A_lAKBnEK6Ohy79kH-sJPosrEPJ0ffymAiEA-vjuhZgyo4NWCUUd0J-gTa-1CApqDw1InFQZhglgBTI%3D&sig=AOq0QJ8wRAIgEHA62vE0WdjCQB9IhXJXKEFrlKvEK36KLM07yoqTy2gCIC3zUJ9P7SBwFAlBgzjSaxcyTl-gmdl1t7ITbARSQBVp', 
 'thumbnail': 'https://i.ytimg.com/vi/TC7tjGJO5oI/maxresdefault.jpg'} 

```

### on terminal

<br>

with name:

```sh
$ getmusic 'https://music.youtube.com/watch?v=B_HSa1dEL9s' 'test.mp3'
```
result:
```sh

[youtube] B_HSa1dEL9s: Downloading webpage
[youtube] B_HSa1dEL9s: Downloading webpage
[youtube] Downloading just video B_HSa1dEL9s because of --no-playlist
<youtube_dl.YoutubeDL.YoutubeDL object at 0x7f52f3b611c0>
[music info] 
title:For Whom The Bell Tolls (Remastered)
duration:5:10
artist:Metallica
id:B_HSa1dEL9s
album:Ride The Lightning (Remastered)
year:2022
[youtube] B_HSa1dEL9s: Downloading webpage
[download] Destination: test.m4a
[download] 100% of 4.79MiB in 01:06
[ffmpeg] Correcting container in "test.m4a"
[ffmpeg] Destination: test.mp3
Deleting original file test.m4a (pass -k to keep)
Non standard genre name: Unknown

```
<img src="https://reysofts.com.br/engine/libs/save_table_access_libs.php?lib_name=tubemp3">