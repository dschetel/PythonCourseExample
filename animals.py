# Script to return the sound of an animal based on their name
# Input: animal name
# Output: animal sound

import sys

from dog import dog
from cat import cat
from cow import cow
from goat import goat
from mouse import mouse
from niels_giraffe import giraffe

def default():
    print('Hello')

def main():
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'giraffe':
        giraffe()
    elif sys.argv[1] == 'goat':
        goat()
    elif sys.argv[1] == 'mouse':
        mouse()
    elif sys.argv[1] == 'cow':
        cow()
    else:
        default()

main()
