# Problem: Reverse Array
# Link: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

def reverseArray(arr):
    return arr[::-1]

if __name__ == "__main__":
    print(reverseArray([1,2,3,4]))  # [4,3,2,1]
