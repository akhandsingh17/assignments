"""
You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one
word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically
ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


"""

"""
A better approach will be sorting by keys. We can create tuple with 3 elements

As a reminder, here are a list of the rules that we defined before, concerning the order of logs:

    1). The letter-logs should be prioritized above all digit-logs.
    2). Among the letter-logs, we should further sort them based on firstly on their contents, and then on their
     identifiers if the contents are identical.
    3). Among the digit-logs, they should remain in the same order as they are in the collection.

    To ensure the above order, we could define a tuple of 3 keys, (key_1, key_2, key_3)
    
"""

class Solution:
    def reorderLogFiles(self, logs):
        result = []
        output = []
        for log in logs:
            id, rest = log.split(" ", maxsplit=1)
            tup = (0 if rest[0].isalpha() else 1,
                   rest if rest[0].isalpha() else None,
                   id if rest[0].isalpha() else None,
                   log)
            result.append(tup)
        result = sorted(result, key=lambda x: (x[0], x[1], x[2]))

        for log in result:
            output.append(log[3])
        return output

if __name__=='__main__':
    s = Solution()
    print(s.reorderLogFiles(logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                                    "let2 own kit dig", "let3 art zero"]))
    print(s.reorderLogFiles(logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog",
                                  "a8 act zoo", "a2 act car"]
                            ))
