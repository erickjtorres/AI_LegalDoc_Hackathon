import spacy
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from spacy.matcher import PhraseMatcher
from utilities.readability import *


nlp = spacy.load('en')
#To-Do:
#Add or remove stemming? --> perhaps words can appear in different plurals and forms

#Combine find_words and find_emails later
def find_words(docs, word):
    """finds if a word exists in the corpus and returns a
    dictionary with the id of the document as the key and a binary number as the value"""
    dict = {}
    regular = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
    #regular2 = re.compile(r'\bminors\b', re.IGNORECASE) --> add plurals or multiple words later
    for iD in docs:
        if (re.search(regular, docs[iD])):
            dict[iD] = 1
        else:
            dict[iD] = 0
    return dict

#perhaps the email isnt even the contact?
def find_emails(docs):
    """finds if an email exists in the corpus and returns a
    dictionary with the id of the document as the key and a binary number as the value"""
    dict = {}
    #this regular expression may need work
    regular = re.compile(r'[\w\.-]+@[\w\.-]+')
    for iD in docs:
        if (re.search(regular, docs[iD])):
            dict[iD] = 1
        else:
            dict[iD] = 0
    return dict

#this function needs work! --> sometimes does not return the original word
def find_similar(lst_words):
    """Takes an list of words and returns a set of closely related words"""
    new_words = []
    for word in lst_words:
        try:
            #turn the words into a syssets object
            syn = wordnet.synsets(word)[0]
            new_words.append(stem(word))
            new_words.append(word)
            #find the lemmas
            lemmas = syn.lemmas()
        except:
            #if the words does not have any lemmas just append it
            new_words.append(word)
            break;
        #iterate the lemmas and append while also finding related words to each lemma
        for lemma in lemmas:
            new_words.append(lemma.name())
            related_forms = lemma.derivationally_related_forms()
            for form in related_forms:
                new_words.append(form.synset().name().split('.')[0])
    return set(new_words)

def stem(word):
    """Returns the an array with the removed stem of the word"""
    stemmer = PorterStemmer()
    new_word = stemmer.stem(word)
    return new_word

def find_list(docs, word):
    """Creates a list of similar words and finds if those words exist in the corpus. Returns a dict"""
    dict_ = {}
    matcher = PhraseMatcher(nlp.vocab)
    terminology_list = find_similar([word])
    patterns = [nlp(text) for text in terminology_list]
    matcher.add('TerminologyList',  *patterns)
    for iD in docs:
        texts = nlp(docs[iD])
        for sents in texts.sents:
            sents = sents.as_doc()
            matches = matcher(sents)
            #looks at data because personal is not important in this case its an "amod" of data
            if len(matches) > 0 and (iD not in dict_ or dict_[iD] == 0):
                dict_[iD] = 1
            elif iD in dict_:
                dict_[iD] = dict_[iD]
            else:
                dict_[iD] = 0
    return dict_
# # helper function to phrase_matcher()
# def found_match(matcher, doc, i, matches):
#     #there has to be a smarter way of gaining access to variables bellow
#     if doc[matches[0][1]+1].head.text in lst_words and iD not in dict_:
#         dict_[iD] = 1
#     elif doc[matches[0][1]+1].head.text not in lst_words:
#         dict_[iD] = 0

# this functions (and the helpers) will need work if we want to also see for "not selling or not sharing"
# however i found those features redundant
def phrase_matcher(docs, lst_words, keyword=['personal data']):
    """Checks if a list of words relating to a keyword(s) are in a corpus and returns a dictionary
    with document ID as keys and a binary number as a value"""
    dict_ = {}
    matcher = PhraseMatcher(nlp.vocab)
    #keywords in this case is personal data
    terminology_list = keyword
    patterns = [nlp(text) for text in terminology_list]
    matcher.add('TerminologyList',  *patterns)

    for iD in docs:
        texts = nlp(docs[iD])
        for sents in texts.sents:
            sents = sents.as_doc()
            matches = matcher(sents)
            #looks at data because personal is not important in this case its an "amod" of data
            if len(matches) > 0 and sents[matches[0][1]+1].head.text in lst_words and (iD not in dict_ or dict_[iD] == 0):
                dict_[iD] = 1
            elif iD in dict_:
                dict_[iD] = dict_[iD]
            else:
                dict_[iD] = 0
    return dict_

#helper function for find_associated
# def append_assoc(matcher, doc, i, matches):
#     if doc[matches[0][1]+1].head.text not in associated:
#         associated.append(doc[matches[0][1]+1].head.text)
#     print("{0}/{1} <--{2}-- {3}/{4}".format(
#         doc[matches[0][1]+1].text, doc[matches[0][1]+1].tag_, doc[matches[0][1]+1].dep_, doc[matches[0][1]+1].head.text, doc[matches[0][1]+1].head.tag_))

def find_associated(word, docs):
    """Returns a list of words that are associated with a word in sentences belonging to texts of a corpus"""
    associated = []
    matcher = PhraseMatcher(nlp.vocab)
    terminology_list = [keyword]
    patterns = nlp(word)
    matcher.add('TerminologyList',*patterns)

    for iD in docs:
        texts = nlp(docs[iD])
        for sents in texts.sents:
            sents = sents.as_doc()
            matches = matcher(sents)
            if len(matches) > 0 and doc[matches[0][1]+1].head.text not in associated:
                associated.append(doc[matches[0][1]+1].head.text)
    return associated

#Another idea i had was to check if these words and similar existed in the same sentence of personal data
# matcher2 = PhraseMatcher(nlp.vocab)
# sell_words = ['sell', 'selling', 'sold', 'sale']
# share_words = ['share','sharing', 'disclosing', 'discloses']
# similarwords = word_finder.find_similar(sell_words)
# patterns = [nlp(text) for text in similarwords]
# matcher2.add('TerminologyList', None, *patterns)

# matcher3 = PhraseMatcher(nlp.vocab)
# not_words = ['not', 'wouldn\'t', 'no', 'don\'t']
# similarwords = word_finder.find_similar(not_words)
# patterns = [nlp(text) for text in similarwords]
# matcher3.add('TerminologyList', None, *patterns)


# READIBILITY FUNCTION --> Using Functions provided by Matthew Dixon
# def readibility_function(docs):
#     dale = {}
#     flesch = {}
#     smog = {}
#     fog = {}
#     for iD in docs:
#         dale[iD] = dale_chall_readability_score(docs[iD])
#         flesch[iD] = flesch_reading_ease(docs[iD])
#         smog[iD] = smog_index(docs[iD])
#         dict[iD] = gunning_fog(docs[iD])


def dale_read_score(docs):
    dict = {}
    for iD in docs:
        dict[iD] = dale_chall_readability_score(docs[iD])
    return dict

def reading_ease(docs):
    dict = {}
    for iD in docs:
        dict[iD] = flesch_reading_ease(docs[iD])
    return dict

#smog index is useless
# def smog(docs):
#     dict = {}
#     for iD in docs:
#         dict[iD] = smog_index(docs[iD])
#     return dict

def fog(docs):
    dict = {}
    for iD in docs:
        dict[iD] = gunning_fog(docs[iD])
    return dict

def avg_sent_len(docs):
    dict = {}
    for iD in docs:
        dict[iD] = avg_sentence_length(docs[iD])
    return dict
