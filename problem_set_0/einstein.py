#Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def formula(mass):
    speed_of_light = 300000000
    energy = mass * speed_of_light**2
    return energy

def main():
    mass = int(input("M: "))
    E = formula(mass)
    print(f" E = {E:,}")
main()