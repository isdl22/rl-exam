# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:10:45 2017

@author: wdp
"""

t =1 (1,2,'a','b')
t1[0]
del t1[0]


dic = {}
dic['파이썬'] = 'www.python.org'
dic['애플'] = 'www.apple.com'
dic['마이크로소프트'] = 'www.microsoft.com'
				
dic.keys()
dic.values()

dic.pop('애플')
dic

dic = { }
dic['나는'] = ('I',0)
dic['소년'] = ('boy',2)
dic['이다'] = ('am',1)
dic['피자'] = ('pizza',2)
dic['먹는다'] = ('eat',1)

#dictionary 사전 정의
dic = { }
dic['나는'] = ('I',0)
dic['소년'] = ('boy',2)
dic['입니다'] = ('am',1)

# 번역할 문장을 단어별로 나누어 리스트형으로 저장
result = ''
input_kor = input('번역할 한글을 입력하세요 ~ ')
input_list = input_kor.split(' ')
print(input_list)

for i in range(len(input_list)): 
    for j in input_list:
        if dic[j][1]==i:
            
            result = result + dic[j][0] + ' '
            
print(result)

#csv 파일을 파이썬으로 불러오게 할 수 있는 모듈
import csv

file = open("D:\data\smt_dic.csv","r")
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    print(emp_list[1],emp_list[3],emp_list[4])
    

#dictionary 사전 정의
dic = { }
dic['나는'] = ('I',0)
dic['소년'] = ('boy',2)
dic['입니다'] = ('am',1)

#csv 파일을 파이선으로 불러오기
import csv
smt_dic = {}
file = open("D:\data\smt_dic.csv","r")
emp_csv = csv.reader(file)
# 불러온 데이터를 사전형으로 저장하기
for emp_list in emp_csv:
    smt_dic[ emp_list[1] ] = (emp_list[3], emp_list[4])
    smt_dic[ emp_list[2] ] = (emp_list[3], emp_list[4])
    
result = ''
input_kor = input('번역할 문장을 입력하세요 ~')
input_list = input_kor.split(' ')

for i in range(len(input_list)): 
    for j in input_list:
        if smt_dic[j][1]==str(i):
            
            result = result + smt_dic[j][0] + ' '
            
print(result)


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#s1,s2 교집합

s1 & s2

#s1,s2 합집합

s1 | s2

#s1,s2 차집합

s1 - s2

import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5])
    

import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[5]) == 3000:
        print(emp_list[1],emp_list[5])
        



import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[2] in ('ANALYST', 'CLERK'):
        print(emp_list[1],emp_list[2])
        
x = 1
y = 2
if x >= y:
	print('x가 y보다 크거나 같습니다.')
else:
    print('x가 y보다 작습니다')
    
x = int(input('숫자를 입력하시오 ~'))

if x % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

def mod(x):
    if x % 2 == 0:
        print('짝수입니다')
    else:
        print('홀수입니다')
mod(10)`

x = int(input('첫번째 숫자를 입력하시오 ~'))
y = int(input('마지막 숫자를 입력하시오 ~'))

result=(x+y)*((y-x+1)/2)
print(result)

x = int(input('첫번째 숫자를 입력하시오 ~'))
y = int(input('마지막 숫자를 입력하시오 ~'))

def gauss(x,y):
    return ((x+y)*((y-x+1)/2))
gauss(x,y)

import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1] == 'SCOTT':
        print(emp_list[5])


import csv
ename = input('이름을 입력하시오 ~')
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1] == ename:
        print(emp_list[5])

import csv
ename = input('이름을 입력하시오 ~')
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1] == ename:
        if int(emp_list[5]) >= 3000:
            print ('고소득자입니다.')
        elif int(emp_list[5]) >= 2000:
            print ('적당합니다.')
        else:
            print('저소득자입니다.)

import csv
file = open("D:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
 
ename = input('이름을 입력하세요.')
 
for emp_list in emp_csv:
    if emp_list[1] == ename.upper():
        if int(emp_list[5]) >= 3000 :
            print('고소득입니다.')
        elif int(emp_list[5]) >= 2000 :
            print('적당합니다.')
        else :
            print('저소득입니다.')

            

for i in (1,2,3):
    print(i)
    
for i in 'I am a boy':
    print(i)
    
for i in range(1,11):
    print(i)
    
for i in range(11):
    print(i)
    
for i in range(1,11,2):
    print(i)
    
    
star★

for i in range(1,11):
    print('★'*i)
    

for i in range(10,0,-1):
    print('★'*i)
    
x = int(input('가로의 숫자를 입력하세요~'))
y = int(input('세로의 숫자를 입력하세요~'))

for i in range(1,y+1):
    print('★'*x)
        


x = int(input('가로의 숫자를 입력하세요~'))
y = int(input('세로의 숫자를 입력하세요~'))

for i in range(y):
    c = '' # 변수 초기화
    for j in range(x):
        c+='★ '
    print(c)


for i in range(2,10):
    result = ''
    for j in range(1,10):
        result = i * j
        print(i,' × ',j,'=',result)
        
for i in range(1,10):
    result = ''
    for j in range(2,10):
        result += (str(j) + ' X ' + str(i)+ ' = ' + str(i*j)).ljust(13)
        print(result)

        #ljust 함수 : 오라클 의 lpad와 같다
        # select lpad(문자열,13,' ') from emp;

result += (str(j) + ' x ' + str(i)+ ' = ' + str(i*j)+ '\t')

for i in range(10):
    if i % 2 == 1: # 2로 나눈 나머지값이 1이 된다는 것은 i 가 홀수 라는 것이다.
        continue
    print(i)

for i in range(10):
    if i % 2 == 1:
        continue
    print(i)
    
num = 0

for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
jumsu = [90,25,67,45,80]
num = 0

for i in jumsu:
    num = num + 1
    if i < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % num)
    
import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
emp = {}
for emp_list in emp_csv:
    emp[emp_list[1]] = (emp_list[5])
print(emp)
emp.values(1)
for i in len(emp):
    if emp[emp.values()] >= 3000:
            continue
        print("%d 축하합니다. 고소득자입니다." % num)

import csv
file = open("D:\data\emp2.csv","r")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    z=print(emp_list[5])
print(z)
jumsu1 = [5000,2850,2450,2975,1250,1600,1500,950,1250,3000,800,3000,1100,3000]
num = 0

for i in jumsu1:
    num = num + 1
    if i < 3000:
        continue
    print("%d번 축하합니다. 고소득자입니다." % num)
    

