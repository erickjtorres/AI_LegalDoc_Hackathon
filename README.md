# AI Legal Documents Hackathon
The goal of the hackathon was to engineer features and fit a model that will correctly predict the GDPR scores of legal documents.

##  Dependencies:
* python 3.0
* scikit-learn
* numpy
* spacy (and english model)
* nltk 
* textstat

## Instructions
1. The dataset is a corpus of privacy notices which have been extracted by a web crawler and a list of scores associated with each document ID. The document’s ID appears in the filename.
2. You are first required to extract features from the textual documents, document***.txt . The list of features that you should extract is given in the table below. Further resources and tips for how to extract the feature using python code are also given. We also specify recommended python libraries for performing the task, but you are free to use any approach or tool.
3. Read the description of each feature carefully and integrate the code into your main code so that it generates a feature set which might look like the example feature set in example.csv.
4. Normalize your feature set and combine the labels provided in training labels.csv. Note that the labels are integers between 1 and 5, representing the strength of the document. 5 is the highest.
5. Split your dataset into training and testing, use cross-validation or otherwise.
6. Apply a machine learning multi-classifier to the labeled, normalized, training set. You might want to start from the multi-logistic classifier example with the IRIS dataset in scikit-learn.
7. Use the F1-score to assess the performance of the multi-classifier.
8. Optionally, assess the model for over-fitting.
9. When you receive the testing corpus (note this is not provided at the beginning of the hackathon), apply your model to the processed text documents and generate scores. Store your results in a file with document Id and predicted score. See sample submission.csv. Note that the submission need not be sorted by id.

## Scoring
The team with the highest mean f1-score on the submitted model output will win the competition.
There are currently prizes for the top three teams who may be required to give a quick presentation
at GCSI 2018. Good luck!