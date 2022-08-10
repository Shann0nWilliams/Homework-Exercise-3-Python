import math

print("BMI Calculator")
print()
print("1. Weight in pounds, height in inches")
print("2. Weight in kilograms, height in meters")
print()
Choice=int(input("Choice: "))
print()


if Choice==1:
    WeightLB=float(input("Weight in pounds?:"))
    print()
    HeightIN=float(input("Height in inches?:"))
    print()
    print()
    print("Result..............")
    print()
    print(" Weight:        ",(WeightLB),"pounds")
    print(" Height:        ",(HeightIN),"inches")
    print(" BMI:           ",round(WeightLB/(HeightIN*HeightIN)*703,1))
    BMI=float(round(WeightLB/(HeightIN*HeightIN)*703,1))

elif Choice==2:
    WeightKG=float(input("Weight in kilograms?:"))
    print()
    HeightM=float(input("Height in meters?:"))
    print()
    print()
    print("Result..............")
    print()
    print(" Weight:        ",(WeightKG),"kilograms")
    print(" Height:        ",(HeightM),"meters")
    print(" BMI:           ",round(WeightKG/(HeightM*HeightM),1))
    BMI=float(round(WeightKG/(HeightM*HeightM),1))

if BMI>=30:
    print(" Status:         Obese")
elif BMI>25<29:
    print("Status:          Overweight")
elif BMI>18.5<25:
    print(" Status:         Normal")
elif BMI<18.5:
    print(" Status:         Underweight")
