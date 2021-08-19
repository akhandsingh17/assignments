# Replace None value with previous value present in a list.
def return_filled_array(a):
    if a is None:
        return None
    if not a:
        return []
    p = None
    return ([p:=e if e is not None else p for e in a])

assert return_filled_array(None) == None
assert return_filled_array([]) == []
assert return_filled_array([None,8,None]) == [None,8,8]
assert return_filled_array([1,None,2]) == [1,1,2]
assert return_filled_array([5,None,None]) == [5,5,5]
assert return_filled_array([1,None,2,3,None,None,5,None]) == [1,1,2,3,3,3,5,5]
assert return_filled_array([1,4,None,None,3]) ==  [1,4,4,4,3]