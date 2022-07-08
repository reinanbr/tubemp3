from tubemp3 import search_ytdl_plus as syp

vds = syp('garçon')

for vd in vds:
    print(vd)
    print('')