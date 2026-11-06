import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print("Тек. состояние:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

id_1 = id(first)
id_2 = id(second)
del first, second
k = gc.collect()
print(k)

print("add_ex ========")

gc.disable()

f_1 = []
s_1 = []

f_1.append(s_1)
s_1.append(f_1)

f_2 = []
s_2 = []

f_2.append(s_2)
s_2.append(f_2)

f_3 = []
s_3 = []

f_3.append(s_3)
s_3.append(f_3)

del f_1, s_1, f_2, s_2, f_3, s_3

k = gc.collect()

print(k)
gc.enable()

print("prac_task ========")
import sys

k1 = gc.collect()
first = []
second = []
third = []
first.append(second)
second.append(third)
third.append(first)
indep = []

print("first ссылается на second", first[0] is second)
print("second ссылается на third", second[0] is third)
print("third ссылается на  first", third[0] is first)
print("indep независим", sys.getrefcount(indep) == 2)

del first, second, third
k2 = gc.collect()

print ("До создания графа:", k1)
print("После удаления графа:", k2)
print("Независимый узел остался доступен", indep)