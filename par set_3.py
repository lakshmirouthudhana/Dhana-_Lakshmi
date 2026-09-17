'''
marks=int(input("Enter student's marks:")
if marks>0 and marks<100:
    if marks>=90:
        print("Grade: A")
        print("Remark: Outstanding")
    elif marks<90 and marks>=80:
        print("Grade: B")
        print("Remark: Excellent!")
    elif marks<80 and marks>=70:
        print("Grade: C")
        print("Remark: Good")
    elif marks<70 and marks>=60:
        print("Grade: D")
        print("Remark: Fair, needs improvement")
    elif marks<60 and marks>=50:
        print("Grade: E")
        print("Remark: Poor, needs serious improvement")
    else:
        print("Grade: F")
        print("Remark: Failed, needs to reappear")
else:
    print("Invalid marks entered


--> Even-Odd Checker:-

num = int(input("Enter a number:"))

if num == 0:
    print("Zero is neither even nor odd")

elif num < 0 and num % 2 == 0:
    print("Negative Even Number")

elif num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

----> Month number using if-elif-else

month = int(input("Enter month number:"))
if month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month == 3 or month == 4 or month == 5:
    print("Season: Spring")
elif month == 6 or month == 7 or month == 8:
    print("Season: Summer")
elif month == 9 or month == 10 or month == 11:
    print("Season: Autumn")
else:
    print("Invalid month entered")
  

# Month number using if-elif-else
'''
month = int(input("Enter month number: "))

if month in [12, 1, 2]:
    print("Season: Winter")

elif month in [3, 4, 5]:
    print("Season: Spring")

elif month in [6, 7, 8]:
    print("Season: Summer")

elif month in [9, 10, 11]:
    print("Season: Autumn")

else:
    print("Invalid month entered")
