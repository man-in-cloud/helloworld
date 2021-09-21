w = float(input("what your weight? "))
t = input("L for lbs or K for kilogram: ")
t = str(t.lower())

if t == "l":
    a = w / 0.45
    b = "weight in lbs is " + str(a)
elif t == "k":
    a = w / 0.45
    b = "weight in kg is " + str(a)
else:
    b = "enter L for lbs or K for kilogram"
print(b)