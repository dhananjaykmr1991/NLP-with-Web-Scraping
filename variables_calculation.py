from typing import List
import re
import read_data
from nltk.tokenize import regexp_tokenize,sent_tokenize,SyllableTokenizer,word_tokenize,RegexpTokenizer
from nltk.corpus import stopwords

def positive_score(words):
    p_score= [1 for i in words if i in read_data.get_positive_words()]
    return p_score

def negative_score(word):
    n_score = [1 for i in word if i in read_data.get_negative_words()]
    return n_score


def AverageSentenceLength(data):
    tk = RegexpTokenizer('\s+', gaps=True)
    words = tk.tokenize(data)
    sentence=sent_tokenize(data)
    return words,sentence

def percentage_of_complex_words(data):
    tk = RegexpTokenizer('\s+', gaps=True)
    word = tk.tokenize(data)
    syt = SyllableTokenizer()
    comp_word_count = [i for i in word if len(syt.tokenize(i))>2]
    return comp_word_count

def fog_index(data):
    sentence = sent_tokenize(data)
    sentence_word_count = [len(i) for i in sentence]
    sum=0
    for i in sentence_word_count: sum+=i
    try:
        return sum/len(sentence_word_count)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
        return 0

def word_count(data):
    data1=re.sub("[^0-9a-zA-Z '-]+", " ",data)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data1)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    return filtered_sentence


def syllable_count_per_word(data):
    tk = RegexpTokenizer('\s+', gaps=True)
    words=tk.tokenize(data)
    no_end1 = [re.sub(r'es$', ' ', i) for i in words]
    no_end2 = [re.sub(r'ed$', ' ', i) for i in no_end1]
    listToStr = ' '.join([str(elem) for elem in no_end2])
    print(listToStr)
    output2 = [i for i in listToStr if i in ['a', 'e', 'i', 'o', 'u']]
    try:
        a = len(output2) / len(no_end2)
        return round(a, 3)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")

def personal_pronouns(data):
    r = re.compile(r'\bi\b | \bwe\b | \bmy\b| \bus\b | \bour\b', flags=re.I | re.X)
    pro_count=r.findall(data)
    return len(pro_count)

def average_word_length(data):
    tk = RegexpTokenizer('\s+', gaps=True)
    words = tk.tokenize(data)
    chr_list = re.sub(r'', ',', data)
    try:
        a=len(chr_list) / len(words)
        return a
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
