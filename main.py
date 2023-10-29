p = str(input("Input your name: "))
x = int(input("Input body weight(Kg): "))
y = int(input("Input body height(Cm): "))
u = (y/(10*10))*(y/(10*10))

def BMI():
    print("================================")
    print(f"Name: {p}")
    print("================================")
    print(f"Weight: {x}")
    print(f"Height: {y}")
    print(f"BMI: {x/u} Kg/M^2")
    if x/u < 18:
        print(">>> You are very thin")
    elif x/u > 25:
        print(">>> Too much weight")
    elif x/u > 18 or BMI < 25:
        print(">>> Normal weight")
    print("================================")

BMI()