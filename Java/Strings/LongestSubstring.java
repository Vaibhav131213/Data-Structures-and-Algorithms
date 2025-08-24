// Problem: Longest Substring Without Repeating Characters
// Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

import java.util.*;

public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> seen=new HashMap<>();
        int l=0, res=0;
        for(int r=0;r<s.length();r++){
            char c=s.charAt(r);
            if(seen.containsKey(c) && seen.get(c)>=l){
                l=seen.get(c)+1;
            }
            seen.put(c,r);
            res=Math.max(res,r-l+1);
        }
        return res;
    }

    public static void main(String[] args){
        System.out.println(new LongestSubstring().lengthOfLongestSubstring("abcabcbb")); // 3
    }
}
