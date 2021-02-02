def sum_of_squares(n):

  sum=0
  for i in range(1, n+1):
     sum += (i*i)
  return sum

#driver program
n = int(input('Enter number of your choice'))
print(sum_of_squares(n))


