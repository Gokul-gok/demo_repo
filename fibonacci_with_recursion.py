def recursion(num) -> int:
  if num<=1:
    return num
  else:
    return recursion(num-1) + recursion(num-2)


ip=int(input('enter the no. of terms: '))

if ip<=0:
  print('enter a positive integer')
  
else:
  for item in range(ip):
    print(recursion(item))
