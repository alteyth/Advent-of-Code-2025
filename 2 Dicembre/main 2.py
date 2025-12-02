def check_ids(id_tuple: tuple) -> int:   
    id_range = range(id_tuple[0], id_tuple[1] + 1)
    value = 0
    for id in id_range:
        str_value = str(id)
        str_conc = str(id) + str(id)
        str_conc = str_conc[1:]
        str_conc = str_conc[:-1]
        if str(id) in str_conc:
            value += id
    return value
             

if __name__ == "__main__":
    file = open("./2 Dicembre/input.txt")
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

    print(f"Completato. La password è: {password}")