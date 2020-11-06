import itertools as iter
from pprint import pprint

#1.두 개의 주사위로 나올 수 있는 중복을 제외한 모든 경우의 수 구하기
print(list(iter.permutations([1,2,3,4,5,6],2)))


#2.잘못 입력한 생년월일을 찾아주기
a = ['001130', '981211', '020418', '970831', '9912312']
b = list(iter.filterfalse(lambda x: len(x) == 6, a))
print(b)


#3.잘못 입력한 시험 점수가 있을 경우 찾아주기.(시험 점수의 만점은 100점)
a = [75, 100, 80, 97, 95, 88, 102]
func = lambda x: x<=100
b = list(iter.dropwhile(func, a))
print(b)


#모듈 함수
import os

#1 현재 디렉토리 확인하기
print(os.getcwd())

#2 디렉토리 경로 변경하기
os.chdir("C:\\")

#3 현재 디렉토리의 파일 목록 확인하기
os.listdir()

#4 파일의 이름을 변경하기
os.rename("test.txt", "result.txt")

#5 경로에 해당하는 정보 확인하기
os.stat("python.exe")


