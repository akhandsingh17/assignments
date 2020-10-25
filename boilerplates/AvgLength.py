def avg_word_length(mystring):
    filtered = ''.join(filter(lambda x: x not in '".,;!', mystring))
    words = [word for word in filtered.split() if word]
    if words:
        result = sum(map(len, words))/len(words)
        return result
    else:
        return None

if __name__ == "__main__":
     assert avg_word_length('') == None
     assert avg_word_length('ibm') == 3
     assert avg_word_length('ibm microsoft') == 6
     assert avg_word_length(' Hello World ') == 5
     assert avg_word_length('The movie ends with The-end') == 4.6