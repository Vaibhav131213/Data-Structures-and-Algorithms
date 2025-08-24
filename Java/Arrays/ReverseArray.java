// Problem: Reverse Array
// Link: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

import java.util.*;

public class ReverseArray {
    public void reverse(int[] arr) {
        int l=0, r=arr.length-1;
        while(l<r){
            int tmp=arr[l];
            arr[l]=arr[r];
            arr[r]=tmp;
            l++; r--;
        }
    }

    public static void main(String[] args) {
        int[] arr={1,2,3,4};
        new ReverseArray().reverse(arr);
        System.out.println(Arrays.toString(arr)); // [4,3,2,1]
    }
}
