# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import string
from nltk.corpus import stopwords
from nltk import PorterStemmer

# Folder Path
directory = "/Users/rishabhgoel/Documents/Fall22/IR/citeseer"

# Change the directory
os.chdir(directory)

stopwords = set(stopwords.words('english'))

word_list = []
word_dict = {}
stem_list = []
stem_dict = {}


def tokenize(content):
    translation = str.maketrans({key: None for key in string.punctuation})
    return content.translate(translation).lower().split()


def stemmer():
    porter_stemmer = PorterStemmer()

    for word in word_list:
        if word not in stopwords:
            value = porter_stemmer.stem(word)
            stem_list.append(value)

            if value in stem_dict:
                stem_dict[value] += 1
            else:
                stem_dict[value] = 1


def calculate(token_list, token_dict, title):
    print(f"{title}\n")
    print(f"Total number of words: {len(token_list)}")
    print(f"Total number of words: {len(token_dict)}")
    print()
    print("Top 20 words in order of reducing frequencies: ")
    sorted_word_list = [ele[0] for ele in sorted(token_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[:20]]
    print(', '.join(sorted_word_list))
    print()

    print("Stopwords in top 20 are: ")
    stopwords_in_top_20 = []
    for ele in sorted_word_list:
        if ele in stopwords:
            stopwords_in_top_20.append(ele)

    if len(stopwords_in_top_20) != 0:
        print(', '.join(stopwords_in_top_20))
    else:
        print("No stopwords found")

    print()
    max_percentage_number = 0.15*(len(token_list))
    num_words = 0
    current_total = 0
    sorted_list = sorted(token_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for item in sorted_list:
        if current_total < max_percentage_number:
            current_total += item[1]
            num_words += 1

    print(f"Minimum number of unique words accounting for 15% of the total number of words in the collection: {num_words}")
    print("------------------------------------------------------------------------------------------------------\n")


def read_files(file_directory):
    for filename in os.listdir(file_directory):
        file = file_directory + '/' + filename
        f = open(file, 'r')
        content = f.read()
        tokens = tokenize(content)

        for token in tokens:
            word_list.append(token)

            if token in word_dict:
                word_dict[token] += 1
            else:
                word_dict[token] = 1

        f.close()


if __name__ == '__main__':
    read_files(directory)
    stemmer()
    calculate(word_list, word_dict, "After tokenizing and removing punctuation")
    calculate(stem_list, stem_dict, "After stemming and removing stopwords")
