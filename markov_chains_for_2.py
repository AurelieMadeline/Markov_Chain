#!/usr/bin/env python

from sys import argv

# from collections import Counter

import random

from string import digits



# def make_text(max_words,merged_word_list):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""

    # first_words = random.choice(merged_word_list.keys())

    # for i in range(max_words):
    #     next_words = merged_word_list.get(first_words, None)

    #     word = random.choice(next_words)

    #     if i == 0:
    #         print word.capitalize(),
    #     elif i == max_words-1:
    #         print word + "."
    #     else:
    #         print word,

    #     first_words = new_words(first_words, word)

#want to modify function to check for period after value, to capitalize following value, search for prepositions and conjunctions at end of sentence.


def make_text(merged_word_list):

    first_words = random.choice(merged_word_list.keys())
    value = random.choice(merged_word_list[first_words])

    next_words = first_words[1], first_words[2], value

    print first_words
    print value
    return_string=value.capitalize()

    while next_words in merged_word_list.keys() and len(return_string)<140:

        value = random.choice(merged_word_list[next_words])

        return_string += " " + value

        next_words = next_words[1], next_words[2], value

    print return_string + "."

    # while first_words in merged_word_list.keys():
    #     markov_sentence= start

    #     if len
        

         








# def new_words(first_words, word):

#     return first_words[1:] + (word,)



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
    # main(argv[1])
