#Apertura File
file = open("./1 December/input.txt", "r")
password = 0
current_value = 50


for line in file:
    if "R" in line:
        line = int(line[1:])
        current_value =  current_value + line
        current_value = current_value % 100
        if current_value == 0:
            password = password + 1
    else:
        line = int(line[1:])
        current_value =  current_value - line
        current_value = current_value % 100
        if current_value == 0:
            password = password + 1

print(f"Completato. La password è: {password}" )

