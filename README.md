# Information Retrieval Assignment 1
### Rishabh Goel


### Steps to execute

<u>Method 1</u>:
1. Import the code to Pycharm 
2. Click the play button next to main

<u>Method 2</u>:
1. In terminal, navigate to the directory where your code is stored
2. Run `python main.py`


_**Note: Edit the directory in main.py where the text files are stored**_

### Functionality

#### _def read_files(file_directory)_
1. The directory location is provided from where all the files would be read
2. This function calls the **tokenize()** function which takes the read document as input and returns a tokenized list
3. These tokens are then added into the word_list as well as word_dict along with the word frequencies


#### _def tokenize(content)_
1. A translation table is created for the punctuations where each punctuation would be removed
2. The input file is translated using this table and then converted to lower case and split based on the whitespaces


#### _def stemmer()_
1. PorterStemmer() is imported from NLTK
2. All the tokens in word_list which are not stopwords are stemmed and then added to stem_list and stem_dict along with the word frequencies


#### _def calculate()_
1. Total number of words
2. Vocabulary size
3. Top 20 words in order of reducing frequencies
4. Stopwords in top 20 words
5. Minimum number of unique words accounting for 15% of the total number of words in the collection


### Result

```
Total number of words: 476198
Vocabulary size: 19886

Top 20 words in order of reducing frequencies: 
the, of, and, a, to, in, for, is, we, that, this, are, on, an, with, as, by, data, be, information

Stopwords in top 20 are: 
the, of, and, a, to, in, for, is, we, that, this, are, on, an, with, as, by, be

Minimum number of unique words accounting for 15% of the total number of words in the collection: 4
------------------------------------------------------------------------------------------------------

After stemming and removing stopwords

Total number of words: 294256
Vocabulary size: 13778

Top 20 words in order of reducing frequencies: 
system, use, data, agent, inform, model, paper, queri, user, learn, algorithm, 1, approach, problem, applic, present, base, web, databas, comput

Stopwords in top 20 are: 
No stopwords found

Minimum number of unique words accounting for 15% of the total number of words in the collection: 24
------------------------------------------------------------------------------------------------------
```


### References

https://likegeeks.com/python-remove-punctuation/#Using_nltk
https://www.geeksforgeeks.org/python-stemming-words-with-nltk/