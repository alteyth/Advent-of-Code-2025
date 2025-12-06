def mult(i: int) -> int:
    amount = 1
    for x in range(len(result[i])):
        amount *= result[i][x]
    return amount

def add(i: int) -> int:
    amount = 0
    for x in range(len(result[i])):
        amount += result[i][x]
    return amount

   
if __name__ == "__main__":
    file = open("./6 December/input.txt")
    liste = [line for line in file]

    numbers = []
    operations = []
    rows = len(liste)
    for i in range(rows - 1):
        numbers.append(liste[i])
    operations = [x for x in liste[rows - 1]]
    for elemento in operations[:]:
        if elemento == " ":
            operations.remove(elemento)
    
    trasposta = list(map(list, zip(*numbers)))
    trasposta = [col for col in trasposta if any(ch != '\n' for ch in col)]
    for list in trasposta:
        for x in list[:]:
            if x == " ":
                list.remove(x)
    fixed_matrix = []
    for i in range(len(trasposta)):
        trasposta[i] = ("".join(trasposta[i]))

    result = []
    current = []

    for x in trasposta:
        if x == '':
            if current:
                result.append(current)
                current = []
        else:
            current.append(x)

    if current:
        result.append(current)
    result = [[int(x) for x in group] for group in result]

    print(result)
    total = 0
    for i in range(len(operations)):
        if operations[i] == "*":
            total += mult(i)
        else:  
            total += add(i)

    print(total)