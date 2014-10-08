#!/usr/bin/env python

from sys import argv

from collections import Counter

import random


# def make_text(merged_word_list):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""

#     max_words = 40

#     first_words = random.choice(merged_word_list.keys())

#     for i in range(max_words):

#         next_words = merged_word_list.get(first_words, None)

#         if next_words == None:
#             # if the start isn't in map, we got to the end of the
#             # original text, so we have to start again.
#             make_text(max_words-i)
#             return

#         # choose a random suffix
#         word = random.choice(next_words)

#         print word,

#         first_words = new_words(first_words, word)

#     print "."

def make_text(word_list):

    max_words = 40

    first_words = random.choice(word_list.keys())

    for i in range(max_words):
        next_words = word_list.get(first_words, None)

        if next_words == None:
            make_text(max_words-i)
            return

        word = random.choice(next_words)

        if i == 0:
            print word.capitalize(),
        elif i == max_words-1:
            print word + "."
        else:
            print word,

        first_words = new_words(first_words, word)

#want to modify function to check for period after value, to capitalize following value


def new_words(first_words, word):

    return first_words[1:] + (word,)


    #with merged_word_list error is TypeError: cannot concatenate 'str' and 'tuple' objects



def make_chains(filename):
    word_list={}

    with open(filename) as text_sample:
        text_sample = text_sample.read()
        words = text_sample.strip().lower().split()

        
        for i in range(len(words)-3):
            key = (words[i], words[i+1], words[i+2])
            value = words[i+3]
            word_list[key] = word_list.get(key, [value])

    return word_list


# def link_chains(word_list_1, word_list_2):

#     word_list_1, word_list_2 = set(word_list_1), set(word_list_2)

#     merged_word_list = dict(word_list_1 | word_list_2)

#     # print type(merged_word_list) prints <type 'dict'>



# def main(filename_1, filename_2):

#     word_list_1, word_list_2 =  make_chains(filename_1), make_chains(filename_2)

#     merged_word_list = link_chains(word_list_1, word_list_2)

#     # new_text = make_text(merged_word_list)

def main(filename):
    word_list = make_chains(filename)

    output_text = make_text(word_list) 


    

if __name__ == "__main__":
    # main(argv[1], argv[2])
    main(argv[1])
