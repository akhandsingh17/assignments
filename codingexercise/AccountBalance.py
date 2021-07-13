"""
A transaction log format is shown as following:

D means deposit while W means withdrawal.
Suppose the following input is supplied to your program:

$ cat log.csv
Name,Operation,Amount
John,D,300
John,D,300
Jane,W,200
Jane,D,100
John,D,300
Jane,D,500
Jane,W,200

Print net amount for Jane and John separately

"""
from csv import reader


class Transaction:
    def __init__(self, name, transaction_type, amount):
        self.name = name
        self.type = transaction_type
        self.amount = amount

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.name, self.type, self.amount)


class LogHandler:
    def __init__(self, filepath=None):
        self.filePath = filepath
        self.dict = {}

    def getfilename(self):
        print("Enter the absolute file path")
        self.filePath = input()
        try:
            self.readFile()
        except FileNotFoundError:
            print('No such file %s . Check file name and path and try again.' % self.filepath)

    def readFile(self):
        with open(self.filePath, 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header:
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    transaction = Transaction(row[0], row[1], row[2])
                    sign = int(-1 if transaction.type == 'W' else 1)
                    self.dict[transaction.name] = self.dict.get(transaction.name, 0) + (sign * int(transaction.amount))


def main():
    log = LogHandler()
    print(log.getfilename())


if __name__ == '__main__':
    main()
