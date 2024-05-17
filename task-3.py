def move_disks(n, source, auxiliary, target, pegs):
    if n == 1:
        # Move the disk from source to target
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {pegs}")
    else:
        # Move n-1 disks from source to auxiliary
        move_disks(n-1, source, target, auxiliary, pegs)
        
        # Move the nth disk from source to target
        move_disks(1, source, auxiliary, target, pegs)
        
        # Move the n-1 disks from auxiliary to target
        move_disks(n-1, auxiliary, source, target, pegs)

def hanoi_tower(n):
    pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {pegs}")
    move_disks(n, 'A', 'B', 'C', pegs)
    print(f"Кінцевий стан: {pegs}")

# Виклик функції з кількістю дисків n = 3
hanoi_tower(3)
