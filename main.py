# Created By: Rishabh Goel
# Created Date: Sept 3, 2022

import os
import string
from nltk.corpus import stopwords
from nltk import PorterStemmer

# Folder Path
directory = "/Users/rishabhgoel/Documents/Fall22/IR/citeseer"

# Change the directory
os.chdir(directory)

# Set of stopwords from english
stopwords = set(stopwords.words('english'))

word_list = []
word_dict = {}
stem_list = []
stem_dict = {}


# Helper method to add item to list as well as dictionary
def add_to_list_and_dict(item, item_list, item_dict):
    item_list.append(item)

    if item in item_dict:
        item_dict[item] += 1
    else:
        item_dict[item] = 1


# Method to tokenize the text
def tokenize(content):
    translation = str.maketrans({key: None for key in string.punctuation})
    return content.translate(translation).lower().split()


# Method to stem the tokens using Porter Stemmer
def stemmer():
    porter_stemmer = PorterStemmer()

    for word in word_list:
        if word not in stopwords:
            value = porter_stemmer.stem(word)
            add_to_list_and_dict(value, stem_list, stem_dict)


# Method to read the text files from the file directory on line 10
def read_files(file_directory):
    for filename in os.listdir(file_directory):
        file = file_directory + '/' + filename
        f = open(file, 'r')
        content = f.read()
        tokens = tokenize(content)

        for token in tokens:
            add_to_list_and_dict(token, word_list, word_dict)

        f.close()


# Method to answer the questions in the assignment
def calculate(token_list, token_dict, title):
    print(f"{title}\n")
    print(f"Total number of words: {len(token_list)}")
    print(f"Vocabulary size: {len(token_dict)}")
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


# Starting point of the program
if __name__ == '__main__':
    read_files(directory)
    stemmer()
    calculate(word_list, word_dict, "After tokenizing and removing punctuation")
    calculate(stem_list, stem_dict, "After stemming and removing stopwords")
