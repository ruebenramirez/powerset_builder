
def subsets(set):
    if len(set) == 0:
        return[[]]
    else:
        build = []
        for nums in subsets(set[1:]):
            # print("set[0] " + str(set[0]))
            # print("nums: " + str(nums))
            print("set[0] + nums: " + str([set[0]]) + " " + str(nums))
            build.append(nums)
            mini_set = [[set[0]] + nums]
            build.extend(mini_set)
        return build


print(subsets([]))        # -> [[]]
print(subsets([1]))       # -> [[], [1]]
print(subsets([1, 2]))    # -> [[], [1], [2], [1, 2]]
print(subsets([1, 2, 3]))
# -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
