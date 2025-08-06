#demoFile.py
#파일쓰기
f= open("c:\\demoFile.txt", "w", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open("c:\\demoFile.txt", "r", encoding="utf-8")
print(f.read())
f.close()