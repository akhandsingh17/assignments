"""
You are given a list of data entries that represent entries and exits of groups of
 people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}
This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside

"""

class Solution:
    def __init__(self, entry):
        self.entry = entry
        self.result = []

    def busy_period_finder(self):

        if self.entry:
            self.entry = sorted(self.entry, key=lambda x:x['timestamp'])
            count = self.entry[0]['count']
        for i in range(1, len(self.entry)):
            if self.entry[i]['type'] == 'enter':
                count += self.entry[i]['count']
            else:
                count -= self.entry[i]['count']
            self.result.append((self.entry[i]['timestamp'],count))
        x = sorted(self.result, key = lambda x:x[1], reverse=True)
        return (x[0][0] , x[1][0])

if __name__ == "__main__":
    entry = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526576928, "count": 3, "type": "enter"},
        {"timestamp": 1526580382, "count": 2, "type": "exit"},
        {"timestamp": 1526581928, "count": 6, "type": "enter"},
        {"timestamp": 1526591382, "count": 3, "type": "exit"},
        {"timestamp": 1529598382, "count": 7, "type": "exit"},
    ]
    s = Solution(entry)
    print(s.busy_period_finder())

