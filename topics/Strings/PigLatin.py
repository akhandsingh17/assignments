"""

Pig Latin is a farcical "language" used to entertain children, but also to teach them some valuable language concepts along the way.  Translating English to Pig Latin is simple:

1) Take the first consonant (or cluster of consonants) of a word, move it to the end of the word, and add a suffix of "ay"
2) If a word begins with a vowel, just add "way" at the end
3) For the sake of readability, separate the Pig Latin-ized parts of the word with a dash `-`

"""

class PigLatin:
    def __init__(self):
        self.VOWEL_LIST = ('a', 'e', 'i', 'o', 'u')
        self.CONSONANT_SUFFIX = 'ay'
        self.VOWEL_SUFFIX = 'way'
        self.SEPERATOR = '-'

    def pigLatinize(self, phrase):
        self.result = []
        ## base case

        words = [word for word in phrase.split() if word]
        for word in words:
            if word[0].lower() not in self.VOWEL_LIST:
                self.result.append(word[1:] + self.SEPERATOR + word[0] + self.CONSONANT_SUFFIX)
            else:
                self.result.append(word + self.SEPERATOR + self.VOWEL_SUFFIX)
        return " ".join(self.result)

def main():
    s = PigLatin()
    assert (s.pigLatinize("pig")) == "ig-pay"
    assert (s.pigLatinize("pig latin")) == "ig-pay atin-lay"
    assert (s.pigLatinize("Pig Latin")) == "ig-Pay atin-Lay"
    assert (s.pigLatinize("egg")) == "egg-way"

if __name__ == "__main__":
    main()