# Sort an Array of 0s, 1s and 2s
'''APPROACH:
1. Use nums.sort() to sort the elements in ascending order.
2. Return the sorted array using return nums.
3. Take input from the user, convert it into a list of integers, and print the sorted array.
Why it works: The sort() method arranges the elements in ascending order by modifying the original list.
Time Complexity: \(O(n \log n)\)
Space Complexity: \(O(n)\) auxiliary space in Python's sorting implementation.'''
def sort(nums):
    nums.sort()
    return nums
nums=list(map(int,input().split()))
print(sort(nums))
'''TEST CASES:
Example 1 Input: nums = [1, 0, 2, 1, 0] Output: [0, 0, 1, 1, 2] Explanation: There are two 0s, two 1s and one 2. 
Example 2 Input: nums = [0, 0, 1, 1, 1] Output: [0, 0, 1, 1, 1] Explanation: The array is already in non-decreasing order.'''