print("ex_A ==========")

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print("ex_B ==========")
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

print("ex_B_2 =========")

first = [10, 20]
second = [10, 20]

print(f"== : {first == second}")
print(f"is : {first is second}")
print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

print("prac_task =========")
import copy

conf_1 = {
    "name": "name_1",
    "pars": ["par_1", "par_2", "par_3"],
    "params": ["p1", "p2"]

}

conf_2 = conf_1
conf_2["params"][0] = "p_0"

print("Нежелательное изменение", conf_1["params"][0])
print("conf_1", conf_1)
print("conf_2", conf_2)

print("Независимая конфигурация ========")
conf_1 = {
    "name": "name_1",
    "pars": ["par_1", "par_2", "par_3"],
    "params": ["p1", "p2"]

}
conf_2 = copy.deepcopy(conf_1)

conf_2["params"][0] = "p_0"

assert conf_2["params"][0] != conf_1["params"][0], "Новые параметры запуска не должны совпадать"

print("conf_1", conf_1)
print("conf_2", conf_2)
print("Все объекты оказались независимыми")


