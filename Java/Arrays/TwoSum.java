// Problem: Two Sum
// Link: https://leetcode.com/problems/two-sum/

import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int i=0;i<nums.length;i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        TwoSum sol = new TwoSum();
        int[] ans = sol.twoSum(new int[]{2,7,11,15},9);
        System.out.println("["+ans[0]+","+ans[1]+"]"); // [0,1]
    }
}
