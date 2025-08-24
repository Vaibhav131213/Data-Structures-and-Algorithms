# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # [0,1]
