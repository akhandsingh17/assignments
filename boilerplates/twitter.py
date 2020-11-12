"""
# UAM = number of distinct minutes a user spends on twitter in a given month

# Input:

# Now assume you are given 30 days of raw logs that have the format:

# |user_id | timestamp_ms | action_id |
# For this problem, we can assume all actions count as activity events and all activity is captured in this table.
# Expected Output:

# Table computing the number of users who spent the number of minutes on twitter.

# | # minutes | # users |

# e.g.:

# 421 users spend between 33 minutes on twitter
# 311 users spend between 34 minutes on twitter

# | # minutes | # users |
# |        33 |     421 |
# |        34 |     311 |

"""

rows = set()
logs = [(1, 445853, 101), (2, 445854, 101), (1, 485945, 102),
        (1, 455853, 12), (2, 545854, 101), (1, 445853, 12),
        (3, 455853, 12), (4, 545854, 101), (5, 445853, 12)]
for record in logs:
    userid = record[0]
    nearest_min = record[1] // (1000 * 60)
    rows.add((userid, nearest_min))
dct = {}
for userid, nearest_min in rows:
    dct[userid] = dct.get(userid, 0) + 1

invert_dct = {}
for key, val in dct.items():
    invert_dct[val] = invert_dct.get(val, 0) + 1
print(invert_dct)
