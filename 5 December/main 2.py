def sort_list(items):
    return sorted(items, key=lambda x: int(x.split("-")[0]))

def merge_intervals(items):
    intervals = []
    for item in items:
        a, b = item.split("-")
        intervals.append([int(a), int(b)])

    intervals.sort()

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last = merged[-1]

        if start <= last[1] + 1:        
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])

    return merged

def count_elements(intervals):
    return sum(b - a + 1 for a, b in intervals)

if __name__ == "__main__":
    with open("./5 December/input.txt") as f:
        lines = f.readlines()

    split_index = lines.index("\n")
    fresh = [line.strip() for line in lines[:split_index]]

    fresh = sort_list(fresh)
    merged = merge_intervals(fresh)
    total = count_elements(merged)

    print("Total:", total)
