from tubemp3 import get_from_link as gfl

tst = gfl(url='https://youtube.com/watch?v=B_HSa1dEL9s')

# for typ in tst.types.keys():
#     print('\n',10*'=+=')
#     print(typ)
    
# print(tst.types['m4a'])

tst.download_mp3('for_the.mp3')

#print(tst.formats)

print(tst.get_info_music())
