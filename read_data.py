import os
import re


def get_stopwords() -> list[str]:
    '''
    iterating through each stopwords file and joining then togather'''
    stpwrd = ''
    for file in os.listdir("stopwords"):
        with (open(f"stopwords/{file}", "r") as f):
            data = re.sub("[^0-9a-zA-Z'-]+", " ", f.read()
                          ).lower().replace('- ', ' ').replace(' -', ' ')
            stpwrd = data + stpwrd
            f.close()
    return stpwrd.split(' ')


def get_positive_words() -> list[str]:
    '''
    Reading positive from file and Making a list'''
    with open("Pos_Neg_words/positive-words.txt") as f:
        positive_words = f.read()
        f.close()
        positive_words_list = [i.strip() for i in positive_words.split('\n')]

    return positive_words_list


def get_negative_words() -> list[str]:
    '''
    Reading positive from file and Making a list'''
    with open("Pos_Neg_words/negative-words.txt") as f:
        negative_words = f.read()
        f.close()
        negative_words_list = [i.strip() for i in negative_words.split('\n')]

    return negative_words_list



