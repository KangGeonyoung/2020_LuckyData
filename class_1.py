#class 1



#def & lambda
def plus(x, y):
    return x+y

f = lambda x, y : x+y

print(plus(1, 2))
print(f(1, 2))

print("-----------------------------")

def multi(x, y):
    return x*y

g = lambda x, y: x*y
print(multi(3, 4))
print(g(3, 4))

print("-----------------------------")

def mod(x, y):
    return x%y

h = lambda x, y: x%y
print(mod(9, 4))
print(h(9, 4))

print("-----------------------------")



#등차수열
print("등차수열")
def AS(start, d):
    while True:
        yield start
        start = start + d
    

a = AS(1, 7)
for i in range(4):
    print(next(a))

print("-----------------------")
#등비수열
print("등비수열")
def GS(start, r):
    while True:
        yield start
        start = start * r


g = GS(1, 3)
for i in range(4):
    print(next(g))

print("-----------------------")
#누승수열
print("누승수열")
def factorial():
    n = 0;
    f = 1;
    s = 0;
    while True:
        n=n+1;
        f=f*n;
        s=s+f;
        yield s

result=factorial()
for i in range(5):
    print(next(result))



#List & Dict
def getCelsius():
    degree_F = float(input("Enter a Fahrenheit degree : "))
    degree_C = 5 * (degree_F - 32) / 9
    return degree_C

def getFahrenheit():
    degree_C = float(input("Enter a Celsius degree : "))
    degree_F = (9 * degree_C / 5) + 32
    return degree_F

def getKelvin():
    degree_C = float(input("Enter a Celsius degree : "))
    degree_K = degree_C + 273.15
    return degree_K

degreeFunctions = [getCelsius, getFahrenheit, getKelvin]

print("temperature converter")
print("1. Fahrenheit -> Celsius")
print("2. Celsius -> Fahrenheit")
print("3. Celsius -> Kelvin")

print()
choice = int(input("Enter a choice_number : "))
print()

print(degreeFunctions[choice-1]())



#LCM & GCD
def LCM(x, y):
    if x > y:
        LCM = x
    else:
        LCM = y

    while 1:
        if LCM % x == 0 and LCM % y == 0:
            break
        else:
            LCM += 1
            
    return LCM


def GCD(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r

    return x

x = int(input('Enter the x value : '))
y = int(input('Enter the y value : '))
print('LCM of {0} and {1} = '.format(x,y), LCM(x, y))
print('GCD of {0} and {1} = '.format(x,y), GCD(x, y))
