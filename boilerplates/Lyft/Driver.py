class Bucket:
    def __init__(self):
        self.bucket = []

    def GET(self, key):
        for (k, v) in self.bucket:
            if k == key:
                print(v)   # Key the value for a given key
        return -1

    def SET(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def UNSET(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

    def NUMWITHVALUE(self, value):
        for (k, v) in self.bucket:
            if v == value:
                print(k)
        return -1

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def SET(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].SET(key, value)


    def GET(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].GET(key)


    def UNSET(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].UNSET(key)


    def NUMWITHVALUE(self, value):
        """
        :param value:
        :return: variable assigned this value or return 0 if no value found
        """


class Driver():
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
        try:
            lines = [line for line in input_file.read().splitlines()]
            hashmap = MyHashMap()  # initialize the hash map
            for line in lines:
                commands = [command for command in line.split()]
                if commands[0] == 'SET':
                    hashmap.SET(int(commands[1]), int(commands[2]))
                elif commands[0] == 'GET':
                    hashmap.GET(int(commands[1]))
                elif commands[0] == 'UNSET':
                    hashmap.UNSET(int(commands[1]))
         #       elif commands[0] == 'NUMWITHVALUE':    # work in progress
                elif commands[0] == 'END':
                    return None
        finally:
            input_file.close()

def main():
    obj = Driver()
    obj.get_filename()

if __name__=='__main__':
    main()