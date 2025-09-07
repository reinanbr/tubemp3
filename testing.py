import os
import subprocess
import sys
from kitano import puts



#using files code on tests directory

from tests.test_get_info import test_get_info_music
from tests.test_get_link import test_get_link
from tests.test_music_download import test_download

def run_all_tests():
    puts('running get info music test...')
    test_get_info_music()
    puts('running get link test...')
    test_get_link()
    puts('running music download test...')
    test_download()
    puts("All tests passed!")
