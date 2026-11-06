import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

print("weak_ref_exp ========")
import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print("prac_task ========")

reg = weakref.WeakValueDictionary()
class Record:
    pass
obj_1 = Record()
obj_2 = Record()

reg["1"] = obj_1
reg["2"] = obj_2
reg["3"] = Record()

print(list(reg))

del obj_1
print(f"После удаления временной сильной ссылки {list(reg)}")

del obj_2
print(f"После удаления еще одной временной ссылки {list(reg)}")


