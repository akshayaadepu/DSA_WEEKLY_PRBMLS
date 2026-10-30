# Leaders in an Array
'''APPROACH:
1. Create two empty lists: leaders and not_leaders.
2. Use an outer loop to select each element.
3. Use an inner loop to compare the selected element with all elements on its right.
4. If nums[i] < nums[j], store index i in not_leaders.
5. After checking all right-side elements, check whether index i is absent from not_leaders.
6. If absent, append nums[i] to leaders.
7. Return the leaders list.
why it works: The algorithm identifies leaders by comparing each element with all elements to its right, 
ensuring that only those greater than all subsequent elements are included.
Time Complexity: O(n²)
Space Complexity: O(n)'''
def leader(nums):
    leaders = []
    not_leaders = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                not_leaders.append(i)
        if i not in not_leaders:
            leaders.append(nums[i])
    return leaders
nums = list(map(int, input().split(',')))
print(leader(nums))
#test cases:
"""Input: nums = [1, 2, 5, 3, 1, 2] Output: [5, 3, 2] 
Explanation: 5, 3 and 2 are greater than every element to their right.
Example 2 
Input: nums = [-3, 4, 5, 1, -4, -5] 
Output: [5, 1, -4, -5] Explanation: Each listed value is strictly greater than all values to its right."""