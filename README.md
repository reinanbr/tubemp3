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



### coding

#### with query

```py
from tubemp3.api import search_music

video_list = search_music("the landing")
i = 0
for video_info in video_list:
    print(f"n[{i}]")
    for key,value in video_info.items():
        print(f"{key}: {value}")
    i+=1

```
<hr>
<br>
<br>
<img src="https://reysofts.com.br/engine/libs/save_table_access_libs.php?lib_name=tubemp3">
