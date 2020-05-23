# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 08:31:12 2018

@author: bhara
"""
import random
import time
from os import system
from math import floor
from sys import argv
def truncateFloat(f, n):
    return floor(f * 10 ** n) / 10 ** n
rndno=None
try:
	rndno=int(argv[len(argv)-1])
except ValueError:
	rndno=100
input("Begin test?")
listOfOperators=['+','-','*','/']
tt=0
cs=0
ws=0
cdict=dict.fromkeys(listOfOperators,0) #count of occurance of operator
tdict=dict.fromkeys(listOfOperators,0) #time taken for calculating each operator
for i in range(10):
	system('cls') #Clear screen
	#Generating random numbers and sign
	a=random.randint(0,rndno)
	b=random.randint(1,rndno)
	greater=a if a>b else b
	greater=len(str(greater))
	op=listOfOperators[random.randint(0,len(listOfOperators)-1)]
	cdict[op]+=1
	s=str(a)+op+str(b)
	print('  '+'%0{0}d'.format(greater)%a+'\n'+op.rjust(2)+'%0{0}d'.format(greater)%b)
	print('-----')
	st=time.time()*1000
	try:
		if op == '/':
			inp=str('%.2f'%truncateFloat(float(input()),2))
		else:
			inp=int(input())
	except ValueError:
		inp=0
	et=time.time()*1000
	ctt=et-st
	tt=tt+ctt
	tdict[op]+=ctt/1000
	print("Time taken= "+str(round(ctt/1000,2)))
	if op=='/':
		corrans=str('%.2f'%truncateFloat(eval(s),2))
	else:
		corrans=int(eval(s))
	if inp==corrans:
		print('Correct')
		cs+=1
	else:
		print('Wrong')
		ws+=1
		print('Correct answer is:',corrans)
	input()
print('total time in minutes=','%.2f'%(tt/60000))
print('correct score=',cs)
print('wrong score=',ws)
print('op\tcount\ttime\tavg')
for k in cdict.keys():
	try:
		print(k,'\t',cdict[k],'\t','%.2f'%tdict[k],'\t','%.2f'%(tdict[k]/cdict[k]),sep='')
	except ZeroDivisionError:
		pass
input('Press Enter to exit!')
