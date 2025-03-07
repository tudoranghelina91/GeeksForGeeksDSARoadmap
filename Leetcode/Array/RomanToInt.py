def romanToInt(s):
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    
    for a, b in zip(s, s[1:]):
        if map[a] < map[b]:
            num -= map[a]
        else:
            num += map[a]

    return num + map[s[-1]]

# Example usage
if __name__ == "__main__":
    roman_numeral = "MCMXCIV"
    result = romanToInt(roman_numeral)
    print(f"The integer value of the Roman numeral {roman_numeral} is {result}")