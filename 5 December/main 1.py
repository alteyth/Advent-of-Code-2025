def check_item(item: int) -> bool:
    for range in fresh:
        range = range.split("-")
        if (item >= int(range[0])) and (item <= int(range[1])):
            return True
    return False

if __name__ == "__main__":
    file = open("./5 December/input.txt")
    file_list = file.readlines()

    split_index = file_list.index("\n")

    fresh = [line.strip() for line in file_list[:split_index]]
    available = [line.strip() for line in file_list[split_index + 1:]]
    available = [int(line) for line in available]

    total_fresh = 0

    for item in available:
        if check_item(item):
            total_fresh += 1

    print(f"Total fresh available items: {total_fresh}")