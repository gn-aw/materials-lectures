import tracemalloc
import sys

print("Сценарий 1: использование list()")
tracemalloc.start()
numbers = list(range(100_000))
cur, peak_list= tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Число элементов: 100000")
print(f"Размер внешнего объекта: {sys.getsizeof(numbers) / 1000: .3f} КБ")
print(f"Текущий объем: {cur / 1000: .3f} КБ")
print(f"Пиковый объем: {peak_list / 1000: .3f} КБ")
print("=========================")

print("Сценарий 2: использование range()")
tracemalloc.start()
numbers = range(100_000)
cur, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Число элементов: 100000")
print(f"Размер внешнего объекта: {sys.getsizeof(numbers)} б")
print("Число элементов: 100000")
print(f"Текущий объем: {cur / 1000: .3f} КБ")
print(f"Пиковый объем: {peak_range / 1000: .3f} КБ")
print("=========================")

print(f"Отношение пиковых объемов list / range: много больше") ##Иначе получится умножение или деление на 0.