# demo index.py

strA = "파이썬은 강력해"
strB = "python is veru powerful"

print(len(strA))
print(len(strB))
print(strA[:2])
print(strB[:6])
print(strB[-3:])

strC = """이번에는 
다중의 라인을 
저정합니다.  """
print(strC)


print("---리스트 형식---")
lst = [10,20,30]
print(len(lst))
print(lst[0])
lst.append(40)
lst.insert(1,5)
print(lst)
lst.remove(20)
print(lst)

print("---Tuple---")
tp = (100,200,300)
print(len(tp))
print(tp[1])
print(tp.index(300))

#함스를 정의 
def calc(a,b):
    return a+b, a*b
#함수를 호출 
print(calc(3,4))

print("id: %s, name: %s" % ("kim", "김유신"))

args = (5,6)
print(calc(*args))

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))