a = lambda x: x*2

nums = [1, 2, 5, 7, 11, 15, 77, 77, 13, 99, 121]
nums2 = [3, 6, 8, 12, 33, 43, 99, 123, 254]
total_nums = [nums, nums2]
b = set(filter(lambda x: x%2 != 0, nums))
print(b)

c = list(map(lambda x: x*2, nums))
print(c)

