def isValid(s: str) -> bool:
    open_brackets = '([{'
    close_brackets = ')]}'
    num_open_brackets = 0
    num_close_brackets = 0
    num_valid_pairs = 0
    for char in s:
        if char in open_brackets:
            num_open_brackets += 1
        elif char in close_brackets:
            num_close_brackets += 1
            if num_close_brackets > num_open_brackets:
                return False
            if char == ')' and '(' in s[num_valid_pairs:]:
                num_valid_pairs = s.index('(', num_valid_pairs) + 1
            elif char == ']' and '[' in s[num_valid_pairs:]:
                num_valid_pairs = s.index('[', num_valid_pairs) + 1
            elif char == '}' and '{' in s[num_valid_pairs:]:
                num_valid_pairs = s.index('{', num_valid_pairs) + 1
            else:
                return False
    result = num_open_brackets == num_close_brackets
    return result

if __name__ == "__main__":
    line = input()
    if isValid(line):
        print('valid')
    else:
        print('invalid')