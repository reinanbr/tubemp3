from tubemp3.api import info_url


url='https://music.youtube.com/watch?v=B_HSa1dEL9s'

res = info_url(url)

for key in res.keys():
    print(f'{key}: {res[key]}','\n')