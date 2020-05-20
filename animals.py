# Script to return the sound of an animal based on their name
# Input: animal name
# Output: animal sound

import sys
from dog import dog

def default():
    print('Hello')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()

main()
