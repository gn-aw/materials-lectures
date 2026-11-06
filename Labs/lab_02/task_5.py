import sys

print("part_1 ========")
l1 = []
l2 = [x for x in range(1, 11)]
print(l2)
c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
s = "ABCDEFGHIJ"
i = 1
none = None

print(f"Пустой список: {sys.getsizeof(l1)}")
print(f"Список целых чисел: {sys.getsizeof(l2)}")
print(f"Кортеж целых чисел: {sys.getsizeof(c)}")
print(f"Строка: {sys.getsizeof(s)}")
print(f"Целое число: {sys.getsizeof(i)}")
print(f"None: {sys.getsizeof(none)}")

print("part_2 ========")

l = []
cur_size = sys.getsizeof(l)
step_count = 0
for i in range (1, 101):
    l.append(i)
    if sys.getsizeof(l) != cur_size:
        print("Номер шага:", step_count)
        print("Длинна:", len(l))
        print("Размер:", sys.getsizeof(l))
        print("")
    cur_size = sys.getsizeof(l)
    step_count += 1

print("part_3 ========")
import tracemalloc

print("vers_1 ====")
tracemalloc.start()
numbers = list(range(100_000))
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Текущий объем: {cur / 1000: .3f} КБ")
print(f"Пиковый объем: {peak / 1000: .3f} КБ")

print("vers_2 ====")
tracemalloc.start()
numbers = range(100_000)
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Текущий объем: {cur / 1000: .3f} КБ")
print(f"Пиковый объем: {peak / 1000: .3f} КБ")
