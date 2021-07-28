"""
# Print all subarray with 0 sum
# Given an array, print all subarray in the array which has sum 0

"""


def AllSubArraySum(ary):
    result = []
    dict = {}
    idx = -1
    curr_sum = 0
    dict[curr_sum] = idx
    for idx, val in enumerate(ary):
        curr_sum += val
        if curr_sum in dict.keys():
            result.append(ary[dict.get(curr_sum)+1:idx+1])
        else:
            dict[curr_sum] = idx
    return result


def main():
    ary = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    print(AllSubArraySum(ary))

if __name__ == '__main__':
    main()
