// Problem: Valid Anagram
// Link: https://leetcode.com/problems/valid-anagram/

import java.util.Arrays;

public class AnagramCheck {
    public boolean isAnagram(String s, String t){
        char[] a=s.toCharArray(), b=t.toCharArray();
        Arrays.sort(a); Arrays.sort(b);
        return Arrays.equals(a,b);
    }

    public static void main(String[] args){
        System.out.println(new AnagramCheck().isAnagram("anagram","nagaram")); // true
    }
}
