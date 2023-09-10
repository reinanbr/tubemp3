from tubemp3.trash.api import get_info_url,get_info_search


# url='https://music.youtube.com/watch?v=B_HSa1dEL9s'

# res = get_info_url(url)

# for key in res.keys():
#     print(f'{key}: {res[key]}','\n')

query = 'waht is love'
vds = get_info_search(query)

for vd in vds:
    del vd['ytdl']
    print(vd,'\n')
# for key in vds.keys():
#     print('\n',f'{key}: {vds[key]}')
    
# print(len(vds['entries']))