from tubemp3.api import search_music,get_info_link
from tubemp3.file import download 
from sys import argv



def main():
    command_dict = {'file':False,'link':False,'search':False}
#    print(argv)
    for command in argv:
        if '.mp3' in command:
            command_dict['file'] = command
        if 'https:' in command:
            command_dict['link'] = command
        if len(command.split(' ')) > 1:
            command_dict['search'] = command

    print('tube search info:')
    for key,value in command_dict.items():
        print(f'{key}: {value}')

    music = search_music(command_dict['search']) if command_dict['search'] else get_info_link(command_dict['link'])
    if music:
        return download(music,path=command_dict['file'])
    else:
        return music
    


if __name__=='__main__':
    main()
