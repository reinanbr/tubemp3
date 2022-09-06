from tubemp3 import get_from_link as gfl

tst = gfl(url='https://music.youtube.com/watch?v=B_HSa1dEL9s')

# for typ in tst.types.keys():
#     print('\n',10*'=+=')
#     print(typ)
    
# print(tst.types['m4a'])

# tst.download()

#print(tst.formats)

print(tst.get_info_music())
