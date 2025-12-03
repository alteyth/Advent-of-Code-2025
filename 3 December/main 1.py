def check_joltage(line: str) -> int:
    largest = 11

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if int(line[i] + line[j]) > largest:
                largest = int(line[i] + line[j])

    return largest


if __name__ == "__main__":
    file = open("./3 December/input.txt", "r")
    joltage = 0

    for line in file:
        line = line.strip()
        joltage += check_joltage(line)

    print(f"Total joltage is: {joltage}")