import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print(original)
print(alias)
print(shallow)
print(deep)

print("change_1 ========")
original.append(["Databases", 5])
print(f"original list: {original} list_id: {id(original)} first_id and first_mark_id: {id(original[0])}")
print(f"alias list: {alias} list_id: {id(alias)} first_id: {id(alias[0])}")
print(f"shallow list: {shallow} list_id: {id(shallow)} first_id: {id(shallow[0])}")
print(f"deep list: {deep} list_id: {id(deep)} first_id: {id(deep[0])}")
print("change_2 ========")
original[0][1] = 3
print(f"original list: {original} list_id: {id(original)} first_id and first_mark_id: {id(original[0])}")
print(f"alias list: {alias} list_id: {id(alias)} first_id: {id(alias[0])}")
print(f"shallowlist: {shallow} list_id: {id(shallow)} first_id: {id(shallow[0])}")
print(f"deep list: {deep} list_id: {id(deep)} first_id: {id(deep[0])}")

print("wrong_matrix ========")
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1

print(wrong_matrix)
print(correct_matrix)