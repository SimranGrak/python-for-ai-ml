#break keyword associated with loop in python

#WAP to print 1 to 10 but if we get multiple of 6 anywhere then break the loop or come outside the loop
i=1

while i<=10:
  if (i%6==0):
    break
  print(i)
  i+=1       #updation

print("outside the loop!")