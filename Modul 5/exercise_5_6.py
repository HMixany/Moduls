def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        new_text = text.split(' ')
        for word in new_text:
            word = word.replace('.', '').replace(',', '').replace('!', '')
            for spam in spam_words:
                if spam.lower() in word.lower() and len(spam) == len(word):
                    return True
    else:
        for spam in spam_words:
            if text.lower().find(spam.lower()) != -1:
                return True
    return False
