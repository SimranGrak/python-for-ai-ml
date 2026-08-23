#WAF to calculate factorial of number n

def calc_fact(n):
  fact=1
  for i in range(1,n+1):
    fact*=i

  return fact


number=int(input("enter value of n:"))
factorial=calc_fact(number)
print(factorial)