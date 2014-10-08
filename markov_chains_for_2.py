#!/usr/bin/env python

from sys import argv

# from collections import Counter

import random

from string import digits


def make_text(merged_word_list):

    first_words = random.choice(merged_word_list.keys())
    value = random.choice(merged_word_list[first_words])

    next_words = first_words[1], first_words[2], value

    return_string=value.capitalize()

    while True:

        return_string += " " + value

        if next_words not in merged_word_list.keys():
            continue

        if len(return_string) < 140:

            value = random.choice(merged_word_list[next_words])

            next_words = next_words[1], next_words[2], value
        
        else:
            print return_string + "."
            break



def make_chains(filename):
    word_list={}

    with open(filename) as text_sample:
        text_sample = text_sample.read()
        words = text_sample.strip().lower().replace(digits, "").split()

        
        for i in range(len(words)-3):
            key = (words[i], words[i+1], words[i+2])
            value = words[i+3]
            word_list[key] = word_list.get(key, [value])

    return word_list



def link_chains(word_list_1, word_list_2):

    merged_word_list = dict(word_list_1.items() + word_list_2.items())

    make_text(merged_word_list)

    



def main(filename_1, filename_2):

    word_list_1 =  make_chains(filename_1)

    word_list_2 = make_chains(filename_2)

    link_chains(word_list_1, word_list_2)


  

if __name__ == "__main__":
    main(argv[1], argv[2])
