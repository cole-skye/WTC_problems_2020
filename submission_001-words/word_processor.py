
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    lower_key = list(filter(lambda word : word, split(', .?', text.lower())))
    return lower_key


def words_longer_than(length, text):
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    texts = list(filter(lambda word : word, split(', .?', text.lower())))
    longer = list(filter(lambda word : len(word) > length, texts))
    return longer


def words_lengths_map(text):
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    texts = list(filter(lambda word : word, split(', .?', text.lower())))
    lengths = list([len(word) for word in texts])
    lengths.sort()
    num_dict = {x : lengths.count(x) for x in lengths}
    return num_dict

def letters_count_map(text):
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    texts = list(filter(lambda word : word, split(', .?', text.lower())))
    texts2 = ''.join(texts)
    letterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}    
    letterCount = {i : texts2.count(i) for i in letterCount}
    most_used = max(letterCount, key = letterCount.get)
    return letterCount


def most_used_character(text):
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    if text == '':
        return None
    else:
        texts = list(filter(lambda word : word, split(', .?', text.lower())))
        texts2 = ''.join(texts)
        letterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}    
        letterCount = {i : texts2.count(i) for i in letterCount}
        most_used = max(letterCount, key = letterCount.get)
        return most_used
