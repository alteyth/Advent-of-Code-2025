def check_joltage(line: list[int]) -> int:
    result, start = 0, 0
    length = len(line)
    for digit_pos in range(12):
        end = length - (12 - digit_pos) + 1
        max_digit = max(line[start:end])
        start = line.index(max_digit, start, end) + 1
        result = result * 10 + max_digit
    return result


if __name__ == "__main__":
    file = open("./3 December/input.txt", "r")
    joltage = 0

    for line in file:
        line = line.strip()
        line_list = [int(digit) for digit in line]
        joltage += check_joltage(line_list)

    print(f"Total joltage is: {joltage}")