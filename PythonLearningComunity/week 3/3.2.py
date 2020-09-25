start_day=int(input("On which day are you going to jail on from 0 to 6(aka computer language)\n"))
lenght=int(input("How long is your sentence?\n"))
number=(start_day+lenght)%7
if number==0:
    print("Monday")
elif number==1:
    print("Tuesday")
elif number==2:
    print("It is Wednesday my dude")
elif number==3:
    print("Thursday")
elif number==4:
    print("Finally Friday")
elif number==5:
    print("Saturday it is")
elif number==6:
    print("SUNDAYFUNDAY")
else:
    print("Invalid input bro")