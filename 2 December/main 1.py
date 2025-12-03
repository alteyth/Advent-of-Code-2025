def check_ids(id_tuple: tuple)-> int:   
    id_range = range(id_tuple[0], id_tuple[1] + 1)
    value = 0;
    for id in id_range:
        length = len(str(id))
        if length % 2 == 0:
            str_id = str(id)
            factor = int(length / 2)
            first_half = [str_id[x] for x in range(0, factor)]
            second_half = [str_id[x] for x in range(factor, length)]
            if first_half == second_half:
                value += id
    return value
                

if __name__ == "__main__":
    file = open("./2 December/input.txt")
    full_string = file.read()
    range_list = full_string.split(",")

    string_tuples = []
    int_tuples = []
    password = 0

    for element in range_list:
        string_tuples.append(tuple(element.split("-")))
        int_tuples = [(int(x), int(y)) for (x, y) in string_tuples]

    for tuple in int_tuples:
        password += check_ids(tuple)

    print(f"Password: {password}")