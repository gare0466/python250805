print("hello python")
result = 3 + 5
print(result)

for i in [1,2,3]:
    print(i)

    # 파이썬 기본 자료형 비교

# list (리스트) - 순서 있음, 변경 가능, 중복 허용
my_list = [1, 2, 3, 4, 4]
print("List:", my_list)

# tuple (튜플) - 순서 있음, 변경 불가, 중복 허용
my_tuple = (1, 2, 3, 4, 4)
print("Tuple:", my_tuple)

# set (셋) - 순서 없음, 변경 가능, 중복 불가
my_set = {1, 2, 3, 4, 4}
print("Set:", my_set)

# dict (딕셔너리) - 키:값 쌍, 순서 있음(3.7 이상), 키 중복 불가
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dict:", my_dict)

# set 형식을 하나 더 예제로 보여주기 (빈 set과 빈 dict 차이)
empty_set = set()
empty_dict = {}
print("Empty set:", empty_set, type(empty_set))
print("Empty dict:", empty_dict, type(empty_dict))
