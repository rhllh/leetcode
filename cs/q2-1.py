"""
You are given two strings: pattern and source. 
The first string pattern contains only the symbols 0 and 1, and the second string source contains *only lowercase English letters*.

Your task is to calculate the number of substrings of source that match pattern. 

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
– “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” 
    matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
– “010” doesn’t match source[1..3] = "maz" 
– “010” matches source[2..4] = "azi" 
– “010” doesn’t match source[3..5] = "zin" 
– “010” doesn’t match source[4..6] = "ing"

So, there are 2 matches. For a visual demonstration, see the example video. 

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
– There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

Guaranteed constraints:
1 ≤ source.length ≤ 103
1 ≤ pattern.length ≤ 103
"""
def countSubstrings(pattern, source):
    vowels = ['a','e','i','o','u','y']
    n = len(pattern)
    
    output = 0
    for i in range(len(source)-2):
        count = 0
        for j in range(n):
            if pattern[j] == "0" and source[i+j] not in vowels:
                break
            elif pattern[j] == "1" and source[i+j] in vowels:
                break
            else:
                count += 1
        if count == n:
            output += 1
            
    return output
    

if __name__ == "__main__":
    print(countSubstrings("010", "amazing"))
    print(countSubstrings("100", "codesignal"))