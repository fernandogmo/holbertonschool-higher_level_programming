#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = ''
    if roman_string:
        for r in roman_string:
            if r == 'I':
                total += 1
            elif r in 'VX':
                total += nums[r]
                if prev == 'I':
                    total -= 2
            elif r in 'LC':
                total += nums[r]
                if prev == 'X':
                    total -= 20
            elif r in 'DM':
                total += nums[r]
                if prev == 'C':
                    total -= 200
            else:
                return 0
            prev = r
    return total
