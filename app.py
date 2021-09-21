w = float(input("What's your weight? "))
t = input("Enter L for lbs or K for kilogram: ")
t = str(t.lower())

if t == "l":
    a = w / 0.45
    b = "Your weight in lbs is " + str(a)
elif t == "k":
    a = w * 0.45
    b = "Your weight in kg is " + str(a)
else:
    b = "Please enter L for lbs or K for kilogram"
print(b)
