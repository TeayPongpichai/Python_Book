# -*- coding: utf-8 -*-
"""Book_Basic_Python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dh9YsY7HMhuZXQ6tzgdVq4lvt289Y7iB
"""

price = 110
if price >= 110: # Basic If
  print('Discount 5%')

price = 100
if price >= 100: #If Else
  print('Discount 5%')
else:
  print('No Discount')
print('Bye')

temp = 32
if temp < 30: #if Elif
  print('Fan off')
elif temp >=30 and temp < 40:
  print('Small Fan')
else:
  print ('Turn on a Big Fan')

temp = 40
if temp >= 40:
  print('Turn on a big fan \
  Location : buiding 1 floor 1')
print('Done')

for count in range(3): #Loop for
  print('test for')
  print(count)
print('done')

for v in range(4,6): #Loop for แบบกำหนด ค่าเริ่มต้น และค่าสุดท้าย
  print(v)
print('end program')

count = 0
while count < 3: #Loop while
  print('Hi')
  count = count + 1

name = 'kobkiat'
print('Hi,',name)
print('Hi, %s'%format(name))

a = 2.9
b = 3.2789
name = 'kobkiat'
print('Hi',name,'a =',a)
print('Hi',name,'a = ',a,',','b = ',b)
print('Hi, %s a = %d b =%.3f' %(name,a,b)) # %d คือจำนวนเต็ม %.3f คือทศนิยม 3 ตำแหน่ง

