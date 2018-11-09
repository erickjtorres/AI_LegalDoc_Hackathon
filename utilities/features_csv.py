import csv
from utilities.feature_engineering import *
# from utilities.feature_engineering import *

def to_csv(docs, labels, csv_name):
    contact_email = find_emails(docs)
    minor = find_words(docs, 'minor')
    geo_location = find_words(docs, 'geo-location')
    vendors = find_words(docs, 'vendors')
    print('----Done Finding Words!----')

    sell_words = ['sell', 'selling', 'sold', 'sale', 'furnishing', 'consent']
    share_words = ['share','sharing', 'disclosing', 'discloses', 'public', 'provide']
    # not_words = ['not', 'wouldn\'t', 'no', 'don\'t']
    sell_personal = phrase_matcher(docs, sell_words)
    share_personal = phrase_matcher(docs, share_words)
    print('----Done Phrase Matching!----')

    #cookies --> needs work
    cookies = find_list(docs, 'Cookies')
    print('----Done finding Cookies!----')

    #provided by Dixon
    #smog is useless!!!
    # smog_index = smog(docs)
    fog_index = fog(docs)
    print('----Done fog index!----')
    avg_sentence_length = avg_sent_len(docs)
    print('----Done avgerage sentence length!----')
    flesch_reading_ease = reading_ease(docs)
    print('----Done flesch reading ease!----')
    dale_chall_readability_score = dale_read_score(docs)
    print('----Done Readability!----')

    #creating the csv file
    with open(csv_name + '.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['iD', 'minor', 'geo-location', 'contact_email',
                    'vendors', 'sell_personal', 'share_personal', 'cookies', 'fog_index', 'avg_sentence_length',
                    'flesch_reading_ease', 'dale_chall_readability_score', 'Score'])
        for iD in docs:
            writer.writerow([iD, minor[iD], geo_location[iD], contact_email[iD], vendors[iD],
            sell_personal[iD], share_personal[iD], cookies[iD], fog_index[iD],
            avg_sentence_length[iD], flesch_reading_ease[iD], dale_chall_readability_score[iD], labels[iD]])
