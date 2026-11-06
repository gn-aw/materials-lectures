student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
print(f"1) first symb: {student[:1]} last symb: {student[-1:]}")
print(f"2) name: {student.split()[0]} surname: {student.split()[1]}")
print(f"3) up: {student.upper()} low: {student.lower()}")
print(f"4) {student.split()[0][:1]}. {student.split()[1][:1]}.")
print(f"5) {course[::-1]}")
print("6.1)")
pers = float(completed/total * 100)
print("%s - %s: %d/%d (%.1f%%)"  % (student, course, completed, total, pers))
print("6.2)")
print("{} - {}: {}/{} ({}%)".format(student, course, completed, total, float(completed/total * 100)))
print("6.3)")
print(f"{student} - {course}: {completed}/{total} ({round(float(completed/total * 100), 1)}%)")
symbol = "Я"
print("7)")
print(ord(symbol))
print(chr(ord(symbol)))
print(f"{symbol.encode("utf-8")} len: {len(symbol.encode("utf-8"))}")
print("8")
err = "python"
##err[0] = chr(1071)