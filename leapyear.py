year = 2000

if year%100 == 0 and year%400 != 0:
    print (" Not Leap Year")
elif year%4 == 0:
    print ("Leap Year")
else:
    print ("Not Leap Year")

