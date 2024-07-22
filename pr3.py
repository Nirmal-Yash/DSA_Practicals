def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
