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

</p>
</p>
<p align='center'> <b>Library for getting music from YouTube</b></p>
<hr/>

## Instalation

```sh
pip3 install tubemp3 -U
```


## Examples:

### Terminal:
```sh
$ tubemp3 'https://music.youtube.com/watch?v=Wy_6jN1Yrx8&si=pgL_4Ozjafkkms8X' '/sdcard/Alarms/root_kali.mp3'
```
result:
```sh
tube search info:
file: /sdcard/Alarms/root_kali.mp3
link: https://music.youtube.com/watch?v=Wy_6jN1Yrx8&si=pgL_4Ozjafkkms8X
search: False
info music link:
'query': '3.1_4-root@kali.0cc'
'url': 'https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1738566553&ei=ORegZ4qnNKSc4dUPgbDywQo&ip=138.0.23.42&id=o-AKs3YMQ-E3ngo8HXEdUIYXkkMZrmRFfSEDYK79WPKP3P&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1738544953%2C&mh=dZ&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-pmcg-bg0z&ms=au%2Crdu&mv=m&mvi=1&pcm2cms=yes&pl=24&rms=au%2Cau&gcr=br&initcwndbps=1708750&bui=AY2Et-NY-2_d96Ox17PCCMFdO2vwtutP_n2aVof6gFPmupRoeqEUr8lEvjt44HR45GAuyvbfgWrhdGnJ&spc=9kzgDddQQsLHA1uNQA2PvbqsxaXAROJQ713a2K9X7R6MC62-2upuYWeXOA&vprv=1&svpuc=1&mime=audio%2Fwebm&ns=sHpH7Tpj8F2w3ws75U722VcQ&rqh=1&gir=yes&clen=3091263&dur=152.021&lmt=1714673885014039&mt=1738544457&fvip=16&keepalive=yes&lmw=1&fexp=51326932%2C51371294&c=TVHTML5&sefc=1&txp=1318224&n=iN-hWz-ihfa5jQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cgcr%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Crms%2Cinitcwndbps&lsig=AGluJ3MwRQIgcOHHh1rFXTuN5BZSK6KxoEO-ZMz1NlG37cLafeOmBK0CIQDegHyle5ONBj6Ii5XJYpmQI5sq_TpCYm3U5-aYnhQpbw%3D%3D&sig=AJfQdSswRgIhAJFeIkNJH1y9FyuGiAgS8gj_6vvkk_9D_8ahJE1zEhZmAiEA1jVCKoPyTe8AgjkeDP6G4MgirkQdPPuYMaE1sWqgLRg%3D'
'title': '3.1_4-root@kali.0cc'
'track': '3.1_4-root@kali.0cc'
'artist': 'Mac Quayle'
'album': 'Mr. Robot, Vol. 5 (Original Television Series Soundtrack)'
'art_album': 'https://cdn-images.dzcdn.net/images/cover/651fa1e2e9c54162cb4f2ad93ec94ae8/500x500-000000-80-0-0.jpg'
'filesize': '3091263'
'duration': '152'
'channel': 'Mac Quayle - Topic'
'thumbnail': 'https://i.ytimg.com/vi_webp/Wy_6jN1Yrx8/maxresdefault.webp'
'format': 'webm'
'year': '2018'
downloading `/tmp/3.1_4-root@kali.0cc_.webm`
/tmp/3.1_4-root@kali.0cc_.webm: 100%|██████████████| 3.09M/3.09M [01:16<00:00, 40.5kB/s]
/tmp/3.1_4-root@kali.0cc.jpg: 100%|█████████████████| 96.1k/96.1k [00:00<00:00, 268kB/s]
converting /tmp/3.1_4-root@kali.0cc_.webm to /sdcard/Alarms/root_kali.mp3...
Input #0, matroska,webm, from '/tmp/3.1_4-root@kali.0cc_.webm':
  Metadata:
    encoder         : google/video-file
  Duration: 00:02:32.02, start: -0.007000, bitrate: 162 kb/s
  Stream #0:0(eng): Audio: opus, 48000 Hz, stereo, fltp (default)
Stream mapping:
  Stream #0:0 -> #0:0 (opus (native) -> mp3 (libmp3lame))
Press [q] to stop, [?] for help
Output #0, mp3, to '/sdcard/Alarms/root_kali.mp3':
  Metadata:
    TSSE            : Lavf61.1.100
  Stream #0:0(eng): Audio: mp3, 44100 Hz, stereo, fltp, 256 kb/s (default)
      Metadata:
        encoder         : Lavc61.3.100 libmp3lame
[libmp3lame @ 0x300010def0] Trying to remove 1152 samples, but the queue is empty
[out#0/mp3 @ 0x30001131a0] video:0KiB audio:4752KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.018065%
size=    4753KiB time=00:02:32.01 bitrate= 256.1kbits/s speed=28.3x
saving metadata from `/sdcard/Alarms/root_kali.mp3...
/sdcard/Alarms/root_kali.mp3
```

### with links
```py
from tubemp3.api import get_info_link as gil
from tubemp3.file import download

music = gil('https://music.youtube.com/watch?v=yspAcpXEzSM&si=gKIVwPIQ-tbQjKQ_')
download(music)
```
Result:
```sh
info music link:
'query': 'Panamericano Agressivo'
'url': 'https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1738567215&ei=zxmgZ_PkLbCkobIPvPPziQI&ip=138.0.23.42&id=o-ANcW0y9ncd9f1txUgIwH7T8DE4vnL7Al0noeEsinZM_M&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1738545615%2C&mh=Hm&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-pmcg-bg0z&ms=au%2Crdu&mv=m&mvi=1&pcm2cms=yes&pl=24&rms=au%2Cau&gcr=br&initcwndbps=1420000&bui=AY2Et-PBFAL3kl8xujN63o-C3kHGGDyw7OObwA78iBYckkffSa7qSaQ-UgEceCkrJilHlGosOAjPtUnN&spc=9kzgDaSHACPHreUFeBbN_K0wkKNpnKXhaQmYqnM9v4-NoTb4ovTTiDNXjw&vprv=1&svpuc=1&mime=audio%2Fwebm&ns=ylj7Dz81yguVZpHMqPLgUoIQ&rqh=1&gir=yes&clen=2169698&dur=137.101&lmt=1714920334464908&mt=1738545419&fvip=7&keepalive=yes&lmw=1&fexp=51326932%2C51371294&c=TVHTML5&sefc=1&txp=2318224&n=z2nkBqRkIkVlHQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cgcr%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Crms%2Cinitcwndbps&lsig=AGluJ3MwRQIhAOpTD5xDprbvkCM45hV-wWYDf8IcWDOp7PIsnNtBQbCdAiB_fpCo5xiBE5If0Gjotc17UEczRME5ep7LKIGTlJKerQ%3D%3D&sig=AJfQdSswRAIgPyWGjeoC7r1vydH0-iLVt1oR2sr_mXfYSxWeEqxTt5wCIAb4DPL37opckyI9607R5AdhuoNQpM3Xp4kmppng4_D5'
'title': 'Panamericano Agressivo'
'track': 'Panamericano Agressivo'
'artist': 'DJ Patrick R'
'album': 'Panamericano Agressivo'
'art_album': 'https://cdn-images.dzcdn.net/images/cover/b2b6a1e074d7300f59aa1776e54d72b3/500x500-000000-80-0-0.jpg'
'filesize': '2169698'
'duration': '137'
'channel': 'DJ Patrick R - Topic'
'thumbnail': 'https://i.ytimg.com/vi_webp/yspAcpXEzSM/maxresdefault.webp'
'format': 'webm'
'year': '2023'
downloading `/tmp/Panamericano Agressivo_.webm`
/tmp/Panamericano Agressivo_.webm: 100%|███████████| 2.17M/2.17M [01:08<00:00, 31.7kB/s]
/tmp/Panamericano Agressivo.jpg: 100%|█████████████| 87.9k/87.9k [00:00<00:00, 1.00MB/s]
converting /tmp/Panamericano Agressivo_.webm to Panamericano Agressivo.mp3...
Input #0, matroska,webm, from '/tmp/Panamericano Agressivo_.webm':
  Metadata:
    encoder         : google/video-file
  Duration: 00:02:17.10, start: -0.007000, bitrate: 126 kb/s
  Stream #0:0(eng): Audio: opus, 48000 Hz, stereo, fltp (default)
Stream mapping:
  Stream #0:0 -> #0:0 (opus (native) -> mp3 (libmp3lame))
Press [q] to stop, [?] for help
Output #0, mp3, to 'Panamericano Agressivo.mp3':
  Metadata:
    TSSE            : Lavf61.1.100
  Stream #0:0(eng): Audio: mp3, 44100 Hz, stereo, fltp, 256 kb/s (default)
      Metadata:
        encoder         : Lavc61.3.100 libmp3lame
[out#0/mp3 @ 0x3000113120] video:0KiB audio:4285KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.020033%
size=    4286KiB time=00:02:17.08 bitrate= 256.1kbits/s speed=28.2x
saving metadata from `Panamericano Agressivo.mp3...
```

### music info
```py
from tubemp3.api import search_music

query = "like a player wolverine deadpool chor"
music = search_music(query)[0]

for key,value in music.items():
    print(f"'{key}': '{value}'")
```

Result:
```sh
Size yt result: 13                                                                      Extracting info...                                                                      Size result search: 10                                                                  'query': 'like a player wolverine deadpool chor'                                        'url': 'https://rr1---sn-npqpo5g5cg-2o1e.googlevideo.com/videoplayback?expire=1738570292&ei=1CWgZ9fVMb-bobIPnbCeoQ0&ip=138.0.23.42&id=o-ABMgIX4upyaWB2JefBj0a9Zu7hGBA2zWXVR53ti-8ue6&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1738548692%2C&mh=Ld&mm=31%2C29&mn=sn-npqpo5g5cg-2o1e%2Csn-pmcg-bg0e&ms=au%2Crdu&mv=m&mvi=1&pl=24&rms=au%2Cau&gcr=br&initcwndbps=1617500&bui=AY2Et-MbKGhVyirSm3TLiyRO6KhNSohF2eKXL0r6lNMOFbTlHwgtxL4klmuYRbSCB2JIRGlc30P6oIGS&spc=9kzgDWB-VukVI0kJyKu4OUt7OdHiD6v2Ky58EJPoBr-vTpb_exZY2d_hMg&vprv=1&svpuc=1&mime=audio%2Fwebm&ns=AcI2wvgcy7_yddFn6j-5nX8Q&rqh=1&gir=yes&clen=5488555&dur=339.021&lmt=1730240121229520&mt=1738548302&fvip=11&keepalive=yes&lmw=1&fexp=51326932%2C51371294&c=TVHTML5&sefc=1&txp=4532434&n=cki1JiqhS31N7g&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cgcr%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=AGluJ3MwRAIgT_eyw8NQYEFkQtZDNSoAJzmdPYqVZ3Lkm-mC1I0DgB0CIAIW5H2DR9BRjLJ_cyoNSCkejEF0GD6QaOs0LjFvLLgA&sig=AJfQdSswRgIhAO0R7U7B1GlsnatVGrR5rW1-g6_nPxDLz4FBneiyD_KhAiEAjjUogdPkBZl7rtfQgKPJfYSRkDWgs4iViVZINv1hHw4%3D'                                          'title': 'Deadpool & Wolverine Theme | Like a Prayer (Complete Version)'                'artist': 'José Carlos'                                                                 'album': 'Unknown'                                                                      'art_album': 'https://i.ytimg.com/vi/PmE0r_yC2U8/maxresdefault.jpg'                     'track': 'Deadpool & Wolverine Theme | Like a Prayer (Complete Version)'                'filesize': '5488555'                                                                   'duration': '339'                                                                       'channel': 'José Carlos'                                                                'thumbnail': 'https://i.ytimg.com/vi/PmE0r_yC2U8/maxresdefault.jpg'                     'format': 'webm'                                                                        'year': '2024'
```

### Downloads
```py
from tubemp3.api import search_music                                                                        
from tubemp3.file import download                                                                           

query = "like a player wolverine deadpool chor"

music = search_music(query)[0]
download(music)
```


<hr>
<br>
<br>
<img src="https://reysofts.com/evox/api/save_access_lib.php?key_lib=tubemp3_py">
