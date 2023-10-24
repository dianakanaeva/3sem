class HardDrive:
    def __init__(self, hd_id, capacity, name):
        self.hd_id = hd_id
        self.capacity = capacity
        self.name = name

class PC:
    def __init__(self, pc_id, ram, cores):
        self.pc_id = pc_id
        self.ram = ram
        self.cores = cores

class PC_HD:
    def __init__(self, pc_id, hd_id):
        self.hd_id = hd_id
        self.pc_id = pc_id

PCs = [
    PC(1, "DDR4-2400", 4),
    PC(2, "DDR3-1600", 8),
    PC(3, "DDR4-3200", 6),
    PC(4, "DDR3-1866", 4),
    PC(5, "DDR4-2666", 12)
]

HDs = [
    HardDrive(1, "1TB", "HDD-1TB"),
    HardDrive(2, "500GB", "SSD-500GB"),
    HardDrive(3, "1TB",  "NVMe-1TB"),
    HardDrive(4, "2TB", "SATA-2TB"),
    HardDrive(5, "2TB", "SSHD-2TB"),
    HardDrive(6, "1TB", "SSD-1TB"),
    HardDrive(7, "2TB", "HDD-2TB"),
    HardDrive(8, "500GB", "NVMe-500GB")
]

PC_HDs = [
    PC_HD(1, 1),
    PC_HD(1, 8),
    PC_HD(2, 2),
    PC_HD(2, 6),
    PC_HD(3, 4),
    PC_HD(3, 5),
    PC_HD(4, 3),
    PC_HD(5, 7)
]

# Запрос 1: Вывести список всех связанных жестких дисков и компьютеров, отсортированный по жестким дискам, сортировка по компьютерам произвольная.

print("\nЗапрос 1")
sorted_HDs = sorted(HDs, key=lambda x: x.name)

for hd in sorted_HDs:
    for pc_hd in PC_HDs:
        if pc_hd.hd_id == hd.hd_id:
            for pc in PCs:
                if pc_hd.pc_id == pc.pc_id:
                    print(hd.name, ' ', hd.capacity, "  -  ", pc.ram, ' ', pc.cores)
                    break
            break

# Запрос 2: Вывести список компьютеров с количеством жестких дисков в каждом компьютере, отсортированный по количеству жестких дисков.

print("\nЗапрос 2")
mas = {}
for pc in PCs:
    count = 0
    for pc_hd in PC_HDs:
        if pc.pc_id == pc_hd.pc_id:
            count += 1
    mas[pc.ram, pc.cores] = {count}

sorted_mas = dict(sorted(mas.items(), key=lambda x: x[1]))

for key, value in sorted_mas.items():
    print(key, value)

# Запрос 3: Вывести список всех жестких дисков, у которых название заканчивается на «1TB», и операционную систему их компьютеров.

print("\nЗапрос 3")

for hd in HDs:
    if hd.name.endswith("1TB"):
        for pc_hd in PC_HDs:
            if hd.hd_id == pc_hd.hd_id:
                for pc in PCs:
                    if pc_hd.pc_id == pc.pc_id:
                        print(hd.name, "  -  ", pc.ram)
                        break
                break
