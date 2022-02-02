
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
<a href='https://instagram.com/gpftc_ifsertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-darkviolet?logo=instagram&style=flat'></a>
<a href='https://discord.gg/pFZP86gvEm'><img src='https://img.shields.io/discord/856582838467952680.svg?label=discord&logo=discord'></a>

</p>
</p>
<p align='center'> <b>Library for getting music from YouTube</b></p>
<hr/>

## Instalation
```sh
sudo apt install ffmpeg -y
```

```sh
$ pip3 install tubemp3 -U
```

## Examples

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