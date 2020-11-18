"""
# Travel Buddies
#
# Let’s say Airbnb launches a new feature called "Travel Buddies". As part of this feature, users create wishlists of cities they want to visit. For the purpose of this question, let these wishlists be provided as a file with the following format:
#
# <user name>,<city 1>,<city 2>...
# <user name>,<city 1>,<city 2>...
# ...
#
# You can stub the file out like this
# wishlists = [
#   "U1,Amsterdam,Barcelona,London,Prague",
#   "U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne",
#   "U3,London,Boston,Amsterdam,Madrid",
#   "U4,Barcelona,Prague,London,Sydney,Moscow",
#   "U5,Amsterdam,Barcelona,London,Prague"
# ]
#
#
# We’ll define a Travel Buddy as:
# User A is a travel buddy of user B if 50% or more of the cities in A's wishlist are also contained in B’s wishlist
#
# A Travel Buddy also has a Rank, which is defined as
# The number of cities contained in the wishlists of both users
#
# 1)  Now, write a method that takes your wishlist as input and prints out your travel buddies sorted by rank.
#
# 2)  After implementing and testing that method, write a method that takes in your wishlist and a number n,
 and returns the top n recommendations based on your wishlist.
#
# We’ll define a Recommendation as:
# A city that is contained in a travel buddy’s wishlist and not yours

"""
from collections import defaultdict

class TravelBuddy:
    def __init__(self, wishlists):
        self.wishlists = wishlists
        self.userdict = {}
        self.buddy_list = defaultdict(list)

    def getTravelBuddy(self):
        # create a dict with user as key and cities as values
        records = [row.partition(",") for row in self.wishlists if row]
        for record in records:
            user = record[0]
            cities = record[2].split(",")
            self.userdict[user] = set(cities)
        for user1, cities1 in self.userdict.items():
            for user2, cities2 in self.userdict.items():
                if user1 != user2:
                    try:
                        common = cities1.intersection(cities2)
                        score = len(cities1.intersection(cities2)) / len(cities1)
                        if score >= 0.5:
                            self.buddy_list[user1].append((user2, len(common), common))
                    except:
                        ZeroDivisionError
        return self.buddy_list

    def getTravelRecommendation(self, key):
        if len(self.buddy_list[key]) > 0:
            return self.buddy_list[key][-1]

if __name__ == '__main__':
    wishlists = [
      "U1,Amsterdam,Barcelona,London,Prague",
      "U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne",
      "U3,London,Boston,Amsterdam,Madrid",
      "U4,Barcelona,Prague,London,Sydney,Moscow",
      "U5,Amsterdam,Barcelona,London,Prague"
    ]
    t = TravelBuddy(wishlists)
    print(t.getTravelBuddy())
    print(t.getTravelRecommendation('U1'))
    print(t.getTravelRecommendation('U2'))
    print(t.getTravelRecommendation('U3'))
    print(t.getTravelRecommendation('U4'))