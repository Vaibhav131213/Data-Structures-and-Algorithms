# Problem: Maximum Subarray (Kadane’s Algorithm)
# Link: https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
