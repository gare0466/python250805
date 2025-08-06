#demoFile.py
#파일쓰기
f= open("c:\\demoFile.txt", "w", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open("c:\\demoFile.txt", "r", encoding="utf-8")
print(f.read())
f.close()

#문자열 처리
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))  # 문자열 길이
print(len(strB))  # 문자열 길이
print(strB.upper())  # 대문자 변환
print("MBC2580".isalnum())
print("2580".isdecimal())  # 숫자 여부
data = "<<< spam and ham >>>"
result = data.strip("<> ")  # 양쪽 공백과 특정 문자 제거
print(data)
print(result)  # 결과 출력
result2 = result.replace("spam", "egg")  # 문자열 치환
print(result2)  # 치환된 문자열 출력
# 리스트로 리턴
lst = result2.split()  #공백으로 
print(lst)  # 리스트 출력
print(":".join(lst))  # 리스트를 문자열로 결합

#정규식 표현식
import re
pattern = re.search("[0-9]*th", "35th")
print(result)  # 정규식 검색 결과 출력
print(pattern.group())  # 검색된 문자열 출력

# pattern = re.match("[0-9]*th", "  35th")
# print(result)  # 정규식 검색 결과 출력
# print(pattern.group())  # 검색된 문자열 출력

result = re.search("apple", "this is apple")
print(result.group)  # 정규식 검색 결과 출력

result = re.search(r"\d{4}", "올해는 2025년입니다 ")
if result:
	print(result.group())  

result = re.search(r"\d{5}", "우리동네는 ")
if result:
	print(result.group())  