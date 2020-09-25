mark=float(input("how much did you get on the exam\n"))
if mark<40:
    print("F3")
elif mark>=40 and mark<45:
    print("F2")
elif mark>=45 and mark<50:
    print("F1")
elif mark>=50 and mark<60:
    print("Third")
elif mark>=60 and mark<70:
    print("Second")
else:
    print("Wow First!")

print("And this is how the rest of the class did:")
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

for number in numbers:
    if number < 40:
        print(number,"-F3")
    elif number >= 40 and number < 45:
        print(number,"-F2")
    elif number >= 45 and number < 50:
        print(number,"-F1")
    elif number >= 50 and number < 60:
        print(number,"-Third")
    elif number >= 60 and number < 70:
        print(number,"-Second")
    else:
        print(number,"-Wow First!")