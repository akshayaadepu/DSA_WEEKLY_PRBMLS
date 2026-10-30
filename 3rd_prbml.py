#Rearrange Array Elements by Sign
'''
Approach:
1. Create two empty lists, pos and neg, to store positive and negative numbers separately.
2. Traverse the array. If num > 0, append it to pos; otherwise, append it to neg.
3. Create an empty list called result.
4. Traverse the pos list using a loop and append one positive number from pos, followed by one negative number from neg.
5. Return the result list containing alternating positive and negative numbers, starting with a positive number.
Why it works: The two lists preserve the original order of their respective numbers, and alternating between them creates the required arrangement.
Time Complexity:O(n)
Space Complexity:O(n)
Example 1 Input: nums = [2, 4, 5, -1, -3, -4] Output: [2, -1, 4, -3, 5, -4] 
Explanation: Positive and negative values each keep their original relative order. 
Example 2 Input: nums = [1, -1, -3, -4, 2, 3] Output: [1, -1, 2, -3, 3, -4] 
Explanation: The output alternates signs and begins with a positive value.'''
def rearrangeArray(nums):
    pos=[]
    neg=[]
    result=[]
    for num in nums:
        if num>0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result
nums=list(map(int,input().split()))
print(rearrangeArray(nums))