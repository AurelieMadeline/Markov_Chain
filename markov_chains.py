#!/usr/bin/env python
# songs_lyrics1=open("Bonobo.txt", "r")
# songs_lyrics2=open("Ellery.txt", "r")

from sys import argv
from string import punctuation
from string import digits

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    #populates dictionary of words and frequency for song_lyrics_first

    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main(song_lyric_choices):
    word_list={}
    # Change this to read input_text from a file
    nonwords = punctuation + digits

    #reads file
    with open(songs_lyric_choices[1]) as song_lyrics_first:
        for line in song_lyrics_first:
            aline = line.strip().lower()

            #removes nonalpha characters
            for char in nonwords:
                aline = aline.replace(char, "")

            #returns list of words
            aline = aline.split()

    



    with open(song_lyric_choices[2]) as song_lyrics_second:

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main(argv[1], argv[2])