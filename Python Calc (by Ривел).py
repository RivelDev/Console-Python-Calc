# / деление, * умножение, @ степень
import math
res = 'Yes'
while res == 'Yes':
  first_num = int(input())
  maths = input()
  second_num = int(input())
  
  
  
  if maths == ('+'):
    print('Result: ', first_num + second_num)

  if maths == ('-'):
    print ('Result: ', first_num - second_num)
  
  if maths == ('*'):
    print ('Result: ', first_num * second_num)

  if maths == ('/'):
    print('Result: ', first_num / second_num)
  
  if maths == '@':
    print('Result: ', first_num ** second_num)
    
res = input('Сыграть еще раз? [Yes|No]: ')
