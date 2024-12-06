# TF-IDF Feature Extraction from Scratch

This Python program replicates the functionality of scikit-learn's `TfidfVectorizer` from scratch. The program takes a list of sentences (treated as documents) and computes the Term Frequency-Inverse Document Frequency (TF-IDF) scores for each word in the corpus. The output is displayed in a DataFrame, with the columns representing unique words and the rows representing the documents.

## Tasks

### 1. Preprocessing the Text
- Remove punctuation from sentences.
- Convert all words to lowercase.
- Extract distinct words from the entire corpus.

### 2. Calculate Term Frequency (TF)
Term Frequency (TF) is calculated as the count of occurrences of a word in a given document.

\[
TF(w, \text{doc}) = \text{count}(w, \text{doc})
\]

Where:
- `count(w, doc)` is the frequency of word `w` in document `doc`.

### 3. Calculate Inverse Document Frequency (IDF)
Inverse Document Frequency (IDF) is calculated for each unique word across the corpus.

\[
IDF(w, D) = \ln \left(\frac{|D|}{1 + df(w, D)}\right)
\]

Where:
- `df(w, D)` is the Document Frequency, or the number of documents containing the word `w`.
- `|D|` is the total number of documents in the corpus.

### 4. Compute the TF-IDF Score
The TF-IDF score is calculated by multiplying the TF and IDF values for each word in a document.

\[
TF\text{-}IDF(w, \text{doc}, D) = TF(w, \text{doc}) \times IDF(w, D)
\]

### 5. Display Results in a DataFrame
The results will be displayed in a pandas DataFrame, where:
- Columns represent the unique words in the corpus.
- Rows represent the documents (sentences).

## Example

Given the following list of sentences:

```python
corpus = [
    'this is the first document Document.',
    'this is the second ',
    'this document is the third document.',
    'and this is the fourth one.',
    'is this the fifth document?'
]

         and  document  fifth  first  is  one  second  the  third  ...
document   0         1      0      1   1    0       0    1      0   ...
document2  0         0      0      0   1    0       1    1      0   ...
...
