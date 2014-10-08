#!/usr/bin/env python
# songs_lyrics1=open("Bonobo.txt", "r")
# songs_lyrics2=open("Ellery.txt", "r")

from sys import argv
from string import punctuation
from string import digits


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."


def make_chains(filename):
    word_list={}
    with open(filename) as song_lyrics_text:
        txt = song_lyrics_text.read()
        words = txt.strip().lower().split()
    # print words

            #removes nonalpha characters
            # for char in nonwords:
            #     aline = aline.replace(char, "")

            #returns list of words
            # words = aline.split() 
        
        for i in range(len(words)-2):
            key = (words[i], words[i+1])
            value = words[i+2]
            word_list[key] = word_list.get(key, [value])
            # if key not in word_list.keys():
            #     word_list[key] = [value]
            # else:
            #     word_list[key].append(value)

    return word_list


    #print word_list


    # with open(song_lyric_choices[2]) as song_lyrics_second:

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

def main(song_lyrics1, songs_lyrics2):
    song_1 = make_chains(song_lyrics1)
    song_2 = make_chains(songs_lyrics2)


    make_text(song_1)
    make_text(song_2)
    
    # Change this to read input_text from a file
    # nonwords = punctuation + digits

    #reads file

if __name__ == "__main__":
    main(argv[1], argv[2])