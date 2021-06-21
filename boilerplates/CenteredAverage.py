
def centered_average(nums):
    nums.sort()
    result = []
    for i in range(1, len(nums)-1):
        result.append(nums[i])
    return sum(result)/len(result)

if __name__ == "__main__":
    centered_average([1, 2, 3, 4, 100])
    centered_average([1, 1, 5, 5, 10, 8, 7])
    centered_average([-10, -4, -2, -4, -2, 0])

