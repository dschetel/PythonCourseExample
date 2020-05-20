# Script to return the sound of an animal based on their name
# Input: animal name
# Output: animal sound

import sys
from cat import cat

def default():
    print('Hello')

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()

main()
