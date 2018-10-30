import csv
from utilities.feature_engineering import *
# from utilities.feature_engineering import *

def to_csv(docs, labels):
    contact_email = find_emails(docs)
    minor = find_words(docs, 'minor')
    geo_location = find_words(docs, 'geo-location')
    vendors = find_words(docs, 'vendors')
    print('----Done Finding Words!----')

    sell_words = ['sell', 'selling', 'sold', 'sale']
    share_words = ['share','sharing', 'disclosing', 'discloses']
    # not_words = ['not', 'wouldn\'t', 'no', 'don\'t']
    sell_personal = phrase_matcher(docs, sell_words)
    share_personal = phrase_matcher(docs, share_words)
    print('----Done Phrase Matching!----')

    #provided by Dixon
    smog_index = smog(docs)
    fog_index = fog(docs)
    avg_sentence_length = avg_sent_len(docs)
    flesch_reading_ease = reading_ease(docs)
    dale_chall_readability_score = dale_read_score(docs)
    print('----Done Readability!----')

    #creating the csv file
    with open('newcsv.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['iD', 'minor', 'geo-location', 'contact_email',
                    'vendors', 'sell_personal', 'share_personal', 'smog_index', 'fog_index', 'avg_sentence_length',
                    'flesch_reading_ease', 'dale_chall_readability_score', 'Score'])
        for iD in Docs:
            writer.writerow([iD, minor[iD], geo_location[iD], contact_email[iD], vendors[iD],
            sell_personal[iD], share_personal[iD], smog_index[iD], fog_index[iD],
            avg_sentence_length[iD], flesch_reading_ease[iD], dale_chall_readability_score[iD], labels[iD]])
