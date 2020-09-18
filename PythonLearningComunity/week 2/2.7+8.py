a= int(input("What is the time does the clock show now?"))
b= int (input("how many hours is the alarm in?"))
c= b%12
d=c+a
if d<12:
    print (d)
else:
    print(d-12)