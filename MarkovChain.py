#!/usr/bin/env python

from sys import argv

# from collections import Counter

import random

from string import ascii_uppercase

punctuation = ["@", "#", "$", "%", "&", "*", "[", "]", "{", "}", "/", "(", ")"]
digits = [0,1,2,3,4,5,6,7,8,9]
end = ["?", ".", "!"]

def make_text(merged_word_list):

    while True:
        
        return_string= ""

        first_words = random.choice(merged_word_list.keys())
        value = random.choice(merged_word_list[first_words])
        
        if value in ascii_uppercase:
            return_string = value
            break
        else: 
            continue

    # next_words = first_words[1], first_words[2], value
    next_words = first_words[1], value

    return_string= ""

    while True:

        return_string += " " + value

        if next_words not in merged_word_list.keys():
            continue

        if len(return_string) < 70:

            value = random.choice(merged_word_list[next_words])

            # next_words = next_words[1], next_words[2], value
            next_words = next_words[1], value
        
        elif len(return_string) < 140:

            value = random.choice(merged_word_list[next_words])

            if value[-1] in end:
                print return_string + " " + value
                break

            # next_words = next_words[1], next_words[2], value
            next_words = next_words[1], value
        
        else:
            print return_string + "."
            break




def make_chains(filename):
    word_list={}
  
    with open(filename) as text_sample:
        text_sample = text_sample.read()
        words = text_sample.strip().replace('"', " ")
        for char in punctuation:
                words.replace(str(char), " ")
        for char in digits:
                words.replace(str(char), " ")
        words = words.split()

        
        for i in range(len(words)-2):
            key = (words[i], words[i+1])
            value = words[i+2]
            word_list.setdefault(key, []).append(value)

        # for i in range(len(words)-2):
        #     key = (words[i], words[i+1])
        #     value = words[i+2]
        #     # word_list[key] = word_list.get(key, []).append(value)
        #     word_list.setdefault(key, []).append(value)
    return word_list





def link_chains(word_list_1, word_list_2):

    useful_keys = set(word_list_1) & set(word_list_2)

    merged_word_list = dict(word_list_1.items() + word_list_2.items())

    print "There are %d points of intersection between these text samples." % len(useful_keys)

    make_text(merged_word_list)

    



def main(filename_1, filename_2):

    word_list_1 =  make_chains(filename_1)

    word_list_2 = make_chains(filename_2)

    link_chains(word_list_1, word_list_2)


  

if __name__ == "__main__":
    main(argv[1], argv[2])
