import pandas as pd
import numpy as np
import re
import math
from collections import defaultdict

"""# **Task-1**

1. for sentences given in assignment file.
"""

# creating a function for preprocessing
def preprocess(corpus):
    cleaned_corpus = []
    for doc in corpus:
        cleaned_doc = re.sub(r'[^\w\s]', '', doc).lower()
        cleaned_corpus.append(cleaned_doc)
    return cleaned_corpus

corpus = [
    'this is the first document Document.',
    'this is the second ',
    'this document is the third document.',
    'and this is the fourth one.',
    'is this the fifth document?'
]

cleaned_corpus = preprocess(corpus)
print(cleaned_corpus)

# creating a function for getting Unique words
def get_distinct_words(corpus):
    words = set()
    for document in corpus:
        words.update(document.split())
    return words

distinct_words = get_distinct_words(cleaned_corpus)
print(distinct_words)

# function for calculating TF
def cal_tf(corpus, distinct_words):
    tf = []
    for document in corpus:
        word_count = defaultdict(int)
        for word in document.split():
            word_count[word] += 1
        document_tf = {}
        for word in distinct_words:
            document_tf[word] = word_count[word]
        tf.append(document_tf)
    return tf

tf = cal_tf(cleaned_corpus, distinct_words)
print(tf)

# function for calculating IDF
def cal_idf(corpus, distinct_words):
    idf = {}
    total_documents = len(corpus)
    for word in distinct_words:
        doc_freq = 0
        for document in corpus:
            if word in document.split():
                doc_freq += 1
        idf[word] = math.log(total_documents / doc_freq) + 1
    return idf

idf = cal_idf(cleaned_corpus, distinct_words)
print(idf)

# function for calculating score

def cal_tf_idf(tf, idf):
    tf_idf = []
    for document_tf in tf:
        document_tf_idf = {}
        for word, value in document_tf.items():
            document_tf_idf[word] = value * idf[word]
        tf_idf.append(document_tf_idf)
    return tf_idf

tf_idf = cal_tf_idf(tf, idf)

print(tf_idf)

#creating the dataframe
df = pd.DataFrame(tf_idf, index=range(len(corpus)), columns=sorted(list(distinct_words)))
print(df)

"""# **Task-2**
2. for the 4 documents.
"""

# Read the contents of files
file_names=['/content/document_1.txt','/content/document_2.txt','/content/document_3.txt','/content/document_4.txt']

def prepro(document_names):
    word_count_dict = {}
    total_word_count_dict = {}

    for file in document_names:

            # Extract document name without file extension
            doc_name = file.split('/')[-1].split('.')[0]

            # Read the document
            with open(file,'r') as f:
             text=f.read()
             print(f'Content of {doc_name}:')
             print(text)
             print('\n')


            # Remove punctuation and convert to lowercase
            text = re.sub(r'[^\w\s]', '', text)
            words = text.lower().split()

            # Create a dictionary for word counts
            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1

            # Store word counts and total word count
            word_count_dict[doc_name] = dict(word_count)
            total_word_count_dict[doc_name] = len(words)

    return word_count_dict, total_word_count_dict

word_count_dict, total_word_count_dict = prepro(file_names)

print("Word Count Dictionary:")
for document, word_count in word_count_dict.items():
    print(f"{document}: {word_count}")

print("\nTotal Word Count Dictionary:")
for document, total_word_count in total_word_count_dict.items():
    print(f"{document}: {total_word_count}")

def calculate_tf(word_count_dict, total_word_count_dict):
    tf_dict = {}

    for document, word_count in word_count_dict.items():
        tf = {}
        total_words = total_word_count_dict[document]
        for word, count in word_count.items():
            tf[word] = count / total_words  # here i am taking average but in quetion its only mention count
        tf_dict[document] = tf

    return tf_dict

tf_dict = calculate_tf(word_count_dict, total_word_count_dict)

print("\nTerm Frequency (TF) Dictionary:")
for document, tf in tf_dict.items():
    print(f"{document}: {tf}")

def calculate_idf(word_count_dict):
    idf_dict = {}
    total_documents = len(word_count_dict)

    # Calculate document frequency (df) for each word
    df = {}
    for document, word_count in word_count_dict.items():
        for word in word_count.keys():
            df[word] = df.get(word, 0) + 1

    # Calculate IDF for each word
    for word, doc_freq in df.items():
        idf = math.log(total_documents / doc_freq) + 1
        idf_dict[word] = idf

    return idf_dict

idf_dict = calculate_idf(word_count_dict)

print("Inverse Document Frequency (IDF) Dictionary:\n")
for word, idf in idf_dict.items():
    print(f"{word}: {idf}")

def score(tf_dict, idf_dict):
    tf_idf_dict = {}

    for document, tf in tf_dict.items():
        tf_idf = {}
        for word, tf_value in tf.items():
            tf_idf[word] = tf_value * idf_dict.get(word, 0)
        tf_idf_dict[document] = tf_idf

    return tf_idf_dict

tf_idf_dict = score(tf_dict, idf_dict)

print("\nTF-IDF Dictionary:")
for document, tf_idf in tf_idf_dict.items():
    print(f"{document}: {tf_idf}")

def dataframe(tf_idf_dict):

    # Get all unique words
    words = set()
    for tf_idf in tf_idf_dict.values():
        words.update(tf_idf.keys())

    # Create DataFrame
    df = pd.DataFrame(index=tf_idf_dict.keys(), columns=sorted(list(words)))

    # Fill DataFrame with TF-IDF values
    for document, tf_idf in tf_idf_dict.items():
        for word, value in tf_idf.items():
            df.loc[document, word] = value

    return df

tf_idf_df =dataframe(tf_idf_dict)

# Fill NaN values with 0
pd.set_option('future.no_silent_downcasting', True) # to avoid future waring
tf_idf_df.fillna('0.0000', inplace=True)

print(tf_idf_df)
