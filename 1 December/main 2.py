N = 100  
password = 0
current_value = 50

with open("./1 December/input.txt", "r", encoding="utf-8") as f:
    for raw in f:
        line = raw.strip()

        direction = line[0]
       
        steps = int(line[1:])

        if direction == "R":
            # numero di volte che (current_value + k) % N == 0 per k in 1..steps
            crossings = (current_value + steps) // N
            current_value = (current_value + steps) % N

        elif direction == "L":
            # per sinistra trasformiamo in equivalente "destra" partendo da (N - current_value) % N
            inv_start = (N - current_value) % N
            crossings = (inv_start + steps) // N
            current_value = (current_value - steps) % N

        password += crossings

print(f"Completato. La password è: {password}")
