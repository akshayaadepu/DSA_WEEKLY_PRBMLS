'''APPROCH:
- current_sum: Stores the sum of the current subarray.
- max_sum: Stores the maximum sum found so far.
1. Add the current element to current_sum.
2. Check whether current_sum is greater than max_sum.
3. If yes, update max_sum.
4. Otherwise, reset current_sum to zero.
why it works:Kadane's Algorithm works because a negative running sum reduces the future subarray sum,
 so we discard it and start a new subarray to find the maximum sum
Time Complexity: O(n)
Space Complexity: O(1)
'''
#Kadane's Algorithm — Maximum Subarray Sum
def max_subarray(nums):
    max_sum=nums[0]
    current_sum=0
    for num in nums:
        current_sum+=num
        if current_sum>max_sum:
            max_sum=current_sum
        elif current_sum<0:
            current_sum=0
        else:
            current_sum=current_sum
    return max_sum
nums=list(map(int, input().split(',')))
result = max_subarray(nums)
print(result)
#test cases
"""
Example 1 Input: nums = [2, 3, 5, -2, 7, -4] 
Output: 15 Explanation: The subarray [2, 3, 5, -2, 7] has sum 15. 
Example 2 Input: nums = [-2, -3, -7, -2, -10, -4] 
Output: -2 Explanation: The maximum sum is the largest individual element, -2."""