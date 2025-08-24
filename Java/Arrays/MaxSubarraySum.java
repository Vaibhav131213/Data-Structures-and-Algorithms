// Problem: Maximum Subarray
// Link: https://leetcode.com/problems/maximum-subarray/

public class MaxSubarraySum {
    public int maxSubArray(int[] nums) {
        int max=nums[0], curr=nums[0];
        for(int i=1;i<nums.length;i++){
            curr = Math.max(nums[i], curr+nums[i]);
            max = Math.max(max, curr);
        }
        return max;
    }

    public static void main(String[] args){
        int[] nums={-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(new MaxSubarraySum().maxSubArray(nums)); // 6
    }
}
