# Given a ´dictionary, print the key for nth highest value present in the dict.
# Dictionary Initialization

listOfKeys = list()
Tv = {'Ritika': 5, 'Sam': 27, 'John': 12, 'Sachin': 14, 'Mark': 19, 'Shaun' : 27}
keymax = max(Tv.items(), key=lambda x:x[1])[1]
for key, value in Tv.items():
    if value == keymax:
        listOfKeys.append(key)
print(listOfKeys)