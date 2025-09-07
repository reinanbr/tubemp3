from test_get_info import test_get_info_music
from test_get_link import test_get_link
from test_music_download import test_download
from kitano import puts


def run_all_tests():
    puts('=+=+=+=+=+=+= running get info music test... =+=+=+=+=+=+=')
    test_get_info_music()
    puts('=+=+=+=+=+=+= running get link test... =+=+=+=+=+=+=')
    test_get_link()
    puts('=+=+=+=+=+=+= running music download test... =+=+=+=+=+=+=')
    test_download()
    puts("All tests passed!")


if __name__ == "__main__":
    run_all_tests()