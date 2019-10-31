#!/usr/bin/env python
# coding: utf-8

import string
import nltk
import pandas as pd
from nltk.corpus import wordnet
from spacy.lang.en import English
from nltk.stem import WordNetLemmatizer, SnowballStemmer

def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

def get_lemma(word):
    return sb.stem(word)

def prepare_text_for_ML(text):
    tags_to_keep = ['JJ', 'NN', 'NNP', 'NNPS', 'NNS']
    tokens = tokenize(text)
    tagged = [token for token in tokens if nltk.pos_tag([token])[0][1] in tags_to_keep]  # Keep certain POS tags.
    tokens = [token for token in tokens if wordnet.synsets(token)]  # Return only English text.
    tokens = [token for token in tokens if token not in en_stop]  # Remove stop-words.
    tokens = [x for x in tokens if not isinstance(x, int)]  # Remove integers.
    tokens = [x for x in tokens if len(x) > 3]  # Remove words with less than 3 letters.
    tokens = [get_lemma(token) for token in tokens]  # Lemmatize words.
    return tokens

if '__main__' == __name__:

    nltk.download('words')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

    sb = SnowballStemmer('english')
    words = set(nltk.corpus.words.words())
    parser = English()
    numbers = list(range(1, 200))
    en_stop = list(set(nltk.corpus.stopwords.words('english'))) + list(string.punctuation) + ['switzerland', 'swiss',
                                                                                              'canton', 'spain', 'catalan',
                                                                                              'spanish'] + numbers
    dataset = pd.read_excel('./data/swiss_foundations.xlsx', encoding='utf-8')
    dataset = dataset.fillna('')
    corpus = []
    for grams in dataset['Mission']:
        corpus.append(grams)
    swiss_corpus = corpus
    dataset = pd.read_excel('./data/spanish_dataframe_english.xlsx',encoding='utf-8')

    dataset = dataset[['Activities', 'Areas_Activity', 'Clasificacion', 'Clasificacion_Specifies', 'Codig_Activity', 'Ends', 'History', 'Sectors attended: Cultural, investigation, environment or cooperation', 'Sectors attended: social services and health', 'Type_activities']]
    dataset = dataset.fillna('')

    dataset['Combined'] = list(zip(dataset.Ends, dataset.Activities, dataset.Codig_Activity, dataset.History))
    corpus = []
    for grams in dataset['Combined']:
        corpus.append((' '.join([w + ' ' for w in grams])).strip())
    spanish_corpus = corpus
    spanish_corpus_fines_only = list(dataset['Ends'])
    preprocessed_swiss, preprocessed_spanish = [], []
    for swiss_line in swiss_corpus:
        preprocessed_swiss.append(prepare_text_for_ML(swiss_line))
    for spanish_line in spanish_corpus:
        preprocessed_spanish.append(prepare_text_for_ML(spanish_line))
    preprocessed_both = preprocessed_swiss + preprocessed_spanish

    preprocessed_spanish_fines_only = []

    for spanish_line in spanish_corpus_fines_only:
        preprocessed_spanish_fines_only.append(prepare_text_for_ML(spanish_line))

    preprocessed_both_fines_only = preprocessed_swiss + preprocessed_spanish_fines_only

    joined_both_data_fines_only = []

    for el in preprocessed_both_fines_only:
        joined_both_data_fines_only.append(' '.join(el))

    with open('./data/preprocessed_both_fines_only.txt', 'w') as f:
        for item in joined_both_data_fines_only:
            f.write("%s\n" % item)
