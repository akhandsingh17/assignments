"""
Implement a program that counts occurrences of words in a given file.
The input will have mul ple lines, with each line containing one or more words. The output will
be each word and how many  mes it appears. You should print each word and its count on a
separate line. The output should sort the words in lexicographically sorted order

"""
import argparse
import os

class WordCounter:

    def __init__(self, file_path=None):
        self.file_path = file_path

    def get_filename(self):
        print('enter the filename: ')
        self.file_path = input()
        try:
            self.readFile()
        except FileNotFoundError:
            print('No such file %s . Check file name and path and try again.' % (self.file_path))

    def readFile(self):
        input_file = open(self.file_path, 'r')
        freqs = {}  # hash-map to store the word and it's frequency
        try:
           content = [line.split() for line in input_file.read().splitlines() if line.split()]
           words = [item for sublist in content for item in sublist]
           for word in words:
               freqs[word] = 1 + freqs.get(word, 0)
           print(self.outFile(freqs))
        finally:
            input_file.close()

    def outFile(self, dct):
        sorted(dct.items(), key=lambda x: x[0])
        for word, counter in dct.items():
            print(word, counter)


def main():
    counter = WordCounter()
    counter.get_filename()

if __name__=='__main__':
    main()