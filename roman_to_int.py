'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M..

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

def romanToInt(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0 # To keep track of the previous numeral's value

    # We loop through the string from end to start
    for i in range(len(s) -1, -1, -1):
        current_value = roman_values[s[i]] # Convert the character to numeral

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total

s = "MCMXCIV"
print(romanToInt(s)) # Output: 1994
'''
Explanation:
1) V (5) is bigger than prev_value (0) so the total becomes 0 + 5 = 5
2) I (1) is smaller than prev_value (5) so the total becomes 5 - 1 = 4
3) C (100) is bigger than prev_value (1) so the total becomes 4 + 100 = 194
3) X (10) is smaller than prev_value (100) so the total becomes 194 - 10 = 94
4) M (1000) is bigger than prev_value (10) so the total becomes 94 + 1000 = 1094
5) C (100) is smaller than prev_value (1000) so the total becomes 1094 - 100 = 994
6) M (1000) is bigger than prev_value (100) so the total becomes 994 + 1000 = 1994
'''