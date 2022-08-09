from tubemp3 import get_from_link as gfl

tst = gfl(url='https://youtu.be/TLCyHgQOXtw')

# for typ in tst.types.keys():
#     print('\n',10*'=+=')
#     print(typ)
    
# print(tst.types['m4a'])

# tst.download()

print(tst.formats)

tst.download_video()