from nltk.corpus import wordnet
#improve using stemming --> https://www.nltk.org/api/nltk.stem.html
def find_similar(lst_words):
    """Takes an array of words and returns a set of closely related words"""
    new_words = []
    for word in lst_words:
        try:
            syn = wordnet.synsets(word)[0]
            lemmas = syn.lemmas()
        except:
            new_words.append(word)
            break;
        for lemma in lemmas:
            new_words.append(lemma.name())
            related_forms = lemma.derivationally_related_forms()
            for form in related_forms:
                new_words.append(form.synset().name().split('.')[0])
    return set(new_words)


x = [ 'gathering', 'delete', 'gather', 'record', 'process', 'breach', 'receive',  'Review', 'templates', 'constitute', 'data', 'definition', 'processed', 'erased', 'intended', 'have', 'completed', 'public', 'copies', 'deleted', 'needs', 'to', 'obtained', 'provide', 'obtains', 'sets', 'breaches', 'communicate', 'disclosure', 'disclose', 'been', 'transferred', 'use', 'disclosed', 'Article', 'share', 'for', 'individuals', 'name', 'collect', 'obtain', 'with', 'transferring', 'shares', 'protect', 'changes', 'require', 'retain', 'Individuals', 'processes', 'notify', 'Access', 'Correct', 'Erase', 'Export', 'keeping', 'hold', 'manage', 'originates', 'Insert', 'used', 'collected', 'Sharing', 'treated', 'keep', 'rights', 'using', 'store', 'received', 'records', 'protecting', 'be', 'handle', 'shared', 'complete', 'remove', 'complies', 'transfer', 'enter', 'privacy', 'preferences', 'decrypted', 'collection', 'constitutes', 'from', 'considered', 'sharing', 'means', 'Processing', 'collecting', 'database', 'controllers', 'taken', 'comes', 'update', 'transparent', 'upon', 'regarding', 'refers', 'you', 'includes', 'handled', 'defined', 'find', 'sending', 'affecting', 'protected', 'transmit', 'transmitted', 'needed', 'remains', 'retaining', 'rectify', 'uses', 'required', 'held', 'holds', 'keeps', 'purposes', 'relates', 'called', 'ensure', 'anonymise', 'Categories', 'erasing', 'view', 'after', 'prevent', 'access', 'party', 'violations', 'communicated', 'stored', 'courts', 'Communications', 'inputting', 'forwarded', 'outlined', 'concerning', 'protection', 'sent', 'acquired', 'kept', 'entered', 'send', 'stores', 'add', 'trained', 'handling', 'involving', 'including', 'encrypted', 'maintain', 'covered', 'compromised', 'included', 'safeguarded', 'limit', 'disclosing', 'managed', 'gathered', 'sell', 'given', 'treat', 'special', 'information', 'rectified', 'reuse', 'Description', 'investigate', 'breachs', 'between', 'holder', 'corrected', 'Storing', 'collects', 'about', 'over', 'VII', 'captured', 'rocessing', 'immigration', 'towards', 'accessed', 'containing', 'save', 'include', 'Loss', 'breached', 'belong', 'transmitting', 'comprises', 'username', 'Using', 'supply', 'Providing', 'deleting', 'secure', 'are', 'Recitals', 'exploit', 'excluding', 'except', 'subject', 'affect', 'involved', 'transfers', 'Impact', 'PI', 'provided', 'categories', 'submit', 'pass', 'email', 'by', 'receives', 'submitting', 'face', 'and/or', 'Disclosing', 'safeguard', 'correcting', 'correct', 'onto', 'corrects', 'health', 'Holding', 'House', 'security', 'person', 'boss', 'retains', 'need', 'get', 'securing', 'around', 'consent', 'flows', 'Protect', 'made', 'account', 'destroy', 'request', 'indicated', 'contain', 'see', 'secrecy', 'subsidiaries', 'granted', 'reveal', 'providing', 'referred', 'Retention', 'To', 'concerns', 'Securing', 'stating', 'Without', 'running', 'furnishing', 'requirements', 'erase', 'move', 'rely', 'retained', 'give', 'money', 'Updating', 'analyse', 'submitted', 'removed', 'involves', 'set', 'overlap', 'inaccurate', 'mining', 'mined', 'manages', 'what', 'takes', 'understand', 'amend', 'controller', 'say', 'policies', 'Allego', 'depends', 'Tool', 'identify', 'publish', 'treats', 'maintains']
