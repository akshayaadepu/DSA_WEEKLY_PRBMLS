#MAJORITY ELEMENT I
#time comlexity O(n^2) and space complexity O(n)
'''
Approach
1. Create repeat to store each distinct number.
2. Create non_repeat to store numbers that appear again.
3. Traverse the array.
4. If a number is already in repeat, add it to non_repeat; otherwise, add it to repeat.
5. Find the most frequent number in non_repeat and return it.
WHY IT WORKS?
The majority element appears more than n/2 times. Since the problem guarantees that a majority element exists, 
the most frequent number in non_repeat will also be the majority element.
Test case 1 — Given example
Input:7, 0, 0, 1, 7, 7, 2, 7, 7 Expected output:7

Test case 2 — Given example
Input:1 1 1 2 1 2 Expected output:1
Test case 3 — Additional edge case
Input:5 Expected output:5
'''
def majorityElement(nums):
    repeat=[]
    non_repeat=[]
    for num in nums:
        if num in repeat:
            non_repeat.append(num)
        else:
            repeat.append(num)
    return max(non_repeat,key=non_repeat.count)
nums=list(map(int,input().split()))
print(majorityElement(nums))
