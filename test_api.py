from tubemp3.api_deizer import get_info_music


music1 = get_info_music('the landing first man')

for key, value in music1.items():
    print(f"{key}: {value}")


print("\n",10*"=+=","\n")

music2 = get_info_music("lithium nirvana")

for key, value in music2.items():
    print(f"{key}: {value}")


