def mult(i: int) -> int:
    amount = 1
    for x in range(rows - 1):
        # print(f"Number: {numbers[x][i]}")
        amount *= numbers[x][i]
        # print(f"Amount {amount} dell'iterazione {x}-esima della i = {i}")
    return amount

def add(i: int) -> int:
    amount = 0
    for x in range(rows - 1):
        amount += numbers[x][i]
    return amount


if __name__ == "__main__":
    file = open("./6 December/input.txt")
    liste = [line.rstrip() for line in file]
    liste = [r.split(" ") for r in liste]
    for lista in liste:
        for elemento in lista[:]:
            if not elemento:
                lista.remove(elemento)
    numbers = []
    operations = []
    rows = len(liste)
    for i in range(rows - 1):
        liste[i] = [int(x) for x in liste[i]]
        numbers.append(liste[i])
    operations = [x for x in liste[rows - 1]]

    total = 0

    for i in range(len(operations)):
        if operations[i] == "*":
            total += mult(i)
        else:  
            total += add(i)
    print(total)