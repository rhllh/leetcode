"""
Given an array of unique integers numbers, your task is to find the number of pairs of indices (i, j) such
that i ≤ j and the sum numbers[i] + numbers[j] is equal to some power of 2. Note: The numbers 2^0 = 1, 2^
1 = 2, 2^2 = 4, 2^3 = 8, etc. are considered to be powers of 2.

Examples:
For numbers = [1, -1, 2, 3], the output should be solution(numbers) = 5.
• There is one pair of indices where the sum of the elements is 2^0 = 1: (1, 2): numbers[1] + numbers[2]= -1 + 2 = 1
• There are two pairs of indices where the sum of the elements is 2^1 = 2: (0, 0) and (1, 3)
• There are two pairs of indices where the sum of the elements is 2^2 = 4: (0, 3) and (2, 2)
• In total, there are 1 + 2 + 2 = 5 pairs summing to powers of 2.

For numbers = [2], the output should be solution(numbers) = 1.
• The only pair of indices is (0, 0) and the sum is equal to 2^2 = 4. So, the answer is 1.

For numbers = [-2, -1, 0, 1, 2], the output should be solution(numbers) = 5.
• There are two pairs of indices where the sum of the elements is 2^0 = 1: (2, 3) and (1, 4)
• There are two pairs of indices where the sum of the elements is 2^1 = 2: (2, 4) and (3, 3)
• There is one pair of indices where the sum of the elements is 2^2 = 4: (4, 4)
• In total, there are 2 + 2 + 1 = 5 pairs summing to powers of 2.

Guaranteed constraints:
• 1 ≤ numbers.length ≤ 10^5
• -10^6 ≤ numbers[i] ≤ 10^6
"""
from collections import defaultdict

def findPowerPairs(numbers):
    # two sum!
    d = defaultdict(int)
    res = 0
    
    for num in numbers:
        # increment count of this number
        d[num] += 1
        
        # each possible power of 2 from 2^0 to 2^20
        for two_power in range(21):
            # another way to get 2^k = (1 << two_power)
            complement = 2**two_power - num
            
            # if complement exists in dict, 1 pair is added to res
            res += d[complement]
    
    return res

print(findPowerPairs([1, -1, 2, 3]))
print(findPowerPairs([2]))
print(findPowerPairs([-2, -1, 0, 1, 2]))