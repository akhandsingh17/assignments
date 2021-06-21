
"""
convert the negative annotated string into a positive intent
"""

def convertIntent(str):
    result = ''
    if str.find('not') < str.find('bad'):
        result = str[:str.find('not')] + 'good' + str[str.find('bad')+3]
    else:
        result = str
    return result

if __name__ == '__main__':
    assert convertIntent('This movie is not so bad!!') == 'This movie is good!'
    assert convertIntent('This dinner is not that bad!') == 'This dinner is good!'
    assert convertIntent('This tea is not hot') == 'This tea is not hot'
    assert convertIntent("It's bad yet not") == "It's bad yet not"

